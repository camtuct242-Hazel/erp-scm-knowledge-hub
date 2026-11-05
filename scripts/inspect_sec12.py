for i in range(1, 7):
    fn = f'outputs/content/chapters/CHAP_0{i}.md'
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = text.find('12. Bài kiểm tra nhanh')
    if idx == -1:
        idx = text.find('12.')
    print(f"\n==================== {fn} (Section 12) ====================")
    if idx != -1:
        print(text[idx:idx+1000])
    else:
        print("Not found Section 12!")
