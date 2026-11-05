# -*- coding: utf-8 -*-
# Exams 1 to 5 (Questions 1 to 125)

def get_exams_1_to_5():
    questions = []

    # ==========================================
    # EXAM 01: ERP Fundamentals & SCM Flows (chap-01)
    # Q001 - Q025: 10 Basic, 10 Intermediate, 5 Advanced
    # ==========================================
    
    # Basic (1-10)
    questions.append({
        "id": "QUES-001",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Core Concept",
        "difficulty": "Basic",
        "question_en": "What is the primary architectural purpose of an Enterprise Resource Planning (ERP) system in modern enterprises?",
        "question_vi": "Mục đích kiến trúc chủ yếu của hệ thống Hoạch định Nguồn lực Doanh nghiệp (ERP) trong các doanh nghiệp hiện đại là gì?",
        "options_en": [
            "To eliminate information silos by integrating business processes across functional departments into a unified database",
            "To exclusively automate the financial bookkeeping of the accounting department",
            "To replace human managers with automated artificial intelligence algorithms",
            "To serve as an isolated spreadsheet tool for individual factory workers"
        ],
        "options_vi": [
            "Xóa bỏ các đảo thông tin bằng cách tích hợp các quy trình nghiệp vụ giữa các phòng ban vào một cơ sở dữ liệu hợp nhất",
            "Chỉ tự động hóa duy nhất công tác ghi chép sổ sách của phòng kế toán",
            "Thay thế hoàn toàn các nhà quản lý bằng các thuật toán trí tuệ nhân tạo tự động",
            "Đóng vai trò như một công cụ bảng tính độc lập cho từng công nhân nhà máy"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP systems unify disparate business processes (sales, procurement, production, inventory, finance) around a centralized data model, eliminating departmental silos.",
        "explanation_vi": "Hệ thống ERP hợp nhất các quy trình nghiệp vụ phân tán (bán hàng, mua hàng, sản xuất, kho vận, tài chính) trên một mô hình dữ liệu tập trung, xóa bỏ hoàn toàn tình trạng cát cứ dữ liệu."
    })

    questions.append({
        "id": "QUES-002",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "SCM Definition",
        "difficulty": "Basic",
        "question_en": "According to Jacobs & Chase (2013), how is Supply Chain Management formally defined?",
        "question_vi": "Theo Jacobs & Chase (2013), Quản trị Chuỗi Cung ứng (SCM) được định nghĩa chính thức như thế nào?",
        "options_en": [
            "Processes that move information and material to and from the manufacturing and service processes of the firm",
            "The physical maintenance of highway vehicles and delivery trucks",
            "The management of corporate human resource payrolls",
            "The advertising design of consumer marketing campaigns"
        ],
        "options_vi": [
            "Các quy trình luân chuyển thông tin và nguyên vật liệu đến và đi từ các quy trình sản xuất và dịch vụ của doanh nghiệp",
            "Công tác bảo trì phương tiện cơ giới đường bộ và xe tải giao hàng",
            "Quy trình quản lý bảng lương nhân sự của tập đoàn",
            "Thiết kế quảng cáo cho các chiến dịch tiếp thị người tiêu dùng"
        ],
        "correct_answer": 0,
        "explanation_en": "Jacobs & Chase (2013) define supply chain as the processes that move information and material to and from the manufacturing and service operations.",
        "explanation_vi": "Jacobs & Chase (2013) định nghĩa chuỗi cung ứng là tập hợp các quy trình luân chuyển cả thông tin và vật chất hai chiều giữa nhà sản xuất, dịch vụ và khách hàng."
    })

    questions.append({
        "id": "QUES-003",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Core ERP Modules",
        "difficulty": "Basic",
        "question_en": "Which of the following is NOT one of the core ERP functional modules identified in the textbook?",
        "question_vi": "Phân hệ nào sau đây KHÔNG phải là một trong những module chức năng ERP cốt lõi được nêu trong giáo trình?",
        "options_en": [
            "Cryptocurrency Speculation Management",
            "Purchasing & Procurement",
            "Production Planning",
            "Sales and Distribution"
        ],
        "options_vi": [
            "Quản lý Đầu cơ Tiền mã hóa",
            "Mua hàng & Cung ứng",
            "Kế hoạch Sản xuất",
            "Bán hàng & Phân phối"
        ],
        "correct_answer": 0,
        "explanation_en": "Standard ERP systems cover Purchasing, Production Planning, Sales-Distribution, Inventory Management, Warehousing, HRM, and Finance.",
        "explanation_vi": "Các phân hệ ERP chuẩn mực gồm Mua hàng, Kế hoạch Sản xuất, Bán hàng & Phân phối, Quản trị Tồn kho, Kho bãi, Nhân sự và Tài chính."
    })

    questions.append({
        "id": "QUES-004",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Material Flow",
        "difficulty": "Basic",
        "question_en": "In a supply chain network, the physical flow of goods moves primarily in which direction?",
        "question_vi": "Trong mạng lưới chuỗi cung ứng, luồng vật chất hàng hóa vật lý chủ yếu dịch chuyển theo hướng nào?",
        "options_en": [
            "Downstream from suppliers through manufacturing and distribution to end customers",
            "Upstream from end customers back to raw material extractors",
            "Exclusively in a horizontal loop between competing retail stores",
            "It does not move physically and exists only as financial credit"
        ],
        "options_vi": [
            "Xuôi dòng (Downstream) từ nhà cung cấp qua nhà máy sản xuất và trung tâm phân phối đến khách hàng cuối",
            "Ngược dòng (Upstream) từ người tiêu dùng cuối quay về điểm khai thác nguyên liệu thô",
            "Chỉ chạy theo vòng tròn ngang giữa các cửa hàng bán lẻ cạnh tranh nhau",
            "Không chuyển dịch vật lý mà chỉ tồn tại dưới dạng ghi nợ tín dụng tài chính"
        ],
        "correct_answer": 0,
        "explanation_en": "Physical materials flow downstream (suppliers -> manufacturers -> distributors -> customers), while funds flow upstream, and information flows bidirectionally.",
        "explanation_vi": "Vật tư hữu hình dịch chuyển xuôi dòng từ thượng nguồn xuống hạ nguồn, trong khi dòng tiền chảy ngược lên và dòng thông tin luân chuyển hai chiều."
    })

    questions.append({
        "id": "QUES-005",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Information Flow",
        "difficulty": "Basic",
        "question_en": "What is the primary role of information flow in an integrated SCM system?",
        "question_vi": "Vai trò chính của luồng thông tin trong hệ thống SCM tích hợp là gì?",
        "options_en": [
            "To transmit customer demand signals, order status, and inventory visibility across all echelons",
            "To delay product deliveries to inflate warehousing rental income",
            "To conceal production capacity bottlenecks from executive leaders",
            "To isolate individual supply chain partners from market feedback"
        ],
        "options_vi": [
            "Truyền tải tín hiệu nhu cầu thị trường, trạng thái đơn hàng và mức tồn kho minh bạch trên mọi tầng chuỗi",
            "Làm chậm tiến độ giao hàng để tăng tiền thuê kho bãi",
            "Che giấu các điểm nghẽn công suất sản xuất khỏi ban giám đốc",
            "Cô lập các đối tác trong chuỗi cung ứng khỏi phản hồi thị trường"
        ],
        "correct_answer": 0,
        "explanation_en": "Information flows provide end-to-end visibility of orders, schedules, and inventory, mitigating distortions like the bullwhip effect.",
        "explanation_vi": "Luồng thông tin giúp minh bạch hóa tiến độ đơn hàng và lượng tồn kho thực tế, giảm thiểu hiện tượng méo mó thông tin (hiệu ứng Bullwhip)."
    })

    questions.append({
        "id": "QUES-006",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Master Data",
        "difficulty": "Basic",
        "question_en": "What is 'Master Data' in the context of an enterprise ERP system?",
        "question_vi": "'Dữ liệu chủ' (Master Data) trong ngữ cảnh hệ thống ERP doanh nghiệp là gì?",
        "options_en": [
            "Core, persistent business entities such as Material Master, Vendor Master, and Customer Master",
            "Temporary cache files deleted at the end of each work shift",
            "Marketing email templates sent to prospective newsletter subscribers",
            "Personal social media credentials of executive board members"
        ],
        "options_vi": [
            "Các thực thể dữ liệu nghiệp vụ cốt lõi, lâu bền như Hồ sơ Vật tư, Hồ sơ Nhà cung cấp và Hồ sơ Khách hàng",
            "Các tệp bộ nhớ tạm thời bị xóa bỏ sau mỗi ca làm việc",
            "Các mẫu email tiếp thị gửi cho người đăng ký nhận bản tin",
            "Tài khoản mạng xã hội cá nhân của các thành viên ban giám đốc"
        ],
        "correct_answer": 0,
        "explanation_en": "Master data forms the stable foundational records referenced in daily transactions across multiple ERP modules.",
        "explanation_vi": "Dữ liệu chủ là tập hợp các bản ghi định danh cốt lõi và ổn định, được tham chiếu liên tục trong mọi giao dịch hàng ngày của các phân hệ ERP."
    })

    questions.append({
        "id": "QUES-007",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Implementation",
        "difficulty": "Basic",
        "question_en": "Why do traditional functional departments struggle without an integrated ERP system?",
        "question_vi": "Vì sao các phòng ban chức năng truyền thống gặp nhiều trở ngại nếu không có hệ thống ERP tích hợp?",
        "options_en": [
            "Each department maintains disparate data spreadsheets, causing synchronization delays and conflicting reports",
            "All functional departments use the exact same automated software program",
            "Employees are legally prohibited from speaking across different departments",
            "Raw material suppliers refuse to accept digital currency"
        ],
        "options_vi": [
            "Mỗi phòng ban sử dụng các file dữ liệu rời rạc, gây chậm trễ đồng bộ và tạo ra các báo cáo mâu thuẫn số liệu",
            "Tất cả các bộ phận đều dùng chung một phần mềm tự động hoàn toàn giống nhau",
            "Nhân viên bị pháp luật cấm giao tiếp giữa các phòng ban khác nhau",
            "Các nhà cung cấp nguyên liệu từ chối nhận thanh toán kỹ thuật số"
        ],
        "correct_answer": 0,
        "explanation_en": "Fragmented point solutions create data silos, mismatched metrics, redundant entry, and operational friction.",
        "explanation_vi": "Sử dụng các phần mềm rời rạc dẫn đến đảo dữ liệu, số liệu chênh lệch, nhập liệu trùng lặp và gây xung đột trong điều hành."
    })

    questions.append({
        "id": "QUES-008",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Procurement in ERP",
        "difficulty": "Basic",
        "question_en": "What business document initiates the external procurement process in an ERP purchasing module?",
        "question_vi": "Chứng từ nghiệp vụ nào khởi động quy trình mua hàng đối ngoại trong phân hệ mua sắm của ERP?",
        "options_en": [
            "Purchase Requisition (PR) approved into a Purchase Order (PO)",
            "Bill of Lading signed by the customer delivery recipient",
            "End-of-year tax clearance certificate",
            "Corporate annual shareholder dividend announcement"
        ],
        "options_vi": [
            "Yêu cầu Mua hàng (Purchase Requisition - PR) được phê duyệt thành Đơn Đặt Hàng Mua (Purchase Order - PO)",
            "Vận đơn đường biển có chữ ký của người nhận hàng cuối cùng",
            "Biên bản quyết toán thuế thu nhập doanh nghiệp cuối năm",
            "Thông báo chia cổ tức thường niên cho các cổ đông"
        ],
        "correct_answer": 0,
        "explanation_en": "An internal department creates a Purchase Requisition, which is approved and converted by purchasing into an official Purchase Order sent to the supplier.",
        "explanation_vi": "Quy trình mua hàng bắt đầu từ Yêu cầu mua hàng nội bộ (PR), sau đó được phê duyệt và chuyển đổi thành Đơn đặt mua (PO) gửi cho nhà cung cấp."
    })

    questions.append({
        "id": "QUES-009",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Sales & Distribution",
        "difficulty": "Basic",
        "question_en": "What is an ATP (Available-to-Promise) check in an ERP Sales and Distribution (SD) module?",
        "question_vi": "Kiểm tra ATP (Available-to-Promise) trong phân hệ Bán hàng & Phân phối (SD) của ERP là gì?",
        "options_en": [
            "An automated verification that uncommitted stock or scheduled production is available to fulfill a customer delivery date",
            "A background check on the personal credit history of the delivery truck driver",
            "A manual inspection of factory smoke emissions",
            "A legal warranty guaranteeing that raw materials will never spoil"
        ],
        "options_vi": [
            "Quy trình tự động kiểm tra lượng tồn kho chưa cam kết hoặc tiến độ sản xuất khả dụng để xác nhận ngày giao hàng cho khách",
            "Kiểm tra lý lịch tư pháp cá nhân của tài xế lái xe tải giao hàng",
            "Kiểm tra thủ công nồng độ khí thải tại các ống khói nhà máy",
            "Một cam kết pháp lý bảo đảm rằng nguyên vật liệu sẽ không bao giờ hư hỏng"
        ],
        "correct_answer": 0,
        "explanation_en": "ATP dynamically queries current inventory and planned incoming replenishment to commit realistic delivery dates to customers.",
        "explanation_vi": "ATP đối soát lượng tồn kho thực tế và kế hoạch nhập hàng trong tương lai để cam kết ngày giao hàng khả thi cho đơn đặt hàng bán."
    })

    questions.append({
        "id": "QUES-010",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Finance Integration",
        "difficulty": "Basic",
        "question_en": "When goods are physically received into the warehouse (Goods Receipt), how does ERP ensure financial integration?",
        "question_vi": "Khi hàng hóa được thực nhận vào kho (Goods Receipt), hệ thống ERP đảm bảo tính tích hợp tài chính như thế nào?",
        "options_en": [
            "It automatically posts an inventory asset debit and an unbilled GR/IR liability credit in the general ledger",
            "It deletes all prior accounting records to conserve hard drive space",
            "It requires the warehouse clerk to manually visit the bank with cash",
            "It delays all journal entries until the end of the fiscal quarter"
        ],
        "options_vi": [
            "Hệ thống tự động ghi Nợ tài khoản Tồn kho và ghi Có tài khoản Phải trả trung gian (GR/IR) trên sổ cái kế toán",
            "Hệ thống tự động xóa toàn bộ sổ sách kế toán cũ để tiết kiệm dung lượng ổ cứng",
            "Yêu cầu thủ kho phải trực tiếp mang tiền mặt ra ngân hàng nộp",
            "Hoãn lại toàn bộ các bút toán định khoản cho đến cuối quý tài chính"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP creates instantaneous journal entries upon Goods Receipt, debiting Inventory and crediting the Goods Receipt/Invoice Receipt (GR/IR) clearing account.",
        "explanation_vi": "Giao dịch Nhập kho (Goods Receipt) kích hoạt tự động bút toán kế toán: Tăng tài sản tồn kho và ghi nhận công nợ tạm tính với nhà cung cấp (GR/IR)."
    })

    # Intermediate (11-20)
    questions.append({
        "id": "QUES-011",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "MRP Logic",
        "difficulty": "Intermediate",
        "question_en": "How does Material Requirements Planning (MRP) in ERP utilize the Bill of Materials (BOM)?",
        "question_vi": "Quy trình Hoạch định Nhu cầu Nguyên vật liệu (MRP) trong ERP sử dụng Định mức Vật tư (BOM) như thế nào?",
        "options_en": [
            "It explodes finished goods production schedules into net requirements for subassemblies and raw materials based on lead times",
            "It prints paper product catalogs for retail marketing displays",
            "It calculates the severance pay for retired factory employees",
            "It randomly shuffles warehouse storage bin assignments each evening"
        ],
        "options_vi": [
            "Bóc tách kế hoạch sản xuất thành phẩm thành nhu cầu tịnh cho từng cụm chi tiết và nguyên liệu thô dựa trên thời gian giao hàng",
            "In các cuốn catalogue giới thiệu sản phẩm bằng giấy để trưng bày tại các đại lý bán lẻ",
            "Tính toán tiền trợ cấp thôi việc cho các công nhân nhà máy về hưu",
            "Xáo trộn ngẫu nhiên vị trí các kệ để hàng trong kho vào mỗi buổi tối"
        ],
        "correct_answer": 0,
        "explanation_en": "MRP uses the BOM hierarchy to explode dependent demand, matching gross requirements against current stock and open orders to generate planned procurement proposals.",
        "explanation_vi": "MRP phân rã cây định mức vật tư BOM để tính toán nhu cầu phụ thuộc, cân đối giữa tồn kho khả dụng và đơn hàng mở để tạo đề xuất mua sắm/sản xuất."
    })

    questions.append({
        "id": "QUES-012",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Cross-Functional Flow",
        "difficulty": "Intermediate",
        "question_en": "What is the standard document lifecycle in an ERP Order-to-Cash (O2C) business process?",
        "question_vi": "Vòng đời chứng từ chuẩn mực trong quy trình nghiệp vụ Order-to-Cash (O2C) của ERP là gì?",
        "options_en": [
            "Sales Inquiry -> Sales Quotation -> Sales Order -> Outbound Delivery -> Goods Issue -> Billing/Invoice -> Cash Receipt",
            "Cash Receipt -> Goods Issue -> Sales Order -> Purchase Requisition",
            "Vendor Invoice -> Bill of Lading -> Production Order -> Scrap Report",
            "Sales Order -> Tax Audit -> Employee Review -> Depreciation Ledger"
        ],
        "options_vi": [
            "Hỏi giá -> Báo giá bán -> Đơn đặt hàng bán -> Lệnh xuất kho -> Xuất hàng -> Hóa đơn bán hàng -> Thu tiền khách hàng",
            "Thu tiền mặt -> Xuất hàng -> Đơn bán hàng -> Yêu cầu mua hàng",
            "Hóa đơn nhà cung cấp -> Vận đơn -> Lệnh sản xuất -> Biên bản thanh lý phế liệu",
            "Đơn bán hàng -> Kiểm tra thuế -> Đánh giá nhân sự -> Khấu hao tài sản"
        ],
        "correct_answer": 0,
        "explanation_en": "The O2C cycle traces the customer journey from quotation and order confirmation to picking, shipping, invoicing, and accounts receivable settlement.",
        "explanation_vi": "Quy trình O2C theo dõi trọn vẹn hành trình từ báo giá, tạo đơn, đóng gói, xuất kho, xuất hóa đơn tài chính cho đến khi tiền về tài khoản doanh nghiệp."
    })

    questions.append({
        "id": "QUES-013",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Procure-to-Pay Flow",
        "difficulty": "Intermediate",
        "question_en": "What is the significance of the 'Three-Way Match' in ERP Procure-to-Pay (P2P) systems?",
        "question_vi": "Ý nghĩa của cơ chế 'Khớp 3 Chiều' (Three-Way Match) trong phân hệ Procure-to-Pay (P2P) của ERP là gì?",
        "options_en": [
            "It verifies that quantities, items, and unit prices match across the Purchase Order, Goods Receipt note, and Vendor Invoice before payment",
            "It requires three separate signatures from government tax inspectors",
            "It validates that three different shipping trucks delivered the merchandise",
            "It matches the warehouse temperature, humidity, and barometric pressure"
        ],
        "options_vi": [
            "Đối soát để đảm bảo số lượng, mặt hàng và đơn giá khớp hoàn toàn giữa Đơn Đặt Hàng (PO), Phiếu Nhập Kho (GR) và Hóa Đơn Nhà Cung Cấp (Vendor Invoice) trước khi thanh toán",
            "Yêu cầu phải có đủ ba chữ ký riêng biệt từ các thanh tra cơ quan thuế",
            "Xác nhận rằng có đúng ba xe tải khác nhau cùng tham gia chở lô hàng đến",
            "Kiểm tra sự ăn khớp giữa nhiệt độ, độ ẩm và áp suất không khí tại nhà kho"
        ],
        "correct_answer": 0,
        "explanation_en": "The three-way match prevents fraudulent or erroneous disbursements by mathematically verifying PO terms, physical goods received, and vendor invoice billings.",
        "explanation_vi": "Khớp 3 chiều ngăn ngừa rủi ro thất thoát bằng cách tự động so sánh chi tiết trên Đơn mua hàng (PO), Thực tế nhập kho (GR) và Hóa đơn đòi tiền (Invoice)."
    })

    questions.append({
        "id": "QUES-014",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Bullwhip Effect",
        "difficulty": "Intermediate",
        "question_en": "How does ERP implementation help mitigate the Bullwhip Effect in multi-tier supply chains?",
        "question_vi": "Việc triển khai ERP giúp giảm thiểu Hiệu ứng Bullwhip (Chiếc roi da) trong chuỗi cung ứng đa tầng như thế nào?",
        "options_en": [
            "By sharing real-time point-of-sale customer demand directly with upstream tiers, reducing order forecasting distortions",
            "By mandating that suppliers maintain infinite physical warehouse capacity",
            "By prohibiting customers from modifying their seasonal purchasing habits",
            "By increasing shipping lead times to several months"
        ],
        "options_vi": [
            "Bằng cách chia sẻ dữ liệu nhu cầu bán lẻ thời gian thực cho các mắt xích thượng nguồn, loại bỏ sự khuếch đại dự báo sai lệch",
            "Bằng cách bắt buộc các nhà cung cấp phải duy trì diện tích kho bãi vô hạn",
            "Bằng cách cấm người tiêu dùng thay đổi thói quen mua sắm theo mùa",
            "Bằng cách kéo dài thời gian giao hàng lên nhiều tháng"
        ],
        "correct_answer": 0,
        "explanation_en": "The bullwhip effect is caused by demand distortion amplifying upstream. ERP visibility gives suppliers real-time end-consumer consumption data, dampening safety-stock padding.",
        "explanation_vi": "Hiệu ứng Bullwhip sinh ra do phóng đại nhu cầu khi truyền ngược chuỗi. ERP cung cấp dữ liệu bán hàng thực tế giúp các nhà sản xuất không phải dự trữ đệm quá đà."
    })

    questions.append({
        "id": "QUES-015",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "SCM Reverse Logistics",
        "difficulty": "Intermediate",
        "question_en": "What business processes are included under 'Reverse Logistics' within enterprise SCM?",
        "question_vi": "Quy trình nghiệp vụ nào sau đây thuộc phạm trù 'Logistics Thu hồi' (Reverse Logistics) trong SCM doanh nghiệp?",
        "options_en": [
            "Customer product returns, warranty repairs, defective recalls, and end-of-life recycling",
            "Outbound finished goods delivery to regional retail outlets",
            "Raw material extraction from underground domestic oil fields",
            "Direct foreign investment in international securities"
        ],
        "options_vi": [
            "Xử lý hàng khách trả lại, bảo hành sửa chữa, thu hồi sản phẩm lỗi và tái chế linh kiện hết hạn sử dụng",
            "Giao hàng thành phẩm xuất xưởng tới các đại lý bán lẻ khu vực",
            "Khai thác dầu thô nguyên liệu từ các giếng dầu nội địa dưới lòng đất",
            "Đầu tư trực tiếp ra nước ngoài vào các thị trường chứng khoán quốc tế"
        ],
        "correct_answer": 0,
        "explanation_en": "Reverse logistics coordinates the upstream return of physical goods from customers back to the producer for credit, repair, remanufacture, or disposal.",
        "explanation_vi": "Logistics thu hồi điều phối dòng hàng chảy ngược từ khách hàng về phía doanh nghiệp để đổi trả, sửa chữa, tái chế hoặc tiêu hủy theo quy định."
    })

    questions.append({
        "id": "QUES-016",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Customization vs Configuration",
        "difficulty": "Intermediate",
        "question_en": "From a Business Analyst standpoint, what is the critical difference between ERP 'Configuration' and 'Customization'?",
        "question_vi": "Dưới góc nhìn của một Business Analyst, sự khác biệt then chốt giữa 'Cấu hình' (Configuration) và 'Tùy biến' (Customization) ERP là gì?",
        "options_en": [
            "Configuration sets pre-built system switches and tables without code changes, whereas Customization requires writing custom source code",
            "Configuration requires rewriting the underlying database engine from scratch",
            "Customization is always completely free and supported by standard software patches",
            "There is no difference; both terms refer to purchasing new office computer hardware"
        ],
        "options_vi": [
            "Cấu hình là thiết lập các tham số, bảng tùy chọn có sẵn mà không can thiệp mã nguồn; Tùy biến là lập trình thêm mã nguồn mới để mở rộng chức năng",
            "Cấu hình đòi hỏi phải lập trình lại toàn bộ hệ quản trị cơ sở dữ liệu từ đầu",
            "Tùy biến luôn hoàn toàn miễn phí và được các bản vá lỗi chính hãng hỗ trợ sẵn",
            "Không có sự khác biệt; cả hai thuật ngữ đều chỉ việc mua sắm phần cứng máy tính văn phòng mới"
        ],
        "correct_answer": 0,
        "explanation_en": "Configuration leverages standard vendor options (tables, rules), while customization involves writing custom software code, increasing implementation cost and upgrade risks.",
        "explanation_vi": "Cấu hình sử dụng các tùy chọn chuẩn của phần mềm, trong khi tùy biến đòi hỏi viết thêm code riêng, làm tăng chi phí và rủi ro khi nâng cấp phiên bản."
    })

    questions.append({
        "id": "QUES-017",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Warehouse Management System (WMS)",
        "difficulty": "Intermediate",
        "question_en": "How does an Extended Warehouse Management (EWM/WMS) module differ from basic Inventory Management (IM) in an ERP suite?",
        "question_vi": "Phân hệ Quản trị Kho mở rộng (EWM/WMS) khác biệt thế nào với phân hệ Quản lý Tồn kho cơ bản (IM) trong bộ giải pháp ERP?",
        "options_en": [
            "IM tracks quantity and valuation at the storage location level, whereas WMS manages exact bin-level coordinates, putaway strategies, and wave picking tasks",
            "IM manages physical forklifts while WMS only handles employee payroll",
            "WMS is used only for outdoor parking lots, while IM is used for indoor offices",
            "IM calculates corporate tax while WMS prints shipping box carton labels"
        ],
        "options_vi": [
            "IM quản lý số lượng và giá trị tồn kho ở cấp vị trí lưu trữ (Storage Location); WMS quản lý chi tiết đến từng tọa độ ô kệ (Bin-level), chiến lược xếp hàng và chia lệnh lấy hàng (Wave picking)",
            "IM quản lý xe nâng hàng trong khi WMS chỉ tính lương cho nhân viên kho",
            "WMS chỉ dùng cho bãi đỗ xe ngoài trời, còn IM chỉ dùng trong phòng làm việc",
            "IM tính thuế thu nhập doanh nghiệp trong khi WMS chỉ in tem nhãn thùng hàng"
        ],
        "correct_answer": 0,
        "explanation_en": "Basic Inventory Management (IM) monitors book inventory balances and monetary values, while WMS/EWM directs physical micro-movements, bin locations, and worker labor execution.",
        "explanation_vi": "Quản lý tồn kho IM chỉ theo dõi số dư trên sổ sách và giá trị tiền tệ, còn WMS/EWM trực tiếp điều phối từng lệnh bốc xếp, chỉ định tọa độ ô kệ cụ thể trong kho."
    })

    questions.append({
        "id": "QUES-018",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Integration Architecture",
        "difficulty": "Intermediate",
        "question_en": "What role does an Enterprise Service Bus (ESB) or API Gateway play in connecting ERP to external logistics providers?",
        "question_vi": "Hạ tầng trục tích hợp (ESB) hoặc cổng kết nối API đóng vai trò gì khi kết nối ERP với các đối tác logistics bên ngoài?",
        "options_en": [
            "It facilitates standardized message translation (EDI, JSON, XML) and protocol routing between internal ERP tables and carrier tracking systems",
            "It physically propels freight containers through high-speed pneumatic tubes",
            "It functions as an emergency backup generator during factory electrical blackouts",
            "It prevents warehouse workers from accessing the internet on company computers"
        ],
        "options_vi": [
            "Chuẩn hóa và chuyển đổi thông điệp dữ liệu (EDI, JSON, XML), điều phối kết nối giữa cơ sở dữ liệu ERP với hệ thống theo dõi của các hãng vận tải",
            "Đẩy các container hàng hóa chạy qua các đường ống khí nén tốc độ cao",
            "Đóng vai trò máy phát điện khẩn cấp khi nhà máy xảy ra sự cố mất điện",
            "Ngăn chặn nhân viên kho truy cập mạng internet trên máy tính công ty"
        ],
        "correct_answer": 0,
        "explanation_en": "Integration middleware translates transactional payloads (e.g., EDI 214 shipment status, EDI 850 POs) between the core ERP system and disparate third-party logistics platforms.",
        "explanation_vi": "Trục tích hợp đóng vai trò thông dịch viên dữ liệu chuẩn (EDI, API), giúp hệ thống ERP trao đổi trạng thái đơn hàng và định vị vận chuyển với hệ thống của hãng vận tải."
    })

    questions.append({
        "id": "QUES-019",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Change Management",
        "difficulty": "Intermediate",
        "question_en": "Why is Organizational Change Management (OCM) considered vital for ERP project success?",
        "question_vi": "Vì sao Quản trị Sự thay đổi Tổ chức (OCM) được xem là yếu tố sống còn cho sự thành công của một dự án ERP?",
        "options_en": [
            "ERP imposes standardized cross-functional workflows that disrupt legacy departmental habits, requiring user training and stakeholder buy-in",
            "OCM automatically generates database table schemas without human intervention",
            "It is a legal formality required only for publicly traded multinational banks",
            "It ensures that legacy paper spreadsheets are framed and hung on office walls"
        ],
        "options_vi": [
            "ERP áp đặt các quy trình chuẩn hóa liên phòng ban làm thay đổi thói quen làm việc cũ, đòi hỏi phải đào tạo và tạo sự đồng thuận từ người dùng",
            "OCM giúp tự động tạo lập lược đồ bảng cơ sở dữ liệu mà không cần con người can thiệp",
            "Đó chỉ là một thủ tục hình thức bắt buộc đối với các ngân hàng đa quốc gia",
            "Nó đảm bảo các sổ sách bảng tính giấy cũ được đóng khung treo lên tường văn phòng"
        ],
        "correct_answer": 0,
        "explanation_en": "Technical functionality fails if employees resist new cross-departmental business processes; OCM addresses training, cultural alignment, and user adoption.",
        "explanation_vi": "Một hệ thống kỹ thuật tốt sẽ thất bại nếu nhân sự kháng cự quy trình mới; OCM tập trung đào tạo, chuyển đổi nhận thức và xây dựng văn hóa làm việc theo chuẩn mới."
    })

    questions.append({
        "id": "QUES-020",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Audit Trail",
        "difficulty": "Intermediate",
        "question_en": "What is an 'Audit Trail' in an ERP transactional environment?",
        "question_vi": "'Vết kiểm toán' (Audit Trail / Dấu vết ghi nhận) trong môi trường giao dịch ERP là gì?",
        "options_en": [
            "An immutable chronological record showing who created, altered, or approved a business transaction, with timestamps and previous values",
            "A physical footpath worn by security guards patrolling the warehouse perimeter",
            "A list of external delivery truck license plates parked at loading bays",
            "A temporary browser cache history cleared upon logging off"
        ],
        "options_vi": [
            "Bản ghi nhật ký bất biến theo trình tự thời gian cho biết ai đã tạo, chỉnh sửa hoặc phê duyệt một giao dịch, kèm dấu mốc thời gian và giá trị cũ",
            "Lối đi tuần tra của nhân viên an ninh xung quanh khuôn viên nhà kho",
            "Danh sách biển số xe tải đang dừng đỗ tại các cửa bốc dỡ hàng",
            "Lịch sử bộ nhớ tạm của trình duyệt web bị xóa sạch ngay khi đăng xuất"
        ],
        "correct_answer": 0,
        "explanation_en": "Audit trails provide accountability and compliance (e.g., SOX) by logging user IDs, timestamps, document numbers, and precise field modifications.",
        "explanation_vi": "Vết kiểm toán ghi lại chính xác danh tính người thực hiện, thời điểm và nội dung thay đổi trên từng chứng từ, phục vụ kiểm soát nội bộ và tuân thủ pháp lý."
    })

    # Advanced (21-25)
    questions.append({
        "id": "QUES-021",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "BA Requirements Elicitation",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is eliciting requirements for an ERP inventory replenishment module. Which requirement represents a true 'Functional Requirement' rather than a business rule or non-functional constraint?",
        "question_vi": "Một Business Analyst đang khơi gợi yêu cầu cho phân hệ bổ sung hàng tồn kho trong ERP. Yêu cầu nào sau đây đại diện cho một 'Yêu cầu Chức năng' (Functional Requirement) thực thụ?",
        "options_en": [
            "The system shall automatically generate a Purchase Requisition when the available stock level falls to or below the calculated Reorder Point (ROP)",
            "Inventory holding cost shall be budgeted at 21% of average inventory valuation per fiscal year",
            "The database shall support a 99.99% uptime availability across all operational calendar days",
            "Suppliers with more than 3 late deliveries shall have their vendor rating downgraded by purchasing managers"
        ],
        "options_vi": [
            "Hệ thống phải tự động tạo Yêu cầu Mua hàng (PR) khi tồn kho khả dụng giảm xuống bằng hoặc dưới Điểm đặt hàng lại (ROP) đã tính toán",
            "Chi phí lưu kho phải được lập ngân sách bằng 21% giá trị tồn kho bình quân hàng năm",
            "Cơ sở dữ liệu phải đáp ứng thời gian hoạt động liên tục (uptime) đạt 99.99% trong năm",
            "Nhà cung cấp giao trễ hạn quá 3 lần sẽ bị trưởng phòng mua hàng hạ bậc xếp hạng"
        ],
        "correct_answer": 0,
        "explanation_en": "A functional requirement specifies a discrete behavior or software action ('The system shall generate a PR when stock <= ROP'). The others are a business parameter, an NFR, and a business policy.",
        "explanation_vi": "Yêu cầu chức năng định rõ hành động cụ thể mà phần mềm phải thực thi (tự động sinh PR khi tồn kho chạm ROP). Các lựa chọn còn lại là thông số, NFR và quy chế quản lý."
    })

    questions.append({
        "id": "QUES-022",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "SCM Network Optimization Trade-offs",
        "difficulty": "Advanced",
        "question_en": "In enterprise supply chain network design, what fundamental trade-off occurs when a company increases its number of regional distribution centers (DCs)?",
        "question_vi": "Trong thiết kế mạng lưới chuỗi cung ứng, sự đánh đổi (trade-off) căn bản nào xảy ra khi doanh nghiệp tăng thêm số lượng trung tâm phân phối (DC) khu vực?",
        "options_en": [
            "Outbound freight costs to local customers decrease and delivery speed increases, but aggregate safety stock holding costs and facility overhead increase",
            "Both total inventory holding costs and total transportation costs decrease to zero",
            "Total facility costs decrease while customer transit times increase dramatically",
            "Inbound transportation costs from factories decrease while customer dissatisfaction increases"
        ],
        "options_vi": [
            "Chi phí vận chuyển chặng cuối tới khách hàng giảm và tốc độ giao hàng nhanh hơn, nhưng tổng chi phí tồn kho an toàn và phí vận hành kho bãi lại tăng cao",
            "Cả chi phí lưu kho và chi phí vận chuyển đều cùng lúc giảm xuống bằng 0",
            "Tổng chi phí kho bãi giảm đi trong khi thời gian giao hàng tới khách lại tăng vọt",
            "Cước vận chuyển đầu vào từ nhà máy giảm đi nhưng sự không hài lòng của khách hàng tăng lên"
        ],
        "correct_answer": 0,
        "explanation_en": "More distribution centers position stock closer to demand (cutting last-mile freight and lead time), but decentralizing inventory eliminates risk pooling, inflating total safety stock holding costs.",
        "explanation_vi": "Tăng số lượng kho giúp rút ngắn quãng đường giao hàng chặng cuối, nhưng phân tán hàng hóa làm mất hiệu ứng gom rủi ro (risk pooling), khiến tổng tồn kho an toàn tăng vọt."
    })

    questions.append({
        "id": "QUES-023",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Post-Implementation Audit",
        "difficulty": "Advanced",
        "question_en": "Six months after go-live, an ERP audit reveals warehouse stockouts despite the ERP system reporting adequate inventory. Which root cause should a Senior BA investigate first?",
        "question_vi": "Sáu tháng sau khi vận hành chính thức (Go-live), kiểm toán phát hiện kho bị hết hàng dù hệ thống ERP báo vẫn còn tồn kho. Là một Senior BA, bạn nên điều tra nguyên nhân gốc rễ nào trước tiên?",
        "options_en": [
            "Discrepancies between physical stock and book inventory caused by unrecorded scrap, physical shrinkage, or delayed goods issue transaction postings",
            "The mathematical failure of Wilson's square root calculus inside the CPU",
            "A deliberate conspiracy by external competitor marketing agencies",
            "An excess of physical sunlight entering warehouse loading docks"
        ],
        "options_vi": [
            "Sự sai lệch giữa tồn kho thực tế và tồn sổ sách do phế phẩm không được ghi nhận, thất thoát hoặc chậm trễ nhập liệu các giao dịch xuất kho",
            "Thuật toán đạo hàm căn bậc hai của Wilson trong chip xử lý CPU bị tính toán sai",
            "Âm mưu phá hoại có chủ đích từ phòng tiếp thị của công ty đối thủ",
            "Lượng ánh sáng mặt trời chiếu vào cửa bốc dỡ hàng trong kho quá nhiều"
        ],
        "correct_answer": 0,
        "explanation_en": "Inventory record inaccuracies stem from operational discipline failures: delayed transaction logging, unrecorded damage, or physical theft, creating 'phantom inventory' in the ERP system.",
        "explanation_vi": "Tồn kho 'ma' trên hệ thống ERP xuất phát từ lỗi kỷ luật vận hành: nhân viên xuất hàng nhưng quên ghi nhận, hàng hỏng không báo phế hoặc hao hụt thực tế."
    })

    questions.append({
        "id": "QUES-024",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "Total Cost of Ownership (TCO)",
        "difficulty": "Advanced",
        "question_en": "When calculating the Total Cost of Ownership (TCO) for a tier-1 ERP replacement, which hidden cost category is frequently underestimated by business sponsors?",
        "question_vi": "Khi tính toán Tổng Chi phí Sở hữu (TCO) cho dự án thay thế hệ thống ERP, hạng mục chi phí ẩn nào thường bị các nhà tài trợ dự án đánh giá thấp nhất?",
        "options_en": [
            "Legacy data cleansing, system integration testing, end-user business process retraining, and post-go-live productivity dips",
            "The initial purchase price of the vendor base software license",
            "The physical cost of purchasing printer paper and ballpoint pens",
            "The price of corporate coffee beans in the employee lounge"
        ],
        "options_vi": [
            "Làm sạch dữ liệu cũ (Data Cleansing), kiểm thử tích hợp, đào tạo lại quy trình nghiệp vụ cho người dùng và sự sụt giảm năng suất giai đoạn đầu sau Go-live",
            "Giá mua bản quyền phần mềm gốc từ nhà cung cấp giải pháp",
            "Chi phí mua giấy in văn phòng và bút bi viết bảng",
            "Tiền mua hạt cà phê phục vụ phòng nghỉ giải lao của nhân viên"
        ],
        "correct_answer": 0,
        "explanation_en": "Software licenses are often only 15-25% of TCO; data cleaning, process transformation, custom interfaces, and the post-implementation productivity slump account for the majority of expenditures.",
        "explanation_vi": "Chi phí bản quyền thường chỉ chiếm một phần nhỏ trong TCO; phần lớn chi phí nằm ở việc làm sạch dữ liệu, xây dựng tích hợp và tổn thất do sụt giảm năng suất ban đầu."
    })

    questions.append({
        "id": "QUES-025",
        "exam_id": "EXAM-01",
        "chapter_id": "chap-01",
        "topic": "ERP Cloud Architecture",
        "difficulty": "Advanced",
        "question_en": "What is the primary architectural advantage of a Multi-Tenant Cloud ERP architecture (e.g., SAP S/4HANA Cloud, Oracle Fusion) over an On-Premises legacy system?",
        "question_vi": "Lợi thế kiến trúc hàng đầu của mô hình ERP Đám mây Đa người thuê (Multi-Tenant Cloud ERP) so với hệ thống On-Premises truyền thống là gì?",
        "options_en": [
            "Continuous, automated feature updates managed by the vendor with reduced internal infrastructure overhead and rapid scalability",
            "The ability to completely rewrite vendor core source code without restriction",
            "Elimination of all network bandwidth and internet connectivity requirements",
            "Zero requirement for defining master data or setting user authorization roles"
        ],
        "options_vi": [
            "Các bản nâng cấp tính năng được nhà cung cấp cập nhật tự động định kỳ, giảm thiểu chi phí quản lý hạ tầng phần cứng nội bộ và mở rộng quy mô linh hoạt",
            "Khả năng chỉnh sửa tùy ý toàn bộ mã nguồn lõi của nhà sản xuất mà không gặp bất kỳ giới hạn nào",
            "Loại bỏ hoàn toàn yêu cầu về đường truyền băng thông mạng và kết nối internet",
            "Không bao giờ cần phải định nghĩa dữ liệu chủ hoặc thiết lập phân quyền người dùng"
        ],
        "correct_answer": 0,
        "explanation_en": "Cloud ERP delivers continuous innovation via quarterly vendor releases on shared infrastructure, shifting capital expenditure (CapEx) to predictable operational expenditure (OpEx).",
        "explanation_vi": "Cloud ERP mang lại sự đổi mới liên tục qua các bản cập nhật định kỳ từ nhà cung cấp, giải phóng doanh nghiệp khỏi gánh nặng duy trì máy chủ phần cứng đắt đỏ."
    })

    return questions

print("Exams 1 to 5 generator module ready.")
