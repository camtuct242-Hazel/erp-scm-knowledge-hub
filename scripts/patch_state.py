with open("outputs/app/app.js", "r", encoding="utf-8") as f:
    code = f.read()

target = "window.App = {\n    init: function() {"
replacement = "window.App = {\n    state: state,\n    init: function() {"

if target in code:
    code = code.replace(target, replacement)
elif target.replace("\n", "\r\n") in code:
    code = code.replace(target.replace("\n", "\r\n"), replacement.replace("\n", "\r\n"))
else:
    print("Not found directly, searching...")

with open("outputs/app/app.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated app.js with state exposure!")
