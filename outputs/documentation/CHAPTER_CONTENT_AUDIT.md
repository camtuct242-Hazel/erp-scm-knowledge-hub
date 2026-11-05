# BÁO CÁO KIỂM TOÁN CHẤT LƯỢNG NỘI DUNG 6 CHƯƠNG & KHÓA PHIÊN THI TÍNH GIỜ
# CHAPTER CONTENT AUDIT & TIMED EXAM SESSION LOCK VERIFICATION REPORT

---

## 1. TỔNG QUAN & BỐI CẢNH (EXECUTIVE SUMMARY)

**Dự án:** ERP & Supply Chain Management Knowledge Hub  
**Vị trí ứng dụng:** `C:\Kiến thức cần học\ERP (SCM)\outputs\app\`  
**Thời gian hoàn thành:** 05/11/2026  
**Tác giả:** Nguyễn Đăng Cẩm Tú (Hazel)  
**Mục tiêu đợt Phase 3B:** Khắc phục triệt để các khuyết tật hiển thị toán học LaTeX và Markdown trên toàn bộ 6 chương giáo trình, nâng cấp hệ thống điều hướng đọc chương hai đầu trang (Top/Bottom Navigation), chuẩn hóa khối bình luận BA Insight của Chương 3 tại nguồn gốc, ẩn mặc định đáp án câu hỏi ôn tập Mục 12 và triển khai cơ chế Khóa Phiên Thi Tính Giờ (Timed Exam Session Lock) đạt chuẩn bảo vệ phiên thi chuyên nghiệp.

**Kết quả kiểm thử tự động (Edge Headless qua CDP):** **20/20 Test Cases Đạt Chuẩn Tuyệt Đối (Pass Rate: 100.0%)**.

---

## 2. BẢNG KIỂM TOÁN CHI TIẾT THEO TỪNG CHƯƠNG (CHAPTER-BY-CHAPTER AUDIT)

### 2.1 Chương 1: Tổng quan Hệ thống ERP & Vận tải Tuyến tính (`CHAP_01.md`)
- **Khuyết tật phát hiện ban đầu:**
  - Mục 4.3 (Heuristic vs Simplex LP): Khối phương trình `\begin{aligned}` chứa ký hiệu `\$` trong toán học (`\mathbf{\$152.535}`), khiến KaTeX ném lỗi `ParseError: Can't use function '$' in math mode`.
  - 5 bước Heuristic tham lam dính chữ với các chỉ số dưới toán học ($c_{ij}$, $x_{ij}$).
  - Mục 12: Đáp án câu hỏi trắc nghiệm ôn tập hiển thị công khai ngay dưới phương án D.
- **Biện pháp khắc phục đã triển khai:**
  - Viết lại toàn bộ 5 bước phân bổ Heuristic thành danh sách có thứ tự rõ ràng, tách biệt giữa lời dẫn tiếng Việt và đại lượng toán học ($c_{21} = 352\text{ USD} \implies x_{21} = 80\text{ xe}$).
  - Chuẩn hóa khối tính toán chi phí Heuristic: sử dụng `\mathbf{152.535\text{ USD}}` hoàn toàn hợp lệ trong chế độ toán KaTeX.
  - Đóng gói toàn bộ đáp án Mục 12 vào thẻ `<details class="review-answer-accordion">` với nút bấm sư phạm ` Xem đáp án và giải thích / Reveal answer and explanation`.
- **Kết quả kiểm tra thực tế:** Render thành công **81 node KaTeX**, 2/2 khối accordion đóng mặc định và mở mượt mà khi nhấp chuột.

### 2.2 Chương 2: Biến thể Bài toán Vận tải & Ràng buộc Thực tế (`CHAP_02.md`)
- **Khuyết tật phát hiện ban đầu:**
  - Xuất hiện **37 ký tự Tab (`\t`)** do lỗi escape chuỗi trong script Python thế hệ trước, biến dạng các từ khóa LaTeX thành: `30ext đơn vị` (từ `\text`), `30imes27` (từ `\times`), và mất mũi tên `Nhà máy 2 \to Sản phẩm 3`.
  - Bảng Excel Solver Mục 4.2 sử dụng bảng Markdown thô, bị tràn giao diện trên màn hình độ phân giải thấp.
  - Mục 12: Đáp án ôn tập hiển thị lộ thiên.
- **Biện pháp khắc phục đã triển khai:**
  - Rà soát và loại bỏ toàn bộ 37 ký tự Tab, khôi phục 100% cú pháp chuẩn `\text`, `\times`, `\to`.
  - Tái cấu trúc bảng phân bổ Excel Solver bằng bảng HTML chuẩn `.table-responsive` kết hợp `.content-table`, định dạng rõ ràng các cột Nhà máy, Phân bổ sản phẩm, Chi phí đơn vị và Thành tiền; tính tổng chi phí $Z^* = \$3.260\text{/ngày}\quad (\$3,260\text{/day})$.
  - Bọc đáp án Mục 12 vào accordion tương tác.
- **Kết quả kiểm tra thực tế:** 0 ký tự Tab còn sót lại, bảng hiển thị sắc nét có thanh cuộn ngang êm ái, render thành công **60 node KaTeX**.

### 2.3 Chương 3: Trung chuyển, Khoảng Nhu cầu & Phân công Nhị phân (`CHAP_03.md`)
- **Khuyết tật phát hiện ban đầu:**
  - Nhận xét của BA sau bảng phân bổ Case 2.2 bị dính vào chế độ toán do dấu `$` bao quanh ký hiệu tiền tệ, biến dạng chữ tiếng Việt thành chuỗi ký tự lỗi: `30/ngaˋy,nhưngtrongthựcte^ˊ,chiphıˊquảnlyˊvaˋchiphıˊthie^ˊtlậpmaˊytie^ˊtkiệmđượcvượtxaconso^ˊ 30 này...`.
  - Nhận xét ban đầu khẳng định thiên lệch *"phương án Case 2.2 luôn được ưu tiên"* mà chưa phân tích tính đánh đổi kinh tế thực tế.
  - Mục 12: Đáp án trắc nghiệm hiển thị lộ liễu.
- **Biện pháp khắc phục đã triển khai:**
  - Xóa bỏ triệt để đoạn văn lỗi tại tệp nguồn `CHAP_03.md` và đồng bộ vào `data.js`.
  - Xây dựng khối Callout chuyên nghiệp `.ba-insight-callout` song ngữ:
    - **Tiếng Việt:** *Góc nhìn Business Analyst — Đánh đổi giữa chi phí trực tiếp và chi phí vận hành*: Làm rõ Case 2.2 đắt hơn 30 USD/ngày về chi phí trực tiếp nhưng tiết kiệm chi phí đổi khuôn và quản lý; khẳng định BA cần định lượng tổng chi phí thực tế thay vì vội vàng kết luận Case 2.2 luôn tốt hơn.
    - **Tiếng Anh:** *Business Analyst Insight — Trade-off Between Direct and Operational Costs* với văn phong học thuật chuẩn mực.
  - Định dạng rõ tiền tệ `30 USD/ngày` và `USD 30/day`, không đặt trong math mode.
  - Đóng gói đáp án trắc nghiệm Mục 12 vào accordion.
- **Kết quả kiểm tra thực tế:** Không còn bất kỳ dấu vết nào của chuỗi ký tự lỗi `30/nga`, khối Callout BA Insight hiển thị trang trọng chuẩn Balletcore, render **53 node KaTeX**.

### 2.4 Chương 4: Quản trị Tồn kho Khoa học & Mô hình EOQ Cơ bản (`CHAP_04.md`)
- **Khuyết tật phát hiện ban đầu:** Các công thức chứa chỉ số dưới `_` và phép nhân `\times` trong hàm TVC và ROP có nguy cơ bị bộ parser Markdown diễn giải nhầm thành thẻ `<em>`; đáp án trắc nghiệm Mục 12 hiển thị sẵn.
- **Biện pháp khắc phục:** Ứng dụng động cơ Two-Pass Math Protection trong `app.js`; bọc đáp án câu hỏi ôn tập Mục 12 vào accordion.
- **Kết quả kiểm tra thực tế:** Render hoàn hảo **94 node KaTeX** (công thức căn bậc hai Wilson, đồ thị răng cưa và bảng phân tích xung đột phòng ban).

### 2.5 Chương 5: Các Biến thể Quản trị Tồn kho Thực tế (`CHAP_05.md`)
- **Khuyết tật phát hiện ban đầu:** Công thức phân số lồng nhau của mô hình EPQ và bài toán chiết khấu số lượng bậc thang cần được bảo vệ nguyên vẹn; đáp án câu hỏi ôn tập Mục 12 chưa có tương tác ẩn/hiện.
- **Biện pháp khắc phục:** Bảo vệ toán học ngoại tuyến; bọc đáp án câu hỏi ôn tập Mục 12 vào accordion tương tác.
- **Kết quả kiểm tra thực tế:** Render hoàn hảo **121 node KaTeX** (đỉnh tồn kho $I_{\max}$, thời gian chạy máy $t_1$, thời gian máy nghỉ $t_2$, công thức thiếu hàng và bảng chiết khấu giá).

### 2.6 Chương 6: Tích hợp Quy trình Doanh nghiệp O2C & P2P (`CHAP_06.md`)
- **Khuyết tật phát hiện ban đầu:** Bảng đối chiếu 3 bên (3-Way Matching) và bút toán hạch toán tài khoản bù trừ GR/IR; đáp án câu hỏi ôn tập Mục 12 hiển thị sẵn.
- **Biện pháp khắc phục:** Chuẩn hóa bảng hạch toán; bọc đáp án Mục 12 vào accordion tương tác.
- **Kết quả kiểm tra thực tế:** Render sắc nét **27 node KaTeX** cùng sơ đồ luồng dữ liệu nghiệp vụ tích hợp.

---

## 3. CƠ CHẾ ĐIỀU HƯỚNG ĐỌC CHƯƠNG HỌC (CHAPTER NAVIGATION)

Đã triển khai hệ thống điều hướng đồng bộ ở cả **Đỉnh trang (Top Bar)** và **Chân trang (Bottom Nav)** của trình đọc bài giảng:

- **Bố cục chuẩn:**  
  `[ ← Chương trước / Previous Chapter ]` | `[  Danh sách chương / Chapter List ]` | `[ Chương tiếp theo / Next Chapter → ]`
- **Thanh Banner Thông tin:** Hiển thị nổi bật Huy hiệu số chương (Badge: `Chương 01` đến `Chương 06`), Tiêu đề chương học song ngữ và dòng phụ đề sư phạm.
- **Kiểm soát biên (Boundary Guarding):**
  - Tại **Chương 1**: Nút "Chương trước" tự động vô hiệu hóa (`disabled` attribute, class `.disabled`, opacity 0.45, tooltip *"Đây là chương đầu tiên"*).
  - Tại **Chương 6**: Nút "Chương tiếp theo" tự động vô hiệu hóa (`disabled` attribute, class `.disabled`, opacity 0.45, tooltip *"Đây là chương cuối cùng"*).
- **Trải nghiệm đọc mượt mà:** Khi chuyển chương, hệ thống tự động cuộn màn hình êm ái về đầu trang (`window.scrollTo({ top: 0, behavior: 'smooth' })`), nạp đúng nội dung chương mới và tái lập chỉ mục mục lục 12 phần (TOC).

---

## 4. KHÓA PHIÊN THI TÍNH GIỜ (TIMED EXAM SESSION LOCK)

### 4.1 Phạm vi áp dụng & Phân biệt Chế độ
- **Chế độ Luyện tập (Practice Mode):** Hoàn toàn tự do (Unrestricted). Người học có thể chuyển qua lại giữa các câu hỏi, xem giải thích tức thì, tự do nhấp menu chuyển sang Từ điển, Flashcards, Case Studies hoặc Giáo trình mà không bị khóa.
- **Chế độ Thi tính giờ (Timed Exam Mode):** Kích hoạt cơ chế **Khóa Phiên Thi Toàn Diện (Strict Session Lock)** nhằm bảo vệ tính nghiêm túc của kỳ thi 30 phút.

### 4.2 Hành vi Khóa Điều hướng Nội bộ (Internal Navigation Lock)
Khi bắt đầu bài thi tính giờ (`App.startExam(examId, 'timed')`):
1. Thẻ `<body>` được gắn class `.exam-locked`.
2. Toàn bộ thanh menu điều hướng chính (`.nav-links`), các nút chuyển nhanh trên Header và các hành động khác bị ẩn hoàn toàn khỏi màn hình (`display: none !important`).
3. Logo và thương hiệu nền tảng (`.brand-wrapper`) bị vô hiệu hóa sự kiện nhấp chuột (`pointer-events: none`).
4. Bất kỳ nỗ lực điều hướng có chủ ý nào thông qua hàm `App.navigateTo(viewName)` đều bị chặn lại và tự động mở **Hộp thoại Xác nhận Thoát thi (`#modal-exit-exam`)**.
5. Giao diện làm bài thi vẫn giữ nguyên 100% tính năng: Chuyển câu trước/sau, ghim xem lại (Flag), bảng 25 câu hỏi (Question Palette), đồng hồ đếm ngược và nút nộp bài.

### 4.3 Hộp thoại Xác nhận Thoát Thi Chuẩn Mực
Đường thoát bài thi duy nhất là nút bấm đỏ nổi bật **"Thoát bài thi" / "Exit Exam"** trên thanh công cụ thi, kích hoạt Modal xác nhận:
- **Tiêu đề:** `Thoát bài thi?` (EN: `Exit examination?`)
- **Nội dung cảnh báo:**  
  *Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này. Bạn có chắc chắn muốn thoát không?*  
  *(EN: If you exit now, all answers entered during this examination attempt will be permanently discarded. Your current attempt cannot be restored. Are you sure you want to exit?)*
- **Hành vi nút bấm:**
  - `Tiếp tục làm bài` / `Continue Exam`: Đóng hộp thoại, giữ nguyên 100% các câu trả lời đã chọn và đồng hồ đếm ngược tiếp tục chạy bình thường.
  - `Thoát và xóa bài thi` / `Exit and Discard Attempt`: Dừng đồng hồ (`clearInterval`), xóa sạch câu trả lời tạm thời của lượt thi hiện tại (`state.userAnswers = []`), gỡ bỏ khóa điều hướng (`.exam-locked`), gỡ bỏ sự kiện bảo vệ trình duyệt, đóng modal và đưa người học về màn hình danh sách đề thi (`#view-exams`).
  - **Bảo toàn dữ liệu lịch sử:** Lịch sử các bài thi đã hoàn thành trước đó (`state.examHistory`) cùng dữ liệu Flashcards và tiến độ giáo trình được bảo tồn nguyên vẹn 100%.

### 4.4 Bảo vệ Cấp Trình duyệt (Browser-Level Protection)
- Đăng ký sự kiện `window.addEventListener('beforeunload', ...)` khi thi tính giờ để hiển thị cảnh báo mặc định của trình duyệt nếu người học vô tình tải lại trang (F5) hoặc đóng tab.
- Đăng ký sự kiện `window.addEventListener('popstate', ...)` kết hợp `history.pushState` để bắt sự kiện khi người dùng bấm nút Quay lại (Back button) của trình duyệt, tự động mở Hộp thoại Xác nhận Thoát thi thay vì làm mất bài thi.
- Tự động gỡ bỏ hoàn toàn các event listener này ngay khi bài thi kết thúc hoặc khi người dùng xác nhận thoát thi hợp lệ.

### 4.5 Xử lý Khi Hết Giờ Làm Bài (Timer Expiration)
- Khi đồng hồ đếm ngược chạm mốc `00:00`, hàm `App.tickTimer()` tự động gọi `App.submitExamNow()`.
- Hệ thống chấm điểm tự động, ghi nhận kết quả vào lịch sử bài thi, tự động gỡ bỏ khóa điều hướng `.exam-locked`, gỡ bỏ `beforeunload` và hiển thị màn hình kết quả thi (`#view-exam-results`). Hoàn toàn không gây xung đột hoặc trùng lặp dữ liệu nộp bài.

---

## 5. BẢNG TỔNG HỢP KIỂM THỬ HỒI QUY TỰ ĐỘNG (20/20 PASS)

| Test Case ID | Tên Kịch Bản Kiểm Thử | Kỳ Vọng Kỹ Thuật & Nghiệp Vụ | Kết Quả Thực Tế | Trạng Thái |
|:---:|---|---|---|:---:|
| **TC-01** | Chapter 1 Boundary Navigation | Nút "Chương trước" bị vô hiệu hóa tại Chương 1 | `prevTop.disabled = true`, class `.disabled` | **PASS** |
| **TC-02** | Next Chapter Navigation | Nút "Chương tiếp theo" chuyển từ Ch.1 sang Ch.2 | Nạp đúng `chap-02`, badge cập nhật 'Chương 02' | **PASS** |
| **TC-03** | Sequential Chapter Navigation | Điều hướng tuần tự qua Ch.2 $\to$ Ch.3 $\to$ Ch.4 $\to$ Ch.5 | Nạp chính xác từng chương theo thứ tự | **PASS** |
| **TC-04** | Chapter 6 Boundary Navigation | Nút "Chương tiếp theo" bị vô hiệu hóa tại Chương 6 | `nextTop.disabled = true`, class `.disabled` | **PASS** |
| **TC-05** | Bottom Navigation Cluster | Nút điều hướng chân trang hoạt động tương đương đỉnh trang | Nhấp nút PrevBottom chuyển từ Ch.6 về Ch.5 | **PASS** |
| **TC-06** | Chapter List Navigation | Nút "Danh sách chương" đưa về trang tổng quan giáo trình | Section `#view-chapters` kích hoạt active | **PASS** |
| **TC-07** | Bilingual Navigation Labels | Nhãn nút chuyển ngữ chính xác theo ngôn ngữ chọn | EN: `← Previous Chapter` / VI: `← Chương trước` | **PASS** |
| **TC-08** | Chapter 3 Corrupted BA Check | Chuỗi ký tự lỗi `30/nga` và `vượt xa con số $30` không tồn tại | Không tìm thấy bất kỳ chuỗi lỗi nào trong DOM | **PASS** |
| **TC-09** | Chapter 3 Clean BA Callout | Khối `.ba-insight-callout` hiển thị đủ nội dung song ngữ chuẩn | Callout hiện diện, đủ phân tích chi phí trực tiếp vs vận hành | **PASS** |
| **TC-10** | Review Answers Hidden Initially | Đáp án câu hỏi ôn tập Mục 12 đóng mặc định | 2/2 accordion ở trạng thái đóng (`open = false`) | **PASS** |
| **TC-11** | Review Answers Reveal Interaction | Nhấp vào summary sẽ mở xem đáp án và giải thích | Thuộc tính `open = true`, hiển thị lời giải chi tiết | **PASS** |
| **TC-12** | Chapter 2 Table Cleanliness | Bảng phân bổ 4.2 hiển thị sạch không có ký tự tab | Bảng responsive hiện diện, tổng chi phí $3.260 hiển thị đúng | **PASS** |
| **TC-13** | Practice Mode Unrestricted Nav | Chế độ luyện tập không khóa thanh điều hướng | Menu `.nav-links` hiển thị bình thường | **PASS** |
| **TC-14** | Timed Exam Navigation Locked | Chế độ thi tính giờ ẩn thanh điều hướng và khóa brand | `.nav-links` bị ẩn (`display: none`), timer hiển thị | **PASS** |
| **TC-15** | In-App Navigation Blocked | Cố gắng bấm chuyển trang trong lúc thi sẽ bị chặn | Chặn điều hướng, mở Modal `#modal-exit-exam` | **PASS** |
| **TC-16** | Continue Exam State Retention | Chọn "Tiếp tục làm bài" giữ nguyên câu trả lời và timer | Modal đóng, đáp án 'B' được bảo lưu, bài thi tiếp diễn | **PASS** |
| **TC-17** | Confirm Exit Clears Attempt | Chọn "Thoát và xóa bài thi" xóa câu trả lời, mở khóa nav | Xóa đáp án, gỡ `.exam-locked`, về `#view-exams` | **PASS** |
| **TC-18** | Timer Expiration Auto-Submit | Đồng hồ về 00:00 tự động nộp bài và mở khóa điều hướng | Tự động chấm điểm, lưu lịch sử, mở khóa nav | **PASS** |
| **TC-19** | All 6 Chapters KaTeX Render | Cả 6 chương học render thành công công thức toán KaTeX | Ch1: 81; Ch2: 60; Ch3: 53; Ch4: 94; Ch5: 121; Ch6: 27 nodes | **PASS** |
| **TC-20** | Existing Modules Regression | Bảo toàn 62 flashcards, 4 case studies và 8 prompt chips AI | Đủ 62 thẻ, 4 cases responsive, 8 chips cố vấn AI | **PASS** |

---

## 6. HẠN CHẾ CÒN LẠI VÀ LƯU Ý KỸ THUẬT

1. **Thông điệp `beforeunload` của trình duyệt:** Theo tiêu chuẩn bảo mật của các trình duyệt hiện đại (Chrome, Edge, Firefox, Safari), văn bản tùy biến trong hàm `beforeunload` sẽ bị trình duyệt ghi đè bằng thông điệp bảo mật mặc định (ví dụ: *"Changes you made may not be saved"*). Ứng dụng đã xử lý tối ưu bằng cách hiển thị Modal tùy biến song ngữ đầy đủ khi người dùng tương tác trong ứng dụng.
2. **Biểu đồ Mermaid ngoại tuyến:** Sơ đồ quy trình Mermaid được cấu hình nạp an toàn khi có thư viện; trường hợp xem ngoại tuyến thuần túy, nội dung văn bản quy trình và các bảng biểu đối chiếu vẫn được hiển thị đầy đủ, không ảnh hưởng đến trải nghiệm tiếp thu kiến thức.

---
*Báo cáo được khởi tạo tự động dựa trên kết quả kiểm thử thực tế trên Microsoft Edge Headless CDP.*
