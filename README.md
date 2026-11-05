# ERP & Supply Chain Management Knowledge Hub
### Nền Tảng Học Tập & Thực Hành Chuyên Sâu Hoạch Định Nguồn Lực Doanh Nghiệp & Quản Trị Chuỗi Cung Ứng

[![Bilingual: Vietnamese / English](https://img.shields.io/badge/Language-Bilingual%20(VI%20%7C%20EN)-B8737E.svg)](outputs/app/index.html)
[![Standard: UEH 2020](https://img.shields.io/badge/Curriculum-UEH%202020%20Standard-E8C5C8.svg)](outputs/app/index.html)
[![Role: Business Analyst](https://img.shields.io/badge/Perspective-Business%20Analyst%20(BA)-8C6D73.svg)](outputs/app/index.html)
[![Offline Capable](https://img.shields.io/badge/Architecture-100%25%20Offline%20Standalone-success.svg)](outputs/app/index.html)

---

## 1. Giới Thiệu Dự Án (Overview)

**ERP & Supply Chain Management Knowledge Hub** là nền tảng học tập tri thức giáo dục độc lập được thiết kế chuyên biệt nhằm chuẩn hóa và nâng cao năng lực cho sinh viên, giảng viên và chuyên viên **Business Analyst (BA)** trong các lĩnh vực:
- **Hoạch định Nguồn lực Doanh nghiệp (Enterprise Resource Planning - ERP)**: Kiến trúc 3 tầng (Database, Application, Presentation), tích hợp luồng nghiệp vụ O2C (Order-to-Cash) và P2P (Procure-to-Pay), loại bỏ ốc đảo thông tin (Information Silos).
- **Mô hình Vận tải Tuyến tính (Linear Programming - Transportation Model)**: Thuật toán Northwest Corner, VAM (Vogel's Approximation Method), Stepping-Stone, MODI (Modified Distribution Method), kỹ thuật giải toán cực tiểu hóa chi phí và các biến thể thoái vị (degeneracy), mất cân đối cung cầu.
- **Quản trị Tồn kho Khoa học (Inventory Management)**: Lô đặt hàng kinh tế (EOQ), Lượng sản xuất kinh tế (EPQ), Mô hình chiết khấu theo số lượng (Quantity Discount), Điểm tái đặt hàng (ROP) kèm tồn kho an toàn (Safety Stock).

Nền tảng được xây dựng theo phong cách thiết kế **Balletcore Aesthetic** (gam màu Dusty Rose, Soft Mauve, Warm Linen), tối ưu hóa trải nghiệm đọc học thuật dài hạn, không gây mỏi mắt và loại bỏ hoàn toàn các emoji trang trí không cần thiết.

---

## 2. Kiến Trúc Tính Năng Cốt Lõi (Core Features)

1. **Giáo trình Điện tử 6 Chương Toàn diện (Interactive Textbook)**:
   - Toàn bộ nội dung học liệu 6 tuần chuẩn giáo trình UEH 2020 song ngữ (Việt - Anh).
   - Tích hợp điều hướng 2 đầu trang (`← Chương trước | Danh sách chương | Chương tiếp theo →`).
   - Khối phân tích nghiệp vụ độc quyền **BA Perspective Callouts**.
   - Câu hỏi ôn tập cuối chương với cơ chế Accordion bảo mật đáp án.
   - Kết xuất công thức toán học chuyên sâu offline bằng **KaTeX Engine**.

2. **Ngân Hàng 250 Câu Hỏi Trắc Nghiệm & Hệ Thống Thi Tính Giờ (250 Exam Bank)**:
   - 10 đề thi chuẩn mực (mỗi đề 25 câu hỏi phủ kín 6 chương).
   - Hai chế độ linh hoạt: **Luyện tập (Practice Mode)** và **Thi 30 phút (Timed Exam Mode)**.
   - Cơ chế bảo vệ phiên thi **Exam Session Lock**: Khóa menu điều hướng, cảnh báo popstate/unload, chặn rời phòng thi đột ngột.
   - Tách biệt hộp thoại nộp bài và thoát bài với cơ chế loại trừ nghiêm ngặt (`Modal Exclusivity`).

3. **62 Thẻ Ghi Nhớ Thuật Ngữ & Công Thức (62 Flashcards)**:
   - Thẻ lật 3D tương tác bàn phím (Spacebar để lật, Phím mũi tên để chuyển thẻ).
   - Thuật toán Lặp lại Ngắt quãng (Spaced Repetition) với phân loại thẻ *Đã thuộc* vs *Cần ôn lại*.
   - Bộ lọc đa chiều theo Chương (Chapters) và Phân loại (Concepts, Formulas, Models, BA Perspective).

4. **Từ Điển Thuật Ngữ Chuyên Ngành (Bilingual Glossary)**:
   - Hơn 30+ đại thuật ngữ chuẩn ERP/SCM quốc tế (SAP, Oracle, SCM Master Data).
   - Tìm kiếm thời gian thực song ngữ và tra cứu liên kết chéo.

5. **Bộ Nghiên Cứu 4 Tình Huống Kinh Điển (4 Comprehensive Case Studies)**:
   - **Case 1**: *Texago Corp.* — Định vị nhà máy tối ưu hóa chi phí vận tải đường biển & đường ống.
   - **Case 2**: *Better Products Company* — Cân bằng cung cầu và giải quyết thoái vị trong vận tải.
   - **Case 3**: *Atlantic Coast Tire (ACT)* — Tối ưu hóa tồn kho đa điểm phân phối và chính sách EOQ.
   - **Case 4**: *SOCA Company* — Mô hình EPQ với năng lực sản xuất hữu hạn và chiết khấu thiết lập máy.
   - Bộ tính toán mô phỏng Solver tích hợp trực tiếp trên giao diện web.

6. **Trợ Lý AI Cố Vấn Tri Thức Hợp Nhất (Unified AI Consultant)**:
   - Chế độ Tri thức Offline (**Grounded Mode**) hoạt động 100% không cần Internet hay API Key.
   - Tùy chọn cấu hình Live API (Google Gemini, OpenAI) dành cho thảo luận mở rộng.
   - 8 kịch bản tham vấn định sẵn (Prompt Chips) chuẩn nghiệp vụ BA.

---

## 3. Cấu Trúc Thư Mục Dự Án (Directory Structure)

```text
ERP (SCM)/
├── index.html                     # Entry point chuyển hướng tĩnh
├── netlify.toml                   # Cấu hình xuất bản tự động trên Netlify
├── .gitignore                     # Cấu hình loại trừ bảo mật mã nguồn
├── README.md                      # Tài liệu tổng quan dự án
├── outputs/
│   ├── app/                       # Ứng dụng Web hoàn chỉnh (Standalone Single Page App)
│   │   ├── index.html             # Giao diện chính của ứng dụng
│   │   ├── style.css              # Hệ thống thiết kế Balletcore Design System
│   │   ├── app.js                 # Bộ điều khiển trung tâm (Controller & State Management)
│   │   ├── data.js                # Cơ sở dữ liệu tĩnh song ngữ (Data Bundle)
│   │   ├── assets/                # Hình ảnh minh họa & sơ đồ tình huống
│   │   └── vendor/                # Thư viện offline cục bộ (KaTeX, Marked)
│   ├── content/                   # Nội dung Markdown của 6 chương học
│   │   ├── chapters/              # CHAP_01.md -> CHAP_06.md
│   │   └── cases/                 # CASE_01.md -> CASE_04.md
│   ├── data/                      # Dữ liệu JSON chuẩn hóa (Exams, Flashcards, Glossary)
│   └── documentation/             # Báo cáo kỹ thuật, kiểm thử & nghiệm thu
│       ├── TEST_REPORT.md         # Báo cáo kiểm thử tự động toàn diện (CDP Browser Tests)
│       ├── ENHANCEMENT_REPORT.md  # Báo cáo nâng cấp chất lượng nội dung & UX
│       └── ...
└── scripts/                       # Bộ công cụ kiểm thử tự động (Edge Headless CDP Suite)
    ├── regression_test_phase3b.py # Kiểm thử điều hướng 6 chương & LaTeX
    ├── regression_test_phase3c.py # Kiểm thử Modal & Phân cấp chân trang
    └── test_emojis_phase1.py      # Kiểm thử tuân thủ quy chuẩn Emoji Cleanup
```

---

## 4. Hướng Dẫn Vận Hành (Getting Started)

### Chạy Cục Bộ (Offline Local Mode)
Ứng dụng được thiết kế hoàn toàn tương thích với giao thức `file://` và không yêu cầu cài đặt máy chủ hay kết nối mạng Internet.

1. Tải hoặc clone mã nguồn về thiết bị:
   ```bash
   git clone https://github.com/camtuct242-Hazel/erp-scm-knowledge-hub.git
   ```
2. Mở trực tiếp tệp `outputs/app/index.html` bằng bất kỳ trình duyệt hiện đại nào (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari).

---

## 5. Tác Quyền & Định Chuẩn Học Thuật (Attribution & Framework)

- **Tác giả nền tảng**: **Nguyễn Đăng Cẩm Tú (Hazel)**
- **Giáo trình tham chiếu chính**: Giáo trình *ERP Transportation & Inventory Textbook for Students* (UEH 2020).
- **Khung năng lực tích hợp**: Business Analyst Competency Framework (IIBA BABOK Guide v3).
- **Bản quyền**: Dự án học tập và nghiên cứu phi thương mại.
