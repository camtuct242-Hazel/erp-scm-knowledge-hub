import glob
import os
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

def check_file_emojis(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    found = []
    for line_idx, line in enumerate(c.splitlines(), 1):
        for ch_idx, ch in enumerate(line):
            if is_emoji(ch):
                found.append((line_idx, ch, line.strip()))
    return found

tests = [
    ("outputs/app/index.html", 0, "All UI emojis removed"),
    ("outputs/app/app.js", 0, "All UI emojis and prompts removed"),
    ("outputs/app/style.css", 0, "All stylesheet emojis removed"),
    ("outputs/content/chapters/CHAP_01.md", 0, "Chapter 1 clean"),
    ("outputs/content/chapters/CHAP_02.md", 0, "Chapter 2 clean"),
    ("outputs/content/chapters/CHAP_03.md", 1, "Chapter 3: exactly 1 emoji in BA Note"),
    ("outputs/content/chapters/CHAP_04.md", 0, "Chapter 4 clean"),
    ("outputs/content/chapters/CHAP_05.md", 0, "Chapter 5 clean"),
    ("outputs/content/chapters/CHAP_06.md", 0, "Chapter 6 clean"),
    ("outputs/app/data.js", 1, "App data: exactly 1 emoji in BA Note"),
]

for json_fp in glob.glob("outputs/data/*.json"):
    tests.append((json_fp, 0, f"{os.path.basename(json_fp)} clean"))

all_passed = True
print("=" * 60)
print("PHASE 1 EMOJI VALIDATION SUITE")
print("=" * 60)

for filepath, expected_count, desc in tests:
    found = check_file_emojis(filepath)
    actual_count = len(found)
    passed = (actual_count == expected_count)
    if not passed:
        all_passed = False
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {desc}: {filepath} (Expected: {expected_count}, Got: {actual_count})")
    for line_no, ch, line in found:
        print(f"       -> L{line_no} [{ch}]: {line[:70]}")

print("=" * 60)
if all_passed:
    print("ALL PHASE 1 EMOJI CHECKS PASSED PERFECTLY!")
else:
    print("SOME CHECKS FAILED!")
print("=" * 60)
