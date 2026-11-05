with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    text = f.read()
import json, re
m = re.search(r'window\.APP_DATA\s*=\s*(\{.*\});', text, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    c34 = next(c for c in data['flashcards'] if c['id'] == 'FC-034')
    print('FC-034 keys and values:')
    for k in ['question_vi', 'question_en', 'answer_vi', 'answer_en', 'front', 'back']:
        print(f"  {k}: {repr(c34.get(k))}")
