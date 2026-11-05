# Update TEST_REPORT.md
with open('outputs/documentation/TEST_REPORT.md', 'r', encoding='utf-8') as f:
    c = f.read()

target = '''  | 15 | Professional Footer Attribution | Xác nhận thông tin tác giả và định vị nền tảng trên chân trang | Hiển thị: *"Created by Nguyễn Đăng Cẩm Tú (Hazel)"* | **PASS** |
- **Tỷ lệ kiểm thử tự động giai đoạn 2**: **15 / 15 (100.0%)**.
- **Đánh giá**: **PASS**.'''

repl = '''  | 15 | Professional Footer Attribution | Xác nhận thông tin tác giả và định vị nền tảng trên chân trang | Hiển thị: *"Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)"* (VI) / *"Author: Nguyễn Đăng Cẩm Tú (Hazel)"* (EN) | **PASS** |
- **Tỷ lệ kiểm thử tự động giai đoạn 2**: **15 / 15 (100.0%)**.
- **Đánh giá**: **PASS**.'''

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
repl_norm = repl.replace('\r\n', '\n')

assert target_norm in c_norm, 'target not found in TEST_REPORT.md'
c_norm = c_norm.replace(target_norm, repl_norm, 1)

sec_3_target = '## 3. Kết Luận & Đánh Giá Nghiệm Thu (Acceptance Verdict)'
sec_2_11 = '''### 2.11 Kiểm Thử Hồi Quy Toàn Diện Giai Đoạn 3C: Khắc Phục Lỗi Nút Thoát Thi Tính Giờ & Tinh Chỉnh Phân Cấp Chân Trang (Phase 3C Suite)
- **Phương pháp**: Khởi chạy Microsoft Edge Headless với giao thức Chrome DevTools Protocol (CDP), nạp trực tiếp ứng dụng độc lập qua đường dẫn `file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html`.
- **Nguyên nhân cốt lõi đã điều tra & khắc phục**:
  1. *Lỗi lồng ghép thẻ HTML (HTML Nesting Defect)*: Trong `index.html`, thẻ `<div id="modal-submit-exam">` bị thiếu thẻ đóng `</div>` trước thẻ `<div id="modal-exit-exam">`, dẫn đến việc `#modal-exit-exam` bị lồng hoàn toàn làm con của `#modal-submit-exam`. Vì phần tử cha có thuộc tính `display: none`, khi người dùng bấm "Thoát bài thi", modal thoát dù được thêm class `.active` vẫn bị cha ẩn đi (người dùng cảm giác nút không phản hồi). Ngược lại, khi bấm "Nộp Bài Thi", modal cha kích hoạt hiển thị làm lộ ra cả modal con đang active, tạo ra hiện tượng 2 hộp thoại xác nhận chồng chéo tuần tự bất thường.
  2. *Tách biệt hoàn toàn luồng xử lý*: Đưa `#modal-exit-exam` và `#modal-submit-exam` thành 2 phần tử ngang hàng (siblings) độc lập trực tiếp dưới `body`. Bổ sung các phương thức chuyên biệt `handleExitExam()`, `handleSubmitExam()`, `confirmExitExam()`, `confirmSubmitExam()` với cơ chế đóng triệt để modal đối ứng (`modal exclusivity`) nhằm đảm bảo tại một thời điểm chỉ có tối đa 1 modal xác nhận được hiển thị.
  3. *Tái cấu trúc Chân trang (Footer)*: Loại bỏ hoàn toàn nhãn `Created by:`, thay thế bằng hệ phân cấp học thuật chuẩn mực: Tiêu đề trang trọng **ERP & Supply Chain Management Knowledge Hub**, mô tả định vị tinh tế, đường phân cách thanh mảnh, tác quyền chính quy **Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)** (VI) / **Author: Nguyễn Đăng Cẩm Tú (Hazel)** (EN), và thông điệp chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực BA.
- **Kịch bản kiểm thử**: 20 ca kiểm thử tự động chuyên sâu kiểm tra cấu trúc DOM, tính độc lập của modal, luồng thoát bài thi, luồng nộp bài thi, cơ chế khóa phiên thi và phân cấp chân trang song ngữ (tệp thực thi `scripts/regression_test_phase3c.py`).
- **Bảng tổng hợp kết quả 20/20 Phase 3C Test Cases**:
  | STT | Tên Kịch Bản Kiểm Thử | Kỳ Vọng Kỹ Thuật & Nghiệp Vụ | Kết Quả Thực Tế | Trạng Thái |
  |:---:|---|---|---|:---:|
  | 01 | Modal DOM Separation & Sibling Hierarchy | 2 modal là anh em cùng cấp, không lồng ghép nhau | `isExitInsideSubmit=false, areSiblings=true` | **PASS** |
  | 02 | Modals Initial Inactive State | Khởi tạo ban đầu cả 2 modal đều đóng (`display: none`) | Không có class `.active`, cả hai đều ẩn | **PASS** |
  | 03 | Timed Exam Initialization & Session Lock | Bắt đầu thi tính giờ: khóa menu, kích hoạt timer | `examActive=true, locked=true, timer=visible` | **PASS** |
  | 04 | Exit Button Opens ONLY Exit Modal | Nhấp "Thoát bài thi" CHỈ mở duy nhất Exit Modal | `exitModal.active=true, submitModal.active=false` | **PASS** |
  | 05 | Continue Exam from Exit Modal | Chọn "Tiếp tục làm bài" bảo lưu nguyên vẹn đáp án và timer | Đóng modal, bài thi tiếp diễn, đáp án giữ nguyên | **PASS** |
  | 06 | Submit Button Opens ONLY Submit Modal | Nhấp "Nộp Bài Thi" CHỈ mở Submit Modal (không mở Exit) | `submitModal.active=true, exitModal.active=false` | **PASS** |
  | 07 | Continue Exam from Submit Modal | Chọn "Làm Tiếp" đóng submit modal, bảo lưu câu trả lời | Đóng modal, bài thi tiếp diễn, câu trả lời bảo toàn | **PASS** |
  | 08 | Strict Modal Exclusivity | Chuyển đổi qua lại giữa 2 modal bảo đảm tính loại trừ | Tại mỗi thời điểm chỉ 1 modal mở, modal kia đóng | **PASS** |
  | 09 | Navbar Interception During Timed Exam | Nhấp chuyển trang trong navbar bị chặn, mở Exit modal | Điều hướng bị chặn, chỉ mở Exit confirmation | **PASS** |
  | 10 | Confirmed Exit Discards Attempt | Xác nhận thoát: hủy câu trả lời hiện tại, mở khóa nav | Xóa đáp án phiên, gỡ lock, về trang `#view-exams` | **PASS** |
  | 11 | Confirmed Submit Workflow | Xác nhận nộp: chấm điểm, lưu lịch sử, hiển thị kết quả | Chấm điểm, mở khóa nav, hiển thị bảng điểm | **PASS** |
  | 12 | Footer Heading & Tagline (VI) | Tiêu đề và khẩu hiệu chân trang hiển thị chuẩn tiếng Việt | Đúng nguyên văn tiêu đề và định vị học thuật | **PASS** |
  | 13 | Footer Author Attribution (VI) | Tác quyền hiển thị "Tác giả:..." và KHÔNG chứa "Created by" | `"Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)"`, không có `Created by` | **PASS** |
  | 14 | Footer Academic Alignment (VI) | Định hướng song ngữ & chuẩn hóa giáo trình UEH (VI) | Hiển thị chính xác thông điệp chuẩn hóa | **PASS** |
  | 15 | Footer Heading & Tagline (EN) | Tiêu đề và khẩu hiệu chân trang hiển thị chuẩn tiếng Anh | Đúng nguyên văn tiêu đề và định vị tiếng Anh | **PASS** |
  | 16 | Footer Author Attribution (EN) | Tác quyền tiếng Anh: "Author:..." và KHÔNG chứa "Created by" | `"Author: Nguyễn Đăng Cẩm Tú (Hazel)"`, không có `Created by` | **PASS** |
  | 17 | Footer Academic Alignment (EN) | Định hướng song ngữ & chuẩn hóa giáo trình UEH (EN) | Hiển thị chuẩn xác thông điệp tiếng Anh | **PASS** |
  | 18 | Footer Divider & Container Styling | Đường phân cách tinh tế 48px và container tối đa 850px | `width=48px, height=1px, maxWidth=850px` | **PASS** |
  | 19 | Default Language Reset & i18n Sync | Khôi phục mặc định tiếng Việt, bảo toàn tính toàn vẹn i18n | Trạng thái đồng bộ, nhãn tác giả tiếng Việt đúng | **PASS** |
  | 20 | Clean Application State & Zero Overlays | Không còn lớp phủ overlay hay bẫy pointer-events dư thừa | Cả 2 modal đóng, body không bị khóa | **PASS** |
- **Tỷ lệ kiểm thử tự động giai đoạn 3C**: **20 / 20 (100.0%)**.
- **Đánh giá**: **PASS**.

---

'''

assert sec_3_target in c_norm, 'sec_3_target not found in TEST_REPORT.md'
c_norm = c_norm.replace(sec_3_target, sec_2_11 + sec_3_target, 1)

with open('outputs/documentation/TEST_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print('TEST_REPORT.md updated successfully.')

# Update ENHANCEMENT_REPORT.md
with open('outputs/documentation/ENHANCEMENT_REPORT.md', 'r', encoding='utf-8') as f:
    er = f.read()

er = er.replace('Created by Nguyễn Đăng Cẩm Tú (Hazel)', 'Tác giả: Nguyễn Đăng Cẩm Tú (Hazel) (VI) / Author: Nguyễn Đăng Cẩm Tú (Hazel) (EN)')

with open('outputs/documentation/ENHANCEMENT_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(er)

print('ENHANCEMENT_REPORT.md updated successfully.')
