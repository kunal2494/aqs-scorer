import urllib.request
import json
import math
import os

api_key = os.environ.get("GEMINI_API_KEY", "")
model = "gemini-3.1-flash-lite"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

# Simplified AQS guide for lightweight model
simplified_aqs_guide = """
You are scoring an author on 12 dimensions (D1 to D12) using a 0-100% scale. Below are strict evidence-based scoring rules:

D1 Thought Leadership (Weight: 41.4)
- 10-25%: Local/company leader, basic seniority.
- 30-60%: Recognized industry expert, book author, course creator.
- 60-80%: Regional/national speaker, multiple books, major authority.
- 80%+: Global influencer, keynote speaker, creator of major technologies.

D2 Tech Demand (Weight: 33.0)
- 10-30%: Niche/legacy tech.
- 30-60%: Standard tech (e.g. general web, standard languages, databases).
- 60-90%: High growth (e.g. Cloud, Security, DevOps, Go, Rust, Swift).
- 90%+: Hyper-demand (e.g. Generative AI, LLMs, Advanced Cybersec).

D3 Alignment (Weight: 27.6)
- 10-30%: Indirect fit to the book title.
- 30-60%: Moderate fit, some matching experience.
- 60-90%: High fit, direct expert in the book topic.
- 90%+: Perfect fit, world-class alignment.

D4 Experience (Weight: 27.6)
- 10-30%: 1-5 years.
- 30-60%: 5-10 years.
- 60-80%: 10-15 years.
- 80-90%: 15-20 years.
- 90%+: >20 years.

D5 Expertise (Weight: 27.6)
- 10-30%: Intermediate developer/practitioner.
- 30-60%: Senior developer/architect.
- 60-90%: Principal engineer, Director, Subject Matter Expert.
- 90%+: Leading global authority.

D6 Recognition (Weight: 21.9)
- 10-30%: Company level awards.
- 30-60%: Certified professional, MVP, minor speaker.
- 60-90%: Major certifications (e.g. AWS Solutions Architect, CISA), MVP, speaker at large conferences.
- 90%+: International awards, keynotes.

D7 Innovation (Weight: 24.0)
- 10-30%: Standard commercial work.
- 30-60%: Contributes to open source, minor innovations.
- 60-90%: Creator of popular libraries, core contributor.
- 90%+: Creator of major framework/language.

D8 Publications (Weight: 11.1)
- 10-30%: Blog posts, documentation.
- 30-60%: 1 technical book or course published.
- 60-90%: 2-5 technical books or courses.
- 90%+: >5 books.

D9 Reach (Weight: 54.9) -> USE VERIFIED REACH METRICS EXACTLY:
- 0-10%: No reach evidence/Unknown.
- 10-20%: <1k followers/students.
- 20-30%: 1k-5k followers/students.
- 30-40%: 5k-20k followers/students.
- 40-50%: 20k-50k followers/students.
- 50-60%: 50k-75k followers/students.
- 60-70%: 75k-100k followers/students.
- 70-79%: 100k-200k followers/students.
- 80-89%: 200k-500k followers/students.
- 90%+: >500k followers/students.

D10 Writing Quality (Weight: 16.5)
- 10-30%: Basic documentation/comments.
- 30-60%: Clean articles, tutorials.
- 60-90%: Engaging writer, well-structured books.

D11 Academic Credentials (Weight: 11.1)
- 10-30%: Self-taught or certifications.
- 30-60%: Bachelor's degree in CS/engineering.
- 60-80%: Master's degree in CS/engineering.
- 80-90%: Ph.D. or top-tier university degree.

D12 Cross-disciplinary Reach (Weight: 3.3)
- 10-30%: Niche tech focus only.
- 30-60%: Tech + management or business.
- 60-90%: Multidisciplinary (Tech + Art/Health/Law).
"""

system_prompt = f"""You are an expert acquisitions editor. You use the AQS scoring system to assess technical professionals using the DA12 framework.
{simplified_aqs_guide}

Respond ONLY in JSON format of this structure:
{{
  "dimensions": {{
    "D1": {{"score_percent": <int>, "justification": "..."}},
    ...
    "D12": {{"score_percent": <int>, "justification": "..."}}
  }}
}}
"""

user_content = """Here is the profile for Fuheng Wu:
Name: Fuheng Wu
Title: Clean Architecture in Swift
Bio: iOS Engineer with years of experience.
LinkedIn Followers: 0
GitHub Followers: 70
Udemy Students: 0
YouTube Subscribers: 0

Search snippets:
- Fuheng Wu is the author of Clean Architecture in Swift, published by Packt.
- Henry Wu (Fuheng Wu) is a Senior iOS Engineer at various companies with over 10 years of experience.
- He has a GitHub profile with 70 followers and several iOS repositories.
"""

payload = {
    "contents": [{
        "parts": [{"text": system_prompt + "\n\n" + user_content}]
    }],
    "generationConfig": {
        "responseMimeType": "application/json",
        "temperature": 0.1
    }
}

req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=30) as response:
        res_data = response.read().decode('utf-8')
        res_json = json.loads(res_data)
        text_response = res_json["candidates"][0]["content"]["parts"][0]["text"]
        scores_data = json.loads(text_response)
        
        DIM_WEIGHTS = {
            "D1": 41.4, "D2": 33.0, "D3": 27.6, "D4": 27.6, "D5": 27.6, "D6": 21.9,
            "D7": 24.0, "D8": 11.1, "D9": 54.9, "D10": 16.5, "D11": 11.1, "D12": 3.3
        }
        
        total_aqs = 0
        print("\nDimension Scores:")
        for dim, data in scores_data["dimensions"].items():
            pct = data["score_percent"]
            weight = DIM_WEIGHTS[dim]
            pts = math.floor((pct / 100.0) * weight)
            total_aqs += pts
            print(f"  {dim}: Pct={pct}%, Pts={pts} ({data['justification'][:50]}...)")
        print("\nTotal Computed AQS:", total_aqs)
except Exception as e:
    print("Error:", e)
