import re

with open("outputs/app/app.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's test parsing JavaScript using a JS engine or checking template literals
print("Scanning app.js...")

# Find all template strings or test running in Edge via CDP
# Replace the unescaped backticks in line 1620 first
bad_str = "- `Số lượng Hóa đơn <= Số lượng Nhập kho (GR)`\\n- `Đơn giá Hóa đơn == Đơn giá PO`"
good_str = "- \\`Số lượng Hóa đơn <= Số lượng Nhập kho (GR)\\`\\n- \\`Đơn giá Hóa đơn == Đơn giá PO\\`"

if bad_str in content:
    print("Found bad string in line 1620! Fixing...")
    content = content.replace(bad_str, good_str)
    with open("outputs/app/app.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed line 1620.")
else:
    print("bad_str not found directly, let's search with regex")
