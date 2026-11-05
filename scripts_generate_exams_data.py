import json

# Generator for 10 Examinations x 25 Questions = 250 Questions
exams_metadata = [
    {
        "id": "EXAM-01",
        "title_en": "Exam 01: ERP Fundamentals & Supply Chain Management Flows",
        "title_vi": "Đề thi 01: Tổng quan ERP & Quản trị Luồng Chuỗi Cung ứng",
        "chapter_id": "chap-01",
        "duration_minutes": 45,
        "description_en": "Assesses foundational ERP concepts, cross-functional module integration (SD, MM, PP, FICO), and physical vs. information flows in SCM.",
        "description_vi": "Đánh giá kiến thức nền tảng về ERP, sự tích hợp liên phòng ban giữa các phân hệ và luồng thông tin/vật tư trong chuỗi cung ứng."
    },
    {
        "id": "EXAM-02",
        "title_en": "Exam 02: LP Transportation Models & P&T Company Case",
        "title_vi": "Đề thi 02: Mô hình Vận tải Tuyến tính & Case Study Công ty P&T",
        "chapter_id": "chap-01",
        "duration_minutes": 45,
        "description_en": "Assesses LP formulation, requirements assumptions, feasible solutions property, and freight optimization in the P&T canned peas network.",
        "description_vi": "Kiểm tra kỹ năng lập mô hình quy hoạch tuyến tính, giả định cung cầu, tính chất nghiệm khả thi và bài toán tối ưu mạng lưới P&T Co."
    },
    {
        "id": "EXAM-03",
        "title_en": "Exam 03: Unbalanced Transportation & Dummy Node Modeling",
        "title_vi": "Đề thi 03: Bài toán Vận tải Không Cân bằng & Kỹ thuật Điểm Giả định",
        "chapter_id": "chap-02",
        "duration_minutes": 45,
        "description_en": "Focuses on supply-demand imbalances, dummy destinations, dummy sources, and the Metro Water District case study.",
        "description_vi": "Trọng tâm về chênh lệch cung cầu, kỹ thuật điểm đến/nguồn giả định và mô hình phân bổ nguồn nước Metro Water District."
    },
    {
        "id": "EXAM-04",
        "title_en": "Exam 04: Route Restrictions, Prohibited Lanes & Big-M",
        "title_vi": "Đề thi 04: Tuyến đường Cấm, Ràng buộc Kỹ thuật & Phương pháp Số M lớn",
        "chapter_id": "chap-02",
        "duration_minutes": 45,
        "description_en": "Assesses mathematical handling of prohibited shipping lanes, the Big-M method, and the Energetic Company energy system case.",
        "description_vi": "Đánh giá cách xử lý tuyến đường cấm, hệ số phạt M lớn và bài toán phân bổ năng lượng Energetic Company."
    },
    {
        "id": "EXAM-05",
        "title_en": "Exam 05: Demand Bounds, Profit Maximization & Assignment Problems",
        "title_vi": "Đề thi 05: Khoảng Nhu cầu [Min, Max], Tối đa hóa Lợi nhuận & Bài toán Phân công",
        "chapter_id": "chap-03",
        "duration_minutes": 45,
        "description_en": "Evaluates interval demand bounds (Middletown), profit maximization transformations (Nifty Co.), Hungarian algorithm, and Better Products 2.2.",
        "description_vi": "Đánh giá khoảng nhu cầu dao động, chuyển đổi hàm tối đa lợi nhuận, thuật toán Hungarian và bài toán phân công Better Products 2.2."
    },
    {
        "id": "EXAM-06",
        "title_en": "Exam 06: Scientific Inventory Management & 4 Cost Components",
        "title_vi": "Đề thi 06: Quản trị Tồn kho Khoa học & 4 Thành phần Chi phí",
        "chapter_id": "chap-04",
        "duration_minutes": 45,
        "description_en": "Tests understanding of inventory types, capital opportunity costs, holding rates, setup costs, stockout penalties, and service levels.",
        "description_vi": "Kiểm tra kiến thức về các loại tồn kho, chi phí cơ hội vốn, tỷ lệ lưu kho, chi phí đặt hàng, thiệt hại hết hàng và mức dịch vụ."
    },
    {
        "id": "EXAM-07",
        "title_en": "Exam 07: Basic Economic Order Quantity (EOQ) & ACT Baseline",
        "title_vi": "Đề thi 07: Lượng Đặt hàng Kinh tế Cơ bản (EOQ) & Phân tích Cơ sở ACT",
        "chapter_id": "chap-04",
        "duration_minutes": 45,
        "description_en": "Covers Wilson EOQ derivation, holding-setup cost parity, cycle time, ROP calculation, and ACT tire baseline optimization.",
        "description_vi": "Bao quát đạo hàm công thức Wilson, điểm cân bằng chi phí lưu kho - đặt hàng, thời gian chu kỳ, điểm ROP và tối ưu hóa ACT."
    },
    {
        "id": "EXAM-08",
        "title_en": "Exam 08: EOQ with Planned Shortages & Quantity Discounts",
        "title_vi": "Đề thi 08: Mô hình EOQ Thiếu hàng Kế hoạch & Chiết khấu theo Số lượng",
        "chapter_id": "chap-05",
        "duration_minutes": 45,
        "description_en": "Focuses on backorder mechanics, maximum inventory reduction, all-units quantity discount breakpoint analysis, and ACT discount cases.",
        "description_vi": "Trọng tâm về cơ chế đơn hàng nợ (backorders), giảm tồn kho đỉnh, phân tích điểm ngưỡng chiết khấu số lượng và case ACT."
    },
    {
        "id": "EXAM-09",
        "title_en": "Exam 09: Economic Production Quantity (EPQ) & Gradual Replenishment",
        "title_vi": "Đề thi 09: Lượng Sản xuất Kinh tế (EPQ) & Bổ sung Dần (SOCA Case)",
        "chapter_id": "chap-05",
        "duration_minutes": 45,
        "description_en": "Assesses finite production lot sizing, gradual inventory build-up factor (1 - d/p), run durations, and television assembly case SOCA.",
        "description_vi": "Đánh giá quy mô lô sản xuất hữu hạn, hệ số tích lũy bổ sung dần (1 - d/p), thời gian chạy máy và case sản xuất tivi SOCA."
    },
    {
        "id": "EXAM-10",
        "title_en": "Exam 10: Enterprise ERP Integration, Decision Modeling & BA Practice",
        "title_vi": "Đề thi 10: Tích hợp Hệ thống ERP, Mô hình hóa Ra quyết định & Thực hành BA",
        "chapter_id": "chap-06",
        "duration_minutes": 60,
        "description_en": "Capstone examination integrating multi-echelon transportation, inventory policies, ERP architecture (SAP/Oracle), and BA functional requirements.",
        "description_vi": "Đề thi tổng hợp tích hợp mạng lưới vận tải đa tầng, chính sách tồn kho, kiến trúc ERP và yêu cầu nghiệp vụ chuyên sâu của BA."
    }
]

print("Defined 10 exams metadata")
