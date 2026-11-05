import json

with open('outputs/data/chapters.json', 'r', encoding='utf-8') as f:
    text = f.read()

print("In chapters.json:", 'Nhận xét của BA' in text or 'Case 2.2' in text)
