import os, re

files_to_check = [
    'outputs/content/chapters/CHAP_01.md',
    'outputs/content/chapters/CHAP_02.md',
    'outputs/content/chapters/CHAP_03.md',
    'outputs/content/chapters/CHAP_04.md',
    'outputs/content/chapters/CHAP_05.md',
    'outputs/content/chapters/CHAP_06.md',
    'outputs/data/chapters.json',
    'outputs/app/data.js'
]

tab_patterns = [
    (r'\text', '\text'),
    (r'\times', '\times'),
    (r'\to', '\to'),
    (r'\tau', '\tau'),
    (r'\theta', '\theta')
]

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n=== Checking {filepath} ===")
    # Check for \t followed by ext, imes, o, au, heta
    m_ext = re.findall(r'(\S{0,10}\text[^\s$]{0,10})', content)
    m_imes = re.findall(r'(\S{0,10}\times[^\s$]{0,10})', content)
    m_to = re.findall(r'(\S{0,10}\to[^\s$]{0,10})', content)
    
    # Also check for \b followed by egin, eta, etc.
    m_begin = re.findall(r'(\S{0,10}\begin[^\s$]{0,10})', content)
    
    # Also check for raw tab characters
    tab_count = content.count('\t')
    print(f"Total tab characters: {tab_count}")
    
    if m_ext:
        print(f"  Found '\\t' + 'ext' ({len(m_ext)}): {m_ext[:5]}")
    if m_imes:
        print(f"  Found '\\t' + 'imes' ({len(m_imes)}): {m_imes[:5]}")
    if m_to:
        print(f"  Found '\\t' + 'o' ({len(m_to)}): {m_to[:5]}")
    if m_begin:
        print(f"  Found '\\x08' + 'egin' ({len(m_begin)}): {m_begin[:5]}")
