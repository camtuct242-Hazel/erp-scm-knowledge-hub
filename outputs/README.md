# ERP & SCM KNOWLEDGE HUB
## Nền Tảng Học Tập Chuyên Sâu Hoạch Định Nguồn Lực Doanh Nghiệp & Quản Trị Chuỗi Cung Ứng
### Enterprise Resource Planning & Supply Chain Management Interactive Learning Platform

---

## 1. Giới Thiệu Dự Án (Project Overview)

**ERP & SCM Knowledge Hub** là một nền tảng học tập số hóa độc lập, toàn diện và song ngữ (Tiếng Việt mặc định & Tiếng Anh), được thiết kế dành cho sinh viên, giảng viên và các chuyên viên Phân tích Nghiệp vụ (Business Analyst - BA) mong muốn làm chủ các nguyên lý vận hành cốt lõi của hệ thống Hoạch định Nguồn lực Doanh nghiệp (ERP) và các mô hình tối ưu hóa Chuỗi cung ứng (Supply Chain Management - SCM).

Hệ thống được phát triển dựa trên việc thẩm định, chuẩn hóa và mở rộng toàn diện từ học liệu giáo trình đại học UEH 2020 (*Enterprise Resource Planning Applied to Logistics & SCM* của tác giả Y Hoang, 149 trang) cùng 4 bộ hồ sơ nghiên cứu tình huống thực tế kinh điển (Texago Corp., Better Products Company, Atlantic Coast Tire Corp., và SOCA TV).

---

## 2. Điểm Nhấn Tính Năng Nổi Bật (Key Features)

### 2.1 Ứng Dụng Web Tự Chứa & Chạy Độc Lập 100% (Zero-Build Standalone App)
- Không yêu cầu cài đặt máy chủ Node.js hay tiến trình build phức tạp.
- Toàn bộ cơ sở dữ liệu (250 câu hỏi, 6 chương học, 4 case studies, 40 thuật ngữ, 30 flashcards, 8 kịch bản AI) đã được đóng gói sẵn trong tệp `outputs/app/data.js` (1.1 MB).
- **Khởi chạy tức thì**: Người dùng chỉ cần nhấp đúp trực tiếp vào tệp `outputs/app/index.html` trong Windows Explorer (`file:///...`) để trải nghiệm toàn bộ nền tảng mà không bị lỗi CORS chặn dữ liệu.

### 2.2 Công Tắc Song Ngữ Bảo Toàn Trạng Thái (State-Preserving Bilingual Engine)
- Ngôn ngữ mặc định là **Tiếng Việt**, hỗ trợ nút chuyển đổi sang **Tiếng Anh** tại thanh điều hướng trên cùng.
- Khi chuyển đổi ngôn ngữ, hệ thống **bảo toàn 100% trạng thái người dùng**: không làm mất câu trả lời trắc nghiệm đang chọn, không reset đồng hồ đếm ngược bài thi, giữ nguyên vị trí thẻ flashcard và tab tài liệu đang đọc.

### 2.3 Hệ Thống Giáo Trình Chuẩn Mực 12 Phần (12-Section Pedagogical Framework)
Gồm 6 chương học chi tiết tương ứng với 6 tuần học của giáo trình:
1. **Chương 1**: Tổng quan ERP, 3 dòng chảy SCM & Mô hình Vận tải Tuyến tính cân bằng (P&T Company Case: \$179.850 $\to$ \$152.535).
2. **Chương 2**: Biến thể Vận tải, Cung $\neq$ Cầu (Dummy Source/Destination), Tuyến cấm & Phương pháp Big-M (Metro Water, Energetic Co., Better Products Case 2.1).
3. **Chương 3**: Khoảng Nhu cầu [Min, Max] (Middletown School), Cực đại hóa Lợi nhuận (Nifty Co.), Phân công Nhị phân 0-1, Thuật toán Hungarian & Better Products Case 2.2.
4. **Chương 4**: Quản trị Tồn kho Khoa học, 4 cấu phần chi phí ($c, K, h, p$), Dẫn xuất công thức Wilson EOQ, Điểm cân bằng chi phí, Điểm đặt hàng lại (ROP) & Atlantic Coast Tire baseline ($Q^* = 573$, tiết kiệm \$382,52/năm).
5. **Chương 5**: Các biến thể EOQ thực tế: Thiếu hàng có kế hoạch (ACT Backorders: $Q^* = 716, S^* = 257$), Chiết khấu số lượng (Breakpoints: $Q = 750$), và Bổ sung dần dần (EPQ - SOCA Case Study: $Q^* = 50.000$, tiết kiệm \$16.000/năm).
6. **Chương 6**: Tích hợp Đa phân hệ (MM, PP, SD, FI/CO, TM, EWM), 3 trụ cột Dữ liệu Chủ (Master Data Governance), 3 chu trình khép kín O2C, P2P (3-Way Matching), Plan-to-Produce & Khung năng lực BA.

Mỗi chương đều tuân thủ nghiêm ngặt 12 phần sư phạm: *Tổng quan, Khái niệm cốt lõi, Thuật ngữ, Mô hình định lượng, Quy trình nghiệp vụ, Minh họa trực quan (Mermaid), Ví dụ thực tế, Ứng dụng ERP (SAP/Oracle tables), Góc nhìn BA, Phân tích phản biện, Tóm tắt và Kiểm tra nhanh.*

### 2.4 Trung Tâm Luyện Thi & Thi Tính Giờ (250 Câu Hỏi Chuẩn Hóa)
- Ngân hàng gồm **10 đề thi × 25 câu = Đúng 250 câu hỏi** trắc nghiệm song ngữ độc nhất.
- Tỷ lệ độ khó khoa học: Đúng **10 câu Cơ bản (40%)**, **10 câu Trung bình (40%)**, và **5 câu Nâng cao (20%)** trên mỗi đề.
- **Chế độ Luyện tập**: Không giới hạn thời gian; click chọn phương án để xem ngay kết quả Đúng/Sai kèm lời giải thích cặn kẽ vì sao phương án đó đúng và chỉ rõ các bẫy sai lầm của 3 phương án còn lại.
- **Chế độ Thi tính giờ**: Đồng hồ đếm ngược 30 phút, bảng điều hướng 25 nút câu hỏi (Unanswered, Answered, Flagged), hộp thoại xác nhận nộp bài, tự động nộp khi hết giờ, bảng điểm tổng kết và xem lại toàn bộ câu hỏi.

### 2.5 Thẻ Ghi Nhớ Phản Xạ Nhanh (Spaced Repetition Flashcards)
- 30 thẻ ghi nhớ bao quát 6 chương học, phân loại theo: Định nghĩa, Mô hình, Công thức, Phân biệt khái niệm và Quy tắc nghiệp vụ ERP.
- Hiệu ứng lật 3D mượt mà trên click hoặc phím Spacebar.
- Đánh dấu "Đã thuộc" và "Cần ôn lại" kèm bộ đếm tiến độ. Hỗ trợ lọc danh sách chỉ xem các thẻ cần ôn lại.

### 2.6 Từ Điển Thuật Ngữ Chuyên Ngành (Bilingual Glossary)
- 40 thuật ngữ cốt lõi song ngữ Anh - Việt.
- Thanh tìm kiếm thời gian thực, bộ lọc danh mục và thanh chữ cái A-Z.
- Modal chi tiết hiển thị: Định nghĩa chuyên ngành, Ví dụ doanh nghiệp thực tế, Ánh xạ bảng dữ liệu ERP (SAP/Oracle), và các thẻ thuật ngữ liên quan có thể nhấp để liên kết chéo.

### 2.7 Thư Viện 4 Tình Huống Doanh Nghiệp (Case Studies & Interactive Solvers)
- Tích hợp 4 Case Studies: Texago Corp. (Case 1), Better Products (Case 2), Atlantic Coast Tire (Case 3), và SOCA (Case 4).
- Mỗi tình huống cung cấp văn bản gốc tiếng Anh đầy đủ (Unabridged Original English), bản dịch tiếng Việt học thuật, và bản đặc tả phân tích Business Analyst.
- **Bộ công cụ tính toán mô phỏng tương tác**:
  - *Texago Solver*: Tính toán và xếp hạng tổng chi phí 3 địa điểm (LA, Galveston, St. Louis).
  - *Better Products Solver*: So sánh phương án chia tách (\$3.260/ngày) và phương án chuyên biệt 0-1 (\$3.290/ngày).
  - *ACT Solver*: Đối chiếu 4 chính sách tồn kho (Trực giác, EOQ cơ bản, Thiếu hàng, Chiết khấu số lượng).
  - *SOCA Solver*: Tính toán tự động cỡ lô EPQ ($Q^*$), mức tồn kho cực đại ($I_{\max}$), thời gian chạy máy ($t_p$) và khoản tiết kiệm ròng.

### 2.8 Cố Vấn Tri Thức AI (AI Study Consultant)
- 8 kịch bản sư phạm chuyên sâu với các prompt chips dựng sẵn.
- Động cơ tri thức chạy ngầm có khả năng nhận diện ngữ cảnh và trả lời lập tức các câu hỏi về Texago, SOCA, ACT, Better Products, EOQ, 3-Way Matching hoàn toàn offline.
- Tùy chọn cấu hình khóa API (Google Gemini hoặc OpenAI) được lưu trữ an toàn trong phiên làm việc cục bộ để trò chuyện tự do với các mô hình LLM lớn bên ngoài.

### 2.9 Thiết Kế Thẩm Mỹ Balletcore (Balletcore Design System)
- Bảng màu lấy cảm hứng từ phong cách Balletcore tinh tế:
  - **Petal Frost**: `#FFD1DC`
  - **Coffee Bean**: `#1B1110`
  - **Vanilla Cream**: `#FFF8F5`
  - **Dusty Rose**: `#DFA6B5`
  - **Warm Ballet Beige**: `#EADFD9`
  - **Muted Mauve**: `#8B7778`
- Sử dụng kiểu chữ tiêu đề có chân thanh lịch (`Playfair Display`), phông chữ giao diện hiện đại (`Plus Jakarta Sans`), và phông chữ đơn cách cho mã lệnh/công thức (`JetBrains Mono`).
- **Tuân thủ tuyệt đối quy tắc người dùng**: Phong cách Balletcore chỉ được thể hiện thông qua bảng màu, typography và đường nét thẻ card; **nghiêm cấm mọi hình ảnh vũ công ballet, giày múa hay nơ ruy băng**.

---

## 3. Cấu Trúc Thư Mục Dự Án (Repository Architecture)

```text
c:\Kiến thức cần học\ERP (SCM)/
│
├── references/                               # Thư mục gốc chứa tài liệu tham khảo (READ-ONLY)
│   ├── Case studies/
│   │   ├── Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg
│   │   ├── Case 1 – A CASE STUDY THE TEXAGO CORP. ...pdf
│   │   ├── Case 2.1 – ASSIGNING PLANTS TO PRODUCTS ...pdf
│   │   ├── Case 3 – The Atlantic coast tire corp (ACT) problem.pdf
│   │   └── Case 4 – SOCA - gradual replenishment.pdf
│   └── ERP transportation  inventory Textbook for Students.pdf
│
└── outputs/                                  # TOÀN BỘ SẢN PHẨM PHÁT TRIỂN NẰM TẠI ĐÂY
    │
    ├── README.md                             # Hướng dẫn tổng quan và vận hành nền tảng
    │
    ├── documentation/                        # Tài liệu phân tích và báo cáo kỹ thuật
    │   ├── REFERENCE_INVENTORY.md            # Bảng kiểm kê và thẩm định tài liệu gốc
    │   ├── TEXTBOOK_CONTENT_AUDIT.md         # Báo cáo thẩm định chi tiết giáo trình 149 trang
    │   ├── CASE_STUDY_INVENTORY.md           # Thẩm định chuyên sâu 4 tình huống & ảnh bổ sung
    │   ├── KNOWLEDGE_ARCHITECTURE.md         # Kiến trúc miền tri thức & Ma trận thuật ngữ song ngữ
    │   ├── REQUIREMENTS.md                   # Đặc tả yêu cầu hệ thống (BRD, FR, NFR, RTM)
    │   ├── TEST_REPORT.md                    # Báo cáo kiểm thử chất lượng toàn diện (100% Pass)
    │   └── TEST_AUDIT_LOG.txt                # Nhật ký kiểm thử tự động
    │
    ├── data/                                 # Cơ sở dữ liệu JSON chuẩn mực
    │   ├── chapters.json                     # Danh mục metadata 6 chương học
    │   ├── examinations.json                 # 10 đề thi × 25 câu = 250 câu hỏi trắc nghiệm
    │   ├── flashcards.json                   # 30 thẻ ghi nhớ phân loại đa chiều
    │   ├── glossary.json                     # 40 thuật ngữ chuyên ngành có ví dụ & ERP mapping
    │   ├── case-studies.json                 # Metadata & tham số 4 tình huống doanh nghiệp
    │   └── scenarios.json                    # 8 kịch bản sư phạm AI Consultant & prompt chips
    │
    ├── content/                              # Nội dung văn bản chuyên sâu (.md)
    │   ├── chapters/                         # 6 chương học giáo trình chuẩn 12 phần
    │   │   ├── CHAP_01.md                    # Chương 1: Tổng quan ERP & Vận tải Tuyến tính
    │   │   ├── CHAP_02.md                    # Chương 2: Biến thể Vận tải & Big-M Tuyến Cấm
    │   │   ├── CHAP_03.md                    # Chương 3: Khoảng Nhu cầu & Phân công 0-1
    │   │   ├── CHAP_04.md                    # Chương 4: Quản trị Tồn kho & EOQ Cơ bản
    │   │   ├── CHAP_05.md                    # Chương 5: Biến thể EOQ: Thiếu hàng, Chiết khấu, EPQ
    │   │   └── CHAP_06.md                    # Chương 6: Tích hợp Quy trình & Vận hành SCM
    │   │
    │   └── case-studies/                     # 4 tình huống nghiên cứu đầy đủ
    │       ├── CASE_01_TEXAGO.md             # Texago Site Selection (Anh + Việt + BA)
    │       ├── CASE_02_BETTER_PRODUCTS.md    # Better Products 2.1 & 2.2 (Anh + Việt + BA)
    │       ├── CASE_03_ACT_TIRE.md           # Atlantic Coast Tire Problem (Anh + Việt + BA)
    │       └── CASE_04_SOCA.md               # SOCA Gradual Replenishment (Anh + Việt + BA)
    │
    └── app/                                  # Ứng dụng web chạy độc lập (Production-Ready)
        ├── index.html                        # Giao diện chính của nền tảng học tập
        ├── style.css                         # Bảng kiểu dáng chuẩn Balletcore
        ├── data.js                           # Cơ sở dữ liệu đóng gói sẵn (1.1 MB)
        └── app.js                            # Động cơ xử lý giao diện, thi thử, flashcards, AI
```

---

## 4. Hướng Dẫn Vận Hành Nền Tảng (User & Installation Guide)

### Cách 1: Khởi Chạy Trực Tiếp (Khuyến Nghị - Đơn Giản Nhất)
Không cần cài đặt bất kỳ phần mềm trung gian nào:
1. Mở Windows Explorer, điều hướng đến thư mục:
   `c:\Kiến thức cần học\ERP (SCM)\outputs\app\`
2. Nhấp đúp chuột vào tệp:
   `index.html`
3. Ứng dụng sẽ tự động mở trên trình duyệt mặc định của bạn (Microsoft Edge, Google Chrome, Firefox, v.v.) và hoạt động đầy đủ tính năng ngay lập tức.

### Cách 2: Chạy Qua Máy Chủ Tĩnh Cục Bộ (Tùy Chọn)
Nếu bạn muốn chạy qua giao thức `http://localhost`:
Mở PowerShell tại thư mục gốc và thực thi lệnh:
```powershell
cd "c:\Kiến thức cần học\ERP (SCM)\outputs\app"
python -m http.server 8000
```
Sau đó truy cập trình duyệt tại địa chỉ: `http://localhost:8000`.

---

## 5. Xác Nhận Kiểm Thử & Nghiệm Thu (Quality Assurance Certification)

Toàn bộ hệ thống đã vượt qua kiểm định tự động với tỷ lệ thành công 100%:
- **Bảo toàn thư mục gốc**: Thư mục `references/` hoàn toàn nguyên vẹn, không có bất kỳ sửa đổi nào.
- **Ngân hàng đề thi**: Đủ 10 đề thi, mỗi đề đúng 25 câu hỏi độc nhất, tỷ lệ 10 Cơ bản / 10 Trung bình / 5 Nâng cao, đầy đủ phương án và giải thích song ngữ chi tiết.
- **Giáo trình**: Đủ 6 chương học, mỗi chương tuân thủ nghiêm ngặt 12 phần sư phạm.
- **Case studies**: Đủ 4 tình huống có văn bản gốc tiếng Anh nguyên vẹn, bản dịch tiếng Việt chuẩn xác và đặc tả Business Analyst.
- **Giao diện & Chức năng**: Công tắc song ngữ mượt mà, đồng hồ đếm ngược 30 phút hoạt động chuẩn xác, bộ công cụ giải toán tương tác cho ra kết quả trùng khớp với số liệu kế toán thực tế.
