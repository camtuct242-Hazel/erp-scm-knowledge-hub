import json
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

for fp in glob.glob('outputs/data/*.json'):
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()
    emos = set(ch for ch in text if is_emoji(ch))
    if emos:
        print(f"{fp}: {len(emos)} distinct emojis: {emos}")
    else:
        print(f"{fp}: No emojis found")
