for name in ['CASE_01_TEXAGO.md', 'CASE_02_BETTER_PRODUCTS.md', 'CASE_03_ACT_TIRE.md', 'CASE_04_SOCA.md']:
    path = f'outputs/content/case-studies/{name}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    has_code_block = '```text' in content
    print(f"{name}: has ```text: {has_code_block}, length: {len(content)}")
