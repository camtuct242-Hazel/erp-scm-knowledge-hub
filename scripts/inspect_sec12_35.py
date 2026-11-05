for i in [3, 5]:
    fn = f'outputs/content/chapters/CHAP_0{i}.md'
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = text.find('## 12. Kiểm tra Đánh giá Kiến thức')
    print(f"\n==================== {fn} (Section 12) ====================")
    print(text[idx:idx+800])
