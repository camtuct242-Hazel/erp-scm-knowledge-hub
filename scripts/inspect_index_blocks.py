with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

def find_block(pattern, text):
    m = re.search(pattern, text)
    if m:
        start = max(0, m.start() - 50)
        end = min(len(text), m.end() + 200)
        print(f"--- MATCH {pattern} ---")
        print(text[start:end])

find_block(r'<head>', text)
find_block(r'id="view-flashcards"', text)
find_block(r'id="view-consultant"', text)
find_block(r'<footer class="app-footer">', text)
