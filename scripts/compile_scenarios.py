import json

scenarios = [
    {
        "id": "scenario-1",
        "category": "explanation",
        "title": {
            "vi": "1. Giải thích Khái niệm Chuyên sâu (Concept Explanation)",
            "en": "1. Deep Concept Explanation"
        },
        "purpose": {
            "vi": "Phân tích bản chất, nguyên lý vận hành và vai trò của một khái niệm cốt lõi trong ERP/SCM từ góc độ hệ thống tích hợp.",
            "en": "Deconstruct principles, operational logic, and strategic role of an ERP/SCM concept within enterprise architecture."
        },
        "system_instruction": "You are a Senior ERP & Supply Chain Management Subject Matter Expert. When explaining concepts, provide: 1) Formal definition in both Vietnamese and English; 2) Underlying operational principle; 3) Why it matters to enterprise operations; 4) Concrete ERP transaction/table mapping (e.g., SAP S/4HANA or Oracle Cloud ERP); 5) Common pitfalls in practice.",
        "prompt_template": "Giải thích chi tiết khái niệm [KHÁI NIỆM] trong hệ thống ERP/SCM. Phân tích nguyên lý vận hành, vai trò thực tế trong doanh nghiệp và cách cấu hình/thể hiện trên hệ thống ERP chuẩn.",
        "example_dialogue": {
            "user": "Giải thích chi tiết khái niệm 'Safety Stock' (Tồn kho an toàn) và cách tính toán trong môi trường ERP.",
            "assistant": "### Tồn kho An toàn (Safety Stock - SS)\n\n**1. Định nghĩa chuẩn:**\nTồn kho an toàn là lượng hàng tồn trữ dự phòng có chủ đích nhằm đối phó với sự không chắc chắn (uncertainty) về nhu cầu khách hàng trong thời gian giao hàng (Lead Time) hoặc sự trễ hạn giao hàng từ nhà cung cấp.\n\n**2. Công thức tính toán chuẩn:**\n$$SS = Z \\times \\sqrt{L \\times \\sigma_D^2 + D^2 \\times \\sigma_L^2}$$\nTrong đó: $Z$ là hệ số dịch vụ (Service Level Factor), $L$ là Lead Time bình quân, $\\sigma_D$ là độ lệch chuẩn nhu cầu, $\\sigma_L$ là độ lệch chuẩn thời gian giao hàng.\n\n**3. Ánh xạ ERP (SAP S/4HANA):**\nĐược cấu hình trong Master Data vật tư (`Material Master`), tab `MRP 2`, trường `Safety Stock` (MARC-EISBE). Khi chạy MRP (MD01N), hệ thống sẽ lập kế hoạch mua hàng/sản xuất khi tồn kho khả dụng rơi xuống dưới ngưỡng này."
        },
        "chips": [
            {
                "label": {
                    "vi": "Tồn kho an toàn (Safety Stock) & Điểm đặt hàng",
                    "en": "Safety Stock & Reorder Point (ROP)"
                },
                "prompt": "Giải thích bản chất của Tồn kho an toàn (Safety Stock) và Điểm đặt hàng lại (ROP) trong ERP. Hệ thống ERP tính toán và tự động kích hoạt Purchase Requisition như thế nào?"
            },
            {
                "label": {
                    "vi": "Mô hình EOQ cơ bản & Giả định",
                    "en": "Basic EOQ & Key Assumptions"
                },
                "prompt": "Giải thích nguyên lý toán học của công thức Wilson EOQ, sự đánh đổi giữa chi phí đặt hàng và lưu kho, cùng các giả định hạn chế khi áp dụng vào thực tế."
            },
            {
                "label": {
                    "vi": "Kế hoạch nhu cầu nguyên vật liệu (MRP II)",
                    "en": "Material Requirements Planning (MRP II)"
                },
                "prompt": "Giải thích cơ chế vận hành của vòng lặp MRP II (BOM, Inventory Master, Master Production Schedule) và quy trình bù trừ ròng (Netting process)."
            },
            {
                "label": {
                    "vi": "Hiệu ứng cái roi da (Bullwhip Effect)",
                    "en": "Bullwhip Effect & Mitigation in ERP"
                },
                "prompt": "Phân tích nguyên nhân cốt lõi gây ra hiệu ứng cái roi da (Bullwhip Effect) trong chuỗi cung ứng và cách hệ thống ERP/CPFR triệt tiêu hiện tượng này."
            }
        ],
        "follow_up_questions": [
            "Khái niệm này tương tác thế nào với các phân hệ MM, PP, SD trong ERP?",
            "Làm sao để một Business Analyst xác định các tham số này khi triển khai hệ thống mới?",
            "Rủi ro lớn nhất nếu doanh nghiệp cấu hình sai tham số này là gì?"
        ]
    },
    {
        "id": "scenario-2",
        "category": "comparison",
        "title": {
            "vi": "2. So sánh & Phân biệt Khái niệm (Concept Comparison)",
            "en": "2. Concept Comparison & Differentiation"
        },
        "purpose": {
            "vi": "Làm rõ sự khác biệt bản chất, ranh giới ứng dụng và các tiêu chí đánh đổi giữa hai hay nhiều khái niệm dễ gây nhầm lẫn.",
            "en": "Distinguish nuanced differences, boundary conditions, and trade-offs between easily conflated concepts."
        },
        "system_instruction": "You are a Senior ERP & Supply Chain Architect. When comparing two concepts: 1) Construct a high-contrast comparison table; 2) Analyze similarities and root differences; 3) Explain specific decision criteria for choosing one over another; 4) Provide concrete enterprise examples.",
        "prompt_template": "So sánh và phân biệt chi tiết giữa [KHÁI NIỆM A] và [KHÁI NIỆM B]. Cung cấp bảng so sánh đa chiều, ví dụ thực tế và tình huống áp dụng cụ thể trong hệ thống ERP.",
        "example_dialogue": {
            "user": "So sánh giữa mô hình EOQ cơ bản và mô hình EPQ (Gradual Replenishment).",
            "assistant": "### So sánh EOQ (Economic Order Quantity) vs. EPQ (Economic Production Quantity)\n\n| Tiêu chí | Mô hình EOQ Cơ Bản | Mô hình EPQ (Bổ sung dần) |\n|---|---|---|\n| **Bản chất nguồn cung** | Mua ngoài từ nhà cung cấp (Purchasing) | Tự sản xuất nội bộ (In-house Manufacturing) |\n| **Tốc độ giao hàng** | Tức thời ($p \\to \\infty$), cả lô $Q$ cập bến cùng lúc | Dần dần với tốc độ hữu hạn $p > d$ |\n| **Đỉnh tồn kho cực đại** | $I_{\\max} = Q$ | $I_{\\max} = Q(1 - d/p) < Q$ |\n| **Khoản chi phí cố định** | Chi phí đặt hàng ($K$ - Ordering Cost) | Chi phí thiết lập máy ($K$ - Setup Cost) |\n| **Công thức cỡ lô** | $Q^* = \\sqrt{\\frac{2KD}{h}}$ | $Q^* = \\sqrt{\\frac{2KD}{h(1 - d/p)}}$ |\n| **Mô-đun ERP quản lý** | SAP MM (Materials Management) | SAP PP (Production Planning) |"
        },
        "chips": [
            {
                "label": {
                    "vi": "EOQ (Mua hàng) vs. EPQ (Sản xuất dần)",
                    "en": "EOQ vs. EPQ (Gradual Replenishment)"
                },
                "prompt": "So sánh mô hình EOQ (đặt hàng tức thời từ NCC) và EPQ (tự sản xuất nội bộ với tốc độ hữu hạn). Tại sao tồn kho đỉnh của EPQ lại luôn nhỏ hơn EOQ?"
            },
            {
                "label": {
                    "vi": "Bài toán Vận tải vs. Bài toán Phân công 0-1",
                    "en": "Transportation vs. 0-1 Assignment Problem"
                },
                "prompt": "So sánh bài toán Vận tải tuyến tính tổng quát và bài toán Phân công nhị phân (0-1 Assignment). Khi nào một bài toán vận tải suy biến thành bài toán phân công?"
            },
            {
                "label": {
                    "vi": "Make-to-Stock (MTS) vs. Make-to-Order (MTO)",
                    "en": "MTS vs. MTO in Production Planning"
                },
                "prompt": "Phân tích sự khác biệt về chiến lược hoạch định nhu cầu, định vị tồn kho đệm và quy trình bán hàng giữa Make-to-Stock (MTS) và Make-to-Order (MTO)."
            },
            {
                "label": {
                    "vi": "2-Way Matching vs. 3-Way Matching",
                    "en": "2-Way Matching vs. 3-Way Matching in AP"
                },
                "prompt": "So sánh cơ chế đối chiếu hóa đơn 2 chiều (2-way) và 3 chiều (3-way matching: PO, Goods Receipt, Invoice) trong phân hệ Mua hàng/Kế toán ERP."
            }
        ],
        "follow_up_questions": [
            "Các hệ thống ERP hỗ trợ chuyển đổi giữa hai mô hình này như thế nào?",
            "Có tình huống nào kết hợp cả hai mô hình này trong cùng một quy trình không?",
            "Chỉ số KPI nào phản ánh hiệu quả vượt trội của một phương pháp?"
        ]
    },
    {
        "id": "scenario-3",
        "category": "business-analysis",
        "title": {
            "vi": "3. Phân tích Tình huống Doanh nghiệp (Business Scenario Analysis)",
            "en": "3. Business Scenario Analysis"
        },
        "purpose": {
            "vi": "Đặt học viên vào một bối cảnh thực tế của doanh nghiệp để mổ xẻ nguyên nhân gốc rễ, rủi ro chuỗi cung ứng và đề xuất giải pháp ERP tương ứng.",
            "en": "Immerse learners in real-world operational challenges to diagnose root causes, assess SCM risks, and formulate ERP interventions."
        },
        "system_instruction": "You are a Principal Supply Chain Consultant. Structure your response as an executive briefing: 1) Executive Summary; 2) Root Cause Analysis (People, Process, Data, Technology); 3) Quantifiable SCM impact; 4) Recommended ERP/SCM solution roadmap; 5) Risk mitigation & KPIs.",
        "prompt_template": "Phân tích tình huống doanh nghiệp sau đây: [MÔ TẢ TÌNH HUỐNG DOANH NGHIỆP]. Xác định nguyên nhân gốc rễ, ảnh hưởng đến chuỗi cung ứng và giải pháp giải quyết bằng phân hệ ERP.",
        "example_dialogue": {
            "user": "Doanh nghiệp bán lẻ thời trang gặp tình trạng: Một số cửa hàng liên tục hết hàng (stockout), trong khi kho trung tâm lại ứ đọng tồn kho đến hạn giảm giá. Dữ liệu bán hàng được tổng hợp thủ công mỗi cuối tuần qua Excel.",
            "assistant": "### Phân tích Tình huống Vận hành Chuỗi Cung ứng Bán lẻ\n\n**1. Chẩn đoán nguyên nhân gốc rễ:**\n- **Độ trễ thông tin (Information Latency):** Dữ liệu POS cuối tuần mới tổng hợp làm sai lệch bức tranh nhu cầu thực tế 5-7 ngày.\n- **Thiếu khả năng hiển thị thời gian thực (End-to-End Visibility):** Không có cơ chế chia sẻ tồn kho đa điểm (Omnichannel inventory).\n- **Quy trình bổ sung thụ động (Push vs. Pull):** Đang đẩy hàng theo cảm tính thay vì tự động kích hoạt theo ngưỡng ROP.\n\n**2. Đề xuất giải pháp ERP/SCM:**\n- Tích hợp POS thời gian thực vào ERP (SAP Retail / CAR).\n- Kích hoạt quy trình tự động tính toán nhu cầu replenishment theo ROP động (Dynamic Reorder Point).\n- Kích hoạt cơ chế điều chuyển kho nội bộ ngang hàng (Store-to-store transfer) trước khi đặt hàng mới."
        },
        "chips": [
            {
                "label": {
                    "vi": "Độ trễ dữ liệu POS gây lệch kho đa điểm",
                    "en": "Retail POS Latency & Stockout Analysis"
                },
                "prompt": "Một chuỗi bán lẻ thời trang bị thiếu hàng tại cửa hàng nhưng dư thừa tại kho tổng do tổng hợp số liệu POS thủ công. Hãy phân tích và đề xuất giải pháp ERP."
            },
            {
                "label": {
                    "vi": "Nhà cung cấp giao trễ làm gián đoạn lắp ráp",
                    "en": "Supplier Delay Disrupting Final Assembly"
                },
                "prompt": "Nhà máy lắp ráp điện tử thường xuyên dừng chuyền do linh kiện nhập khẩu bị chậm tàu 10-15 ngày. Phân tích chính sách tồn kho an toàn và giải pháp ERP SCM."
            },
            {
                "label": {
                    "vi": "Chi phí lưu kho tăng vọt do tích trữ đón chiết khấu",
                    "en": "Skyrocketing Holding Cost from Over-Purchasing"
                },
                "prompt": "Phòng Mua hàng liên tục đặt lô lớn để hưởng chiết khấu số lượng khiến kho quá tải và phát sinh chi phí lưu kho đột biến. Đánh giá tính kinh tế theo mô hình EOQ."
            },
            {
                "label": {
                    "vi": "Đơn hàng khẩn làm vỡ kế hoạch sản xuất",
                    "en": "Rush Orders Breaking MPS Stability"
                },
                "prompt": "Bộ phận Sales liên tục nhận đơn hàng khẩn yêu cầu giao ngay, làm xáo trộn lịch chạy chuyền và phát sinh chi phí thiết lập máy khổng lồ. Cần thiết lập Business Rules nào trong ERP?"
            }
        ],
        "follow_up_questions": [
            "Các chỉ số OTD (On-Time Delivery) và DSI (Days Sales of Inventory) sẽ biến thiên ra sao?",
            "Cần những bảng dữ liệu nào trong ERP để xây dựng dashboard giám sát vấn đề này?",
            "Lộ trình triển khai giải pháp cần bao nhiêu tháng?"
        ]
    },
    {
        "id": "scenario-4",
        "category": "ba-perspective",
        "title": {
            "vi": "4. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (Business Analyst Perspective)",
            "en": "4. Business Analyst (BA) Perspective"
        },
        "purpose": {
            "vi": "Chuyển hóa bài toán kinh doanh và công thức toán học thành tài liệu phân tích nghiệp vụ chuẩn: BRD, FR, NFR, Business Rules và kịch bản kiểm thử UAT.",
            "en": "Translate business problems and mathematical logic into professional BA artifacts: BRDs, FRs, NFRs, Business Rules, and UAT acceptance criteria."
        },
        "system_instruction": "You are a Lead IT Business Analyst specializing in ERP SCM transformations. Format your analysis systematically with: 1) Business Requirements Document (BRD) summary; 2) Functional Requirements (FR-01, FR-02); 3) Non-Functional Requirements (NFR); 4) Explicit Business Rules (BR); 5) Data Entities & Attributes; 6) Acceptance Criteria in Given-When-Then format.",
        "prompt_template": "Đóng vai trò Chuyên viên Phân tích Nghiệp vụ (BA) trưởng cho dự án triển khai phân hệ [PHÂN HỆ ERP]. Hãy xây dựng yêu cầu chức năng (FR), quy tắc nghiệp vụ (Business Rules) và tiêu chí nghiệm thu (UAT Acceptance Criteria) cho quy trình [QUY TRÌNH NGHIỆP VỤ].",
        "example_dialogue": {
            "user": "Xây dựng yêu cầu BA cho tính năng tự động tính toán EOQ và gợi ý đơn hàng mua (PO Proposal) trong hệ thống ERP.",
            "assistant": "### Business Analysis Specification: Automated EOQ & PO Proposal\n\n**1. Functional Requirements (FR):**\n- `FR-PO-01`: Hệ thống PHẢI tự động trích xuất các tham số $D, K, h$ từ bảng lịch sử tiêu thụ và Master Data để tính $Q^* = \\sqrt{2KD/h}$.\n- `FR-PO-02`: Hệ thống PHẢI so sánh tồn kho khả dụng hiện tại với điểm đặt hàng $ROP = d \\times L + SS$. Nếu tồn kho $\\le ROP$, tự động tạo bản ghi `Purchase Requisition` với số lượng $Q^*$.\n\n**2. Business Rules (BR):**\n- `BR-01`: Kích cỡ đặt hàng gợi ý phải làm tròn lên bội số nguyên gần nhất của quy cách đóng gói (`Minimum Order Quantity` và `Packing Size`).\n- `BR-02`: Nếu nhà cung cấp có bảng chiết khấu bậc thang, hệ thống phải tự động tính toán tổng chi phí $TC(Q)$ tại các điểm phá vỡ giá và chọn bậc tối ưu nhất.\n\n**3. Acceptance Criteria (Given-When-Then):**\n- **Scenario:** Tồn kho rơi dưới ngưỡng ROP khi chạy MRP đêm.\n  - *Given* Mặt hàng TYRE-01 có ROP = 180 và tồn kho khả dụng còn 150 đơn vị.\n  - *When* Tiến trình xử lý đêm MRP Batch Run (MD01N) kích hoạt lúc 00:00.\n  - *Then* Hệ thống tạo thành công 01 Purchase Requisition với số lượng đúng bằng $Q^* = 573$ chiếc và gửi thông báo vào Inbox của Buyer phụ trách."
        },
        "chips": [
            {
                "label": {
                    "vi": "BA Spec: Tính toán EOQ & Tự động tạo Purchase Requisition",
                    "en": "BA Spec: EOQ Calculation & Auto Purchase Req"
                },
                "prompt": "Xây dựng tài liệu yêu cầu BA (FR, NFR, Business Rules, UAT Acceptance Criteria) cho tính năng tính toán EOQ và tự động tạo đề xuất mua hàng (Purchase Requisition) trong ERP."
            },
            {
                "label": {
                    "vi": "BA Spec: Quy tắc đối chiếu 3 chiều (3-Way Matching)",
                    "en": "BA Spec: 3-Way Matching & Tolerance Limits"
                },
                "prompt": "Viết bộ yêu cầu nghiệp vụ BA cho quy trình tự động đối chiếu hóa đơn 3-Way Matching (PO, GR, Invoice) kèm theo ma trận xử lý sai số cho phép (Tolerance limits)."
            },
            {
                "label": {
                    "vi": "BA Spec: Quy trình phê duyệt đơn hàng đa cấp",
                    "en": "BA Spec: Multi-level PO Approval Workflow"
                },
                "prompt": "Xây dựng đặc tả luồng duyệt Purchase Order đa cấp (Workflow Approval) dựa trên ngưỡng giá trị ngân sách và phân quyền trách nhiệm (RACI Matrix)."
            },
            {
                "label": {
                    "vi": "BA Spec: Phân bổ lệnh sản xuất theo năng lực chuyền",
                    "en": "BA Spec: Capacity-constrained Production Dispatching"
                },
                "prompt": "Thiết kế yêu cầu chức năng cho mô-đun lập lịch sản xuất hữu hạn (Finite Capacity Scheduling) ngăn chặn tình trạng quá tải xưởng máy."
            }
        ],
        "follow_up_questions": [
            "Các trường dữ liệu nào là bắt buộc trong Data Dictionary của giao diện này?",
            "Làm thế nào để xử lý ngoại lệ khi dữ liệu lịch sử $D$ bị đột biến bất thường?",
            "Ma trận phân quyền (Role & Permission) cho chức năng này nên cấu hình ra sao?"
        ]
    },
    {
        "id": "scenario-5",
        "category": "case-study",
        "title": {
            "vi": "5. Thảo luận Tình huống Nghiên cứu (Case Study Deep Dive)",
            "en": "5. Case Study Discussion"
        },
        "purpose": {
            "vi": "Mổ xẻ 4 tình huống nghiên cứu thực tế (Texago, Better Products, ACT, SOCA), phân tích logic bài toán, kiểm chứng số liệu và thảo luận các hàm ý chiến lược.",
            "en": "Deep dive into the 4 textbook case studies (Texago, Better Products, ACT, SOCA) to audit mathematical models and extract strategic supply chain insights."
        },
        "system_instruction": "You are a Case Method Professor in Enterprise Systems & SCM. For any case study query: 1) Synthesize context and mathematical parameters; 2) State the exact decision variables and objective function; 3) Provide step-by-step numerical verification; 4) Discuss managerial and ERP integration implications.",
        "prompt_template": "Thảo luận chuyên sâu về tình huống [CASE STUDY 1/2/3/4]. Phân tích mô hình toán học đã sử dụng, kết quả định lượng cụ thể và bài học thực tiễn rút ra cho doanh nghiệp.",
        "example_dialogue": {
            "user": "Tại sao trong Case Texago, St. Louis lại là địa điểm được chọn dù chi phí vận chuyển dầu thô đến đó cao hơn Galveston?",
            "assistant": "### Phân tích Quyết định Lựa chọn Địa điểm St. Louis (Texago Corp.)\n\n**1. Bức tranh định lượng toàn diện ($ Millions):**\n- **Galveston, TX:** Vận chuyển dầu thô: $360M | Vận hành nhà máy: $570M | Phân phối thành phẩm: $450M $\\implies$ **Tổng: $1.380M**.\n- **St. Louis, MO:** Vận chuyển dầu thô: $440M | Vận hành nhà máy: $530M | Phân phối thành phẩm: $360M $\\implies$ **Tổng: $1.330M**.\n\n**2. Bản chất kinh tế:**\nDù Galveston có lợi thế sát mỏ dầu Texas giúp giảm chi phí dầu thô (\$360M vs \$440M, tiết kiệm \$80M), St. Louis lại vượt trội nhờ:\n- Chi phí vận hành nhà máy rẻ hơn \$40M (\$530M vs \$570M).\n- Chi phí phân phối sản phẩm tinh chế đến các thị trường trọng điểm (Pittsburgh, Atlanta, Kansas City) rẻ hơn tới \$90M (\$360M vs \$450M).\n\n**3. Bài học chiến lược SCM:**\nTối ưu hóa mạng lưới chuỗi cung ứng là bài toán cực tiểu hóa tổng chi phí trên toàn bộ chuỗi (End-to-End Total Cost), không phải là tối ưu hóa cục bộ một mắt xích riêng lẻ."
        },
        "chips": [
            {
                "label": {
                    "vi": "Case 1 Texago: Phân tích đánh đổi tổng chi phí 3 địa điểm",
                    "en": "Case 1 Texago: 3-Site Total Cost Trade-off"
                },
                "prompt": "Trong Case 1 Texago, phân tích tại sao St. Louis lại là địa điểm tối ưu dù chi phí vận chuyển dầu thô cao hơn Galveston. Trình bày chi tiết bảng so sánh tổng chi phí."
            },
            {
                "label": {
                    "vi": "Case 2 Better Products: Phân bổ sản phẩm & Ràng buộc không chia nhỏ",
                    "en": "Case 2 Better Products: Splitting vs. 0-1 Assignment"
                },
                "prompt": "So sánh kết quả Case 2.1 (cho phép chia tách sản phẩm) và Case 2.2 (phân công nguyên khối). Chi phí gia tăng $30/ngày trong Case 2.2 được bù đắp bằng những lợi ích vận hành nào?"
            },
            {
                "label": {
                    "vi": "Case 3 ACT: Chuyển đổi từ trực quan sang EOQ & Thiếu hàng",
                    "en": "Case 3 ACT: Intuitive vs. EOQ vs. Backorders"
                },
                "prompt": "Phân tích tình huống Atlantic Coast Tire (ACT): Tính toán khoản tiết kiệm khi chuyển từ Q = 1.000 sang EOQ (Q* = 573) và chính sách cho phép thiếu hàng có kế hoạch (Q* = 716, S* = 257)."
            },
            {
                "label": {
                    "vi": "Case 4 SOCA: Cơ chế bổ sung dần (EPQ) & Lợi ích vận hành",
                    "en": "Case 4 SOCA: Gradual Replenishment Dynamics"
                },
                "prompt": "Giải thích tại sao trong Case SOCA, việc tăng kích cỡ lô từ 30.000 lên 50.000 loa lại giúp tiết kiệm $16.000/năm và tạo ra khoảng thời gian trống 33,33 ngày cho các sản phẩm khác."
            }
        ],
        "follow_up_questions": [
            "Nếu chi phí nhiên liệu tăng 20%, quyết định lựa chọn địa điểm trong Case Texago có bị đảo ngược không?",
            "Làm thế nào để đưa ràng buộc năng lực tối đa của kho vào bài toán SOCA?",
            "Nếu ACT không muốn chịu rủi ro mất khách hàng, họ có nên triển khai mô hình thiếu hàng (Planned Shortages) không?"
        ]
    },
    {
        "id": "scenario-6",
        "category": "quantitative",
        "title": {
            "vi": "6. Giải bài toán Định lượng & Tối ưu hóa (Quantitative Problem Solving)",
            "en": "6. Quantitative Problem Solving & Solver"
        },
        "purpose": {
            "vi": "Hướng dẫn từng bước thiết lập mô hình toán học, xác định biến quyết định, hàm mục tiêu, ràng buộc và cách giải trên Excel Solver hoặc QM for Windows.",
            "en": "Guide step-by-step formulation of mathematical models, decision variables, objective functions, constraints, and solver configurations in Excel / QM."
        },
        "system_instruction": "You are a Management Science & Operations Research Tutor. Guide students with pedagogical clarity: 1) Identify input parameters and notation; 2) Define decision variables; 3) Formulate the mathematical objective and constraints; 4) Provide step-by-step manual or derivative calculation; 5) Provide Excel Solver setup instructions (Set Objective, Changing Variable Cells, Constraints, Simplex LP / GRG Nonlinear).",
        "prompt_template": "Giải bài toán định lượng SCM sau: [THÔNG SỐ ĐẦU VÀO]. Hãy thiết lập mô hình toán học hoàn chỉnh, tính toán kết quả tối ưu và hướng dẫn cách thiết lập trên Excel Solver.",
        "example_dialogue": {
            "user": "Cho một nhà kho có nhu cầu D = 10.000 sp/năm, chi phí đặt hàng K = $50/đơn, giá mua c = $20, chi phí lưu kho chiếm 20% giá mua mỗi năm. Tính EOQ và tổng chi phí.",
            "assistant": "### Lời giải Chi tiết Bài toán EOQ\n\n**1. Xác định tham số đầu vào:**\n- Nhu cầu hàng năm: $D = 10.000\\text{ sp/năm}$\n- Chi phí đặt hàng: $K = \\$50/\\text{đơn}$\n- Chi phí lưu kho đơn vị: $h = I \\times c = 20\\% \\times \\$20 = \\$4.00/\\text{sp/năm}$\n\n**2. Tính toán quy mô đặt hàng tối ưu ($Q^*$):**\n$$Q^* = \\sqrt{\\frac{2KD}{h}} = \\sqrt{\\frac{2 \\times 50 \\times 10.000}{4.00}} = \\sqrt{\\frac{1.000.000}{4.00}} = \\sqrt{250.000} = \\mathbf{500\\text{ sản phẩm}}$$\n\n**3. Các chỉ số vận hành kinh tế:**\n- Số đơn hàng mỗi năm: $N = \\frac{D}{Q^*} = \\frac{10.000}{500} = 20\\text{ đơn/năm}$\n- Chi phí đặt hàng hàng năm: $20 \\times 50 = \\$1.000$\n- Chi phí lưu kho hàng năm: $\\frac{500}{2} \\times 4.00 = \\$1.000$\n- Tổng chi phí khả biến: $TVC^* = \\$1.000 + \\$1.000 = \\mathbf{\\$2.000/\\text{năm}}$"
        },
        "chips": [
            {
                "label": {
                    "vi": "Tính EOQ & Điểm hòa vốn chi phí đặt hàng / lưu kho",
                    "en": "Compute EOQ & Holding/Ordering Balance"
                },
                "prompt": "Hướng dẫn giải chi tiết bài toán EOQ với D = 12.000 đơn vị, K = $150, h = $4,00. Trình bày các bước thiết lập hàm mục tiêu và giải bằng Excel Solver GRG Nonlinear."
            },
            {
                "label": {
                    "vi": "Thiết lập bảng vận tải & Dummy Destination khi Cung > Cầu",
                    "en": "Unbalanced Transportation & Dummy Destination"
                },
                "prompt": "Cho bài toán vận tải với 3 nhà máy có tổng cung 16 triệu m3 và 4 khu vực có tổng cầu 12,5 triệu m3. Hướng dẫn cách tạo điểm đến giả (Dummy destination) và thiết lập mô hình Simplex LP."
            },
            {
                "label": {
                    "vi": "Xử lý tuyến đường cấm bằng phương pháp Big-M",
                    "en": "Prohibited Route Modeling via Big-M"
                },
                "prompt": "Giải thích cơ chế toán học của phương pháp Big-M để cấm một tuyến đường vận chuyển trong mô hình quy hoạch tuyến tính và cách gán giá trị M trong thực tế."
            },
            {
                "label": {
                    "vi": "Bài toán chiết khấu số lượng & Kiểm tra Breakpoint",
                    "en": "Quantity Discount & Breakpoint Feasibility"
                },
                "prompt": "Trình bày thuật toán 3 bước để tìm kích cỡ đặt hàng tối ưu khi nhà cung cấp áp dụng biểu giá chiết khấu theo số lượng (All-Units Quantity Discounts)."
            }
        ],
        "follow_up_questions": [
            "Nếu tham số $K$ tăng gấp đôi, cỡ lô tối ưu sẽ thay đổi theo tỷ lệ nào?",
            "Làm thế nào để kiểm tra tính nhạy cảm (Sensitivity Analysis) của nghiệm tối ưu trên Excel?",
            "Có thể áp dụng thuật toán Heuristic nào để tìm nghiệm khởi đầu nhanh cho bài toán vận tải?"
        ]
    },
    {
        "id": "scenario-7",
        "category": "exam-tutor",
        "title": {
            "vi": "7. Gia sư Luyện thi & Giải thích Đáp án (Exam Tutor & Review)",
            "en": "7. Exam Tutor & Answer Review"
        },
        "purpose": {
            "vi": "Hỗ trợ học viên phân tích các câu hỏi trắc nghiệm ôn tập, giải thích cặn kẽ tại sao một đáp án đúng và vì sao 3 phương án còn lại là bẫy sai sót.",
            "en": "Assist students in reviewing exam questions, detailing why the correct option is sound and debunking common distractors."
        },
        "system_instruction": "You are a Patient Academic Exam Tutor. When reviewing a question: 1) Identify the core tested knowledge point; 2) Confirm the correct answer with rigorous justification; 3) Deconstruct each distractor and explain why it is incorrect or misleading; 4) Provide a memory mnemonic or rule of thumb for exam success.",
        "prompt_template": "Giải thích câu hỏi trắc nghiệm sau đây: [NỘI DUNG CÂU HỎI VÀ CÁC PHƯƠNG ÁN A, B, C, D]. Phân tích vì sao phương án được chọn là đúng và các phương án khác sai ở điểm nào.",
        "example_dialogue": {
            "user": "Câu hỏi: Trong mô hình EOQ cơ bản, nếu nhu cầu hàng năm (D) tăng gấp 4 lần trong khi các chi phí khác không đổi, kích cỡ lô tối ưu (Q*) sẽ biến động như thế nào?\nA. Tăng gấp 4 lần\nB. Tăng gấp 2 lần\nC. Giảm một nửa\nD. Không đổi",
            "assistant": "### Hướng dẫn Giải thích Đáp án\n\n**Đáp án đúng: B (Tăng gấp 2 lần)**\n\n**1. Căn cứ toán học:**\nCông thức Wilson EOQ là:\n$$Q^* = \\sqrt{\\frac{2KD}{h}}$$\nNhu cầu $D$ nằm dưới dấu căn bậc hai. Khi thay $D' = 4D$:\n$$Q^{*'} = \\sqrt{\\frac{2K(4D)}{h}} = \\sqrt{4} \\times \\sqrt{\\frac{2KD}{h}} = 2 \\times Q^*$$\nDo đó, cỡ lô tối ưu chỉ tăng gấp $\\sqrt{4} = 2$ lần.\n\n**2. Phân tích các bẫy sai lầm:**\n- **Phương án A (Tăng gấp 4 lần):** Bẫy do suy nghĩ tuyến tính thông thường, quên mất mối quan hệ căn bậc hai.\n- **Phương án C & D:** Hoàn toàn sai logic vì quy mô nhu cầu tăng đương nhiên đòi hỏi quy mô đặt hàng phải tăng để cân bằng chi phí."
        },
        "chips": [
            {
                "label": {
                    "vi": "Độ nhạy của EOQ khi tham số D, K hoặc h thay đổi",
                    "en": "EOQ Parameter Sensitivity Analysis"
                },
                "prompt": "Nếu chi phí lưu kho h tăng gấp 4 lần trong mô hình EOQ cơ bản, kích cỡ đặt hàng tối ưu và tổng chi phí tồn kho sẽ thay đổi ra sao? Phân tích căn cứ toán học."
            },
            {
                "label": {
                    "vi": "Bản chất chi phí tại điểm cân bằng EOQ",
                    "en": "Cost Parity at Basic EOQ Equilibrium"
                },
                "prompt": "Tại điểm tối ưu của mô hình EOQ cơ bản không có chiết khấu, mối quan hệ giữa Chi phí đặt hàng hàng năm và Chi phí lưu kho hàng năm là gì? Chứng minh."
            },
            {
                "label": {
                    "vi": "Bẫy phân công trong bài toán vận tải suy biến",
                    "en": "Degeneracy Traps in Transportation Problems"
                },
                "prompt": "Thế nào là hiện tượng suy biến (Degeneracy) trong bài toán vận tải? Khi nào số lượng ô cơ sở nhỏ hơn m + n - 1 và cách khắc phục bằng đại lượng epsilon (ε)?"
            },
            {
                "label": {
                    "vi": "Phương pháp Hungarian trong bài toán cực đại hóa",
                    "en": "Hungarian Method for Maximization Problems"
                },
                "prompt": "Thuật toán Hungarian được thiết kế gốc cho bài toán cực tiểu hóa chi phí. Khi gặp bài toán phân công cực đại hóa lợi nhuận, bước biến đổi ma trận đầu tiên là gì?"
            }
        ],
        "follow_up_questions": [
            "Dạng câu hỏi này thường xuất hiện ở mức độ nhận biết hay vận dụng cao?",
            "Có mẹo nhớ nhanh nào để không bị nhầm dấu công thức không?",
            "Làm thế nào để kiểm tra lại đáp án bằng phép thử số học nhanh?"
        ]
    },
    {
        "id": "scenario-8",
        "category": "critical-thinking",
        "title": {
            "vi": "8. Tư duy Phản biện & Đánh đổi Chiến lược (Critical Thinking & Strategic Trade-offs)",
            "en": "8. Strategic Trade-offs & Critical Thinking"
        },
        "purpose": {
            "vi": "Kích thích tư duy đa chiều, phản biện các giả định lý tưởng của mô hình toán học và đánh giá các yếu tố bất định trong thực tế vận hành chuỗi cung ứng.",
            "en": "Challenge idealized assumptions of mathematical models and evaluate real-world trade-offs, geopolitical disruptions, and ESG imperatives."
        },
        "system_instruction": "You are a Chief Strategy Officer & Supply Chain Thought Leader. Challenge simplistic assumptions: 1) Question idealized model constraints (e.g., constant demand, zero lead time variance); 2) Expose hidden friction costs (tariffs, ESG carbon footprints, labor disputes); 3) Propose resilient hybrid strategies; 4) Formulate critical strategic questions for executive leadership.",
        "prompt_template": "Phản biện và phân tích tư duy chiến lược cho chủ đề: [CHỦ ĐỀ ĐÁNH ĐỔI / PHẢN BIỆN]. Những giả định nào của mô hình lý thuyết thường bị sụp đổ trong môi trường kinh doanh thực tế đầy biến động?",
        "example_dialogue": {
            "user": "Phản biện chiến lược Lean / JIT (Just-in-Time) trong chuỗi cung ứng toàn cầu sau các biến cố đại dịch và xung đột địa chính trị.",
            "assistant": "### Phản biện Chiến lược Lean / Just-in-Time trong Kỷ nguyên Bất định\n\n**1. Sự sụp đổ của các giả định lý tưởng:**\n- *Giả định 1: Chuỗi cung ứng luôn thông suốt.* Thực tế: Đóng cửa cảng biển, thiếu container rỗng và gián đoạn kênh đào làm Lead Time kéo dài gấp 3 lần.\n- *Giả định 2: Tồn kho bằng 0 là tối ưu tuyệt đối.* Thực tế: Thiếu một con chip bán dẫn \$2 khiến nhà máy ô tô trị giá hàng tỷ USD phải ngừng trệ hàng tuần.\n\n**2. Sự chuyển dịch từ 'Just-in-Time' sang 'Just-in-Case':**\n- Doanh nghiệp không thể chỉ tối ưu hóa chi phí ngắn hạn (Cost Efficiency) mà phải đánh đổi để xây dựng độ bền bỉ (Resilience).\n- Thiết lập mạng lưới nhà cung cấp kép (Dual Sourcing / Nearshoring) thay vì phụ thuộc đơn nguồn giá rẻ.\n- Nâng ngưỡng tồn kho an toàn đệm cho các linh kiện trọng yếu (Critical Components)."
        },
        "chips": [
            {
                "label": {
                    "vi": "Phản biện Lean/JIT: Hiệu quả chi phí vs. Độ kiên cường (Resilience)",
                    "en": "Critique of Lean/JIT: Cost vs. Resilience"
                },
                "prompt": "Phản biện triết lý Just-in-Time (JIT) và lượng tồn kho tối thiểu trong bối cảnh chuỗi cung ứng toàn cầu dễ bị tổn thương bởi thiên tai và xung đột địa chính trị."
            },
            {
                "label": {
                    "vi": "Đánh đổi giữa Chi phí vận tải & Lượng phát thải Carbon (ESG)",
                    "en": "Trade-off: Transport Cost vs. Carbon Emissions"
                },
                "prompt": "Mô hình vận tải tuyến tính truyền thống chỉ tập trung cực tiểu hóa chi phí tài chính ($). Làm thế nào để tích hợp chỉ số phát thải Carbon (ESG Scope 3) vào hàm mục tiêu?"
            },
            {
                "label": {
                    "vi": "Rủi ro khi chấp nhận thiếu hàng có kế hoạch (Planned Shortages)",
                    "en": "Reputational Risks of Planned Shortages"
                },
                "prompt": "Mô hình EOQ cho phép thiếu hàng chứng minh mặt toán học có thể giảm tổng chi phí, nhưng doanh nghiệp đối mặt với rủi ro mất khách hàng vĩnh viễn ra sao?"
            },
            {
                "label": {
                    "vi": "Áp lực tự động hóa ERP vs. Sự linh hoạt của con người",
                    "en": "Full ERP Automation vs. Human Discretion"
                },
                "prompt": "Khi nào doanh nghiệp nên để thuật toán ERP tự động chốt đơn hàng và khi nào cần sự can thiệp phê duyệt chủ quan của con người (Human-in-the-loop)?"
            }
        ],
        "follow_up_questions": [
            "Làm thế nào để lượng hóa chi phí tổn hại thương hiệu khi bị thiếu hàng?",
            "Chuỗi cung ứng của tương lai nên ưu tiên Tối ưu hóa chi phí (Optimization) hay Khả năng thích ứng (Agility)?",
            "Công nghệ GenAI và Machine Learning có thể bù đắp điểm yếu nào của các mô hình toán truyền thống?"
        ]
    }
]

with open("outputs/data/scenarios.json", "w", encoding="utf-8") as f:
    json.dump(scenarios, f, ensure_ascii=False, indent=2)

print("Saved outputs/data/scenarios.json with 8 scenarios.")
