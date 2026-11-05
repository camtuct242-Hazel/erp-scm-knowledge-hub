with open('outputs/documentation/TEST_REPORT.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('## 3. Kết Luận & Đánh Giá Nghiệm Thu')
print(text[idx-200:idx+300])
