with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Head lines:")
for l in lines[:35]:
    print(l, end="")

print("\nLast 35 lines:")
for l in lines[-35:]:
    print(l, end="")
