# -*- coding: utf-8 -*-
# EXAM 06: Scientific Inventory Management & 4 Cost Components (chap-04)
# 25 Questions: Q126 to Q150 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q126 - Q135)
    questions.append({
        "id": "QUES-126",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Scientific Inventory Management Steps",
        "difficulty": "Basic",
        "question_en": "According to the textbook (Slide 76), what are the three sequential steps managers use in scientific inventory management?",
        "question_vi": "Theo giáo trình (Slide 76), ba bước tuần tự mà các nhà quản lý áp dụng trong Quản trị Tồn kho Khoa học là gì?",
        "options_en": [
            "1. Formulate a mathematical model describing inventory behavior; 2. Derive an optimal inventory policy; 3. Use an information processing system to track levels and signal orders",
            "1. Count inventory by hand; 2. Guess the reorder point; 3. Blame warehouse workers for stockouts",
            "1. Order maximum warehouse capacity; 2. Shut down the warehouse; 3. Declare bankruptcy",
            "1. Call suppliers daily; 2. Pay cash for all goods; 3. Store goods in outdoor parking lots"
        ],
        "options_vi": [
            "1. Thiết lập mô hình toán học mô tả hành vi tồn kho; 2. Tìm ra chính sách tồn kho tối ưu; 3. Sử dụng hệ thống xử lý thông tin để theo dõi mức tồn kho và phát tín hiệu đặt hàng",
            "1. Đếm hàng tồn kho thủ công; 2. Đoán mò điểm đặt hàng lại; 3. Đổ lỗi cho nhân viên kho khi hết hàng",
            "1. Đặt mua đầy ắp diện tích kho; 2. Đóng cửa nhà kho; 3. Tuyên bố phá sản doanh nghiệp",
            "1. Gọi điện cho nhà cung cấp mỗi ngày; 2. Trả tiền mặt cho mọi lô hàng; 3. Chất hàng ngoài bãi đỗ xe"
        ],
        "correct_answer": 0,
        "explanation_en": "Slide 76 outlines the 3 steps of scientific inventory management: mathematical modeling, analytical policy derivation, and computerized ERP execution.",
        "explanation_vi": "Giáo trình nêu rõ 3 bước: Mô hình hóa toán học, Tìm chính sách tối ưu bằng giải tích, và Ứng dụng hệ thống ERP để theo dõi và tự động phát lệnh đặt hàng."
    })

    questions.append({
        "id": "QUES-127",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Acquisition Cost Definition",
        "difficulty": "Basic",
        "question_en": "What is the Acquisition Cost (c) in inventory models?",
        "question_vi": "Chi phí Thu mua / Giá vốn (Acquisition Cost - c) trong các mô hình tồn kho là gì?",
        "options_en": [
            "The direct cost paid to replenish each unit of inventory, whether through purchasing from a vendor or manufacturing internally",
            "The annual rent paid to lease the warehouse building",
            "The property tax assessed by the municipal city government",
            "The electricity bill for operating warehouse fluorescent lights"
        ],
        "options_vi": [
            "Chi phí trực tiếp chi trả để bổ sung mỗi đơn vị hàng tồn kho, cho dù mua ngoài từ nhà cung cấp hay tự sản xuất nội bộ",
            "Tiền thuê mặt bằng nhà kho chi trả hàng năm",
            "Thuế tài sản do chính quyền thành phố địa phương thu",
            "Tiền điện chi trả cho hệ thống đèn chiếu sáng trong kho"
        ],
        "correct_answer": 0,
        "explanation_en": "Acquisition cost c is the unit purchase price or manufacturing cost directly incurred to acquire a single unit.",
        "explanation_vi": "Chi phí thu mua c là đơn giá mua hàng từ nhà cung cấp hoặc chi phí biến đổi xuất xưởng để sản xuất ra một đơn vị sản phẩm."
    })

    questions.append({
        "id": "QUES-128",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Setup / Ordering Cost Definition",
        "difficulty": "Basic",
        "question_en": "What is Setup Cost / Ordering Cost (K) in inventory management?",
        "question_vi": "Chi phí Thiết lập / Đặt hàng (Setup Cost - K) trong quản trị tồn kho là gì?",
        "options_en": [
            "The fixed administrative, processing, and machine recalibration cost incurred each time an order is placed, regardless of order size",
            "The cost of buying 1,000 units of physical merchandise",
            "The monthly salary paid to the company chief executive",
            "The interest rate charged by commercial investment banks"
        ],
        "options_vi": [
            "Chi phí cố định về thủ tục hành chính, xử lý đơn và hiệu chỉnh máy móc phát sinh cho mỗi lần đặt hàng, hoàn toàn không phụ thuộc vào quy mô lô hàng",
            "Số tiền bỏ ra để mua 1,000 đơn vị hàng hóa vật lý",
            "Tiền lương hàng tháng chi trả cho giám đốc điều hành công ty",
            "Lãi suất vay vốn do các ngân hàng thương mại áp dụng"
        ],
        "correct_answer": 0,
        "explanation_en": "Setup cost K is a fixed lump-sum expense per replenishment event, covering PO generation, machine changeovers, and receiving dock inspection.",
        "explanation_vi": "Chi phí thiết lập K phát sinh trọn gói cho mỗi lần đặt hàng (PO, cước xe cố định, kiểm tra nghiệm thu, cài đặt máy), không đổi theo số lượng."
    })

    questions.append({
        "id": "QUES-129",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Holding Cost Definition",
        "difficulty": "Basic",
        "question_en": "What is Holding Cost / Carrying Cost (h) in inventory modeling?",
        "question_vi": "Chi phí Lưu kho / Tồn trữ (Holding Cost - h) trong mô hình tồn kho là gì?",
        "options_en": [
            "The total cost associated with holding one unit of inventory in storage for a specific time period (typically one year)",
            "The price charged by delivery trucks to ship goods to retail stores",
            "The penalty fee paid when a delivery arrives three days early",
            "The legal fee paid to incorporate a new business subsidiary"
        ],
        "options_vi": [
            "Toàn bộ chi phí phát sinh để giữ một đơn vị hàng hóa trong kho trong một khoảng thời gian xác định (thường là một năm)",
            "Cước phí xe tải vận chuyển hàng hóa tới các cửa hàng bán lẻ",
            "Khoản tiền phạt phải trả khi một chuyến giao hàng đến sớm trước 3 ngày",
            "Phí dịch vụ pháp lý để thành lập một công ty con mới"
        ],
        "correct_answer": 0,
        "explanation_en": "Holding cost h encompasses capital opportunity cost, warehouse storage, insurance, property taxes, shrinkage, and obsolescence per unit per year.",
        "explanation_vi": "Chi phí lưu kho h bao gồm chi phí vốn bị ứ đọng, tiền thuê kho, bảo hiểm, hao hụt, hư hỏng và lỗi thời tính trên 1 đơn vị/năm."
    })

    questions.append({
        "id": "QUES-130",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Shortage Cost Definition",
        "difficulty": "Basic",
        "question_en": "What is Shortage Cost / Stockout Penalty (p) in inventory models?",
        "question_vi": "Chi phí Thiếu hụt / Phạt hết hàng (Shortage Cost - p) trong mô hình tồn kho là gì?",
        "options_en": [
            "The economic penalty incurred when customer demand occurs but no inventory is available to fulfill it immediately",
            "The discount offered by suppliers for buying in bulk quantities",
            "The cost of discarding expired milk into the trash bin",
            "The fee paid to register a patent with the government"
        ],
        "options_vi": [
            "Tổn thất kinh tế phát sinh khi xuất hiện nhu cầu của khách hàng nhưng không có sẵn hàng trong kho để đáp ứng ngay lập tức",
            "Mức chiết khấu do nhà cung cấp đưa ra khi mua hàng số lượng lớn",
            "Chi phí tiêu hủy các hộp sữa hết hạn sử dụng vào thùng rác",
            "Phí đăng ký bằng sáng chế với cơ quan sở hữu trí tuệ"
        ],
        "correct_answer": 0,
        "explanation_en": "Shortage cost p captures lost sales margin, customer goodwill erosion, delayed cash flow, and emergency expediting expenses.",
        "explanation_vi": "Chi phí thiếu hụt p phản ánh thiệt hại mất uy tín thương hiệu, tiền phạt trễ hạn hợp đồng, mất khách hàng và chi phí vận chuyển hỏa tốc."
    })

    questions.append({
        "id": "QUES-131",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Capital Opportunity Cost Concept",
        "difficulty": "Basic",
        "question_en": "Why is the Cost of Capital Tied Up in Inventory considered an 'Opportunity Cost'?",
        "question_vi": "Vì sao Chi phí Vốn Ứ đọng trong Tồn kho được xem là một 'Chi phí Cơ hội' (Opportunity Cost)?",
        "options_en": [
            "Because money tied up in unsold inventory cannot be invested elsewhere to earn an attractive financial return or reduce debt interest",
            "Because banks give away free money to companies that have zero inventory",
            "Because inventory automatically turns into cash overnight",
            "Because company shareholders do not care about financial returns"
        ],
        "options_vi": [
            "Vì số tiền bị chôn trong hàng tồn kho chưa bán được không thể đem đi đầu tư vào cơ hội khác để sinh lời hoặc trả bớt lãi vay ngân hàng",
            "Vì các ngân hàng tặng tiền miễn phí cho các công ty không có hàng tồn kho",
            "Vì hàng tồn kho sẽ tự động chuyển hóa thành tiền mặt sau một đêm",
            "Vì các cổ đông công ty không quan tâm đến tỷ suất sinh lời tài chính"
        ],
        "correct_answer": 0,
        "explanation_en": "Capital invested in stock incurs an opportunity cost: the foregone return that could have been earned had that capital been deployed in alternative corporate investments.",
        "explanation_vi": "Vốn bị giam trong kho làm mất đi cơ hội kinh doanh khác; lãi suất kỳ vọng hoặc chi phí lãi vay bị mất chính là chi phí cơ hội của đồng vốn."
    })

    questions.append({
        "id": "QUES-132",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Cost of Capital Rate",
        "difficulty": "Basic",
        "question_en": "In the Atlantic Coast Tire Corp. (ACT) case, what percentage rate did the Comptroller estimate for the cost of capital tied up in tire inventory?",
        "question_vi": "Trong case Atlantic Coast Tire Corp. (ACT), Giám đốc Tài chính (Comptroller) đã ước tính tỷ lệ chi phí vốn ứ đọng trong kho lốp xe là bao nhiêu %?",
        "options_en": [
            "15 percent per annum",
            "21 percent per annum",
            "6 percent per annum",
            "1 percent per annum"
        ],
        "options_vi": [
            "15% mỗi năm",
            "21% mỗi năm",
            "6% mỗi năm",
            "1% mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "The ACT case explicitly states: 'The ACT Comptroller estimates that the cost of capital tied up is 15 percent per annum.'",
        "explanation_vi": "Hồ sơ case study ACT nêu rõ: Giám đốc Tài chính ước lượng chi phí vốn bị ứ đọng là 15% mỗi năm."
    })

    questions.append({
        "id": "QUES-133",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Non-Capital Holding Costs",
        "difficulty": "Basic",
        "question_en": "In the ACT case, what percentage rate was estimated for warehouse leasing, insurance, security personnel, and property taxes?",
        "question_vi": "Trong case ACT, tỷ lệ ước tính cho các chi phí thuê kho bãi, bảo hiểm, bảo vệ và thuế tài sản là bao nhiêu %?",
        "options_en": [
            "6 percent of average inventory value per year",
            "15 percent per year",
            "21 percent per year",
            "50 percent per year"
        ],
        "options_vi": [
            "6% giá trị tồn kho bình quân mỗi năm",
            "15% mỗi năm",
            "21% mỗi năm",
            "50% mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "The case estimates physical storage, insurance, personnel, and taxes at 6% of average inventory valuation.",
        "explanation_vi": "Các chi phí thuê kho bãi, bảo hiểm cháy nổ, nhân sự bảo vệ và thuế tài sản được ước tính bằng 6% giá trị tồn kho bình quân."
    })

    questions.append({
        "id": "QUES-134",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Total Holding Cost Rate",
        "difficulty": "Basic",
        "question_en": "By adding the cost of capital (15%) and physical storage/taxes (6%), what is ACT's total annual holding cost percentage rate I?",
        "question_vi": "Cộng chi phí cơ hội vốn (15%) và chi phí kho bãi/thuế (6%), tỷ lệ chi phí tồn trữ hàng năm tổng hợp I của ACT là bao nhiêu %?",
        "options_en": [
            "21 percent per year (15% + 6%)",
            "9 percent per year",
            "30 percent per year",
            "15 percent per year"
        ],
        "options_vi": [
            "21% mỗi năm (15% + 6%)",
            "9% mỗi năm",
            "30% mỗi năm",
            "15% mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Total holding rate I = 15% capital + 6% storage/insurance = 21% per year.",
        "explanation_vi": "Tổng tỷ lệ chi phí tồn trữ hàng năm I = 15% chi phí vốn + 6% chi phí kho/bảo hiểm = 21%/năm."
    })

    questions.append({
        "id": "QUES-135",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Unit Holding Cost Calculation",
        "difficulty": "Basic",
        "question_en": "With a tire purchase price of $20 and a 21% annual carrying rate, what is ACT's unit annual holding cost h?",
        "question_vi": "Với đơn giá mua lốp là $20 và tỷ lệ tồn trữ hàng năm là 21%, chi phí lưu kho đơn vị h của ACT là bao nhiêu?",
        "options_en": [
            "$4.20 per tire per year (0.21 x $20.00)",
            "$20.00 per year",
            "$1.50 per year",
            "$0.21 per year"
        ],
        "options_vi": [
            "$4.20 trên mỗi lốp mỗi năm (0.21 x $20.00)",
            "$20.00 mỗi năm",
            "$1.50 mỗi năm",
            "$0.21 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Unit holding cost h = I * c = 0.21 * $20.00 = $4.20 per tire per year.",
        "explanation_vi": "Chi phí tồn trữ đơn vị h = I x c = 0.21 x $20.00 = $4.20/lốp/năm."
    })

    # Intermediate (Q136 - Q145)
    questions.append({
        "id": "QUES-136",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Order Setup Cost Components",
        "difficulty": "Intermediate",
        "question_en": "How is ACT's total setup cost per order K = $115 derived from employee labor and overhead?",
        "question_vi": "Chi phí đặt hàng K = $115 cho mỗi lần đặt của ACT được cấu thành từ nhân công và chi phí quản lý như thế nào?",
        "options_en": [
            "Labor: 6 hours at $15/hr = $90, plus direct administrative overhead of $25 ($90 + $25 = $115)",
            "Truck fuel: $100 plus driver lunch: $15",
            "Computer software license fee of $115 per day",
            "Fax machine telephone long-distance call charges of $115"
        ],
        "options_vi": [
            "Nhân công: 6 giờ làm việc với mức lương $15/giờ = $90, cộng với chi phí quản lý hành chính văn phòng $25 ($90 + $25 = $115)",
            "Tiền xăng xe tải: $100 cộng với bữa trưa của tài xế: $15",
            "Phí bản quyền phần mềm máy tính $115 mỗi ngày",
            "Cước phí điện thoại gọi đường dài máy fax $115"
        ],
        "correct_answer": 0,
        "explanation_en": "Order processing labor (PO creation, receiving, inspection, data entry, payment) takes 6 hours @ $15 ($90) + overhead ($25) = $115.",
        "explanation_vi": "Quy trình đặt hàng tốn 6 giờ lao động (mức lương $15/giờ) = $90 cộng chi phí quản lý văn phòng $25, tổng cộng K = $115/lần đặt."
    })

    questions.append({
        "id": "QUES-137",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Shortage Cost Mechanism",
        "difficulty": "Intermediate",
        "question_en": "In the ACT case, why is the unit shortage cost estimated at $7.50 per tire short per year rather than an infinite lost sale?",
        "question_vi": "Trong case ACT, vì sao chi phí thiếu hàng lại được ước tính là $7.50/lốp nợ/năm thay vì tính như một đơn hàng bị mất vĩnh viễn?",
        "options_en": [
            "Because retail dealers are willing to wait for tires to arrive (backorders), but ACT incurs customer goodwill loss, discounts to placate delays, and extra clerical expediting",
            "Because retail tire stores immediately go out of business",
            "Because the state government fines wholesalers $7.50 for every missing tire",
            "Because Eversafe refunds ACT $7.50 for every late order"
        ],
        "options_vi": [
            "Vì các đại lý bán lẻ sẵn sàng chờ hàng về (đơn hàng nợ - backorders), nhưng ACT phải chịu tổn thất uy tín, giảm giá xoa dịu khách và tốn công theo dõi đơn",
            "Vì các đại lý bán lẻ sẽ phá sản ngay lập tức nếu thiếu lốp",
            "Vì chính quyền bang phạt nhà bán buôn $7.50 cho mỗi chiếc lốp bị thiếu",
            "Vì Eversafe hoàn lại cho ACT $7.50 cho mỗi đơn hàng bị trễ"
        ],
        "correct_answer": 0,
        "explanation_en": "Under backordering, sales are delayed rather than lost, but late delivery penalties, clerical overhead, and customer dissatisfaction accumulate at $7.50/unit-year.",
        "explanation_vi": "Khách hàng chấp nhận hoãn đơn (backorder), nhưng doanh nghiệp phải chịu chi phí chăm sóc đặc biệt, giảm giá giữ chân và quản lý đơn tồn đọng với mức $7.50/lốp/năm."
    })

    questions.append({
        "id": "QUES-138",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Saw-Toothed Inventory Cycle",
        "difficulty": "Intermediate",
        "question_en": "Why does inventory over time follow a 'saw-toothed' triangular pattern under basic EOQ assumptions?",
        "question_vi": "Vì sao biểu đồ mức tồn kho theo thời gian lại có dạng 'răng cưa' hình tam giác trong các giả định của mô hình EOQ cơ bản?",
        "options_en": [
            "Inventory jumps instantly from 0 to Q when a batch arrives, and then depletes at a steady, continuous constant demand rate down to 0",
            "Because warehouse workers saw lumber inside the facility",
            "Because seasonal weather patterns cause abrupt demand swings",
            "Because suppliers ship random quantities on random calendar days"
        ],
        "options_vi": [
            "Tồn kho nhảy vọt tức thì từ 0 lên Q khi lô hàng mới nhập kho, sau đó giảm dần đều đặn theo tốc độ nhu cầu không đổi cho đến khi chạm mức 0",
            "Vì công nhân nhà kho đang cưa gỗ bên trong cơ sở",
            "Vì thời tiết thay đổi theo mùa làm nhu cầu đảo chiều đột ngột",
            "Vì nhà cung cấp giao các số lượng ngẫu nhiên vào các ngày ngẫu nhiên"
        ],
        "correct_answer": 0,
        "explanation_en": "Instantaneous replenishment creates vertical jumps (+Q), while constant continuous demand causes straight downward sloping consumption (-d*t).",
        "explanation_vi": "Nhập hàng một lần làm tồn kho tăng vọt thẳng đứng (+Q), sau đó hàng xuất bán đều đặn tạo thành đường dốc thẳng đứng xuống 0."
    })

    questions.append({
        "id": "QUES-139",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Average Inventory Calculation",
        "difficulty": "Intermediate",
        "question_en": "Under the saw-toothed cycle with zero minimum stock and maximum stock Q, why is the average inventory level exactly Q / 2?",
        "question_vi": "Trong chu kỳ răng cưa có tồn kho tối thiểu bằng 0 và tồn kho tối đa bằng Q, vì sao mức tồn kho bình quân lại bằng đúng Q / 2?",
        "options_en": [
            "Because inventory drops linearly at a constant rate, making the average of the initial peak (Q) and final trough (0) equal to (Q + 0) / 2 = Q / 2",
            "Because half the inventory is stolen by warehouse mice",
            "Because accounting regulations mandate dividing all assets by 2",
            "Because retail dealers only pay for 50% of the ordered tires"
        ],
        "options_vi": [
            "Vì tồn kho giảm tuyến tính với tốc độ không đổi, nên giá trị trung bình giữa đỉnh bắt đầu (Q) và đáy kết thúc (0) bằng đúng (Q + 0) / 2 = Q / 2",
            "Vì một nửa số hàng tồn kho bị chuột trong kho tha mất",
            "Vì chuẩn mực kế toán bắt buộc phải chia đôi mọi tài sản",
            "Vì các đại lý bán lẻ chỉ thanh toán 50% tiền mua lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "The area under a linear consumption triangle of base T and height Q is (1/2)*Q*T. Dividing by cycle length T gives an average inventory of Q/2.",
        "explanation_vi": "Diện tích tam giác tiêu thụ đáy T và chiều cao Q là (1/2)*Q*T. Chia cho chu kỳ T cho mức tồn kho bình quân hình học là Q/2."
    })

    questions.append({
        "id": "QUES-140",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Annual Setup Cost Formula",
        "difficulty": "Intermediate",
        "question_en": "What is the mathematical expression for Total Annual Setup Cost as a function of order batch size Q and annual demand D?",
        "question_vi": "Biểu thức toán học cho Tổng Chi phí Đặt hàng Hàng năm dưới dạng hàm của kích thước lô Q và nhu cầu năm D là gì?",
        "options_en": [
            "Annual Setup Cost = K * (D / Q), where (D / Q) represents the number of replenishment orders placed per year",
            "Annual Setup Cost = K * Q * D",
            "Annual Setup Cost = (K + D) / Q",
            "Annual Setup Cost = K * (Q / 2)"
        ],
        "options_vi": [
            "Chi phí Đặt hàng Hàng năm = K * (D / Q), trong đó (D / Q) đại diện cho số lần đặt hàng bổ sung trong một năm",
            "Chi phí Đặt hàng Hàng năm = K * Q * D",
            "Chi phí Đặt hàng Hàng năm = (K + D) / Q",
            "Chi phí Đặt hàng Hàng năm = K * (Q / 2)"
        ],
        "correct_answer": 0,
        "explanation_en": "Dividing annual demand D by order size Q gives order frequency N = D/Q. Multiplying by setup cost K yields total annual setup cost K*(D/Q).",
        "explanation_vi": "Lấy nhu cầu năm D chia cho quy mô mỗi lô Q ra số lần đặt hàng trong năm N = D/Q. Nhân với chi phí mỗi lần K cho ra K*(D/Q)."
    })

    questions.append({
        "id": "QUES-141",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Annual Holding Cost Formula",
        "difficulty": "Intermediate",
        "question_en": "What is the mathematical expression for Total Annual Holding Cost in the basic EOQ model?",
        "question_vi": "Biểu thức toán học cho Tổng Chi phí Lưu kho Hàng năm trong mô hình EOQ cơ bản là gì?",
        "options_en": [
            "Annual Holding Cost = h * (Q / 2)",
            "Annual Holding Cost = h * (D / Q)",
            "Annual Holding Cost = h * Q * D",
            "Annual Holding Cost = h / Q"
        ],
        "options_vi": [
            "Chi phí Lưu kho Hàng năm = h * (Q / 2)",
            "Chi phí Lưu kho Hàng năm = h * (D / Q)",
            "Chi phí Lưu kho Hàng năm = h * Q * D",
            "Chi phí Lưu kho Hàng năm = h / Q"
        ],
        "correct_answer": 0,
        "explanation_en": "Multiplying unit holding cost h by average inventory Q/2 gives the total annual carrying expense h*(Q/2).",
        "explanation_vi": "Lấy chi phí lưu kho 1 đơn vị h nhân với mức tồn kho bình quân Q/2 cho ra tổng chi phí lưu kho hàng năm h*(Q/2)."
    })

    questions.append({
        "id": "QUES-142",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Total Variable Cost Trade-off Curve",
        "difficulty": "Intermediate",
        "question_en": "How do Annual Setup Cost and Annual Holding Cost behave as order batch size Q increases?",
        "question_vi": "Chi phí Đặt hàng hàng năm và Chi phí Lưu kho hàng năm biến thiên như thế nào khi quy mô lô đặt hàng Q tăng lên?",
        "options_en": [
            "Annual Setup Cost decreases asymptotically toward zero, while Annual Holding Cost increases linearly",
            "Both costs increase to infinity",
            "Both costs decrease to zero",
            "Setup cost increases linearly while holding cost stays flat"
        ],
        "options_vi": [
            "Chi phí Đặt hàng giảm tiệm cận về 0, trong khi Chi phí Lưu kho tăng tuyến tính theo đường thẳng",
            "Cả hai chi phí đều cùng tăng lên vô hạn",
            "Cả hai chi phí đều cùng giảm về 0",
            "Chi phí đặt hàng tăng tuyến tính còn chi phí lưu kho giữ nguyên nằm ngang"
        ],
        "correct_answer": 0,
        "explanation_en": "Larger batches mean fewer orders (reducing K*D/Q), but higher warehouse piles (increasing h*Q/2), creating the classic U-shaped convex TVC curve.",
        "explanation_vi": "Đặt lô lớn giúp giảm số lần đặt (tiết kiệm phí đơn hàng), nhưng làm tăng hàng tồn trữ trong kho (tốn phí lưu kho), tạo thành đường cong chữ U."
    })

    questions.append({
        "id": "QUES-143",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ACT Current Policy Evaluation",
        "difficulty": "Intermediate",
        "question_en": "Under ACT's historical policy of ordering Q = 1,000 tires, what were its Annual Setup Cost and Annual Holding Cost?",
        "question_vi": "Theo chính sách lịch sử của ACT khi đặt lô Q = 1,000 lốp, Chi phí Đặt hàng hàng năm và Chi phí Lưu kho hàng năm là bao nhiêu?",
        "options_en": [
            "Setup Cost = $690 (6 orders x $115) and Holding Cost = $2,100 (500 avg tires x $4.20), totaling TVC = $2,790",
            "Setup Cost = $2,100 and Holding Cost = $690, totaling $2,790",
            "Setup Cost = $115 and Holding Cost = $4.20, totaling $119.20",
            "Both costs equaled $1,203.74"
        ],
        "options_vi": [
            "Chi phí Đặt hàng = $690 (6 lần đặt x $115) và Chi phí Lưu kho = $2,100 (500 lốp bình quân x $4.20), tổng TVC = $2,790",
            "Chi phí Đặt hàng = $2,100 và Chi phí Lưu kho = $690, tổng TVC = $2,790",
            "Chi phí Đặt hàng = $115 và Chi phí Lưu kho = $4.20, tổng TVC = $119.20",
            "Cả hai chi phí đều bằng đúng $1,203.74"
        ],
        "correct_answer": 0,
        "explanation_en": "D/Q = 6,000/1,000 = 6 orders. Setup = 6 * $115 = $690. Holding = $4.20 * (1,000/2) = $2,100. Total TVC = $2,790.",
        "explanation_vi": "Nhu cầu 6,000 / 1,000 = 6 lần đặt. Đặt hàng = 6 x $115 = $690. Lưu kho = $4.20 x 500 = $2,100. Tổng chi phí TVC = $2,790/năm."
    })

    questions.append({
        "id": "QUES-144",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ABC Inventory Classification",
        "difficulty": "Intermediate",
        "question_en": "In modern ERP inventory management, how does the Pareto ABC classification categorize stocked merchandise?",
        "question_vi": "Trong quản trị tồn kho ERP hiện đại, phân loại ABC theo nguyên lý Pareto phân chia hàng hóa thành các nhóm như thế nào?",
        "options_en": [
            "Class A: ~20% of items accounting for ~80% of annual monetary value (tight control); Class B: moderate value; Class C: ~50% of items accounting for ~5% of value (loose control)",
            "Class A: items made of Aluminum; Class B: items made of Bronze; Class C: items made of Copper",
            "Class A: items stored in Zone A; Class B: items stored in Zone B; Class C: items stored in Zone C",
            "Class A: expired goods; Class B: fresh goods; Class C: damaged goods"
        ],
        "options_vi": [
            "Nhóm A: ~20% chủng loại hàng chiếm ~80% giá trị tiền tệ hàng năm (kiểm soát chặt); Nhóm B: giá trị trung bình; Nhóm C: ~50% số mặt hàng chỉ chiếm ~5% giá trị (kiểm soát nới lỏng)",
            "Nhóm A: hàng làm bằng Nhôm; Nhóm B: hàng làm bằng Đồng thau; Nhóm C: hàng làm bằng Đồng đỏ",
            "Nhóm A: hàng lưu tại Khu A; Nhóm B: hàng lưu tại Khu B; Nhóm C: hàng lưu tại Khu C",
            "Nhóm A: hàng hết hạn; Nhóm B: hàng mới; Nhóm C: hàng bị hỏng"
        ],
        "correct_answer": 0,
        "explanation_en": "ABC classification applies Pareto's law to focus expensive ERP cycle-counting and continuous review policies on high-value Class A items.",
        "explanation_vi": "Quy tắc Pareto 80/20 phân bổ nguồn lực: Nhóm A có giá trị vốn lớn cần theo dõi liên tục và tối ưu chặt chẽ, nhóm C phụ tùng nhỏ có thể đặt lô lớn."
    })

    questions.append({
        "id": "QUES-145",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Inventory Valuation Methods in ERP",
        "difficulty": "Intermediate",
        "question_en": "Which inventory valuation accounting method updates unit inventory cost dynamically after every incoming vendor delivery at a new price?",
        "question_vi": "Phương pháp kế toán định giá tồn kho nào trong ERP cập nhật lại đơn giá tồn kho một cách linh hoạt sau mỗi lần nhập hàng mới có biến động giá?",
        "options_en": [
            "Moving Average Price (MAP)",
            "Standard Costing (STD)",
            "Last-In First-Out (LIFO)",
            "Fairytale Valuation Method"
        ],
        "options_vi": [
            "Giá Bình quân Gia quyền Di động (Moving Average Price - MAP)",
            "Giá Thành Tiêu chuẩn Cố định (Standard Costing - STD)",
            "Nhập sau Xuất trước (LIFO)",
            "Phương pháp Định giá Thần thoại"
        ],
        "correct_answer": 0,
        "explanation_en": "Moving Average Price recalculates the unit valuation immediately upon each Goods Receipt by combining previous inventory value and new delivery invoice value.",
        "explanation_vi": "Phương pháp Bình quân Di động tính lại đơn giá vốn bình quân ngay khi có phiếu nhập kho mới: (Giá trị cũ + Giá trị mới) / Tổng số lượng mới."
    })

    # Advanced (Q146 - Q150)
    questions.append({
        "id": "QUES-146",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "BA Requirements for Inventory Carrying Rate",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is eliciting holding cost parameters for an ERP implementation. Why should the BA challenge finance when they propose using the short-term bank savings deposit rate (e.g., 4%) as the corporate carrying rate I?",
        "question_vi": "Một Business Analyst đang khơi gợi tham số tỷ lệ lưu kho cho dự án ERP. Vì sao BA cần phản biện khi phòng tài chính đề xuất lấy lãi suất tiền gửi tiết kiệm ngân hàng (ví dụ 4%) làm tỷ lệ tồn trữ I?",
        "options_en": [
            "Because true corporate cost of capital reflects the company's Weighted Average Cost of Capital (WACC) or internal hurdle rate (12-20%), and excludes physical storage, insurance, property taxes, and shrinkage risks",
            "Because banks refuse to accept deposits from manufacturing corporations",
            "Because bank savings rates are illegal under corporate governance statutes",
            "Because holding costs must always be exactly 100% of purchase price"
        ],
        "options_vi": [
            "Vì chi phí vốn doanh nghiệp thực tế phải là Chi phí Vốn Bình quân Gia quyền (WACC) hoặc tỷ suất sinh lời kỳ vọng (12-20%), và chưa hề tính đến tiền thuê kho, bảo hiểm, thuế và hao hụt",
            "Vì các ngân hàng từ chối nhận tiền gửi từ các tập đoàn sản xuất",
            "Vì lãi suất tiết kiệm ngân hàng bị luật quản trị doanh nghiệp cấm áp dụng",
            "Vì chi phí lưu kho luôn bắt buộc phải bằng đúng 100% giá mua hàng"
        ],
        "correct_answer": 0,
        "explanation_en": "Carrying cost rate I includes WACC (cost of debt and equity hurdle rate, often 12-18%) plus physical handling, leasing, insurance, taxes, and obsolescence (4-8%), totaling 18-25%.",
        "explanation_vi": "Lãi suất ngân hàng 4% quá thấp so với chi phí cơ hội vốn WACC của doanh nghiệp. Đặt I quá thấp sẽ làm hệ thống ERP tính ra lô đặt hàng EOQ khổng lồ, làm tràn ngập kho."
    })

    questions.append({
        "id": "QUES-147",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ERP System Stock Discrepancy Impact",
        "difficulty": "Advanced",
        "question_en": "If an ERP system overstates warehouse stock by 300 tires due to unrecorded damage scrap, how does this distort the automated reorder algorithm?",
        "question_vi": "Nếu hệ thống ERP ghi nhận tồn kho trên sổ sách cao hơn thực tế 300 lốp do phế phẩm hỏng không được ghi giảm, điều này làm sai lệch thuật toán đặt hàng tự động như thế nào?",
        "options_en": [
            "The system believes stock is above Reorder Point (ROP) and fails to trigger replenishment, leading to unexpected severe stockouts and customer delivery failures",
            "The system automatically orders 10,000 extra tires from the factory",
            "The warehouse building catches fire",
            "The unit purchase price c decreases by 50%"
        ],
        "options_vi": [
            "Hệ thống lầm tưởng lượng hàng sẵn có vẫn nằm trên Điểm đặt hàng lại (ROP) nên không phát lệnh bổ sung, dẫn đến hết hàng thực tế và trễ đơn của khách",
            "Hệ thống tự động phát lệnh đặt thêm 10,000 lốp ngoài ý muốn",
            "Tòa nhà kho hàng bị bốc cháy",
            "Đơn giá mua hàng c tự động giảm đi 50%"
        ],
        "correct_answer": 0,
        "explanation_en": "Phantom inventory prevents inventory tracking algorithms from sensing when physical stock breaches the reorder threshold, blinding ERP MRP engines.",
        "explanation_vi": "Tồn kho ảo trên sổ sách khiến ERP tưởng kho vẫn an toàn, không kích hoạt Purchase Requisition, khiến khách hàng đến lấy hàng thì kho đã trống trơn."
    })

    questions.append({
        "id": "QUES-148",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Continuous vs Periodic Review ERP Architecture",
        "difficulty": "Advanced",
        "question_en": "What architectural ERP prerequisites are required to transition an enterprise from a Periodic Review policy (R, S) to a Continuous Review policy (s, Q)?",
        "question_vi": "Những điều kiện tiên quyết về kiến trúc kỹ thuật ERP nào là bắt buộc để chuyển đổi doanh nghiệp từ chính sách Kiểm tra định kỳ (R, S) sang Kiểm tra liên tục (s, Q)?",
        "options_en": [
            "Real-time transactional inventory tracking via barcode/RFID scanning at all warehouse entry/exit gates, instantaneous Goods Issue/Receipt postings, and automated event triggers",
            "Replacing all delivery trucks with electric bicycles",
            "Demolishing all warehouse interior dividing walls",
            "Printing paper purchase orders once every six months"
        ],
        "options_vi": [
            "Khả năng theo dõi tồn kho giao dịch thời gian thực qua quét mã vạch/RFID tại mọi cửa kho, ghi nhận tức thời phiếu Nhập/Xuất kho và kích hoạt sự kiện tự động",
            "Thay thế toàn bộ xe tải giao hàng bằng xe đạp điện",
            "Đập bỏ toàn bộ các bức tường ngăn cách bên trong nhà kho",
            "In các đơn đặt hàng bằng giấy định kỳ 6 tháng một lần"
        ],
        "correct_answer": 0,
        "explanation_en": "Continuous review (s, Q) requires instantaneous perpetual inventory visibility so the system detects the exact moment on-hand balance touches s, necessitating automated RF scanning and immediate ERP document postings.",
        "explanation_vi": "Kiểm tra liên tục đòi hỏi hệ thống ERP phải biết số dư tức thời sau từng giây giao dịch quét mã vạch, để kích hoạt lệnh bổ sung ngay khi tồn kho chạm điểm s."
    })

    questions.append({
        "id": "QUES-149",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "Holding Cost Capital vs Physical Sensitivity",
        "difficulty": "Advanced",
        "question_en": "If market interest rates rise sharply from 5% to 15% during a macroeconomic tightening cycle, how does this impact an enterprise's optimal order quantities and warehouse strategy?",
        "question_vi": "Nếu lãi suất thị trường tăng vọt từ 5% lên 15% trong chu kỳ thắt chặt tiền tệ, điều này tác động như thế nào đến quy mô lô hàng tối ưu và chiến lược kho bãi của doanh nghiệp?",
        "options_en": [
            "Unit holding cost h increases substantially, forcing optimal batch size Q* to decrease (smaller, more frequent orders) to release expensive tied-up cash capital",
            "Optimal batch size Q* increases to infinity",
            "Holding cost drops to zero because banks pay interest",
            "The company should immediately double all warehouse inventory"
        ],
        "options_vi": [
            "Chi phí lưu kho đơn vị h tăng vọt, buộc quy mô lô tối ưu Q* phải giảm xuống (đặt các lô nhỏ hơn, thường xuyên hơn) để giải phóng dòng tiền bị ứ đọng đắt đỏ",
            "Quy mô lô đặt hàng tối ưu Q* tăng vọt lên vô hạn",
            "Chi phí lưu kho giảm về 0 vì ngân hàng trả lãi suất",
            "Doanh nghiệp nên nhân đôi lượng tồn kho trong toàn bộ các kho ngay lập tức"
        ],
        "correct_answer": 0,
        "explanation_en": "Higher capital costs raise h. In Wilson's formula Q* = sqrt(2KD/h), h is in the denominator; as h grows, optimal Q* drops, driving lean inventory practices.",
        "explanation_vi": "Lãi suất tăng làm chi phí vốn h tăng. Trong công thức Wilson, h nằm dưới mẫu số, do đó Q* giảm xuống, buộc doanh nghiệp phải áp dụng mô hình tinh gọn (Lean JIT)."
    })

    questions.append({
        "id": "QUES-150",
        "exam_id": "EXAM-06",
        "chapter_id": "chap-04",
        "topic": "ERP Vendor Management Inventory (VMI)",
        "difficulty": "Advanced",
        "question_en": "In a Vendor-Managed Inventory (VMI) arrangement enabled by cloud ERP EDI connectivity, who assumes responsibility for tracking stock levels and triggering replenishment orders?",
        "question_vi": "Trong mô hình Tồn kho do Nhà cung cấp Quản lý (VMI) kết nối qua ERP đám mây (EDI), bên nào chịu trách nhiệm theo dõi lượng tồn kho và phát lệnh bổ sung hàng?",
        "options_en": [
            "The upstream supplier monitors the customer's ERP inventory telemetry and proactively dispatches replenishment to maintain target service levels",
            "The end consumer visiting the retail store",
            "An independent freight driver with no knowledge of tire sizes",
            "The municipal tax auditor"
        ],
        "options_vi": [
            "Nhà cung cấp thượng nguồn tự theo dõi dữ liệu tồn kho trong ERP của khách hàng và chủ động điều xe giao hàng để duy trì mức dịch vụ cam kết",
            "Người tiêu dùng cuối cùng khi đến mua hàng tại đại lý",
            "Một tài xế xe tải độc lập không có hiểu biết về thông số lốp xe",
            "Thanh tra viên cơ quan thuế địa phương"
        ],
        "correct_answer": 0,
        "explanation_en": "VMI shifts replenishment responsibility upstream: the vendor monitors inventory via EDI 852 (Product Activity Data) and generates purchase orders on the buyer's behalf.",
        "explanation_vi": "Mô hình VMI chuyển quyền điều phối cho nhà cung ứng: nhà cung ứng đọc số liệu tồn kho qua cổng kết nối EDI và tự động lên lịch giao hàng kịp thời."
    })

    return questions
