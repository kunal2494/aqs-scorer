import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_FILE = os.path.join(SCRIPT_DIR, "raw_responses_partB.json")
CACHE_FILE = os.path.join(SCRIPT_DIR, "search_cache_partB.json")

def fix_line(line):
    line_str = line.strip()
    if not line_str or line_str in ['{', '}']:
        return line
    
    idx = line.find('"": "')
    if idx != -1:
        key_part = line[:idx]
        val_part = line[idx+5:]
    else:
        idx = line.find('": "')
        if idx != -1:
            key_part = line[:idx]
            val_part = line[idx+4:]
        else:
            return line
            
    ends_with_comma = False
    if val_part.endswith(',\n'):
        val_part = val_part[:-2]
        ends_with_comma = True
    elif val_part.endswith(','):
        val_part = val_part[:-1]
        ends_with_comma = True
        
    if val_part.endswith('\n'):
        val_part = val_part[:-1]
        
    if val_part.endswith('"'):
        val_part = val_part[:-1]
        
    escaped_chars = []
    i = 0
    while i < len(val_part):
        if val_part[i] == '\\':
            if i + 1 < len(val_part):
                escaped_chars.append('\\')
                escaped_chars.append(val_part[i+1])
                i += 2
            else:
                escaped_chars.append('\\')
                i += 1
        elif val_part[i] == '"':
            escaped_chars.append('\\')
            escaped_chars.append('"')
            i += 1
        else:
            escaped_chars.append(val_part[i])
            i += 1
            
    fixed_val = "".join(escaped_chars)
    
    newline = key_part + '": "' + fixed_val + '"'
    if ends_with_comma:
        newline += ','
    newline += '\n'
    return newline

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

    # Fix the raw file first
    print("Fixing raw file line by line...")
    with open(RAW_FILE, 'r') as f:
        lines = f.readlines()
        
    fixed_lines = [fix_line(line) for line in lines]
    
    with open(RAW_FILE, 'w') as f:
        f.writelines(fixed_lines)
    print("Raw file fixed successfully.")

    # Now load and parse
    with open(RAW_FILE, 'r') as f:
        raw_responses = json.load(f)

    cache = {}
    for query, text in raw_responses.items():
        results = heuristic_parse(query, text)
        cache[query] = results

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)
    print("Successfully processed raw responses of Part B into search_cache_partB.json")

if __name__ == '__main__':
    main()
