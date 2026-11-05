import urllib.request

try:
    url = "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        content = resp.read()
        print("Success fetching KaTeX! Length:", len(content))
except Exception as e:
    print("Error fetching:", e)
