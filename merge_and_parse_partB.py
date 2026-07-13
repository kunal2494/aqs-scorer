import json
import os
import re

def heuristic_parse(query, text):
    if not text or "No results found" in text or "No results were found" in text:
        return []
        
    sources = {}
    sources_section = re.search(r'Sources:\s*(.*)', text, re.DOTALL)
    if sources_section:
        sources_text = sources_section.group(1)
        matches = re.findall(r'\[(\d+)\]\s+\[([^\]]+)\]\(([^\)]+)\)', sources_text)
        for idx, domain, url in matches:
            sources[int(idx)] = {"domain": domain, "url": url}
            
    main_text = text
    if sources_section:
        main_text = text[:sources_section.start()]
        
    lines = main_text.split('\n')
    blocks = []
    current_block = []
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            if current_block:
                blocks.append("\n".join(current_block))
                current_block = []
        else:
            if line_str.startswith('*') or line_str.startswith('-') or re.match(r'^\d+\.', line_str) or line_str.startswith('###'):
                if current_block:
                    blocks.append("\n".join(current_block))
                current_block = [line_str]
            else:
                current_block.append(line_str)
    if current_block:
        blocks.append("\n".join(current_block))
        
    results = []
    seen_urls = set()
    
    for idx, source_info in sorted(sources.items()):
        citation = f"[{idx}]"
        citing_blocks = []
        for block in blocks:
            if citation in block:
                citing_blocks.append(block)
                
        url = source_info['url']
        if url in seen_urls:
            continue
            
        if not citing_blocks:
            snippet = f"Link to {source_info['domain']} from search results."
            title = f"{source_info['domain']} (Source [{idx}])"
            results.append({
                "title": title,
                "url": url,
                "snippet": snippet
            })
            seen_urls.add(url)
            continue
            
        snippet_parts = []
        title = ""
        for block in citing_blocks:
            clean_block = re.sub(r'\[\d+\]', '', block)
            clean_block = re.sub(r'\s+', ' ', clean_block).strip()
            clean_block = re.sub(r'\*\*|\*', '', clean_block)
            clean_block = re.sub(r'^(?:\*|-|\d+\.)\s+', '', clean_block)
            
            snippet_parts.append(clean_block)
            
            if not title:
                title_match = re.search(r'^(?:\*|-|\d+\.)\s+\*\*(.*?)\*\*[:\s-]', block)
                if title_match:
                    title = title_match.group(1).strip('"\'')
                elif block.startswith('###'):
                    title = block.replace('###', '').strip()
                elif ':' in clean_block:
                    parts = clean_block.split(':', 1)
                    if len(parts[0].split()) <= 6:
                        title = parts[0].strip()
                        
        if not title:
            name_in_query = query.replace('"', '').replace('site:linkedin.com/in', '').replace('site:github.com OR site:udemy.com/user OR site:medium.com', '').strip()
            title = f"{source_info['domain']} - {name_in_query}"
            
        snippet = " ".join(snippet_parts)
        if len(snippet) > 300:
            snippet = snippet[:297] + "..."
            
        results.append({
            "title": title,
            "url": url,
            "snippet": snippet
        })
        seen_urls.add(url)
        
    return results

def main():
    merged_raw = {}
    for i in range(1, 5):
        filepath = f"/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_sub{i}.json"
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    merged_raw.update(data)
                print(f"Loaded {len(data)} queries from sub {i}")
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
        else:
            print(f"File {filepath} not found.")

    print(f"Total merged raw queries: {len(merged_raw)}")
    
    # Read queries lines 41 to 80 of batch_queries.txt to ensure we match them in order
    batch_queries_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"
    if not os.path.exists(batch_queries_path):
        print("Error: batch_queries.txt not found")
        return
        
    with open(batch_queries_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    target_queries = lines[40:80]
    
    cache_partB = {}
    missing_queries = []
    
    for q in target_queries:
        matched_key = None
        for k in merged_raw:
            k_clean = k.replace('\\"', '"').replace('"', '').strip()
            q_clean = q.replace('\\"', '"').replace('"', '').strip()
            if k_clean == q_clean or k == q:
                matched_key = k
                break
                
        if matched_key:
            raw_text = merged_raw[matched_key]
            parsed = heuristic_parse(q, raw_text)
            cache_partB[q] = parsed
        else:
            missing_queries.append(q)
            
    print(f"Matched and parsed {len(cache_partB)} / {len(target_queries)} target queries.")
    if missing_queries:
        print(f"WARNING: {len(missing_queries)} queries were missing from raw responses:")
        for mq in missing_queries:
            print(f"  - {mq}")
            
    output_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_partB.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cache_partB, f, indent=2, ensure_ascii=False)
    print(f"Wrote final search cache to {output_path}")

    # If successfully parsed all, clean up subagent json files
    if len(cache_partB) == len(target_queries):
        print("All queries parsed successfully. Cleaning up temp files...")
        for i in range(1, 5):
            filepath = f"/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_sub{i}.json"
            if os.path.exists(filepath):
                os.remove(filepath)
        print("Cleanup done.")
    else:
        print("Not all queries parsed. Skipping cleanup of subagent files so they can be inspected/re-run.")

if __name__ == "__main__":
    main()
