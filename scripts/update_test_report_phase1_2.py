import shutil

with open('outputs/documentation/TEST_REPORT.md', 'r', encoding='utf-8') as f:
    tr = f.read()

sec_2_12 = '''### 2.12 Dọn Sạch Emoji Giao Diện & Xác Thực Triển Khai GitHub (Phase 1 & Phase 2)
- **Phương pháp**: Rà soát tự động toàn bộ 37 tệp tin mã nguồn, Markdown và JSON trong `outputs/` bằng bộ công cụ Unicode Classifier (`scripts/scan_all_outputs_emojis.py` và `scripts/test_emojis_phase1.py`), kết hợp kiểm thử hồi quy trình duyệt Edge Headless qua CDP.
- **Tổng quan dọn dẹp Emoji (Phase 1)**:
  - Loại bỏ hoàn toàn 71 emoji trang trí mang tính biểu tượng/gạch đầu dòng/nhãn nút khỏi toàn bộ giao diện: Thanh điều hướng, Trang chủ, Đầu mục chương, Thẻ Flashcards, Từ điển Glossary, Đề thi trắc nghiệm, Hồ sơ Tình huống Case Studies, Trợ lý AI và Chân trang.
  - Thay thế biểu tượng cảm xúc bằng nhãn chữ chuẩn mực, ký tự toán học tiêu chuẩn hoặc huy hiệu CSS thanh lịch (`.chat-avatar-badge`).
  - **Số lượng tệp được chỉnh sửa**: 11 tệp (`index.html`, `app.js`, `style.css`, `data.js`, 6 tệp `CHAP_01.md` - `CHAP_06.md`, `CHAPTER_CONTENT_AUDIT.md`).
  - **Vị trí duy nhất giữ lại Emoji theo ngoại lệ hợp lệ (Exception 1 - Ghi chú / Notes)**:
    - Ký tự: `💡` (U+1F4A1).
    - Vị trí: `outputs/content/chapters/CHAP_03.md` (Dòng 128) và bản đồng bộ `outputs/app/data.js`.
    - Thẻ chứa: `<span class="ba-insight-icon">💡</span>` bên trong khối Ghi chú Phân tích BA (`<div class="ba-insight-callout">`).
    - Lý do: Khối này là một **Ghi chú chuyên môn học thuật (Academic Note)** phân tích sự đánh đổi giữa chi phí vận tải và chi phí vận hành kho bãi của chuyên viên BA, tuân thủ chính xác Ngoại lệ 1 được quy định trong tài liệu yêu cầu.
  - Tỷ lệ kiểm thử tuân thủ Emoji: **17 / 17 checks PASS (100%)**.
- **Kết quả Kiểm thử Hồi quy Ứng dụng (Regression Tests)**:
  - Phase 3B Suite (`scripts/regression_test_phase3b.py`): **20 / 20 PASS (100%)** — Điều hướng 6 chương, KaTeX math, bảng biểu, accordion câu hỏi ôn tập.
  - Phase 3C Suite (`scripts/regression_test_phase3c.py`): **20 / 20 PASS (100%)** — Khóa phiên thi tính giờ, tính loại trừ độc lập của 2 modal, phân cấp học thuật chân trang song ngữ.
- **Thông tin Triển khai GitHub (Phase 2)**:
  - **Kho lưu trữ từ xa (Remote)**: `https://github.com/camtuct242-Hazel/erp-scm-knowledge-hub.git`
  - **Nhánh chính (Branch)**: `main`
  - **Quy chuẩn tệp tải lên**: Bao gồm toàn bộ `outputs/` (ứng dụng web, nội dung, cơ sở dữ liệu, tài liệu nghiệm thu), `netlify.toml`, `.gitignore`, `README.md` chuẩn học thuật. Loại trừ 100% `references/`, bản sao lưu an toàn `outputs/backup_before_enhancement/`, tệp tạm thời và bộ nhớ đệm.

---

'''

target_sec3 = '## 3. Kết Luận & Đánh Giá Nghiệm Thu (Acceptance Verdict)'
assert target_sec3 in tr, 'target_sec3 not found in TEST_REPORT.md'
tr = tr.replace(target_sec3, sec_2_12 + target_sec3, 1)

with open('outputs/documentation/TEST_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(tr)

# Also write to outputs/TEST_REPORT.md
with open('outputs/TEST_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(tr)

print("TEST_REPORT.md updated in both outputs/documentation/ and outputs/.")
