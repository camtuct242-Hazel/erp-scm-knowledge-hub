import urllib.request
import json

url = 'https://api.github.com/users/camtuct242-Hazel/repos?per_page=100'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        repos = json.loads(response.read().decode('utf-8'))
        print('Public repos for camtuct242-Hazel:')
        for r in repos:
            print(f" - {r['name']}: {r['html_url']} (branch: {r['default_branch']})")
except Exception as e:
    print('Error:', e)
