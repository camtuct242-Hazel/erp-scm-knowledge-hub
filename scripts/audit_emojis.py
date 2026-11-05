import re
import os
import glob
import unicodedata

# Comprehensive emoji regex pattern
# Note: we should avoid matching standard mathematical symbols, arrows (e.g. ->, ←, →, ↔, ≤, ≥, √, ∑, ∫, etc.), and Greek letters.
# Emojis are generally in:
# - Enclosed Alphanumeric Supplement, Miscellaneous Symbols and Arrows
# - Dingbats: 2700-27BF (except standard math/bullets if needed, but check specifically)
# - Miscellaneous Symbols: 2600-26FF (e.g. ⏱, ⚠️, ☕, ⚡, etc.)
# - Supplemental Symbols and Pictographs: 1F000-1F9FF
# - Symbols and Pictographs Extended-A: 1FA00-1FAFF
# - Transport and Map: 1F680-1F6FF
# - Emoticons: 1F600-1F64F

def is_emoji(char):
    cp = ord(char)
    # Exclude normal ASCII, Latin-1, Greek, Math operators, arrows
    # Common math/arrows to NOT treat as emoji:
    # ← (8592), ↑ (8593), → (8594), ↓ (8595), ↔ (8596), ⇐, ⇒, ⇔
    # √ (8730), ∞ (8734), ≤ (8804), ≥ (8805), ± (177), × (215), ÷ (247), • (8226), … (8230)
    # ✓ (10003), ✕ (10005) - sometimes dingbats, check usage: ✓ and ✕ are used as text checkmarks/crosses.
    if cp in (8592, 8593, 8594, 8595, 8596, 8656, 8658, 8660, 8730, 8734, 8804, 8805, 177, 215, 247, 8226, 8230, 10003, 10005):
        return False
    # Check unicode category or ranges
    cat = unicodedata.category(char)
    # 'So' = Symbol, other; 'Sk' = Symbol, modifier
    # Emoji ranges:
    if 0x1F300 <= cp <= 0x1FAFF: # Pictographs, emoticons, symbols
        return True
    if 0x2600 <= cp <= 0x26FF: # Misc symbols (e.g. ⏱, ⚠️, ⚡, ☕, ⚓, ✈, ⏳)
        return True
    if 0x2700 <= cp <= 0x27BF: # Dingbats (e.g. ✏️, ✒️, ✂️, 💡, ❓, ❗, etc.)
        # exclude ✓ (10003), ✕ (10005)
        if cp in (10003, 10004, 10005, 10006, 10007, 10008):
            return False
        return True
    if 0x1F1E6 <= cp <= 0x1F1FF: # Flags
        return True
    if 0x2300 <= cp <= 0x23FF: # Miscellaneous Technical (e.g. ⏰, ⏱, ⏳)
        if cp in (0x231A, 0x231B, 0x23E9, 0x23EA, 0x23EB, 0x23EC, 0x23F0, 0x23F3, 0x23F1, 0x23F2):
            return True
    return False

def find_emojis_in_file(filepath):
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            emojis_in_line = []
            for idx, ch in enumerate(line):
                if is_emoji(ch):
                    emojis_in_line.append((idx, ch, ord(ch), unicodedata.name(ch, 'UNKNOWN')))
            if emojis_in_line:
                results.append((line_no, line.strip(), emojis_in_line))
    return results

files_to_check = [
    'outputs/app/index.html',
    'outputs/app/app.js',
    'outputs/app/style.css',
    'outputs/app/data.js',
] + glob.glob('outputs/content/chapters/*.md') + glob.glob('outputs/data/*.json')

print(f"Scanning {len(files_to_check)} files for emojis...")
all_findings = {}
for fp in files_to_check:
    findings = find_emojis_in_file(fp)
    if findings:
        all_findings[fp] = findings
        print(f"\n--- {fp}: {len(findings)} lines with emojis ---")
        for line_no, line_text, emojis in findings[:10]:
            emo_chars = ''.join(e[1] for e in emojis)
            print(f"  L{line_no}: [{emo_chars}] {line_text[:80]}")
        if len(findings) > 10:
            print(f"  ... and {len(findings) - 10} more lines")
