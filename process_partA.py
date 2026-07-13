import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_FILE = os.path.join(SCRIPT_DIR, "raw_responses_partA.json")
CACHE_FILE = os.path.join(SCRIPT_DIR, "search_cache_partA.json")

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
    if not os.path.exists(RAW_FILE):
        print(f"Error: {RAW_FILE} does not exist.")
        return

    with open(RAW_FILE, 'r') as f:
        raw_responses = json.load(f)

    cache = {}
    for query, text in raw_responses.items():
        results = heuristic_parse(query, text)
        cache[query] = results

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

    print(f"Successfully processed {len(raw_responses)} queries. Saved cache to {CACHE_FILE}")

if __name__ == '__main__':
    main()
