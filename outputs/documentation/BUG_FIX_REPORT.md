# BÁO CÁO ĐIỀU TRA & KHẮC PHỤC SỰ CỐ TƯƠNG TÁC GIAO DIỆN
## BUG FIX & ROOT CAUSE INVESTIGATION REPORT — ERP KNOWLEDGE HUB

---

## 1. Mô Tả Lỗi Ban Đầu (Original Defect)

### Hiện tượng phát hiện:
Giao diện ứng dụng ERP Knowledge Hub hiển thị đầy đủ về mặt thị giác (CSS, layout, màu sắc Balletcore), nhưng toàn bộ các tương tác của người dùng không hoạt động:
- Không thể chuyển đổi qua lại giữa các tab điều hướng (Navigation Tabs).
- Nhấp chuột vào các nút điều hướng trên thanh Navbar (Tổng quan, Giáo trình, Luyện thi, Flashcards, Thuật ngữ, Case Studies, Cố vấn AI) không chuyển trang hay hiển thị nội dung phân hệ tương ứng.
- Toàn bộ ứng dụng ở trạng thái "đóng băng tương tác" (Visually rendered but not interactive).

---

## 2. Nguyên Nhân Gốc Rễ (Root Cause Analysis)

Thông qua kết nối giám sát trực tiếp Chrome DevTools Protocol (CDP) trên nhân trình duyệt Chromium (Microsoft Edge Headless) tại cổng gỡ lỗi 9222, chúng tôi đã trích xuất được nhật ký lỗi thực tế từ JavaScript Engine:

```text
CONSOLE MSG: {'source': 'console-api', 'level': 'log', 'text': 'Uncaught', 'url': 'file:///.../outputs/app/app.js', 'line': 1620}
EXCEPTION THROWN: {'exceptionId': 1, 'text': "Uncaught SyntaxError: Unexpected identifier 'Số'", 'lineNumber': 1619, 'columnNumber': 407, 'scriptId': '4', 'url': 'file:///.../outputs/app/app.js'}
typeof window.App: 'undefined'
```

### Chi tiết lỗi kỹ thuật:
1. **Lỗi Cú Pháp (SyntaxError) làm sụp đổ toàn bộ quá trình biên dịch `app.js`**:
   - Tại dòng 1620 của tệp [`outputs/app/app.js`](file:///c:/Kiến%20thức%20cần%20học/ERP%20(SCM)/outputs/app/app.js), bên trong hàm `generateIntelligentResponse()`, một chuỗi mẫu (Template Literal) được bao bọc bởi cặp dấu huyền (backticks `` `...` ``).
   - Bên trong chuỗi này, lập trình viên đã viết:
     ```javascript
     - `Số lượng Hóa đơn <= Số lượng Nhập kho (GR)`
     - `Đơn giá Hóa đơn == Đơn giá PO`
     ```
   - Do các dấu backtick bên trong không được thoát chuỗi (escape) bằng dấu gạch chéo ngược (`\``), trình phân tích cú pháp JavaScript của trình duyệt đã hiểu nhầm dấu backtick trước từ `Số` là điểm kết thúc của chuỗi mẫu Template Literal.
   - Trình duyệt ngay lập tức bắt gặp định danh tiếng Việt `Số` đứng trơ trọi như một từ khóa cú pháp không hợp lệ và ném ra lỗi ngoại lệ nghiêm trọng: **`Uncaught SyntaxError: Unexpected identifier 'Số'`**.

2. **Hiệu ứng sụp đổ dây chuyền (Domino Effect)**:
   - Theo cơ chế vận hành của JavaScript, khi một tệp kịch bản gặp lỗi `SyntaxError` ở tầng biên dịch (Parse/Compile Phase), **toàn bộ tệp đó bị hủy bỏ và không có bất kỳ dòng code nào được thực thi**.
   - Do đó, đối tượng toàn cục `window.App` không bao giờ được khởi tạo (`typeof window.App === 'undefined'`).
   - Hàm khởi động `App.init()` không bao giờ được chạy.
   - Khi người dùng nhấp chuột vào bất kỳ nút điều hướng nào trên thanh Navbar (ví dụ: `<button onclick="App.navigateTo('chapters')">`), trình duyệt ném ra lỗi:
     `ReferenceError: App is not defined`.
   - Kết quả: Toàn bộ các tương tác nhấp chuột bị tê liệt hoàn toàn mặc dù cấu trúc DOM và CSS vẫn hiển thị bình thường.

3. **Thiếu điểm đến điều hướng thứ 8 (About Section)**:
   - Theo đặc tả yêu cầu, hệ thống cần cung cấp đủ 8 điểm đến điều hướng: Dashboard, Knowledge Base (Chapters), Practice Center (Exams), Flashcards, Glossary, Case Studies, AI Consultant, và About (Giới thiệu).
   - Phiên bản ban đầu thiếu nút bấm Navbar và thẻ `<section id="view-about">`.

---

## 3. Các Tệp Bị Ảnh Hưởng (Files Affected)

1. [`outputs/app/app.js`](file:///c:/Kiến%20thức%20cần%20học/ERP%20(SCM)/outputs/app/app.js)
2. [`outputs/app/index.html`](file:///c:/Kiến%20thức%20cần%20học/ERP%20(SCM)/outputs/app/index.html)
3. [`outputs/app/data.js`](file:///c:/Kiến%20thức%20cần%20học/ERP%20(SCM)/outputs/app/data.js)

---

## 4. Các Sửa Đổi Cụ Thể Đã Thực Hiện (Exact Modifications)

### A. Sửa lỗi cú pháp trong `outputs/app/app.js`:
- Thoát chuỗi (escape) chính xác các dấu backtick tại dòng 1620:
  ```javascript
  // Trước khi sửa (Gây SyntaxError):
  - `Số lượng Hóa đơn <= Số lượng Nhập kho (GR)`
  - `Đơn giá Hóa đơn == Đơn giá PO`

  // Sau khi sửa (Hợp lệ tuyệt đối):
  - \`Số lượng Hóa đơn <= Số lượng Nhập kho (GR)\`
  - \`Đơn giá Hóa đơn == Đơn giá PO\`
  ```

### B. Bổ sung Điều hướng và Phân hệ Giới Thiệu (About View):
- Thêm mục điều hướng thứ 8 vào Navbar trong `outputs/app/index.html`:
  ```html
  <li><button class="nav-btn" data-view="about" onclick="App.navigateTo('about')"><span data-i18n="nav_about">Giới Thiệu</span></button></li>
  ```
- Thêm phân hệ `<section id="view-about" class="view-section">` vào `outputs/app/index.html` trình bày: Sứ mệnh học thuật, Bối cảnh giáo trình UEH 2020 của tác giả Y Hoang, Cấu trúc 12 mục sư phạm, Khung năng lực Business Analyst, và Kiến trúc Zero-Build độc lập 100%.
- Cập nhật từ điển `I18N.vi` và `I18N.en` trong `outputs/app/app.js` cho `nav_about` và các nội dung liên quan.
- Bổ sung `case 'about':` trong bộ điều tuyến `navigateTo(viewName)` của `outputs/app/app.js`.

### C. Công khai Trạng thái Ứng dụng để Phục Vụ Kiểm Thử (State Exposure):
- Gắn biến trạng thái nội bộ `state` vào đối tượng ứng dụng `window.App.state = state;` giúp các kịch bản kiểm thử tự động có thể truy xuất và xác thực dữ liệu tức thời.

### D. Chuẩn hóa Cấu trúc Dữ liệu Bộ Đề Thi & Từ Điển trong `outputs/app/data.js`:
- Chuẩn hóa các trường `question`, `options` (dưới dạng object dictionary A, B, C, D), `correct_option` (A, B, C, D) và `explanation` đa ngữ giúp trình điều khiển bài thi truy xuất mượt mà không gặp lỗi lệch cấu trúc.

---

## 5. Quy Trình Kiểm Thử & Kết Quả Xác Minh (Test Verification)

Toàn bộ quy trình kiểm thử đã được tự động hóa thông qua Chromium DevTools Protocol (CDP) kết nối tới Microsoft Edge thật chạy chế độ nền (`scripts/full_browser_interaction_test.py`).

| Mã Test | Hạng Mục Kiểm Thử | Tương Tác Người Dùng Mô Phỏng | Kết Quả Thực Tế | Trạng Thái |
|---|---|---|---|---|
| **TC-01** | Khởi tạo Ứng dụng | Tải trang `index.html` và kiểm tra đối tượng toàn cục | `window.App` và `window.APP_DATA` khởi tạo thành công | **PASS** |
| **TC-02** | Điều hướng: Dashboard | Click nút "Tổng Quan" trên Navbar | Chuyển sang `#view-dashboard`, nút gắn class `.active` | **PASS** |
| **TC-03** | Điều hướng: Giáo Trình | Click nút "Giáo Trình" trên Navbar | Chuyển sang `#view-chapters`, hiển thị 6 chương học | **PASS** |
| **TC-04** | Điều hướng: Luyện Thi | Click nút "Luyện Thi & Trắc Nghiệm" | Chuyển sang `#view-exams`, hiển thị 10 đề thi chuẩn | **PASS** |
| **TC-05** | Điều hướng: Flashcards | Click nút "Flashcards" trên Navbar | Chuyển sang `#view-flashcards`, hiển thị bộ 30 thẻ | **PASS** |
| **TC-06** | Điều hướng: Thuật Ngữ | Click nút "Thuật Ngữ" trên Navbar | Chuyển sang `#view-glossary`, hiển thị 40 thuật ngữ | **PASS** |
| **TC-07** | Điều hướng: Case Studies | Click nút "Case Studies" trên Navbar | Chuyển sang `#view-cases`, hiển thị 4 case study | **PASS** |
| **TC-08** | Điều hướng: Cố Vấn AI | Click nút "Cố Vấn AI" trên Navbar | Chuyển sang `#view-consultant`, mở khung chat & prompt chips | **PASS** |
| **TC-09** | Điều hướng: Giới Thiệu | Click nút "Giới Thiệu" trên Navbar | Chuyển sang `#view-about`, hiển thị sứ mệnh & kiến trúc | **PASS** |
| **TC-10** | Công Tắc Chuyển Ngữ | Chuyển Tiếng Việt $\leftrightarrow$ Tiếng Anh | Cập nhật nhãn tức thời, không làm mất trạng thái làm việc | **PASS** |
| **TC-11** | Mô Phỏng Tồn Kho Nhanh | Thay đổi $D=10.000, K=50, h=4$ | Tự động tính toán lại $Q^* = 500$ chiếc, $TVC = \$2.000$ | **PASS** |
| **TC-12** | Đọc Giáo Trình & Mục Lục | Mở Chương 1 $\to$ Kiểm tra 12 phần mục lục | Đủ 12 phần sư phạm chuẩn, checkbox lưu trạng thái OK | **PASS** |
| **TC-13** | Luyện Thi Tự Do (Practice) | Mở Exam 1 $\to$ Chọn phương án A | Hiển thị ngay màu phản hồi và khung giải thích chi tiết | **PASS** |
| **TC-14** | Thi Tính Giờ 30 Phút | Mở Exam 2 $\to$ Đếm ngược $\to$ Nộp bài | Đồng hồ chạy chính xác, tự động chấm điểm và xếp hạng | **PASS** |
| **TC-15** | Thẻ Ghi Nhớ 3D | Nhấp chuột vào thẻ $\to$ Đánh dấu "Đã thuộc" | Thẻ lật xoay 3D, cập nhật bộ đếm thẻ đã thuộc | **PASS** |
| **TC-16** | Tìm Kiếm Từ Điển | Gõ "EOQ" vào ô tìm kiếm $\to$ Mở chi tiết | Lọc tức thì, hiển thị popup ví dụ thực tế & ánh xạ SAP | **PASS** |
| **TC-17** | Bộ Giải Toán Case 1 | Chạy Texago Site Selection Solver | Xếp hạng chính xác: St. Louis (\$1.330M) tối ưu nhất | **PASS** |
| **TC-18** | Cố Vấn Học Tập AI | Chọn Scenario 5 $\to$ Bấm Prompt Chip | Phản hồi thông minh offline chuẩn xác số liệu sách giáo khoa | **PASS** |
| **TC-19** | Giữ Vững Trạng Thái | Chuyển tab liên tục trong khi làm bài | Không phát sinh bất kỳ lỗi JavaScript nào (0 Exceptions) | **PASS** |

**Tổng kết đợt kiểm thử**: **19 / 19 Tests PASSED (100.0%)**.

---

## 6. Các Giới Hạn Còn Lại (Remaining Limitations)

- **Các tính năng AI nâng cao khi không có Internet**: Động cơ AI Consultant tích hợp sẵn chạy ngầm theo phương thức khớp ngữ cảnh tri thức nội bộ chất lượng cao. Khi máy tính người dùng mất kết nối Internet hoàn toàn, tính năng gọi API ra ngoài (Google Gemini / OpenAI) sẽ không thực hiện được; tuy nhiên toàn bộ kho tri thức giáo trình, công thức và 4 case study vẫn được hệ thống offline phản hồi trọn vẹn và chuẩn xác.
