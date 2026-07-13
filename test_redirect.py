import urllib.request
import urllib.parse

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ZYU-HnvOULaf7TO0E11zhO5OuZsb9w6hnbLhqsZjntunsYXQaOY1-QcoDkcAsRBRmu145CGxv9zP8VkBjwTtvZXgN3jz-LpwbVvXIGUi1pMc-MhUsupkDpH8Az6ABZM="

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        print("Final URL:", response.geturl())
except Exception as e:
    print("Error:", e)
