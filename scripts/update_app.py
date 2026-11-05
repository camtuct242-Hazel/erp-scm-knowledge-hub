with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "if (q.includes('act') || q.includes('tire') || q.includes('lốp') || q.includes('rop') || q.includes('wilson') || state.chatContextCase === 'CASE-03') {"
repl = "if (q.includes('act') || q.includes('tire') || q.includes('lốp') || q.includes('rop') || q.includes('wilson') || q.includes('eoq') || q.includes('tồn kho') || q.includes('inventory') || state.chatContextCase === 'CASE-03') {"

if target in text:
    text = text.replace(target, repl, 1)
    with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("app.js updated successfully")
else:
    print("target not found")
