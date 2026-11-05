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
print("APP_DATA keys:", list(app_data.keys()))
for k in app_data:
    if isinstance(app_data[k], list):
        print(f"  {k}: list of {len(app_data[k])} items")
        if len(app_data[k]) > 0:
            print(f"    sample item keys: {list(app_data[k][0].keys())}")
    elif isinstance(app_data[k], dict):
        print(f"  {k}: dict with keys {list(app_data[k].keys())}")
    else:
        print(f"  {k}: {type(app_data[k])}")
