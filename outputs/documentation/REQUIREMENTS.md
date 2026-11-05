# YÊU CẦU HỆ THỐNG & ĐẶC TẢ NGHIỆP VỤ (REQUIREMENTS SPECIFICATION)
## ERP Knowledge Hub: Enterprise Resource Planning & Supply Chain Management Learning Platform

---

## 1. Tổng Quan Dự Án & Phạm Vi Nghiệp Vụ (Project Scope)

Dự án **ERP Knowledge Hub** là nền tảng học tập số hóa độc lập, chuyên sâu và song ngữ (Tiếng Việt mặc định & Tiếng Anh) dành cho sinh viên, giảng viên và chuyên viên Phân tích Nghiệp vụ (Business Analyst - BA) trong lĩnh vực Hoạch định Nguồn lực Doanh nghiệp (ERP) và Quản trị Chuỗi cung ứng (Supply Chain Management - SCM).

Hệ thống được phát triển dựa trên việc thẩm định và chuẩn hóa toàn bộ học liệu giáo trình đại học UEH 2020 (149 trang của tác giả Y Hoang), 4 bộ hồ sơ nghiên cứu tình huống thực tế (Texago Corp., Better Products Company, Atlantic Coast Tire Corp., và SOCA TV), cùng hình ảnh dữ liệu bổ sung.

---

## 2. Ma Trận Truy Xuất Yêu Cầu (Requirements Traceability Matrix - RTM)

| Mã Yêu Cầu | Phân Hệ / Mô-đun | Loại Yêu Cầu | Mô Tả Tóm Tắt | Trạng Thái |
|---|---|---|---|---|
| **REQ-ARC-01** | Architecture | Constraint | Cấu trúc thư mục nghiêm ngặt: `references/` ở chế độ Read-Only tuyệt đối; toàn bộ mã nguồn và dữ liệu lưu tại `outputs/`. | **ĐÃ HOÀN THÀNH** |
| **REQ-LNG-01** | Localization | Functional | Ngôn ngữ mặc định là Tiếng Việt; hỗ trợ nút chuyển đổi sang Tiếng Anh trên toàn bộ giao diện và dữ liệu. | **ĐÃ HOÀN THÀNH** |
| **REQ-LNG-02** | Localization | Non-Functional | Chuyển đổi ngôn ngữ không được làm mất trạng thái làm bài thi, tiến độ thẻ flashcard hoặc tab đang đọc. | **ĐÃ HOÀN THÀNH** |
| **REQ-CHP-01** | Knowledge Base | Functional | 6 chương học giáo trình chuẩn mực (Weeks 1 - 6), mỗi chương tuân thủ nghiêm ngặt 12 phần sư phạm bắt buộc. | **ĐÃ HOÀN THÀNH** |
| **REQ-EXM-01** | Exam Center | Functional | Chính xác 10 đề thi × 25 câu hỏi = 250 câu hỏi trắc nghiệm song ngữ độc nhất, không trùng lặp. | **ĐÃ HOÀN THÀNH** |
| **REQ-EXM-02** | Exam Center | Business Rule | Tỷ lệ độ khó mỗi đề thi: Đúng 10 câu Cơ bản (40%), 10 câu Trung bình (40%), và 5 câu Nâng cao (20%). | **ĐÃ HOÀN THÀNH** |
| **REQ-EXM-03** | Exam Center | Functional | Hỗ trợ 2 chế độ: Chế độ Luyện tập (phản hồi tức thời) và Chế độ Thi tính giờ (đếm ngược 30 phút, nộp tự động khi 00:00). | **ĐÃ HOÀN THÀNH** |
| **REQ-CRD-01** | Flashcards | Functional | Hệ thống 30 thẻ ghi nhớ phân loại theo Định nghĩa, Công thức, Mô hình, Quy tắc ERP và Phân biệt khái niệm. | **ĐÃ HOÀN THÀNH** |
| **REQ-CRD-02** | Flashcards | Interactive | Hiệu ứng lật 3D, đánh dấu Đã thuộc / Cần ôn lại, bộ xáo trộn ngẫu nhiên (Fisher-Yates Shuffle). | **ĐÃ HOÀN THÀNH** |
| **REQ-GLS-01** | Glossary | Functional | Từ điển 40 thuật ngữ chuyên ngành có tìm kiếm thời gian thực, lọc A-Z, ví dụ thực tế và ánh xạ bảng SAP/Oracle. | **ĐÃ HOÀN THÀNH** |
| **REQ-CAS-01** | Case Studies | Functional | 4 Case Studies: Nguyên văn Tiếng Anh đầy đủ + Bản dịch Tiếng Việt + Phân tích BA + Bộ công cụ giải toán tương tác. | **ĐÃ HOÀN THÀNH** |
| **REQ-CAS-02** | Case Studies | Data Audit | Khắc phục triệt để lỗi thiếu dữ liệu nhu cầu của Case 1 Texago thông qua ảnh bổ sung (Pittsburgh 100, Atlanta 80, KC 80, SF 100). | **ĐÃ HOÀN THÀNH** |
| **REQ-AI-01** | AI Consultant | Functional | 8 kịch bản sư phạm định cấu hình sẵn với prompt chips; động cơ phản hồi thông minh chạy offline và tùy chọn API key. | **ĐÃ HOÀN THÀNH** |
| **REQ-UI-01** | UI/UX Design | Design System | Bảng màu Balletcore thanh lịch (Petal Frost, Coffee Bean, Vanilla Cream, Dusty Rose); tuyệt đối KHÔNG hình ảnh vũ công ballet. | **ĐÃ HOÀN THÀNH** |
| **REQ-OFF-01** | Standalone App | Technical | Ứng dụng chạy độc lập không phụ thuộc build server, tự tải được dữ liệu khi mở trực tiếp file `index.html`. | **ĐÃ HOÀN THÀNH** |

---

## 3. Đặc Tả Yêu Cầu Chức Năng (Functional Requirements - FR)

### 3.1 Phân Hệ Giáo Trình (Knowledge Base - FR-KB)
- **FR-KB-01**: Cung cấp mục lục điều hướng 6 chương học (Tuần 1 đến Tuần 6).
- **FR-KB-02**: Mỗi chương bao gồm đầy đủ 12 mục sư phạm chuẩn:
  1. Tổng quan Chương học (Overview, Objectives, Relevance, Pre-requisites)
  2. Các Khái niệm Cốt lõi (Core Concepts với định nghĩa song ngữ)
  3. Thuật ngữ Kỹ thuật & Bảng phân biệt (Key Terminologies)
  4. Mô hình, Khung lý thuyết & Công thức toán học có giải tích mẫu (Quantitative Methods)
  5. Quy trình Nghiệp vụ Doanh nghiệp & Sơ đồ tuần tự (Business Processes)
  6. Minh họa Trực quan (Visual Learning với sơ đồ Mermaid)
  7. Ví dụ Thực tế Doanh nghiệp (Practical Business Examples)
  8. Ứng dụng trong Hệ thống ERP (ERP Applications: Transaction codes, Database tables)
  9. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (Business Analyst Perspective: RACI, FR, NFR, BR, UAT)
  10. Phân tích Phản biện & Đánh đổi Chiến lược (Critical Analysis & Strategic Trade-offs)
  11. Tóm tắt Chương học (Chapter Summary)
  12. Kiểm tra Đánh giá Nhanh (Knowledge Check với câu hỏi tự luyện)
- **FR-KB-03**: Hỗ trợ đánh dấu "Đã hoàn thành chương này" và lưu trạng thái vào `localStorage`.

### 3.2 Phân Hệ Luyện Thi & Trắc Nghiệm (Examination System - FR-EX)
- **FR-EX-01**: Ngân hàng đề thi gồm 10 bài thi chuẩn hóa, mỗi bài 25 câu hỏi độc nhất (tổng cộng 250 câu hỏi).
- **FR-EX-02 (Chế độ Luyện tập)**:
  - Cho phép người học chọn câu trả lời và xem ngay kết quả Đúng/Sai bằng màu sắc (Xanh lá / Đỏ).
  - Tự động hiển thị khung giải thích cặn kẽ vì sao đáp án đúng là chính xác và chỉ rõ bẫy sai lầm của 3 đáp án còn lại.
- **FR-EX-03 (Chế độ Thi tính giờ)**:
  - Đồng hồ đếm ngược từ 30:00 về 00:00 hiển thị ở cả khung thi và thanh điều hướng trên cùng.
  - Cảnh báo thị giác (chuyển sang màu đỏ nhấp nháy) khi thời gian còn dưới 5 phút.
  - Bảng điều hướng 25 nút câu hỏi hiển thị trạng thái: Đang xem, Đã trả lời, Đã đánh dấu xem lại (Flagged).
  - Hộp thoại xác nhận nộp bài hiển thị rõ số câu đã trả lời và số câu còn bỏ trống.
  - Tự động nộp bài khi đồng hồ chạm 00:00.
  - Trang báo cáo kết quả hiển thị Điểm số, Tỷ lệ phần trăm, Phân loại Đạt/Không đạt (ngưỡng 70%), và cho phép xem lại toàn bộ câu hỏi.

### 3.3 Phân Hệ Thẻ Ghi Nhớ (Flashcards System - FR-FC)
- **FR-FC-01**: Danh mục 30 thẻ ghi nhớ bao quát cả 6 chương học.
- **FR-FC-02**: Hỗ trợ lật thẻ 3 chiều (Mặt trước: Câu hỏi/Khái niệm; Mặt sau: Định nghĩa/Công thức/Hàm ý ERP).
- **FR-FC-03**: Thao tác đánh dấu "Đã thuộc" và "Cần ôn lại" kèm bộ đếm tiến độ học tập.
- **FR-FC-04**: Hỗ trợ lọc thẻ theo phân loại: Tất cả, Cần ôn lại, Công thức, Quy tắc ERP.
- **FR-FC-05**: Hỗ trợ phím tắt: Bấm Spacebar để lật thẻ, Phím mũi tên Trái/Phải để chuyển thẻ.

### 3.4 Phân Hệ Từ Điển Thuật Ngữ (Glossary System - FR-GL)
- **FR-GL-01**: Cung cấp 40 thuật ngữ cốt lõi song ngữ Anh - Việt.
- **FR-GL-02**: Tìm kiếm tức thời (Instant search) theo tên tiếng Anh, tên tiếng Việt, từ viết tắt và nội dung định nghĩa.
- **FR-GL-03**: Thanh điều hướng ký tự alphabet (A-Z) lọc nhanh theo chữ cái đầu của thuật ngữ tiếng Anh.
- **FR-GL-04**: Hộp thoại chi tiết thuật ngữ hiển thị đầy đủ: Định nghĩa, Ví dụ doanh nghiệp, Ánh xạ bảng dữ liệu ERP (SAP/Oracle), và các thẻ thuật ngữ liên quan có thể nhấp để liên kết chéo.

### 3.5 Phân Hệ Nghiên Cứu Tình Huống (Case Studies - FR-CS)
- **FR-CS-01**: Tích hợp 4 Case Studies: Texago Corp. (Case 1), Better Products Company (Case 2), Atlantic Coast Tire (Case 3), và SOCA (Case 4).
- **FR-CS-02**: Mỗi tình huống cung cấp văn bản gốc tiếng Anh nguyên vẹn không lược bỏ, bản dịch tiếng Việt học thuật, và bản đặc tả phân tích Business Analyst.
- **FR-CS-03**: Tích hợp bộ công cụ tính toán mô phỏng trực quan:
  - *Texago Solver*: Tính toán và xếp hạng tổng chi phí 3 địa điểm (LA, Galveston, St. Louis).
  - *Better Products Solver*: So sánh phương án chia tách ($3.260/ngày) và phương án chuyên biệt 0-1 ($3.290/ngày).
  - *ACT Solver*: Đối chiếu 4 chính sách tồn kho (Trực giác, EOQ cơ bản, Thiếu hàng, Chiết khấu số lượng).
  - *SOCA Solver*: Tính toán tự động cỡ lô EPQ ($Q^*$), mức tồn kho cực đại ($I_{\max}$), thời gian chạy máy ($t_p$) và khoản tiết kiệm ròng.

### 3.6 Phân Hệ Cố Vấn Tri Thức AI (AI Study Consultant - FR-AI)
- **FR-AI-01**: Cung cấp 8 kịch bản sư phạm chuyên sâu:
  1. Giải thích Khái niệm Chuyên sâu (Concept Explanation)
  2. So sánh & Phân biệt Khái niệm (Concept Comparison)
  3. Phân tích Tình huống Doanh nghiệp (Business Scenario Analysis)
  4. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (BA Perspective)
  5. Thảo luận Tình huống Nghiên cứu (Case Study Discussion)
  6. Giải bài toán Định lượng & Tối ưu hóa (Quantitative Problem Solving)
  7. Gia sư Luyện thi & Giải thích Đáp án (Exam Tutor)
  8. Tư duy Phản biện & Đánh đổi Chiến lược (Critical Thinking)
- **FR-AI-02**: Mỗi kịch bản có 4 prompt chips dựng sẵn, có thể nhấp để tự động điền vào khung chat.
- **FR-AI-03**: Động cơ tri thức chạy ngầm có khả năng nhận diện ngữ cảnh và trả lời lập tức các câu hỏi về Texago, SOCA, ACT, Better Products, EOQ, 3-Way Matching mà không cần internet.
- **FR-AI-04**: Cung cấp giao diện cấu hình API Key (Google Gemini hoặc OpenAI) lưu trữ an toàn tại phiên làm việc cục bộ của trình duyệt.

---

## 4. Đặc Tả Yêu Cầu Phi Chức Năng (Non-Functional Requirements - NFR)

- **NFR-PERF-01 (Tốc độ phản hồi)**: Mọi thao tác chuyển tab, tìm kiếm từ điển, lật flashcard và chuyển câu hỏi thi phải diễn ra dưới 100ms.
- **NFR-PORT-01 (Tính di động & Khả năng chạy Offline)**: Ứng dụng phải hoạt động bình thường khi người dùng mở trực tiếp tệp `outputs/app/index.html` trong bất kỳ trình duyệt hiện đại nào (Chrome, Edge, Firefox, Safari) mà không bị lỗi CORS chặn dữ liệu.
- **NFR-RESP-01 (Đáp ứng đa thiết bị)**: Giao diện thích ứng linh hoạt (Responsive) từ màn hình điện thoại di động (tối thiểu 375px), máy tính bảng (768px - 1024px) đến màn hình máy tính để bàn (1440px+).
- **NFR-PERS-01 (Tính bền bỉ của dữ liệu)**: Tiến độ học tập, điểm thi, thẻ ghi nhớ đã thuộc và cấu hình ngôn ngữ phải được lưu giữ bền vững qua `localStorage` và tự động khôi phục khi tải lại trang.
- **NFR-SECR-01 (Bảo mật thông tin)**: Khóa API người dùng nhập vào chỉ được lưu trong `sessionStorage` của trình duyệt và tuyệt đối không bao giờ được gửi về bất kỳ máy chủ bên thứ ba nào ngoại trừ endpoint của nhà cung cấp mô hình AI chính thức.

---

## 5. Quy Tắc Nghiệp Vụ Doanh Nghiệp (Business Rules - BR)

- **BR-DATA-01**: Tuyệt đối không được can thiệp, chỉnh sửa, đổi tên hoặc xóa các tệp tài liệu gốc trong thư mục `references/`.
- **BR-MATH-01**: Trong mô hình vận tải tuyến tính, nếu tổng cung lớn hơn tổng cầu, hệ thống bắt buộc phải khởi tạo một điểm đến ảo (Dummy Destination) với nhu cầu bằng hiệu số cung - cầu và chi phí đơn vị bằng 0.
- **BR-MATH-02**: Tuyến đường cấm phải được áp dụng hệ số phạt $M$ sao cho $M \gg \max(c_{ij})$ để ép sản lượng phân bổ trên tuyến về 0 trong hàm cực tiểu hóa chi phí.
- **BR-MATH-03**: Trong mô hình EOQ cơ bản, tại điểm tối ưu $Q^*$, chi phí đặt hàng hàng năm và chi phí lưu kho hàng năm bắt buộc phải cân bằng bằng nhau: $\text{AOC}(Q^*) = \text{AHC}(Q^*)$.
- **BR-MATH-04**: Trong mô hình EPQ bổ sung dần, điều kiện tiên quyết là tốc độ sản xuất danh định phải lớn hơn tốc độ tiêu thụ ($p > d$).
- **BR-UI-01**: Phong cách thẩm mỹ Balletcore chỉ được thể hiện thông qua bảng màu tinh tế, kiểu chữ serif/sans-serif hiện đại và đường nét thẻ card mềm mại; nghiêm cấm việc đưa các hình ảnh vũ công ballet, giày múa, nơ ruy băng trang trí sến súa vào giao diện.
