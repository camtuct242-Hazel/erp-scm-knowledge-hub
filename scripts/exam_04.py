# -*- coding: utf-8 -*-
# EXAM 04: Route Restrictions, Prohibited Lanes & Big-M (chap-02)
# 25 Questions: Q076 to Q100 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q076 - Q085)
    questions.append({
        "id": "QUES-076",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Prohibited Route Concept",
        "difficulty": "Basic",
        "question_en": "What is a 'Prohibited Route' in a supply chain transportation problem?",
        "question_vi": "'Tuyến đường Cấm' (Prohibited Route) trong bài toán vận tải chuỗi cung ứng là gì?",
        "options_en": [
            "A specific shipping lane between a supply origin and demand destination that cannot be used due to physical, technical, regulatory, or policy constraints",
            "A public road where toll fees are slightly higher than normal",
            "A highway that is only open during Sunday mornings",
            "A delivery route that passes near a competitor's corporate headquarters"
        ],
        "options_vi": [
            "Một tuyến vận chuyển cụ thể giữa điểm nguồn và điểm đích không thể sử dụng do các rào cản vật lý, kỹ thuật, pháp lý hoặc quy định tổ chức",
            "Một tuyến đường công cộng có mức thu phí qua trạm hơi cao hơn bình thường",
            "Một đường cao tốc chỉ mở cửa lưu thông vào các buổi sáng Chủ nhật",
            "Một tuyến giao hàng tình cờ đi ngang qua trụ sở của đối thủ cạnh tranh"
        ],
        "correct_answer": 0,
        "explanation_en": "A prohibited route represents a disallowed origin-destination pairing due to lack of infrastructure, equipment incompatibility, or trade regulations.",
        "explanation_vi": "Tuyến cấm là cặp điểm nguồn - điểm đích bị phong tỏa do không có đường nối, hạn chế công nghệ hoặc quy định an toàn bắt buộc."
    })

    questions.append({
        "id": "QUES-077",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Big-M Concept",
        "difficulty": "Basic",
        "question_en": "In mathematical optimization, what does the symbol 'M' represent in the Big-M method?",
        "question_vi": "Trong tối ưu hóa toán học, ký hiệu 'M' trong phương pháp số M lớn (Big-M) đại diện cho điều gì?",
        "options_en": [
            "A strictly positive, arbitrarily large penalty cost designed to force the corresponding decision variable to zero in cost minimization",
            "The total number of employees working in the manufacturing plant",
            "The exact distance in miles between New York and Los Angeles",
            "The calendar month during which the optimization software was installed"
        ],
        "options_vi": [
            "Một mức chi phí phạt dương cực lớn tùy ý, được thiết kế để ép biến quyết định tương ứng phải triệt tiêu về 0 trong bài toán cực tiểu hóa chi phí",
            "Tổng số lượng công nhân đang làm việc trong nhà máy sản xuất",
            "Khoảng cách chính xác tính bằng dặm giữa New York và Los Angeles",
            "Tháng dương lịch mà phần mềm tối ưu hóa được cài đặt vào máy tính"
        ],
        "correct_answer": 0,
        "explanation_en": "Big-M introduces an enormous penalty cost into the objective function so the LP solver drives x_ij to 0 unless no other feasible option exists.",
        "explanation_vi": "Số M lớn là hệ số phạt khổng lồ khiến hàm mục tiêu bị đội chi phí khủng khiếp, buộc thuật toán đơn hình không bao giờ chọn ô này."
    })

    questions.append({
        "id": "QUES-078",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Co. Demand Categories",
        "difficulty": "Basic",
        "question_en": "In the Energetic Company case study, what are the three distinct categories of energy requirements in the new building?",
        "question_vi": "Trong case study Energetic Company, ba hạng mục nhu cầu năng lượng riêng biệt trong tòa nhà mới là gì?",
        "options_en": [
            "Electricity (20 units), Water Heating (10 units), and Space Heating (30 units)",
            "Lighting, Air Conditioning, and Swimming Pool Heating",
            "Diesel Fuel, Gasoline, and Jet Kerosene",
            "Computer Power, Cafeteria Cooking, and Elevator Operation"
        ],
        "options_vi": [
            "Điện năng (20 đơn vị), Đun nước nóng (10 đơn vị) và Sưởi ấm không gian tòa nhà (30 đơn vị)",
            "Hệ thống chiếu sáng, Điều hòa không khí và Làm ấm bể bơi",
            "Nhiên liệu Diesel, Xăng không chì và Dầu hỏa máy bay",
            "Nguồn điện máy tính, Nấu ăn căng-tin và Vận hành thang máy"
        ],
        "correct_answer": 0,
        "explanation_en": "The three energy categories in Energetic Co. are electricity (20), water heating (10), and space heating (30), totaling 60 daily units.",
        "explanation_vi": "3 nhu cầu năng lượng của tòa nhà gồm Điện năng (20), Đun nước nóng (10) và Sưởi ấm (30), tổng cộng 60 đơn vị/ngày."
    })

    questions.append({
        "id": "QUES-079",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Co. Energy Sources",
        "difficulty": "Basic",
        "question_en": "What are the three available energy sources in the Energetic Company case study?",
        "question_vi": "Ba nguồn cung cấp năng lượng khả dụng trong case study Energetic Company là gì?",
        "options_en": [
            "Electricity utility, Natural Gas, and a Rooftop Solar Heater",
            "Coal, Wind Turbine, and Nuclear Power",
            "Geothermal, Biomass, and Hydroelectric Dam",
            "Diesel Generator, Wood Fireplace, and Propane Tanks"
        ],
        "options_vi": [
            "Điện lưới công cộng, Khí đốt tự nhiên (Gas) và Giàn năng lượng mặt trời trên mái",
            "Than đá, Tuabin gió và Nhà máy điện hạt nhân",
            "Địa nhiệt, Sinh khối và Thủy điện",
            "Máy phát điện Diesel, Lò sưởi củi và Bình khí propan"
        ],
        "correct_answer": 0,
        "explanation_en": "Energetic Co. evaluates electricity utility, natural gas supply, and an installed rooftop solar heating unit.",
        "explanation_vi": "Ba nguồn cấp năng lượng được xem xét là Điện lưới, Khí gas tự nhiên và Hệ thống pin nhiệt mặt trời trên mái."
    })

    questions.append({
        "id": "QUES-080",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Co. Solar Restriction",
        "difficulty": "Basic",
        "question_en": "In the Energetic Company case, what physical capacity limit restricts the rooftop solar heater?",
        "question_vi": "Trong case Energetic Company, giới hạn công suất vật lý nào hạn chế giàn sưởi năng lượng mặt trời trên mái?",
        "options_en": [
            "The physical surface area of the roof limits the solar heater to providing at most 30 units of energy per day",
            "The solar heater cannot operate on cloudy days",
            "The solar heater can only provide 5 units per month",
            "The roof has zero capacity and can hold no equipment"
        ],
        "options_vi": [
            "Diện tích mặt sàn hữu dụng của mái nhà giới hạn công suất giàn sưởi mặt trời tối đa chỉ cung cấp được 30 đơn vị năng lượng/ngày",
            "Giàn năng lượng mặt trời không thể hoạt động vào những ngày nhiều mây",
            "Giàn năng lượng mặt trời chỉ cấp được tối đa 5 đơn vị mỗi tháng",
            "Mái nhà có tải trọng bằng 0 và không thể đặt bất kỳ thiết bị nào"
        ],
        "correct_answer": 0,
        "explanation_en": "Due to roof size limitations, solar heating capacity is constrained to an upper bound of 30 units per day.",
        "explanation_vi": "Do diện tích mái nhà có hạn, công suất cực đại của hệ mặt trời bị chặn trên ở mức 30 đơn vị/ngày."
    })

    questions.append({
        "id": "QUES-081",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Co. Electricity Exclusivity",
        "difficulty": "Basic",
        "question_en": "In Energetic Co., why can electricity requirements NOT be met by natural gas or solar heating?",
        "question_vi": "Trong case Energetic Co., vì sao nhu cầu điện năng KHÔNG THỂ được đáp ứng bởi khí gas hoặc giàn năng lượng mặt trời?",
        "options_en": [
            "Because gas burners and solar thermal units provide only direct heat, not electricity generation equipment",
            "Because city ordinances make solar panels illegal",
            "Because natural gas freezes when running through electric wires",
            "Because electricity requirements are zero"
        ],
        "options_vi": [
            "Vì các đầu đốt khí gas và giàn nhiệt mặt trời chỉ tạo ra nhiệt năng trực tiếp, không có thiết bị phát điện",
            "Vì quy định của thành phố cấm lắp đặt tấm pin năng lượng mặt trời",
            "Vì khí gas tự nhiên sẽ bị đóng băng khi chạy qua dây dẫn điện",
            "Vì nhu cầu điện năng của tòa nhà bằng 0"
        ],
        "correct_answer": 0,
        "explanation_en": "The facility lacks gas generators or photovoltaic converters; thermal sources can only heat water or space.",
        "explanation_vi": "Hệ thống chỉ trang bị bình đun nhiệt mặt trời và lò sưởi gas, không có máy phát điện nên không thể dùng để chạy thiết bị điện."
    })

    questions.append({
        "id": "QUES-082",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Cost Table Structure",
        "difficulty": "Basic",
        "question_en": "What unit cost is entered for (Natural Gas -> Electricity) in the Energetic Co. cost table?",
        "question_vi": "Cước phí đơn vị nào được nhập cho ô (Khí Gas -> Điện năng) trong bảng chi phí của Energetic Co.?",
        "options_en": [
            "A prohibited symbol ('-') or an astronomically high Big-M cost ($999,999)",
            "$400",
            "$0",
            "-$100"
        ],
        "options_vi": [
            "Ký hiệu cấm ('-') hoặc một mức chi phí phạt Big-M cực lớn ($999,999)",
            "$400",
            "$0",
            "-$100"
        ],
        "correct_answer": 0,
        "explanation_en": "Infeasible pairs in the textbook tableau are marked '-' and modeled in software as Big-M penalty values.",
        "explanation_vi": "Ô kết hợp không khả thi được đánh dấu gạch ngang '-' trong bảng và được mô hình hóa bằng giá trị phạt Big-M trong phần mềm."
    })

    questions.append({
        "id": "QUES-083",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Solar Water Heating Cost",
        "difficulty": "Basic",
        "question_en": "According to Table 3.2 in the textbook, what is the unit cost of using the Solar Heater for Water Heating?",
        "question_vi": "Theo Bảng 3.2 trong giáo trình, đơn giá chi phí khi sử dụng Giàn mặt trời để Đun nước nóng là bao nhiêu?",
        "options_en": [
            "$300 per unit (the lowest among all options)",
            "$600 per unit",
            "$500 per unit",
            "$400 per unit"
        ],
        "options_vi": [
            "$300 trên mỗi đơn vị (mức rẻ nhất trong tất cả các phương án)",
            "$600 trên mỗi đơn vị",
            "$500 trên mỗi đơn vị",
            "$400 trên mỗi đơn vị"
        ],
        "correct_answer": 0,
        "explanation_en": "Table 3.2 lists unit cost of Solar -> Water Heating as $300, making it the most cost-effective heating option.",
        "explanation_vi": "Bảng 3.2 quy định chi phí Năng lượng mặt trời -> Đun nước nóng là $300, là phương án kinh tế nhất."
    })

    questions.append({
        "id": "QUES-084",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Gas Space Heating Cost",
        "difficulty": "Basic",
        "question_en": "According to Table 3.2 in the textbook, what is the unit cost of using Natural Gas for Space Heating?",
        "question_vi": "Theo Bảng 3.2 trong giáo trình, đơn giá chi phí khi sử dụng Khí Gas để Sưởi ấm không gian là bao nhiêu?",
        "options_en": [
            "$500 per unit",
            "$300 per unit",
            "$600 per unit",
            "$400 per unit"
        ],
        "options_vi": [
            "$500 trên mỗi đơn vị",
            "$300 trên mỗi đơn vị",
            "$600 trên mỗi đơn vị",
            "$400 trên mỗi đơn vị"
        ],
        "correct_answer": 0,
        "explanation_en": "Natural Gas space heating unit cost is listed as $500 per unit in Table 3.2.",
        "explanation_vi": "Bảng 3.2 quy định đơn giá sưởi ấm bằng khí gas tự nhiên là $500/đơn vị."
    })

    questions.append({
        "id": "QUES-085",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Excel Explicit Variable Elimination",
        "difficulty": "Basic",
        "question_en": "Instead of entering a large number M, how can an analyst strictly prohibit a route in modern Excel Solver?",
        "question_vi": "Thay vì nhập một số M lớn, một chuyên viên phân tích có thể ngăn cấm một tuyến đường trong Excel Solver bằng cách nào?",
        "options_en": [
            "Add an explicit constraint setting that specific decision variable equal to zero (x_ij = 0)",
            "Delete the column heading from the spreadsheet",
            "Change the font color of the cell to red",
            "Protect the worksheet with a password"
        ],
        "options_vi": [
            "Thêm một ràng buộc tường minh ép biến quyết định đó bằng đúng 0 (x_ij = 0)",
            "Xóa tên tiêu đề cột khỏi bảng tính",
            "Đổi màu chữ của ô tính sang màu đỏ",
            "Đặt mật khẩu khóa bảo vệ trang tính"
        ],
        "correct_answer": 0,
        "explanation_en": "Adding x_ij = 0 eliminates the variable from the basis, completely bypassing numerical scaling issues associated with Big-M.",
        "explanation_vi": "Đặt ràng buộc trực tiếp x_ij = 0 giúp triệt tiêu biến khỏi nghiệm mà không làm phát sinh sai số tính toán như số M lớn."
    })

    # Intermediate (Q086 - Q095)
    questions.append({
        "id": "QUES-086",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Optimal Solution",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for Energetic Co., how should the rooftop solar heater's 30-unit capacity be utilized?",
        "question_vi": "Trong phương án tối ưu của Energetic Co., 30 đơn vị công suất của giàn năng lượng mặt trời nên được phân bổ như thế nào?",
        "options_en": [
            "Allocate 10 units to Water Heating ($300) and 20 units to Space Heating ($400)",
            "Allocate all 30 units to Electricity ($400)",
            "Allocate 30 units to Space Heating and 0 to Water Heating",
            "Leave the solar heater completely idle"
        ],
        "options_vi": [
            "Phân bổ 10 đơn vị cho Đun nước nóng ($300) và 20 đơn vị cho Sưởi ấm không gian ($400)",
            "Phân bổ toàn bộ 30 đơn vị cho Điện năng ($400)",
            "Phân bổ 30 đơn vị cho Sưởi ấm và 0 đơn vị cho Đun nước nóng",
            "Để giàn năng lượng mặt trời hoàn toàn nhàn rỗi không sử dụng"
        ],
        "correct_answer": 0,
        "explanation_en": "Solar achieves its lowest cost at Water Heating ($300 vs $500 gas), consuming 10 units. Its remaining 20 units go to Space Heating ($400 vs $500 gas), fully exhausting its 30-unit capacity.",
        "explanation_vi": "Giàn mặt trời cấp đủ 10 đơn vị cho đun nước (giá $300 rẻ nhất), 20 đơn vị còn lại cấp cho sưởi ấm ($400 rẻ hơn gas $500), khai thác tối đa 30 đơn vị công suất."
    })

    questions.append({
        "id": "QUES-087",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Space Heating Allocation",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for Energetic Co., how is the remaining 10 units of Space Heating satisfied after solar exhausts its capacity?",
        "question_vi": "Trong phương án tối ưu của Energetic Co., 10 đơn vị Sưởi ấm còn lại được đáp ứng từ nguồn nào sau khi giàn mặt trời đã hết công suất?",
        "options_en": [
            "Purchased from Natural Gas at $500 per unit",
            "Purchased from Electricity at $600 per unit",
            "Left unheated so building occupants wear coats",
            "Supplied by a second imaginary solar panel"
        ],
        "options_vi": [
            "Mua từ nguồn Khí Gas tự nhiên với đơn giá $500 trên mỗi đơn vị",
            "Mua từ nguồn Điện lưới với đơn giá $600 trên mỗi đơn vị",
            "Không sưởi ấm để người trong tòa nhà tự mặc thêm áo khoác",
            "Cung cấp bởi một giàn pin mặt trời ảo thứ hai"
        ],
        "correct_answer": 0,
        "explanation_en": "Space heating requires 30 units. Solar covers 20 units. The remaining 10 units are supplied by Natural Gas at $500 (which is cheaper than Electricity at $600).",
        "explanation_vi": "Nhu cầu sưởi cần 30 đơn vị. Mặt trời đáp ứng 20 đơn vị. 10 đơn vị còn lại được cấp từ Khí gas ($500/đơn vị, rẻ hơn dùng điện $600)."
    })

    questions.append({
        "id": "QUES-088",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Energetic Total Optimal Cost",
        "difficulty": "Intermediate",
        "question_en": "What is the minimum total daily energy cost for Energetic Co. under the optimal allocation?",
        "question_vi": "Tổng chi phí năng lượng hàng ngày tối thiểu của công ty Energetic theo phương án tối ưu là bao nhiêu?",
        "options_en": [
            "$24,000 (Electricity: 20x$400=$8,000; Solar Water: 10x$300=$3,000; Solar Space: 20x$400=$8,000; Gas Space: 10x$500=$5,000)",
            "$36,000",
            "$15,000",
            "$30,000"
        ],
        "options_vi": [
            "$24,000 (Điện: 20x$400=$8,000; Mặt trời Nước: 10x$300=$3,000; Mặt trời Sưởi: 20x$400=$8,000; Gas Sưởi: 10x$500=$5,000)",
            "$36,000",
            "$15,000",
            "$30,000"
        ],
        "correct_answer": 0,
        "explanation_en": "Total Cost = (20 * 400) + (10 * 300) + (20 * 400) + (10 * 500) = 8,000 + 3,000 + 8,000 + 5,000 = $24,000 per day.",
        "explanation_vi": "Tổng chi phí tối thiểu = (20 x 400) + (10 x 300) + (20 x 400) + (10 x 500) = 8,000 + 3,000 + 8,000 + 5,000 = $24,000/ngày."
    })

    questions.append({
        "id": "QUES-089",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Physical Infeasibility vs Regulatory Infeasibility",
        "difficulty": "Intermediate",
        "question_en": "From a logistics perspective, what distinguishes a physical route prohibition from a regulatory route prohibition?",
        "question_vi": "Dưới góc độ logistics, điều gì phân biệt tuyến đường cấm do rào cản vật lý với tuyến đường cấm do rào cản pháp lý?",
        "options_en": [
            "Physical prohibitions involve geographical or infrastructure impossibilities (e.g., no pipeline); regulatory prohibitions involve legal bans, permits, or hazardous material restrictions",
            "Physical prohibitions only apply to bicycles",
            "Regulatory prohibitions can be ignored by truck drivers without penalty",
            "Physical prohibitions are always temporary during thunderstorms"
        ],
        "options_vi": [
            "Cấm vật lý liên quan đến rào cản địa lý hoặc thiếu hạ tầng (như không có đường ống dẫn); Cấm pháp lý liên quan đến lệnh cấm vận, giấy phép hoặc hạn chế vận chuyển chất độc hại",
            "Cấm vật lý chỉ áp dụng đối với phương tiện xe đạp",
            "Cấm pháp lý có thể được tài xế xe tải bỏ qua mà không bị phạt",
            "Cấm vật lý luôn mang tính tạm thời trong những lúc trời mưa dông"
        ],
        "correct_answer": 0,
        "explanation_en": "Physical barriers mean infrastructure does not exist; regulatory restrictions mean infrastructure exists but usage is legally prohibited (e.g., HazMat route rules).",
        "explanation_vi": "Rào cản vật lý là do không có hạ tầng kết nối; rào cản pháp lý là có đường nhưng luật cấm lưu thông (như xe chở hóa chất độc hại qua hầm đô thị)."
    })

    questions.append({
        "id": "QUES-090",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "HazMat Routing Constraints",
        "difficulty": "Intermediate",
        "question_en": "When hauling dangerous flammable chemicals in an ERP transportation planning system, why are certain highway segments prohibited?",
        "question_vi": "Khi vận chuyển hóa chất dễ cháy nổ trong hệ thống hoạch định vận tải ERP, vì sao một số đoạn đường cao tốc bị gắn cờ cấm lưu thông?",
        "options_en": [
            "Municipal HazMat regulations prohibit explosive shipments through tunnels, dense metropolitan centers, or protected watershed zones",
            "Highway toll operators refuse to make change for large cash bills",
            "Chemical trucks move too fast for state speed cameras",
            "Refineries prefer storing chemicals indefinitely in truck cabs"
        ],
        "options_vi": [
            "Quy định an toàn chất nguy hại (HazMat) cấm vận chuyển hàng cháy nổ qua hầm chui, trung tâm đô thị đông dân hoặc khu bảo tồn nguồn nước",
            "Nhân viên trạm thu phí từ chối trả lại tiền thừa mệnh giá lớn",
            "Xe chở hóa chất chạy quá nhanh so với camera bắn tốc độ",
            "Nhà máy lọc dầu thích lưu giữ hóa chất vô thời hạn trong cabin xe"
        ],
        "correct_answer": 0,
        "explanation_en": "HazMat routing constraints in enterprise Transportation Management (TM) ensure compliance with environmental and public safety statutes.",
        "explanation_vi": "Các quy định HazMat trong module ERP TM tự động loại trừ các cung đường qua hầm đô thị hoặc khu dân cư để tuân thủ an toàn môi trường."
    })

    questions.append({
        "id": "QUES-091",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Cold-Chain Fleet Compatibility",
        "difficulty": "Intermediate",
        "question_en": "In food or vaccine distribution, why would a standard ambient freight carrier be assigned a Big-M cost for temperature-sensitive shipments?",
        "question_vi": "Trong phân phối thực phẩm hoặc vắc-xin, vì sao một hãng vận tải thông thường lại bị gán chi phí Big-M đối với các đơn hàng nhạy cảm nhiệt độ?",
        "options_en": [
            "Ambient trucks lack refrigerated reefer units, causing spoilage; Big-M ensures only verified cold-chain carriers are assigned by the optimization engine",
            "Ambient truck drivers charge higher union wage rates",
            "Refrigerated goods weigh ten times more than ambient goods",
            "To force food wholesalers to purchase ice bags manually"
        ],
        "options_vi": [
            "Xe tải thông thường không có thùng đông lạnh (reefer), gây hỏng hàng; Big-M đảm bảo chỉ những xe chuyên dụng chuỗi lạnh mới được bộ giải phân bổ",
            "Tài xế xe tải thông thường đòi mức lương công đoàn cao hơn",
            "Hàng đông lạnh nặng gấp 10 lần so với hàng thông thường",
            "Để ép các nhà bán buôn thực phẩm phải tự đi mua túi đá lạnh thủ công"
        ],
        "correct_answer": 0,
        "explanation_en": "Carrier-material incompatibility is modeled via Big-M to prevent unequipped assets from being scheduled for specialized cargo.",
        "explanation_vi": "Sự không tương thích giữa phương tiện và đặc tính vật tư được mô hình hóa bằng Big-M để ngăn hệ thống điều phối xe thường chở hàng lạnh."
    })

    questions.append({
        "id": "QUES-092",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Geopolitical Customs Embargoes",
        "difficulty": "Intermediate",
        "question_en": "How does an international enterprise ERP system model trade embargoes between a specific manufacturing nation and an export destination?",
        "question_vi": "Hệ thống ERP của tập đoàn đa quốc gia mô hình hóa lệnh cấm vận thương mại giữa một quốc gia sản xuất và một thị trường xuất khẩu như thế nào?",
        "options_en": [
            "By setting the transportation arc cost to Big-M or disabling the trade lane in the Global Trade Services (GTS) compliance matrix",
            "By altering the currency symbol in the corporate general ledger",
            "By instructing factory managers to rename the finished product",
            "By shutting down the ERP database every time an order is entered"
        ],
        "options_vi": [
            "Bằng cách gán cước phí tuyến vận tải bằng Big-M hoặc vô hiệu hóa tuyến thương mại trong ma trận tuân thủ Global Trade Services (GTS)",
            "Bằng cách đổi ký hiệu tiền tệ trên sổ cái kế toán tập đoàn",
            "Bằng cách yêu cầu quản đốc nhà máy đổi tên gọi của thành phẩm",
            "Bằng cách tắt máy chủ ERP mỗi khi có đơn hàng mới được nhập"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP Global Trade Services (GTS) modules enforce statutory embargoes by blocking trade lanes or applying infinite penalties in distribution network optimizers.",
        "explanation_vi": "Phân hệ SAP GTS quản lý tuân thủ thương mại quốc tế bằng cách khóa tuyến đường hoặc áp hệ số phạt vô hạn trong thuật toán tối ưu mạng lưới."
    })

    questions.append({
        "id": "QUES-093",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Carrier Weight Bridge Limits",
        "difficulty": "Intermediate",
        "question_en": "A rural highway bridge has a strict gross vehicle weight restriction of 15 tons. In the ERP logistics system, how is this handled for 30-ton heavy trucks?",
        "question_vi": "Một cây cầu đường bộ nông thôn có giới hạn tải trọng xe nghiêm ngặt là 15 tấn. Trong hệ thống ERP logistics, việc này được xử lý thế nào đối với xe 30 tấn?",
        "options_en": [
            "The 30-ton vehicle profile is prohibited from routing across that bridge segment by assigning an infinite cost penalty to that graph edge",
            "The truck is instructed to speed up to cross the bridge faster",
            "The bridge capacity is artificially overwritten in the state database",
            "The driver is instructed to unload half the cargo into the river"
        ],
        "options_vi": [
            "Hồ sơ xe 30 tấn bị cấm lưu thông qua đoạn cầu đó bằng cách gán chi phí phạt vô hạn cho cạnh đồ thị mạng lưới tương ứng",
            "Hướng dẫn tài xế tăng tốc độ để chạy qua cầu thật nhanh",
            "Tự ý sửa lại tải trọng cây cầu trên hệ thống dữ liệu quốc gia",
            "Bắt tài xế bốc dỡ một nửa số hàng vứt xuống sông"
        ],
        "correct_answer": 0,
        "explanation_en": "Vehicle-infrastructure attribute constraints prevent dispatching vehicles whose axle weight exceeds roadway or bridge physical ratings.",
        "explanation_vi": "Ràng buộc tải trọng cầu đường trong ERP TM ngăn chặn việc điều phối các phương tiện vượt quá giới hạn an toàn công trình."
    })

    questions.append({
        "id": "QUES-094",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Sensitivity of Big-M Basis",
        "difficulty": "Intermediate",
        "question_en": "If a transportation simplex report displays a decision variable with a non-zero value in a cell that was assigned a Big-M cost, what does this indicate?",
        "question_vi": "Nếu báo cáo kết quả đơn hình vận tải hiển thị một biến quyết định có giá trị khác 0 tại một ô đã bị gán chi phí Big-M, điều này báo hiệu điều gì?",
        "options_en": [
            "The problem is completely infeasible; the model has no combination of valid open routes that can satisfy all demands simultaneously",
            "The model has found a super-cheap miracle discount",
            "The computer memory has doubled its capacity",
            "All truck drivers will receive bonus payments"
        ],
        "options_vi": [
            "Bài toán hoàn toàn không tồn tại nghiệm khả thi; mô hình không thể tìm được tập hợp tuyến đường hợp lệ nào để đáp ứng đồng thời mọi nhu cầu",
            "Mô hình đã phát hiện ra một mức chiết khấu giá rẻ bất ngờ",
            "Bộ nhớ máy tính đã tăng gấp đôi dung lượng lưu trữ",
            "Tất cả tài xế xe tải sẽ nhận được tiền thưởng năng suất"
        ],
        "correct_answer": 0,
        "explanation_en": "If Big-M appears in the final basis with a positive value, it proves no physical solution exists without violating at least one mandatory constraint.",
        "explanation_vi": "Nếu biến Big-M vẫn xuất hiện dương trong nghiệm cuối cùng, điều đó chứng minh bài toán bị mâu thuẫn ràng buộc và hoàn toàn vô nghiệm."
    })

    questions.append({
        "id": "QUES-095",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Dual Value of Prohibited Route",
        "difficulty": "Intermediate",
        "question_en": "What does the reduced cost of a prohibited route cell tell a logistics executive?",
        "question_vi": "Chi phí giảm (Reduced Cost) của một ô tuyến đường bị cấm cho nhà quản lý logistics biết điều gì?",
        "options_en": [
            "How much the shipping cost along that lane would need to drop before it would ever become economically attractive to open that route",
            "The speed limit on that highway",
            "The exact price of diesel fuel at the destination city",
            "The number of trucks that broke down last year"
        ],
        "options_vi": [
            "Cước phí trên tuyến đó cần phải giảm bao nhiêu trước khi việc mở lại tuyến đường đó trở nên hấp dẫn về mặt kinh tế",
            "Tốc độ tối đa cho phép lưu thông trên tuyến cao tốc đó",
            "Giá dầu diesel chính xác tại thành phố điểm đến",
            "Số lượng xe tải đã bị hỏng hóc trong năm vừa qua"
        ],
        "correct_answer": 0,
        "explanation_en": "Reduced cost indicates the hurdle rate: the amount by which an arc's unit cost must decrease to enter the optimal basic solution.",
        "explanation_vi": "Reduced cost phản ánh rào cản kinh tế: cước phí vận chuyển trên tuyến đó phải giảm bao nhiêu tiền thì tuyến đường đó mới bắt đầu có lợi để đưa vào khai thác."
    })

    # Advanced (Q096 - Q100)
    questions.append({
        "id": "QUES-096",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "BA Exception Handling for Infeasible Runs",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is designing error-handling logic for an automated ERP transportation optimizer. If the LP engine returns an infeasible status due to route prohibitions, what user experience should the system trigger?",
        "question_vi": "Một Business Analyst đang thiết kế quy trình xử lý ngoại lệ cho bộ tối ưu vận tải ERP tự động. Nếu bộ giải trả về trạng thái vô nghiệm do các tuyến đường cấm, hệ thống cần kích hoạt trải nghiệm người dùng nào?",
        "options_en": [
            "Display an actionable alert identifying the specific bottleneck constraints and unserved destinations, and prompt the dispatcher to authorize emergency carrier overrides",
            "Silently crash the user interface without any log notification",
            "Randomly assign deliveries to uncertified carriers without notification",
            "Delete all customer sales orders from the database"
        ],
        "options_vi": [
            "Hiển thị cảnh báo trực quan chỉ rõ các nút thắt cổ chai và các điểm đến không thể phục vụ, đồng thời hướng dẫn điều phối viên phê duyệt các hãng vận tải khẩn cấp thay thế",
            "Âm thầm làm sập giao diện người dùng mà không lưu lại nhật ký lỗi",
            "Tự ý gán đơn hàng cho các nhà xe không đạt chuẩn mà không thông báo",
            "Tự động xóa sạch toàn bộ các đơn hàng bán của khách hàng khỏi hệ thống"
        ],
        "correct_answer": 0,
        "explanation_en": "Professional BA error workflows isolate root-cause bottlenecks (e.g., IIS - Irreducible Inconsistent Subsystems) and guide users to operational remedies.",
        "explanation_vi": "Thiết kế nghiệp vụ chuẩn xác phải cô lập nguyên nhân gây vô nghiệm và cung cấp quy trình phê duyệt ngoại lệ (override) rõ ràng cho nhân viên vận hành."
    })

    questions.append({
        "id": "QUES-097",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Dynamic Lane Blockage in Real-Time ERP",
        "difficulty": "Advanced",
        "question_en": "During a severe winter blizzard, three interstate mountain passes are closed. How should an advanced ERP Transportation Management system react dynamically?",
        "question_vi": "Trong một trận bão tuyết mùa đông nghiêm trọng, ba con đèo qua núi bị phong tỏa. Hệ thống ERP TM tiên tiến cần phản ứng linh hoạt như thế nào theo thời gian thực?",
        "options_en": [
            "Ingest real-time telematics/GIS disruption feeds, dynamically flag the affected arcs as prohibited (M-cost), and instantly re-run the network LP to re-route in-transit shipments",
            "Instruct drivers to abandon their trucks in the snow and walk home",
            "Wait until the fiscal year ends before updating any delivery schedules",
            "Pretend the blizzard does not exist and hold dispatchers personally liable"
        ],
        "options_vi": [
            "Tiếp nhận luồng dữ liệu GIS/viễn thông thời gian thực, tự động gắn cờ cấm (M-cost) cho các cung đường bị ảnh hưởng và chạy lại thuật toán LP để lập lộ trình vòng thay thế",
            "Hướng dẫn tài xế bỏ xe lại trong tuyết và đi bộ về nhà",
            "Chờ đến khi kết thúc năm tài chính mới cập nhật lại lịch trình giao hàng",
            "Coi như trận bão tuyết không tồn tại và quy trách nhiệm cá nhân cho tài xế"
        ],
        "correct_answer": 0,
        "explanation_en": "Event-driven supply chain management integrates real-time GIS telemetry to update network cost graphs and trigger dynamic re-optimization.",
        "explanation_vi": "Hệ thống ERP điều hành chuỗi cung ứng theo sự kiện (event-driven) tự động nhận cảnh báo thời tiết để cập nhật lại ma trận cước và tái tối ưu lộ trình tức thời."
    })

    questions.append({
        "id": "QUES-098",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Combinatorial Explosion with Route Exclusions",
        "difficulty": "Advanced",
        "question_en": "When multiple conditional route exclusions are introduced (e.g., 'If Route A is used, Route B cannot be used'), why can pure LP no longer be used?",
        "question_vi": "Khi xuất hiện các ràng buộc loại trừ có điều kiện (ví dụ: 'Nếu đã chọn Tuyến A thì không được chọn Tuyến B'), vì sao không thể dùng quy hoạch tuyến tính thuần túy?",
        "options_en": [
            "Conditional logic requires binary indicator variables (y in {0, 1}), converting the problem into a Mixed-Integer Linear Program (MILP)",
            "Linear programming formulas become physically illegal under maritime law",
            "The objective function turns into a negative exponential logarithm",
            "There are not enough letters in the alphabet to represent the variables"
        ],
        "options_vi": [
            "Logic điều kiện đòi hỏi các biến chỉ thị nhị phân (y thuộc {0, 1}), biến bài toán thành Quy hoạch Tuyến tính Nguyên Hỗn hợp (MILP)",
            "Các công thức quy hoạch tuyến tính bị luật hàng hải quốc tế nghiêm cấm",
            "Hàm mục tiêu chuyển thành hàm logarit lũy thừa âm",
            "Bảng chữ cái không đủ ký tự để biểu diễn các biến số"
        ],
        "correct_answer": 0,
        "explanation_en": "Conditional 'either-or' constraints violate continuous convexity, requiring 0-1 binary decision variables and branch-and-cut MILP solvers.",
        "explanation_vi": "Ràng buộc điều kiện loại trừ vi phạm tính liên tục lồi, đòi hỏi biến nguyên nhị phân 0-1 và phải giải bằng thuật toán nhánh cận (Branch-and-Cut)."
    })

    questions.append({
        "id": "QUES-099",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "Dual Degeneracy under Artificial Penalties",
        "difficulty": "Advanced",
        "question_en": "How can an operations research analyst mathematically prove that an optimal LP solution is unaffected by the numerical choice of M in the Big-M method?",
        "question_vi": "Làm thế nào một chuyên gia phân tích có thể chứng minh về mặt toán học rằng nghiệm tối ưu LP không bị ảnh hưởng bởi giá trị cụ thể của số M được chọn?",
        "options_en": [
            "By verifying that all decision variables associated with M have an optimal value of zero (x_ij* = 0) and their dual reduced costs remain strictly positive",
            "By asking the software vendor for a written certificate of accuracy",
            "By solving the model on three different computer monitor brands",
            "By calculating the average salary of the dispatching staff"
        ],
        "options_vi": [
            "Bằng cách kiểm tra thấy toàn bộ các biến liên quan đến M đều có nghiệm tối ưu bằng 0 (x_ij* = 0) và chi phí giảm đối ngẫu của chúng mang giá trị dương nghiêm ngặt",
            "Bằng cách yêu cầu nhà cung cấp phần mềm cấp chứng thư kiểm định",
            "Bằng cách giải mô hình trên ba màn hình máy tính của các hãng khác nhau",
            "Bằng cách tính mức lương trung bình của đội ngũ nhân viên điều phối"
        ],
        "correct_answer": 0,
        "explanation_en": "If x_ij* = 0 and reduced cost (c_ij - u_i - v_j) > 0, the prohibited arc is non-basic and has no influence on the primary basis.",
        "explanation_vi": "Khi biến cấm nhận giá trị bằng 0 và chi phí giảm dương nghiêm ngặt, biến này nằm ngoài cơ sở tối ưu và không làm sai lệch các nghiệm còn lại."
    })

    questions.append({
        "id": "QUES-100",
        "exam_id": "EXAM-04",
        "chapter_id": "chap-02",
        "topic": "ERP Regulatory Traceability & Compliance",
        "difficulty": "Advanced",
        "question_en": "In pharmaceutical logistics, why must an ERP audit trail capture the rationale whenever a route prohibition rule is deactivated or modified by a planner?",
        "question_vi": "Trong logistics dược phẩm, vì sao vết kiểm toán ERP bắt buộc phải lưu lại lý do mỗi khi một quy tắc cấm tuyến bị điều phối viên tắt bỏ hoặc sửa đổi?",
        "options_en": [
            "To satisfy FDA/GxP regulatory compliance proving that product integrity, cold-chain continuity, and approved transit corridors were not compromised",
            "To deduct money from the planner's annual holiday bonus",
            "To notify local police that a delivery truck has left the warehouse",
            "To automatically order new tires from Eversafe"
        ],
        "options_vi": [
            "Để đáp ứng tuân thủ quy định của cơ quan dược phẩm (FDA/GxP), chứng minh tính toàn vẹn của thuốc và hành lang vận chuyển được phê duyệt không bị xâm phạm",
            "Để trừ tiền thưởng nghỉ lễ cuối năm của nhân viên điều phối",
            "Để báo cảnh sát địa phương rằng một chiếc xe tải vừa rời khỏi kho",
            "Để tự động đặt mua lốp xe mới từ hãng Eversafe"
        ],
        "correct_answer": 0,
        "explanation_en": "Pharma GxP and chain-of-custody laws require immutable electronic records explaining why transportation routing parameters were manually overridden.",
        "explanation_vi": "Tiêu chuẩn GxP ngành dược bắt buộc phải ghi lại lý do can thiệp quy trình vận chuyển để đảm bảo thuốc không bị vận chuyển qua các tuyến không an toàn."
    })

    return questions
