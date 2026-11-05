with open('scripts/full_browser_interaction_test.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("Lines 1-60 of full_browser_interaction_test.py:")
lines = text.split('\n')
for l in lines[:60]:
    print(l)
