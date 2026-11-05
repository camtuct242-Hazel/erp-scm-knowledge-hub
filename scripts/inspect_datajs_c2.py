import json, re

with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

m = re.search(r'window\.APP_DATA\s*=\s*(\{.*\});', data_js, re.DOTALL)
if m:
    app_data = json.loads(m.group(1))
    c2 = app_data.get('chapterContents', {}).get('chap-02', '')
    print("chap-02 in data.js:")
    print("  tab count:", c2.count('\t'))
    print("  'ext' count:", c2.count('ext'))
    # search for imes
    print("  'imes' occurrences:")
    for match in re.finditer(r'(.{0,15}imes.{0,15})', c2):
        print("   ", repr(match.group(1)))
    print("  'ext' occurrences:")
    for match in re.finditer(r'([^\s$]{0,10}ext[^\s$]{0,10})', c2):
        if not any(k in match.group(1) for k in ['text', 'Next', 'context', 'external']):
            print("   ", repr(match.group(1)))
