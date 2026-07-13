import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(SCRIPT_DIR, "search_cache_partA.json")

# 10 raw responses
raw_responses = {
  '"Jimmy Engström" site:linkedin.com/in': """There are two prominent professionals named Jimmy Engström, both active in different fields. While they have various online profiles, a direct link to a personal LinkedIn profile is often indexed through their professional activities or institutional pages.

### **1. Jimmy Engström (Software Developer & Microsoft MVP)**
This Jimmy Engström is a well-known figure in the .NET development community, particularly for his work with **Blazor**.
*   **Professional Identity:** He is a developer, speaker, and author (e.g., *Web Development with Blazor*).
*   **Affiliations:** He is a long-time Microsoft Most Valuable Professional (MVP) and a co-host of the *Coding After Work* podcast and stream.
*   **Online Presence:** You can find him on platforms like [GitHub](https://github.com/EngstromJimmy) and through his speaking engagements at conferences such as NDC and Øredev. His professional activities are frequently linked to his social media presence, including Twitter (@EngstromJimmy) and LinkedIn.

### **2. Jimmy Engström (Researcher & Doctoral Student)**
This Jimmy Engström is an academic and researcher based at **Malmö University**, Sweden.
*   **Professional Identity:** He is a doctoral student at the Faculty of Technology and Society (Department of Computer Science and Media Technology).
*   **Background:** Before starting his industrial PhD in 2018, he worked extensively in the telecom industry (e.g., Ericsson, Sony) as an embedded software engineer, project manager, and data scientist.
*   **Research Focus:** His work focuses on Context Awareness, indoor positioning systems, and IoT.
*   **Institutional Profile:** His professional details are hosted on the [Malmö University research portal](https://mau.se/en/research/research-portal/researchers/28551065-27a3-4859-a29d-476722d3bb63/).

### **Other Mentions**
There is also a **Jimmy Engström** who serves as a **Director of Personal Lines Analytics Products at Verisk**, where he has worked for many years in insurance analytics and underwriting solutions.""",

  '"Jimmy Engström" site:github.com OR site:udemy.com/user OR site:medium.com': """Jimmy Engström is a prominent software developer, speaker, and author recognized for his expertise in .NET and Blazor development[1][2][3].

### GitHub Presence
Jimmy Engström is active on GitHub, where he maintains repositories related to his professional work and books[2][4][5].
*   **Profile:** [EngstromJimmy](https://github.com/EngstromJimmy)[4]
*   **Key Projects:** He has authored code repositories for his book series, *Web Development with Blazor* (spanning multiple editions)[2][5][6][7], and maintains projects like `Blazm.Components`[8].
*   **Community:** He is also reachable via GitHub Sponsors[9].

### Medium Presence
While he does not appear to maintain a primary blog on Medium, he is frequently mentioned and referenced in articles and book reviews within the platform[3][10][11].
*   **Mentions:** His book, *Web Development with Blazor*, is commonly cited in .NET resource lists and reviewed by tech writers on Medium[3][11].
*   **Activity:** He appears as a user on the platform[12][13], largely within the context of the .NET developer community.

### Udemy Presence
There is no direct instructor profile page found for "Jimmy Engström" on `udemy.com/user`. His educational impact is primarily concentrated through his books published by Packt and his contributions to the .NET community as a speaker and Microsoft MVP[2][5][3].

Sources:
[1] [github.com](https://github.com/EngstromJimmy)
[2] [github.com](https://github.com/EngstromJimmy)
[3] [medium.com](https://medium.com)
[4] [github.com](https://github.com/EngstromJimmy)
[5] [github.com](https://github.com/EngstromJimmy)
[6] [github.com](https://github.com/EngstromJimmy)
[7] [github.com](https://github.com/EngstromJimmy)
[8] [github.com](https://github.com/EngstromJimmy)
[9] [github.com](https://github.com/EngstromJimmy)
[10] [medium.com](https://medium.com)
[11] [medium.com](https://medium.com)
[12] [medium.com](https://medium.com)
[13] [medium.com](https://medium.com)""",

  '"Danny Staple" site:linkedin.com/in': """Danny Staple is a professional software engineer, robotics enthusiast, and author[1][2][3]. He is the director of **ODM Solutions**, a consultancy specializing in automation, software process, and DevOps[1][4].

### Key Professional Information
*   **Specializations:** Automation, DevOps, Python, IoT, and Infrastructure-as-Code[5][6].
*   **Author:** He has authored technical books on robotics, including *Learn Robotics Programming* and *Robotics at Home with Raspberry Pi Pico*, published by Packt Publishing[5][7][3].
*   **Robotics:** He runs the **Orionrobots** website and YouTube channel, where he shares projects involving Raspberry Pi, Arduino, and various robotics builds[4][8][3].
*   **Community:** He is active in tech communities, including Stack Overflow, and mentors at robotics clubs such as CoderDojo[9][3][10].

While a direct link to his LinkedIn profile was not returned in the search results, you can typically find him by searching "Danny Staple ODM Solutions" or "Danny Staple Orionrobots" on LinkedIn, as he references using the platform for contact[1].

Sources:
[1] [odmsolutions.co.uk](https://odmsolutions.co.uk)
[2] [packtpub.com](https://packtpub.com)
[3] [google.com](https://google.com)
[4] [github.io](https://github.io)
[5] [packt.com](https://packt.com)
[6] [packt.com](https://packt.com)
[7] [odmsolutions.co.uk](https://odmsolutions.co.uk)
[8] [youtube.com](https://youtube.com)
[9] [github.com](https://github.com)
[10] [stackoverflow.com](https://stackoverflow.com)""",

  '"Danny Staple" site:github.com OR site:udemy.com/user OR site:medium.com': """Danny Staple has a presence on GitHub, primarily associated with his work on robotics and programming books[1][2]. While he is frequently referenced in articles on Medium[3][4] and is an author of technical publications[5][6], there is no direct evidence of a personal user profile for him on Udemy within the requested search parameters.

### GitHub Presence
*   **Profile:** Danny Staple can be found on GitHub under the username **dannystaple**[1][7].
*   **Content:** His repositories often relate to his books, such as *Learn Robotics Programming*[5][8] and *Robotics at Home with Raspberry Pi Pico*[6]. These repositories provide code and resources for readers of his work[6][8].
*   **Community:** He has participated in various technical discussions and issues, including those for projects like Mu Editor and others[7][9][10].

### Medium & Udemy
*   **Medium:** While his name appears in Medium articles (often in reviews or discussions of his robotics books[3][4]), he does not appear to have an active personal blog or dedicated profile page under his name on the platform.
*   **Udemy:** There were no results for a "Danny Staple" user profile on Udemy.

Sources:
[1] [github.com](https://github.com/dannystaple)
[2] [github.com](https://github.com/dannystaple)
[3] [medium.com](https://medium.com)
[4] [medium.com](https://medium.com)
[5] [github.com](https://github.com/dannystaple)
[6] [github.com](https://github.com/dannystaple)
[7] [github.com](https://github.com/dannystaple)
[8] [github.com](https://github.com/dannystaple)
[9] [github.com](https://github.com/dannystaple)
[10] [github.com](https://github.com/dannystaple)""",

  '"Graeme Davidson" site:linkedin.com/in': """No results found for "Graeme Davidson" site:linkedin.com/in.""",

  '"Graeme Davidson" site:github.com OR site:udemy.com/user OR site:medium.com': """Graeme Davidson has a presence on GitHub under the username **graemedavidson**[1][2].

Key details regarding his GitHub activity include:

*   **Profile:** He is a developer with contributions in various technologies, including Go, Lua, and Python[1][3].
*   **Notable Projects:**
    *   **gitlab-mr-bot:** A webhook service for GitLab that assigns random reviewers to Merge Requests and sends notifications to Slack[1][4].
    *   **nvim-tmux:** A tool for testing Neovim setups[1][3].
    *   **grafana-k8-sidecar:** An archived project involving a Kubernetes operator sidecar for deploying Grafana dashboard resources[1][3].
*   **Other Contributions:** He has also been involved in projects such as `terraform-provider-freeipa`[5].

There were no direct results found for "Graeme Davidson" on `udemy.com/user` or `medium.com`.

Sources:
[1] [github.com](https://github.com/graemedavidson)
[2] [github.com](https://github.com/graemedavidson)
[3] [github.com](https://github.com/graemedavidson)
[4] [github.com](https://github.com/graemedavidson)
[5] [github.com](https://github.com/graemedavidson)""",

  '"Lei Ma" site:linkedin.com/in': """No public LinkedIn profiles were found matching the name "Lei Ma" using that search query.""",

  '"Lei Ma" site:github.com OR site:udemy.com/user OR site:medium.com': """The search for "Lei Ma" across GitHub and Medium reveals several different individuals who share this name, as well as academic references to a prominent researcher in software engineering and deep learning[1][2].

### GitHub Profiles
There are multiple GitHub users with the name Lei Ma or variations thereof:
*   **[microlei](https://github.com/microlei):** Associated with Harvard FAS Informatics, focused on R-based projects[3].
*   **[LeiMazizizi](https://github.com/LeiMazizizi):** A Ph.D. student in geospatial information sciences at the University of Gävle with interests in machine learning and web development[4].
*   **[yu-gi-oh-leilei (Lei-Lei Ma)](https://github.com/yu-gi-oh-leilei):** A researcher in multi-label learning who received their Ph.D. from Anhui University in 2025[5].
*   **[leima0521](https://github.com/leima0521):** An Assistant Professor of Real Estate at the University of Georgia[6].
*   **[malei0311](https://github.com/malei0311):** Describes themselves as a "code-warrior" and "tech-mage"[7].
*   **[ma-labo](https://github.com/ma-labo):** A research lab led by a Prof. Lei Ma[8].

### Medium Presence
Various individuals named Lei Ma have published on Medium, ranging from personal essays to technical data science articles:
*   **Technical Writing:** Some accounts feature articles on Python, data visualization (Bokeh), and customer segmentation[9][10].
*   **Academic Citations:** "Lei Ma" is frequently cited in technical Medium articles discussing research in deep learning, software testing (e.g., DeepGauge), and autonomous driving systems[1][2].
*   **Personal/Other:** Some profiles reflect personal narratives or general interests[11][12].

### Udemy
No specific public profile pages for a "Lei Ma" were indexed under `udemy.com/user` in this search.

Sources:
[1] [medium.com](https://medium.com)
[2] [medium.com](https://medium.com)
[3] [github.com](https://github.com/microlei)
[4] [github.com](https://github.com/LeiMazizizi)
[5] [github.com](https://github.com/yu-gi-oh-leilei)
[6] [github.com](https://github.com/leima0521)
[7] [github.com](https://github.com/malei0311)
[8] [github.com](https://github.com/ma-labo)
[9] [medium.com](https://medium.com)
[10] [medium.com](https://medium.com)
[11] [medium.com](https://medium.com)
[12] [medium.com](https://medium.com)""",

  '"Yousri El Fattah" site:linkedin.com/in': """No results found for "Yousri El Fattah" on linkedin.com/in.""",

  '"Yousri El Fattah" site:github.com OR site:udemy.com/user OR site:medium.com': """Yousri El Fattah is an author, researcher, and CEO of Causal Computing[1][2]. His work and presence can be found across the platforms you requested as follows:

### **GitHub**
*   **Profile:** He maintains a presence on GitHub under the username **yelfattah**[3][4].
*   **Key Content:** His repositories include materials related to his professional work and book collaborations, such as the code repository for his book, *Causal Inference with Bayesian Networks* (co-authored with Reza Bagheri)[1][5]. Other repositories reflect his interest in big data, iOS programming, and technology examples[5].

### **Medium**
*   While he does not appear to have a personal blog under his name on Medium, he is frequently referenced in articles on the platform—most notably in **Packt Hub** publications[6]. Recent articles discuss his book, *Causal Inference with Bayesian Networks*, highlighting its role in bridging theoretical and practical causal reasoning in AI[6][7].

### **Udemy**
*   There are no public instructor profiles found for "Yousri El Fattah" on `udemy.com/user`. While he has extensive experience teaching courses on artificial intelligence and control systems at various universities[1], his current educational outreach appears to be centered around his book and professional research[1][8].

Sources:
[1] [github.com](https://github.com/yelfattah)
[2] [github.com](https://github.com/yelfattah)
[3] [github.com](https://github.com/yelfattah)
[4] [github.com](https://github.com/yelfattah)
[5] [github.com](https://github.com/yelfattah)
[6] [medium.com](https://medium.com)
[7] [medium.com](https://medium.com)
[8] [github.com](https://github.com/yelfattah)"""
}

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
    if not os.path.exists(CACHE_FILE):
        print(f"Error: {CACHE_FILE} does not exist.")
        return

    with open(CACHE_FILE, 'r') as f:
        cache = json.load(f)

    print(f"Loaded existing cache from {CACHE_FILE} containing {len(cache)} entries.")

    for q, val in raw_responses.items():
        parsed = heuristic_parse(q, val)
        cache[q] = parsed

    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

    print(f"Successfully processed and appended 10 missing entries to {CACHE_FILE}. Total entries: {len(cache)}")

if __name__ == '__main__':
    main()
