with open('outputs/documentation/TEST_REPORT.md', 'r', encoding='utf-8') as f:
    text = f.read()

phase3b_section = """
---

### 2.10 Kiểm Thử Hồi Quy Toàn Diện Giai Đoạn 3B: Nội Dung 6 Chương, Điều Hướng & Khóa Phiên Thi (Phase 3B Suite)
- **Phương pháp**: Khởi chạy Microsoft Edge Headless với giao thức Chrome DevTools Protocol (CDP), nạp trực tiếp ứng dụng độc lập qua đường dẫn `file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html`.
- **Kịch bản kiểm thử**: 20 ca kiểm thử tự động chuyên sâu kiểm tra điều hướng 6 chương hai đầu trang, dọn sạch khuyết tật LaTeX/Markdown, ẩn đáp án trắc nghiệm, hiển thị Callout BA Insight chuẩn mực và cơ chế Khóa Phiên Thi Tính Giờ (tệp thực thi `scripts/regression_test_phase3b.py`).
- **Bảng tổng hợp kết quả 20/20 Phase 3B Test Cases**:
  | STT | Tên Kịch Bản Kiểm Thử | Kỳ Vọng Kỹ Thuật & Nghiệp Vụ | Kết Quả Thực Tế | Trạng Thái |
  |:---:|---|---|---|:---:|
  | 01 | Chapter 1 Boundary Navigation | Nút "Chương trước" bị vô hiệu hóa tại Chương 1 | `prevTop.disabled = true`, class `.disabled` | **PASS** |
  | 02 | Next Chapter Navigation | Nút "Chương tiếp theo" chuyển từ Ch.1 sang Ch.2 | Nạp đúng `chap-02`, badge 'Chương 02' | **PASS** |
  | 03 | Sequential Chapter Navigation | Điều hướng tuần tự qua Ch.2 $\\to$ Ch.3 $\\to$ Ch.4 $\\to$ Ch.5 | Nạp chính xác từng chương theo thứ tự | **PASS** |
  | 04 | Chapter 6 Boundary Navigation | Nút "Chương tiếp theo" bị vô hiệu hóa tại Chương 6 | `nextTop.disabled = true`, class `.disabled` | **PASS** |
  | 05 | Bottom Navigation Cluster | Nút điều hướng chân trang hoạt động tương đương đỉnh trang | Nhấp nút PrevBottom chuyển từ Ch.6 về Ch.5 | **PASS** |
  | 06 | Chapter List Navigation | Nút "Danh sách chương" đưa về trang tổng quan giáo trình | Section `#view-chapters` kích hoạt active | **PASS** |
  | 07 | Bilingual Navigation Labels | Nhãn nút chuyển ngữ chính xác theo ngôn ngữ chọn | EN: `← Previous Chapter` / VI: `← Chương trước` | **PASS** |
  | 08 | Chapter 3 Corrupted BA Check | Chuỗi ký tự lỗi `30/nga` và `vượt xa con số $30` không tồn tại | Không tìm thấy bất kỳ chuỗi lỗi nào trong DOM | **PASS** |
  | 09 | Chapter 3 Clean BA Callout | Khối `.ba-insight-callout` hiển thị đủ nội dung song ngữ chuẩn | Callout hiện diện, đủ phân tích chi phí trực tiếp vs vận hành | **PASS** |
  | 10 | Review Answers Hidden Initially | Đáp án câu hỏi ôn tập Mục 12 đóng mặc định | 2/2 accordion ở trạng thái đóng (`open = false`) | **PASS** |
  | 11 | Review Answers Reveal Interaction | Nhấp vào summary sẽ mở xem đáp án và giải thích | Thuộc tính `open = true`, hiển thị lời giải chi tiết | **PASS** |
  | 12 | Chapter 2 Table Cleanliness | Bảng phân bổ 4.2 hiển thị sạch không có ký tự tab | Bảng responsive hiện diện, tổng chi phí $3.260 hiển thị đúng | **PASS** |
  | 13 | Practice Mode Unrestricted Nav | Chế độ luyện tập không khóa thanh điều hướng | Menu `.nav-links` hiển thị bình thường | **PASS** |
  | 14 | Timed Exam Navigation Locked | Chế độ thi tính giờ ẩn thanh điều hướng và khóa brand | `.nav-links` bị ẩn (`display: none`), timer hiển thị | **PASS** |
  | 15 | In-App Navigation Blocked | Cố gắng bấm chuyển trang trong lúc thi sẽ bị chặn | Chặn điều hướng, mở Modal `#modal-exit-exam` | **PASS** |
  | 16 | Continue Exam State Retention | Chọn "Tiếp tục làm bài" giữ nguyên câu trả lời và timer | Modal đóng, đáp án 'B' được bảo lưu, bài thi tiếp diễn | **PASS** |
  | 17 | Confirm Exit Clears Attempt | Chọn "Thoát và xóa bài thi" xóa câu trả lời, mở khóa nav | Xóa đáp án, gỡ `.exam-locked`, về `#view-exams` | **PASS** |
  | 18 | Timer Expiration Auto-Submit | Đồng hồ về 00:00 tự động nộp bài và mở khóa điều hướng | Tự động chấm điểm, lưu lịch sử, mở khóa nav | **PASS** |
  | 19 | All 6 Chapters KaTeX Render | Cả 6 chương học render thành công công thức toán KaTeX | Ch1: 81; Ch2: 60; Ch3: 53; Ch4: 94; Ch5: 121; Ch6: 27 nodes | **PASS** |
  | 20 | Existing Modules Regression | Bảo toàn 62 flashcards, 4 case studies và 8 prompt chips AI | Đủ 62 thẻ, 4 cases responsive, 8 chips cố vấn AI | **PASS** |
- **Tỷ lệ kiểm thử tự động giai đoạn 3B**: **20 / 20 (100.0%)**.
- **Đánh giá**: **PASS**.
"""

insert_idx = text.find('## 3. Kết Luận & Đánh Giá Nghiệm Thu')
if insert_idx != -1:
    text = text[:insert_idx] + phase3b_section + '\n' + text[insert_idx:]

with open('outputs/documentation/TEST_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("TEST_REPORT.md appended with Phase 3B results!")
