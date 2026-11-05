with open('outputs/content/case-studies/CASE_04_SOCA.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines 200-244 of CASE_04_SOCA.md:")
for i in range(200, len(lines)):
    print(f"{i+1}: {lines[i]}", end="")
