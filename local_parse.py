import json
import os
import re

transcript_path = "/Users/fincent/.gemini/antigravity/brain/80b7d530-1fc7-4dba-8722-8f85551b070a/.system_generated/logs/transcript.jsonl"
cache_output_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_missing.json"

target_queries = [
    '"Zhang Zhiwei" site:linkedin.com/in',
    '"Zhang Zhiwei" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Vasyl Zvarydchuk, PhD" site:linkedin.com/in',
    '"Vasyl Zvarydchuk, PhD" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Bunny Kaushik" site:linkedin.com/in',
    '"Bunny Kaushik" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Mona M" site:linkedin.com/in',
    '"Mona M" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Ajeet Singh Raina" site:linkedin.com/in',
    '"Ajeet Singh Raina" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Harsh Manvar" site:linkedin.com/in',
    '"Harsh Manvar" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Evan Williams" site:linkedin.com/in',
    '"Evan Williams" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Joshua Au-Yeung" site:linkedin.com/in',
    '"Joshua Au-Yeung" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"IT Governance Publishing" site:linkedin.com/in',
    '"IT Governance Publishing" site:github.com OR site:udemy.com/user OR site:medium.com',
    '"Andrew Pattison" site:linkedin.com/in',
    '"Andrew Pattison" site:github.com OR site:udemy.com/user OR site:medium.com'
]

def heuristic_parse(query, text):
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
    # Read search entries from transcript
    raw_search_responses = {}
    if not os.path.exists(transcript_path):
        print(f"Error: {transcript_path} does not exist.")
        return

    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                # Check for search_web responses in MODEL planning responses or SEARCH_WEB output steps
                if data.get('type') == 'SEARCH_WEB' and data.get('status') == 'DONE':
                    content = data.get('content', '')
                    m = re.search(r'The search for "(.*?)" returned', content)
                    if m:
                        query_str = m.group(1)
                        header_match = re.search(r'returned the following summary:\s*(.*)', content, re.DOTALL)
                        if header_match:
                            raw_response = header_match.group(1).strip()
                        else:
                            raw_response = content.strip()
                        # Normalize query keys
                        raw_search_responses[query_str.replace('\\"', '"').strip()] = raw_response
            except Exception as e:
                pass

    print(f"Extracted {len(raw_search_responses)} raw search responses.")

    cache = {}
    for q in target_queries:
        q_norm = q.strip()
        matched_key = None
        for k in raw_search_responses:
            if k == q_norm:
                matched_key = k
                break
        
        if matched_key:
            raw_text = raw_search_responses[matched_key]
            if "No results found for" in raw_text or "No LinkedIn profile results were found" in raw_text or raw_text.strip() == "":
                cache[q] = []
            else:
                # Handle special direct URL outputs like Ajeet Singh Raina tech sites
                # "https://github.com/ajeetraina\nhttps://medium.com/@ajeetraina"
                if raw_text.strip().startswith("https://") and "Sources:" not in raw_text:
                    urls = [u.strip() for u in raw_text.strip().split('\n') if u.strip()]
                    parsed = []
                    for u in urls:
                        domain = "github.com" if "github" in u else "medium.com" if "medium" in u else "udemy.com"
                        parsed.append({
                            "title": f"{domain} profile for Ajeet Singh Raina",
                            "url": u,
                            "snippet": f"Direct link to Ajeet Singh Raina's profile on {domain}."
                        })
                    cache[q] = parsed
                else:
                    parsed = heuristic_parse(q, raw_text)
                    cache[q] = parsed
        else:
            print(f"Warning: query not found in log: {q}")
            cache[q] = []

    with open(cache_output_path, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(cache)} entries to {cache_output_path}")

if __name__ == '__main__':
    main()
