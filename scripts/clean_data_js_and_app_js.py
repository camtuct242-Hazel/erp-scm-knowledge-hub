# 1. Clean app.js line 2046 (typing indicator)
with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_c = f.read()

assert '<span>🤖</span>' in app_c, '<span>🤖</span> not found in app.js'
app_c = app_c.replace('<span>🤖</span>', '<span class="chat-avatar-badge">AI</span>')

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(app_c)
print("app.js typing indicator emoji cleaned.")

# 2. Clean 12 reveal button emojis in data.js
with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    data_c = f.read()

target = 'class=\\"btn-reveal-text\\">💡 Xem đáp án và giải thích / Reveal answer and explanation'
replacement = 'class=\\"btn-reveal-text\\">Xem đáp án và giải thích / Reveal answer and explanation'

count = data_c.count(target)
print(f"Found {count} occurrences of target in data.js")
assert count == 12, f"Expected 12 occurrences, found {count}"

data_c = data_c.replace(target, replacement)

with open('outputs/app/data.js', 'w', encoding='utf-8') as f:
    f.write(data_c)
print("data.js 12 reveal button emojis cleaned.")
