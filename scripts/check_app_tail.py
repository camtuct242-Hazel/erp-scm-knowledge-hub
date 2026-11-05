with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Last 25 lines of app.js:")
for l in lines[-25:]:
    print(l, end="")
