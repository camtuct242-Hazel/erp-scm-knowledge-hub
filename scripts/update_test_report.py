with open('outputs/documentation/TEST_REPORT.md', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = """- **Thẻ Flashcards (`flashcards.json`)**:
  - Số lượng: **30 thẻ** (Vượt yêu cầu tối thiểu).
  - Phân loại: Definition (3 thẻ), Model (9 thẻ), Formula (6 thẻ), Distinction (6 thẻ), Business Rule (6 thẻ).
  - Bao quát toàn bộ 6 chương học.
  - Kết quả: **PASS**."""

repl1 = """- **Thẻ Flashcards (`flashcards.json`)**:
  - Số lượng: **62 thẻ song ngữ chuyên sâu** (Được nâng cấp toàn diện từ 30 thẻ lên 62 thẻ phủ kín 6 chương học).
  - Phân loại: Định nghĩa cốt lõi, Mô hình tối ưu hóa, Công thức toán học KaTeX, Quy tắc nghiệp vụ ERP, Góc nhìn Business Analyst.
  - Bao quát toàn bộ 6 chương học (Ch1: 10, Ch2: 10, Ch3: 10, Ch4: 10, Ch5: 11, Ch6: 11).
  - Kết quả: **PASS**."""

phase2_section = """
---

### 2.9 Kiểm Thử Hồi Quy Toàn Diện Nâng Cấp Chất Lượng & UX Giai Đoạn 2 (Phase 2 Regression Suite)
- **Phương pháp**: Khởi chạy Edge Headless kết nối trực tiếp qua CDP, nạp tệp `file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html`, thực thi trọn vẹn 15 test cases (kịch bản kiểm thử tự động tại `scripts/regression_test_enhancements.py`).
- **Bảng tổng hợp kết quả 15/15 Phase 2 Test Cases**:
  | STT | Tên Trường Hợp Kiểm Thử | Mục Tiêu Nghiệp Vụ | Kết Quả Thực Tế | Trạng Thái |
  |:---:|---|---|---|:---:|
  | 01 | Offline Vendor Libraries Integration | Kiểm tra `marked`, `katex`, `renderMathInElement` nạp từ thư mục vendor cục bộ | Đã nạp thành công từ `vendor/` nội bộ | **PASS** |
  | 02 | KaTeX Math Delimiters Verification | Render công thức $EOQ = \sqrt{\\frac{2DS}{H}}$ và display math | Render chính xác cả inline và display | **PASS** |
  | 03 | Flashcards Dataset Distribution | Kiểm tra đủ 62 thẻ ghi nhớ trải đều qua 6 chương học | Đầy đủ 62 thẻ trong `APP_DATA` | **PASS** |
  | 04 | Flashcard Flip, Next & Mastered Status | Thao tác lật thẻ 3D, chuyển tiếp và đánh dấu đã thuộc | Lật thẻ mượt mà, chuyển index, lưu `masteredFlashcards` | **PASS** |
  | 05 | Flashcard Multi-criteria Filtering | Kiểm tra lọc theo từng chương (Ch4: 10 thẻ) và quay về All (62 thẻ) | Bộ lọc chương & phân loại hoạt động chính xác | **PASS** |
  | 06 | Flashcard Shuffle & Formula Display | Xáo trộn ngẫu nhiên và kiểm tra KaTeX render công thức $Q^*$ | Xáo thẻ bảo toàn 100%, render KaTeX cả 2 mặt | **PASS** |
  | 07 | Floating Scroll-To-Top Component | Kiểm tra sự hiện diện, thuộc tính aria-label, title và hàm cuộn | Nút nổi chuẩn Balletcore hiện diện đầy đủ | **PASS** |
  | 08 | Case Studies Module Architecture | Kiểm tra điều hướng 4 bộ tình huống và container hiển thị | 4 thẻ tình huống sẵn sàng, chuyển đổi tức thời | **PASS** |
  | 09 | Case 1 Texago Presentation | Kiểm tra ảnh bổ sung dữ liệu, bảng biểu responsive và công thức toán | Nhúng ảnh `assets/texago_supplementary_data.jpg`, 11 bảng | **PASS** |
  | 10 | Cases 2, 3, 4 Academic Formatting | Kiểm tra bảng biểu ma trận và công thức toán trong Case 2, 3 và 4 | C2: 5 bảng; C3: 3 bảng & 19 math; C4: 1 bảng & 38 math | **PASS** |
  | 11 | Unified AI Consultant Layout | Kiểm tra không gian chat hợp nhất, 8 chip gợi ý kịch bản, ô input và nút gửi | Layout thanh lịch, 8 prompt chip tải sẵn | **PASS** |
  | 12 | Prompt Chip Insertion Mechanism | Nhấp chip gợi ý để chèn prompt vào textarea mà KHÔNG tự động gửi | Prompt điền vào textarea, người dùng tự do sửa trước khi gửi | **PASS** |
  | 13 | Grounded Offline AI Knowledge Response | Gửi truy vấn nghiệp vụ EOQ và nhận câu trả lời chứa KaTeX math | Trả lời chuẩn xác kèm công thức $Q^*$ và TVC | **PASS** |
  | 14 | Bilingual Language Switch (VI <-> EN) | Kiểm tra chuyển đổi ngôn ngữ Việt - Anh bảo toàn trạng thái | Chuyển đổi trơn tru `vi` ⟷ `en`, đồng bộ giao diện | **PASS** |
  | 15 | Professional Footer Attribution | Xác nhận thông tin tác giả và định vị nền tảng trên chân trang | Hiển thị: *"Created by Nguyễn Đăng Cẩm Tú (Hazel)"* | **PASS** |
- **Tỷ lệ kiểm thử tự động giai đoạn 2**: **15 / 15 (100.0%)**.
- **Đánh giá**: **PASS**.
"""

text = text.replace(target1.replace('\r\n', '\n'), repl1.replace('\r\n', '\n'))

insert_idx = text.find('## 3. Kết Luận & Đánh Giá Nghiệm Thu')
if insert_idx != -1:
    text = text[:insert_idx] + phase2_section.replace('\r\n', '\n') + '\n' + text[insert_idx:]

with open('outputs/documentation/TEST_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("TEST_REPORT.md successfully updated!")
