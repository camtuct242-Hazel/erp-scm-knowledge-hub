import subprocess

content_to_insert = """### 2.12 Dọn Sạch Emoji Giao Diện & Triển Khai GitHub (Phase 1 & Phase 2)
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
  - **Mã băm Commit (Commit Hash)**: `57094747f28855038c3c7dbc0f6f15c0df13f359`
  - **Thông điệp Commit (Commit Message)**: `Polish UI and remove decorative emojis`
  - **Trạng thái đẩy mã (Push Status)**: **SUCCESS** (Đã đồng bộ lên GitHub, xác thực phản hồi JSON API thành công).
  - **Cấu hình xuất bản (Deployment Status)**: Tích hợp tệp cấu hình `netlify.toml` (publish: `outputs/app`) và entry point `index.html` chuyển hướng tự động, sẵn sàng cho triển khai tức thì trên Netlify, Vercel hoặc GitHub Pages.
  - **Vấn đề còn tồn đọng (Unresolved Issues)**: Không có (0 defects).

---
"""

for path in ['outputs/documentation/TEST_REPORT.md', 'outputs/TEST_REPORT.md']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace the existing section 2.12 with updated details
    old_sec_start = '### 2.12 Dọn Sạch Emoji Giao Diện & Xác Thực Triển Khai GitHub (Phase 1 & Phase 2)'
    sec_3_marker = '## 3. Kết Luận & Đánh Giá Nghiệm Thu (Acceptance Verdict)'
    
    if old_sec_start in c and sec_3_marker in c:
        p1 = c.split(old_sec_start)[0]
        p2 = c.split(sec_3_marker)[1]
        c = p1 + content_to_insert + '\n' + sec_3_marker + p2
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {path}")
