import os
import glob
import unicodedata

def is_emoji(char):
    cp = ord(char)
    if cp in (8592, 8593, 8594, 8595, 8596, 8656, 8658, 8660, 8730, 8734, 8804, 8805, 177, 215, 247, 8226, 8230, 10003, 10005):
        return False
    if 0x1F300 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x26FF or 0x2700 <= cp <= 0x27BF or 0x1F1E6 <= cp <= 0x1F1FF:
        if cp in (10003, 10004, 10005, 10006, 10007, 10008):
            return False
        return True
    if 0x2300 <= cp <= 0x23FF and cp in (0x231A, 0x231B, 0x23E9, 0x23EA, 0x23EB, 0x23EC, 0x23F0, 0x23F3, 0x23F1, 0x23F2):
        return True
    return False

all_files = []
for root, dirs, files in os.walk('outputs'):
    if 'backup_before_enhancement' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.css', '.json', '.md')):
            all_files.append(os.path.join(root, file))

print(f"Checking {len(all_files)} total files in outputs/...")
file_emoji_counts = {}
for fp in sorted(all_files):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    emos = [ch for ch in content if is_emoji(ch)]
    if emos:
        file_emoji_counts[fp] = (len(emos), set(emos))
        print(f"  {fp}: {len(emos)} emojis {set(emos)}")

if not file_emoji_counts:
    print("No emojis in any files!")
