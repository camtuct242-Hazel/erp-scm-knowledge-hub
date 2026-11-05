import subprocess

with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

print("app.js size:", len(app_js), "chars")
print("data.js size:", len(data_js), "chars")
