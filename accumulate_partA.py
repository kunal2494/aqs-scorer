import json
import os
import re

batch_queries_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/batch_queries.txt"
raw_responses_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/raw_responses_partA.json"
cache_output_path = "/Users/fincent/.gemini/antigravity/scratch/aqs-scorer/search_cache_partA.json"

# 1. Read target queries (first 50)
target_queries = []
with open(batch_queries_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f, 1):
        if 1 <= idx <= 50:
            target_queries.append(line.strip())

# 2. Load raw responses
raw_search_responses = {}
if os.path.exists(raw_responses_path):
    with open(raw_responses_path, 'r', encoding='utf-8') as f:
        raw_search_responses = json.load(f)

# 3. Heuristic Parse function
def heuristic_parse(query, text):
    if not text or "No results found" in text:
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

# 4. Parse and match queries
cache_partA = {}
missing_queries = []
for q in target_queries:
    matched_key = None
    for k in raw_search_responses:
        k_clean = k.replace('\\"', '"').replace('"', '').strip()
        q_clean = q.replace('\\"', '"').replace('"', '').strip()
        if k_clean == q_clean:
            matched_key = k
            break
            
    if matched_key:
        raw_text = raw_search_responses[matched_key]
        parsed = heuristic_parse(q, raw_text)
        cache_partA[q] = parsed
    else:
        missing_queries.append(q)

print(f"Successfully matched and parsed {len(cache_partA)} queries.")
print(f"Missing {len(missing_queries)} queries.")

with open(cache_output_path, 'w', encoding='utf-8') as f:
    json.dump(cache_partA, f, indent=2, ensure_ascii=False)
print(f"Saved cache with {len(cache_partA)} entries to {cache_output_path}")
