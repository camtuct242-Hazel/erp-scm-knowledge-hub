import os
import glob
import re

# ==============================================================================
# 1. CLEAN EMOJIS IN outputs/app/index.html
# ==============================================================================
with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html_replacements = [
    ('⏱️ <span id="nav-timer-val">30:00</span>', '<span id="nav-timer-val">30:00</span>'),
    ('📑 <span data-i18n="btn_chapter_list">Danh sách chương</span>', '<span data-i18n="btn_chapter_list">Danh sách chương</span>'),
    ('⏱️ <span id="active-timer-display">30:00</span>', '<span id="active-timer-display">30:00</span>'),
    ('🚩 <span data-i18n="btn_flag_q">Xem lại sau</span>', '<span data-i18n="btn_flag_q">Xem lại sau</span>'),
    ('🔀 <span data-i18n="btn_shuffle">Trộn Thẻ</span>', '<span data-i18n="btn_shuffle">Trộn Thẻ</span>'),
    ('<option value="all">📚 Tất Cả Các Chương (All Chapters)</option>', '<option value="all" data-i18n="opt_all_chapters">Tất Cả Các Chương (All Chapters)</option>'),
    ('<span data-i18n="fc_filter_needs_review">⏳ Cần Ôn Lại</span>', '<span data-i18n="fc_filter_needs_review">Cần Ôn Lại</span>'),
    ('💡 Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án', 'Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án'),
    ('❌ <span data-i18n="btn_needs_review">Cần Ôn Lại</span>', '<span data-i18n="btn_needs_review">Cần Ôn Lại</span>'),
    ('placeholder="🔍 Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa..."', 'placeholder="Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa..."'),
    ('📄 <span data-i18n="tab_full_analysis">Nội Dung Đầy Đủ & Phân Tích BA</span>', '<span data-i18n="tab_full_analysis">Nội Dung Đầy Đủ & Phân Tích BA</span>'),
    ('🧮 <span data-i18n="tab_interactive_calc">Bộ Tính Toán Mô Phỏng Tương Tác</span>', '<span data-i18n="tab_interactive_calc">Bộ Tính Toán Mô Phỏng Tương Tác</span>'),
    ('🧹 <span data-i18n="btn_clear_chat">Xóa Hội Thoại</span>', '<span data-i18n="btn_clear_chat">Xóa Hội Thoại</span>'),
    ('⚙️ <span data-i18n="btn_api_settings">Cấu hình API Key (Tùy chọn)</span>', '<span data-i18n="btn_api_settings">Cấu hình API Key (Tùy chọn)</span>'),
    ('<span id="chat-mode-badge" class="badge badge-beige">🤖 Chế độ Tri thức Offline (Grounded Mode)</span>', '<span id="chat-mode-badge" class="badge badge-beige">Chế độ Tri thức Offline (Grounded Mode)</span>'),
    ('<span style="font-weight: 600; color: var(--coffee-bean);">🎯 Ngữ cảnh tham vấn:</span>', '<span style="font-weight: 600; color: var(--coffee-bean);" data-i18n="consultant_context_label">Ngữ cảnh tham vấn:</span>'),
    ('💡 Chọn mẫu kịch bản để đưa prompt vào ô soạn thảo:', 'Chọn mẫu kịch bản để đưa prompt vào ô soạn thảo:'),
    ('<span data-i18n="btn_send">Gửi</span> ➔', '<span data-i18n="btn_send">Gửi</span>')
]

for old, new in html_replacements:
    assert old in html, f"Target not found in index.html: {old}"
    html = html.replace(old, new)

with open('outputs/app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html emoji cleanup complete.")


# ==============================================================================
# 2. CLEAN EMOJIS IN outputs/app/app.js
# ==============================================================================
with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

app_replacements = [
    ('btn_reveal_answer: "💡 Xem đáp án và giải thích"', 'btn_reveal_answer: "Xem đáp án và giải thích"'),
    ('fc_hint_flip: "💡 Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án"', 'fc_hint_flip: "Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án"'),
    ('btn_reveal_answer: "💡 Reveal answer and explanation"', 'btn_reveal_answer: "Reveal answer and explanation"'),
    ('fc_hint_flip: "💡 Click the card or press Spacebar to flip and reveal answer"', 'fc_hint_flip: "Click the card or press Spacebar to flip and reveal answer"'),
    ("'glossary-search': lang === 'vi' ? '🔍 Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa...' : '🔍 Search terms, acronyms, definitions...'", "'glossary-search': lang === 'vi' ? 'Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa...' : 'Search terms, acronyms, definitions...'"),
    ('⏱️ ${chap.reading_time_minutes} min', '${chap.reading_time_minutes} min'),
    ('📖 ${chap.reading_time_minutes} mins', '${chap.reading_time_minutes} mins'),
    ("📖 ${state.lang === 'vi' ? 'Luyện tập' : 'Practice'}", "${state.lang === 'vi' ? 'Luyện tập' : 'Practice'}"),
    ("⏱️ ${state.lang === 'vi' ? 'Thi 30 phút' : 'Timed Test'}", "${state.lang === 'vi' ? 'Thi 30 phút' : 'Timed Test'}"),
    (": (state.lang === 'vi' ? '⏳ Cần ôn tập' : 'Needs Review');", ": (state.lang === 'vi' ? 'Cần ôn tập' : 'Needs Review');"),
    ("exEl.innerHTML = `<strong>💡 ${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Example:'}</strong>`", "exEl.innerHTML = `<strong>${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Example:'}</strong>`"),
    ("<span><strong>#${i + 1} ${r.name}</strong> ${r.isBest ? '🏆 (OPTIMAL)' : ''}</span>", "<span><strong>#${i + 1} ${r.name}</strong> ${r.isBest ? '(OPTIMAL)' : ''}</span>"),
    ("modeBadge.innerText = `✨ ${state.lang === 'vi' ? 'Chế độ Live API' : 'Live AI API'} (${state.customProvider})`;", "modeBadge.innerText = `${state.lang === 'vi' ? 'Chế độ Live API' : 'Live AI API'} (${state.customProvider})`;"),
    ("modeBadge.innerText = `🤖 ${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Knowledge Mode'}`;", "modeBadge.innerText = `${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Knowledge Mode'}`;"),
    ("<span>${sc.icon}</span>\n          <span>${sc.label}</span>", "<span>${sc.label}</span>"),
    ("<span>🤖</span>", "<span class=\"chat-avatar-badge\">AI</span>"),
    ("<p>💡 <em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc tự nhập câu hỏi nghiệp vụ / bài toán SCM của bạn vào khung bên dưới.</em></p>", "<p><em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc tự nhập câu hỏi nghiệp vụ / bài toán SCM của bạn vào khung bên dưới.</em></p>"),
    ("const modeBadgeText = msg.mode === 'live' ? '✨ Live AI API' : '🤖 Offline Grounded';", "const modeBadgeText = msg.mode === 'live' ? 'Live AI API' : 'Offline Grounded';"),
    ("<span>${isUser ? '👤' : '🤖'}</span>", "<span class=\"chat-avatar-badge\">${isUser ? 'You' : 'AI'}</span>"),
    ("⚡ Đang truy vấn cơ sở tri thức ERP & giải toán...", "Đang truy vấn cơ sở tri thức ERP & giải toán..."),
    ("return `### 📑 Phân Tích Chuyên Sâu Tình Huống Texago Corp. (Site Selection)", "return `### Phân Tích Chuyên Sâu Tình Huống Texago Corp. (Site Selection)"),
    ("return `### 📑 Phân Tích Mô Hình Sản Xuất Kinh Tế EPQ (Công Ty SOCA)", "return `### Phân Tích Mô Hình Sản Xuất Kinh Tế EPQ (Công Ty SOCA)"),
    ("return `### 📑 Phân Tích Quản Trị Tồn Kho Khoa Học (Atlantic Coast Tire - ACT)", "return `### Phân Tích Quản Trị Tồn Kho Khoa Học (Atlantic Coast Tire - ACT)"),
    ("return `### 📑 Phân Tích Tình Huống Better Products Company (Case 2.1 vs Case 2.2)", "return `### Phân Tích Tình Huống Better Products Company (Case 2.1 vs Case 2.2)"),
    ("return `### 💡 Bản Chất Kiến Trúc 3 Tầng Của Hệ Thống ERP Hiện Đại", "return `### Bản Chất Kiến Trúc 3 Tầng Của Hệ Thống ERP Hiện Đại"),
    ("return `### 💡 Đồng Bộ Quy Trình Doanh Nghiệp Cốt Lõi: O2C & P2P Trong ERP", "return `### Đồng Bộ Quy Trình Doanh Nghiệp Cốt Lõi: O2C & P2P Trong ERP"),
    ("return `### 🤖 Phân Tích & Hướng Dẫn Học Tập ERP & SCM", "return `### Phân Tích & Hướng Dẫn Học Tập ERP & SCM"),
]

# Also clean icon: '...' from scenarios
app_js = re.sub(r"icon:\s*'[^']+',\s*", "", app_js)

app_norm = app_js.replace('\r\n', '\n')
for old, new in app_replacements:
    old_norm = old.replace('\r\n', '\n')
    new_norm = new.replace('\r\n', '\n')
    if old_norm in app_norm:
        app_norm = app_norm.replace(old_norm, new_norm, 1)
    else:
        print(f"Warning: app.js target not found: {old[:50]}")

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(app_norm)
print("app.js emoji cleanup complete.")


# ==============================================================================
# 3. CLEAN EMOJIS IN outputs/content/chapters/*.md
# ==============================================================================
for chap_fp in sorted(glob.glob('outputs/content/chapters/*.md')):
    with open(chap_fp, 'r', encoding='utf-8') as f:
        chap_c = f.read()
    
    old_str = '<span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>'
    new_str = '<span class="btn-reveal-text">Xem đáp án và giải thích / Reveal answer and explanation</span>'
    if old_str in chap_c:
        chap_c = chap_c.replace(old_str, new_str)
        with open(chap_fp, 'w', encoding='utf-8') as f:
            f.write(chap_c)
        print(f"Cleaned reveal button emoji in {chap_fp}")

# ==============================================================================
# 4. CLEAN EMOJIS IN outputs/app/data.js
# ==============================================================================
with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
    data_c = f.read()

old_data_str = '<span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>'
new_data_str = '<span class="btn-reveal-text">Xem đáp án và giải thích / Reveal answer and explanation</span>'
if old_data_str in data_c:
    data_c = data_c.replace(old_data_str, new_data_str)
    with open('outputs/app/data.js', 'w', encoding='utf-8') as f:
        f.write(data_c)
    print("Cleaned reveal button emojis in outputs/app/data.js")

# ==============================================================================
# 5. CLEAN EMOJIS IN outputs/documentation/CHAPTER_CONTENT_AUDIT.md
# ==============================================================================
audit_doc = 'outputs/documentation/CHAPTER_CONTENT_AUDIT.md'
if os.path.exists(audit_doc):
    with open(audit_doc, 'r', encoding='utf-8') as f:
        audit_c = f.read()
    audit_c = audit_c.replace('💡', '').replace('📑', '')
    with open(audit_doc, 'w', encoding='utf-8') as f:
        f.write(audit_c)
    print("Cleaned decorative emojis in CHAPTER_CONTENT_AUDIT.md")
