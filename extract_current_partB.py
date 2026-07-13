import json
import os
import re
import sys

batch_queries_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"
conversation_id = "df878f48-3231-4e24-af4f-97945e97a6d0"
log_path_full = f"/Users/fincent/.gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript_full.jsonl"
log_path_short = f"/Users/fincent/.gemini/antigravity/brain/{conversation_id}/.system_generated/logs/transcript.jsonl"
cache_output_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_partB.json"

def get_target_queries():
    if not os.path.exists(batch_queries_path):
        print(f"Error: {batch_queries_path} not found")
        return []
    with open(batch_queries_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    # Lines 41 to 80 (indices 40 to 79)
    return lines[40:80]

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

def extract_from_logs():
    target_queries = get_target_queries()
    if not target_queries:
        print("No target queries loaded.")
        return
        
    # Find which log path exists
    log_path = log_path_full if os.path.exists(log_path_full) else log_path_short
    if not os.path.exists(log_path):
        print(f"Log path does not exist: {log_path_full} or {log_path_short}")
        return
        
    raw_search_responses = {}
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
            except Exception:
                continue
            
            # Extract content containing search results
            content = data.get('content', '')
            if content and "The search for " in content:
                m = re.search(r'The search for "(.*?)" returned', content)
                if m:
                    query_str = m.group(1)
                    header_match = re.search(r'returned the following summary:\s*(.*)', content, re.DOTALL)
                    if header_match:
                        raw_response = header_match.group(1).strip()
                    else:
                        raw_response = content.strip()
                    raw_search_responses[query_str] = raw_response
                    
    print(f"Total search responses found in log: {len(raw_search_responses)}")
    
    cache_partB = {}
    missing_queries = []
    for q in target_queries:
        matched_key = None
        for k in raw_search_responses:
            k_clean = k.replace('\\"', '"').replace('"', '').strip()
            q_clean = q.replace('\\"', '"').replace('"', '').strip()
            if k_clean == q_clean or k == q:
                matched_key = k
                break
                
        if matched_key:
            raw_text = raw_search_responses[matched_key]
            parsed = heuristic_parse(q, raw_text)
            cache_partB[q] = parsed
        else:
            missing_queries.append(q)
            
    print(f"Matched and parsed {len(cache_partB)} / {len(target_queries)} target queries.")
    
    if missing_queries:
        print(f"Missing {len(missing_queries)} queries:")
        for mq in missing_queries[:5]:
            print(f"  - {mq}")
        if len(missing_queries) > 5:
            print(f"  ... and {len(missing_queries) - 5} more.")
    else:
        print("All queries successfully matched and parsed!")
        
    # Write output to search_cache_partB.json
    with open(cache_output_path, 'w', encoding='utf-8') as f:
        json.dump(cache_partB, f, indent=2, ensure_ascii=False)
    print(f"Wrote cache to {cache_output_path}")

if __name__ == "__main__":
    extract_from_logs()
