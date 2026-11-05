import json

with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'window.APP_DATA = '
if text.startswith('//'):
    line1_end = text.find('\n')
    text = text[line1_end+1:].strip()
if text.startswith(prefix):
    text = text[len(prefix):].strip()
if text.endswith(';'):
    text = text[:-1].strip()

app_data = json.loads(text)
fc = app_data.get('flashcards', [])
print("Flashcards in data.js:", len(fc))
if fc:
    print(json.dumps(fc[0], indent=2, ensure_ascii=False))
