with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

pos = 0
for i, l in enumerate(lines):
    if 'renderconsultantview' in l.lower():
        pos = i
        break

print(f"renderConsultantView at line {pos+1}")
for j in range(pos, min(len(lines), pos + 120)):
    print(f"{j+1}: {lines[j]}", end="")
