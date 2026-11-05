# -*- coding: utf-8 -*-
# EXAM 07: Basic Economic Order Quantity (EOQ) & ACT Baseline (chap-04)
# 25 Questions: Q151 to Q175 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q151 - Q160)
    questions.append({
        "id": "QUES-151",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Basic EOQ Assumptions",
        "difficulty": "Basic",
        "question_en": "Which of the following is a fundamental assumption of the Basic Economic Order Quantity (EOQ) model?",
        "question_vi": "Giả định nào sau đây là giả định căn bản của mô hình Lượng Đặt Hàng Kinh Tế Cơ Bản (Basic EOQ)?",
        "options_en": [
            "A constant, known demand rate, instantaneous batch replenishment delivery, and zero shortages permitted",
            "Demand swings wildly between positive and negative numbers each week",
            "Suppliers refuse to deliver goods unless ordered in prime numbers",
            "The cost of placing an order increases exponentially with every tire purchased"
        ],
        "options_vi": [
            "Tốc độ nhu cầu ổn định và đã biết trước, hàng về tức thời trọn gói cả lô và tuyệt đối không cho phép thiếu hàng",
            "Nhu cầu dao động hỗn loạn giữa số dương và số âm mỗi tuần",
            "Nhà cung cấp từ chối giao hàng trừ khi số lượng đặt là số nguyên tố",
            "Chi phí cho mỗi lần đặt hàng tăng theo hàm mũ đối với từng chiếc lốp mua thêm"
        ],
        "correct_answer": 0,
        "explanation_en": "The basic EOQ assumes constant demand rate D, instantaneous batch delivery, zero stockouts permitted, and fixed costs K, c, h.",
        "explanation_vi": "Mô hình EOQ cơ bản giả định nhu cầu hằng số D, hàng nhập về tức thời nguyên lô, không được phép thiếu hàng và các chi phí cố định."
    })

    questions.append({
        "id": "QUES-152",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Wilson Formula",
        "difficulty": "Basic",
        "question_en": "What is the famous Wilson square root formula for the optimal order quantity Q* in the basic EOQ model?",
        "question_vi": "Công thức căn bậc hai Wilson kinh điển xác định lượng đặt hàng tối ưu Q* trong mô hình EOQ cơ bản là gì?",
        "options_en": [
            "Q* = sqrt((2 * K * D) / h)",
            "Q* = (2 * K * D) / h",
            "Q* = sqrt((K * h) / (2 * D))",
            "Q* = K + D + h"
        ],
        "options_vi": [
            "Q* = sqrt((2 * K * D) / h)",
            "Q* = (2 * K * D) / h",
            "Q* = sqrt((K * h) / (2 * D))",
            "Q* = K + D + h"
        ],
        "correct_answer": 0,
        "explanation_en": "Wilson's classical square root formula is Q* = sqrt((2*K*D)/h), balancing annual ordering and holding costs.",
        "explanation_vi": "Công thức Wilson: Q* = căn bậc hai của ((2 x K x D) / h), cân bằng giữa chi phí đặt hàng và chi phí lưu kho."
    })

    questions.append({
        "id": "QUES-153",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Cost Parity at Optimum",
        "difficulty": "Basic",
        "question_en": "At the exact optimal order quantity Q* derived by the basic EOQ model, what special relationship exists between the two variable cost components?",
        "question_vi": "Tại đúng điểm đặt hàng tối ưu Q* tìm được từ mô hình EOQ cơ bản, mối quan hệ đặc biệt nào xuất hiện giữa hai thành phần chi phí biến đổi?",
        "options_en": [
            "Annual Setup Cost is exactly equal to Annual Holding Cost (K * D / Q* = h * Q* / 2)",
            "Annual Setup Cost is ten times larger than Annual Holding Cost",
            "Annual Holding Cost is reduced to exactly zero",
            "Annual Setup Cost is negative"
        ],
        "options_vi": [
            "Chi phí Đặt hàng hàng năm bằng đúng Chi phí Lưu kho hàng năm (K * D / Q* = h * Q* / 2)",
            "Chi phí Đặt hàng hàng năm lớn gấp 10 lần Chi phí Lưu kho hàng năm",
            "Chi phí Lưu kho hàng năm được triệt tiêu về đúng bằng 0",
            "Chi phí Đặt hàng hàng năm mang giá trị âm"
        ],
        "correct_answer": 0,
        "explanation_en": "At the minimum point of a convex trade-off curve f(Q) = a/Q + bQ, the two terms are identical at the minimum: K*D/Q* = h*Q*/2.",
        "explanation_vi": "Tại cực tiểu của đường cong tổng chi phí TVC, hai nhánh chi phí giao nhau: Chi phí Đặt hàng hàng năm cân bằng tuyệt đối với Chi phí Lưu kho hàng năm."
    })

    questions.append({
        "id": "QUES-154",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT Case Annual Demand",
        "difficulty": "Basic",
        "question_en": "In the Atlantic Coast Tire Corp. (ACT) case, what is the annual demand D for tire size 185/70 R13?",
        "question_vi": "Trong case Atlantic Coast Tire Corp. (ACT), nhu cầu tiêu thụ hàng năm D cho loại lốp 185/70 R13 là bao nhiêu?",
        "options_en": [
            "6,000 tires per year (500 tires/month x 12 months)",
            "1,000 tires per year",
            "12,000 tires per year",
            "500 tires per year"
        ],
        "options_vi": [
            "6,000 lốp mỗi năm (500 lốp/tháng x 12 tháng)",
            "1,000 lốp mỗi năm",
            "12,000 lốp mỗi năm",
            "500 lốp mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "ACT sells tires at a regular rate of 500 per month; annual demand D = 500 * 12 = 6,000 tires/year.",
        "explanation_vi": "Lượng bán ra đều đặn là 500 lốp/tháng; do đó nhu cầu cả năm D = 500 x 12 = 6,000 chiếc lốp."
    })

    questions.append({
        "id": "QUES-155",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT Optimal EOQ Calculation",
        "difficulty": "Basic",
        "question_en": "Given ACT parameters D = 6,000 tires/yr, K = $115/order, and h = $4.20/tire/yr, what is the optimal order quantity Q*?",
        "question_vi": "Với các thông số của ACT: D = 6,000 lốp/năm, K = $115/lần và h = $4.20/lốp/năm, lượng đặt hàng tối ưu Q* là bao nhiêu?",
        "options_en": [
            "573.2 tires (rounded to 573 tires)",
            "1,000 tires",
            "250 tires",
            "716 tires"
        ],
        "options_vi": [
            "573.2 lốp (làm tròn là 573 lốp)",
            "1,000 lốp",
            "250 lốp",
            "716 lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "Q* = sqrt((2 * 115 * 6,000) / 4.20) = sqrt(1,380,000 / 4.20) = sqrt(328,571.43) = 573.21 -> 573 tires.",
        "explanation_vi": "Q* = căn bậc hai của ((2 x 115 x 6,000) / 4.20) = căn(328,571.43) = 573.2 lốp."
    })

    questions.append({
        "id": "QUES-156",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT Optimal Total Variable Cost",
        "difficulty": "Basic",
        "question_en": "What is ACT's Total Variable Cost TVC* when using the optimal EOQ order quantity of Q* = 573.2 tires?",
        "question_vi": "Tổng chi phí biến đổi tồn kho TVC* của ACT khi đặt theo lượng tối ưu Q* = 573.2 lốp là bao nhiêu?",
        "options_en": [
            "$2,407.48 per year (Setup: $1,203.74 + Holding: $1,203.74)",
            "$2,790.00 per year",
            "$1,500.00 per year",
            "$3,200.00 per year"
        ],
        "options_vi": [
            "$2,407.48 mỗi năm (Đặt hàng: $1,203.74 + Lưu kho: $1,203.74)",
            "$2,790.00 mỗi năm",
            "$1,500.00 mỗi năm",
            "$3,200.00 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "TVC* = sqrt(2 * K * D * h) = sqrt(2 * 115 * 6,000 * 4.20) = sqrt(5,796,000) = $2,407.48 per year.",
        "explanation_vi": "TVC* = căn(2 x K x D x h) = căn(2 x 115 x 6,000 x 4.20) = căn(5,796,000) = $2,407.48/năm."
    })

    questions.append({
        "id": "QUES-157",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT EOQ Cost Savings",
        "difficulty": "Basic",
        "question_en": "How much money does ACT save annually by switching from their historical batch of Q = 1,000 tires to optimal Q* = 573 tires?",
        "question_vi": "ACT tiết kiệm được bao nhiêu tiền mỗi năm khi chuyển từ lô đặt hàng lịch sử Q = 1,000 lốp sang lô tối ưu Q* = 573 lốp?",
        "options_en": [
            "$382.52 per year (a 13.7% reduction in variable inventory costs)",
            "$1,000.00 per year",
            "$50.00 per year",
            "$0 (both policies have identical costs)"
        ],
        "options_vi": [
            "$382.52 mỗi năm (giảm 13.7% chi phí biến đổi tồn kho)",
            "$1,000.00 mỗi năm",
            "$50.00 mỗi năm",
            "$0 (hai chính sách tốn chi phí y hệt nhau)"
        ],
        "correct_answer": 0,
        "explanation_en": "Savings = Current TVC ($2,790.00) - Optimal TVC ($2,407.48) = $382.52/year (13.7% savings).",
        "explanation_vi": "Khoản tiết kiệm ròng = $2,790.00 - $2,407.48 = $382.52/năm, tương ứng giảm 13.7% chi phí."
    })

    questions.append({
        "id": "QUES-158",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT Order Frequency",
        "difficulty": "Basic",
        "question_en": "Under ACT's optimal policy Q* = 573.2 tires, how many replenishment orders will ACT place per year?",
        "question_vi": "Theo chính sách tối ưu Q* = 573.2 lốp, ACT sẽ phát hành bao nhiêu đơn đặt hàng bổ sung mỗi năm?",
        "options_en": [
            "Approximately 10.47 orders per year (6,000 / 573.2)",
            "Exactly 6 orders per year",
            "52 orders per year (weekly)",
            "1 order per year"
        ],
        "options_vi": [
            "Khoảng 10.47 lần đặt hàng mỗi năm (6,000 / 573.2)",
            "Đúng 6 lần đặt hàng mỗi năm",
            "52 lần đặt hàng mỗi năm (hàng tuần)",
            "1 lần đặt hàng duy nhất mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Order frequency N = D / Q* = 6,000 / 573.2 = 10.47 orders per year (or an order roughly every 24 working days).",
        "explanation_vi": "Tần suất đặt hàng N = D / Q* = 6,000 / 573.2 = 10.47 lần/năm (trung bình khoảng 24 ngày làm việc đặt 1 lần)."
    })

    questions.append({
        "id": "QUES-159",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ACT Reorder Point Calculation",
        "difficulty": "Basic",
        "question_en": "With daily sales of 20 tires/day (500 tires / 25 working days) and an Eversafe delivery lead time of 9 working days, what is ACT's Reorder Point (ROP)?",
        "question_vi": "Với lượng bán hàng ngày là 20 lốp/ngày (500 lốp / 25 ngày làm việc) và thời gian Eversafe giao hàng là 9 ngày làm việc, Điểm đặt hàng lại (ROP) của ACT là bao nhiêu?",
        "options_en": [
            "180 tires (20 tires/day x 9 working days)",
            "500 tires",
            "573 tires",
            "25 tires"
        ],
        "options_vi": [
            "180 lốp (20 lốp/ngày x 9 ngày làm việc)",
            "500 lốp",
            "573 lốp",
            "25 lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "ROP = daily demand (d) * lead time (L) = 20 * 9 = 180 tires. When inventory drops to 180 tires, a new order must be placed.",
        "explanation_vi": "ROP = d x L = 20 x 9 = 180 lốp. Khi kho còn đúng 180 lốp, thủ kho phải phát hành đơn hàng mới."
    })

    questions.append({
        "id": "QUES-160",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Excel Solver GRG Nonlinear Selection",
        "difficulty": "Basic",
        "question_en": "Why does Microsoft Excel Solver require the GRG Nonlinear solving method rather than Simplex LP when optimizing the basic EOQ model?",
        "question_vi": "Vì sao Microsoft Excel Solver bắt buộc phải dùng phương pháp GRG Nonlinear thay vì Simplex LP khi tối ưu hóa mô hình EOQ cơ bản?",
        "options_en": [
            "Because the objective cell contains K * (D / Q), which has decision variable Q in the denominator, creating a curved nonlinear hyperbola",
            "Because Microsoft Excel cannot spell the word Simplex",
            "Because the tire warehouse is round in shape",
            "Because linear programming is only used for accounting depreciation"
        ],
        "options_vi": [
            "Vì ô hàm mục tiêu chứa biểu thức K * (D / Q), có biến quyết định Q nằm ở mẫu số, tạo thành đường cong phi tuyến hypebol",
            "Vì Microsoft Excel không thể đọc được chữ Simplex",
            "Vì nhà kho chứa lốp xe có hình dáng tròn",
            "Vì quy hoạch tuyến tính chỉ dùng để tính khấu hao tài sản cố định"
        ],
        "correct_answer": 0,
        "explanation_en": "K*D/Q is a nonlinear hyperbolic function of Q. Since the derivative is non-constant, the GRG Nonlinear solver must be used.",
        "explanation_vi": "Thành phần chi phí đặt hàng chứa 1/Q là hàm phi tuyến bậc -1, phá vỡ điều kiện tuyến tính của Simplex LP, bắt buộc phải dùng GRG Nonlinear."
    })

    # Intermediate (Q161 - Q170)
    questions.append({
        "id": "QUES-161",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "EOQ Calculus Derivation",
        "difficulty": "Intermediate",
        "question_en": "What is the first derivative of the Total Variable Cost function d(TVC)/dQ, and how is it used to find Q*?",
        "question_vi": "Đạo hàm bậc nhất của hàm Tổng Chi phí Biến đổi d(TVC)/dQ là gì, và nó được sử dụng để tìm Q* như thế nào?",
        "options_en": [
            "d(TVC)/dQ = -K*D / Q^2 + h / 2. Setting this derivative equal to 0 yields K*D / Q^2 = h / 2, which solves directly to Q* = sqrt(2KD / h)",
            "d(TVC)/dQ = K * D * Q + h",
            "d(TVC)/dQ = 2 * K * D * h",
            "d(TVC)/dQ = 0 for all values of Q"
        ],
        "options_vi": [
            "d(TVC)/dQ = -K*D / Q^2 + h / 2. Cho đạo hàm bằng 0 ta có K*D / Q^2 = h / 2, giải ra Q* = sqrt(2KD / h)",
            "d(TVC)/dQ = K * D * Q + h",
            "d(TVC)/dQ = 2 * K * D * h",
            "d(TVC)/dQ = 0 với mọi giá trị của Q"
        ],
        "correct_answer": 0,
        "explanation_en": "Differentiating TVC(Q) = K*D*Q^-1 + (h/2)*Q with respect to Q gives -KD/Q^2 + h/2. Equating to 0 yields the Wilson root.",
        "explanation_vi": "Lấy đạo hàm TVC theo Q cho -KD/Q^2 + h/2. Cho đạo hàm triệt tiêu về 0 ta tìm được điểm cực tiểu toàn cục Q* = sqrt(2KD/h)."
    })

    questions.append({
        "id": "QUES-162",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "EOQ Convexity Proof",
        "difficulty": "Intermediate",
        "question_en": "How do we prove mathematically that Wilson's formula Q* represents a global MINIMUM cost rather than a maximum?",
        "question_vi": "Làm thế nào để chứng minh về mặt toán học rằng công thức Wilson Q* đại diện cho điểm CỰC TIỂU chi phí toàn cục chứ không phải cực đại?",
        "options_en": [
            "The second derivative d^2(TVC)/dQ^2 = 2*K*D / Q^3 is strictly positive (> 0) for all feasible positive values of Q, proving strict convexity",
            "The second derivative is negative, indicating a concave peak",
            "By asking the factory supervisor for personal confirmation",
            "Because total cost can never exceed $10,000"
        ],
        "options_vi": [
            "Đạo hàm bậc hai d^2(TVC)/dQ^2 = 2*K*D / Q^3 luôn mang giá trị dương nghiêm ngặt (> 0) với mọi Q dương, chứng minh hàm số lồi nghiêm ngặt",
            "Đạo hàm bậc hai mang giá trị âm, biểu thị một đỉnh lõm cực đại",
            "Bằng cách hỏi xin xác nhận cá nhân của quản đốc phân xưởng",
            "Vì tổng chi phí không bao giờ có thể vượt quá $10,000"
        ],
        "correct_answer": 0,
        "explanation_en": "Since K, D, Q > 0, d^2(TVC)/dQ^2 = 2KD/Q^3 > 0 everywhere, establishing strict convexity and confirming that Q* is an absolute global minimum.",
        "explanation_vi": "Vì K, D, Q > 0, đạo hàm bậc hai luôn dương, đồ thị hàm số có bề lõm quay lên trên (hàm lồi), đảm bảo Q* là điểm cực tiểu toàn cục duy nhất."
    })

    questions.append({
        "id": "QUES-163",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "EOQ Sensitivity to Demand Changes",
        "difficulty": "Intermediate",
        "question_en": "If annual demand D for tires quadruples (increases by 400%, from D to 4D), by what factor does the optimal order quantity Q* increase?",
        "question_vi": "Nếu nhu cầu hàng năm D đối với lốp xe tăng gấp 4 lần (từ D lên 4D), quy mô lô đặt hàng tối ưu Q* sẽ tăng lên bao nhiêu lần?",
        "options_en": [
            "It doubles (increases by a factor of sqrt(4) = 2)",
            "It quadruples (increases by a factor of 4)",
            "It increases by a factor of 16",
            "It remains completely unchanged"
        ],
        "options_vi": [
            "Tăng gấp 2 lần (tăng theo thừa số căn bậc hai sqrt(4) = 2)",
            "Tăng gấp 4 lần",
            "Tăng gấp 16 lần",
            "Hoàn toàn không thay đổi"
        ],
        "correct_answer": 0,
        "explanation_en": "Because Q* is proportional to sqrt(D), multiplying D by 4 multiplies Q* by sqrt(4) = 2, demonstrating economies of scale.",
        "explanation_vi": "Do Q* tỷ lệ với căn bậc hai của D, khi nhu cầu tăng gấp 4 thì lô hàng tối ưu chỉ tăng gấp căn(4) = 2 lần, chứng minh tính kinh tế nhờ quy mô."
    })

    questions.append({
        "id": "QUES-164",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "EOQ Flat Bottom Property",
        "difficulty": "Intermediate",
        "question_en": "What is the practical business significance of the 'Flat Bottom' property of the EOQ Total Variable Cost curve?",
        "question_vi": "Ý nghĩa thực tiễn kinh doanh của đặc tính 'Đáy Phẳng' (Flat Bottom) của đường cong Tổng Chi phí Biến đổi EOQ là gì?",
        "options_en": [
            "The TVC curve is relatively insensitive to minor deviations around Q*; ordering slightly more or less (e.g., +/- 10-20%) causes only negligible cost increases",
            "The warehouse floor must be physically leveled with wet cement",
            "The shipping trucks must have flatbed trailers only",
            "The supplier is legally prohibited from changing prices"
        ],
        "options_vi": [
            "Đường cong TVC tương đối trơ với các sai lệch nhỏ xung quanh Q*; đặt hàng chênh lệch đôi chút (+/- 10-20%) chỉ làm tổng chi phí tăng lên không đáng kể",
            "Sàn nhà kho bắt buộc phải được san phẳng bằng xi măng ướt",
            "Các xe tải vận chuyển chỉ được phép sử dụng rơ-moóc sàn phẳng",
            "Nhà cung cấp bị pháp luật cấm điều chỉnh giá bán"
        ],
        "correct_answer": 0,
        "explanation_en": "The flat bottom near Q* provides robustness: rounding Q* to pallet sizes, truckload capacities, or vendor carton packs imposes minimal cost penalties.",
        "explanation_vi": "Đáy phẳng của đường cong TVC mang lại tính bền vững: làm tròn Q* theo quy cách đóng thùng hoặc pallet chỉ làm đội chi phí thêm một vài phần trăm rất nhỏ."
    })

    questions.append({
        "id": "QUES-165",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Cycle Length Formula",
        "difficulty": "Intermediate",
        "question_en": "In the basic EOQ model, what is the formula for the cycle time T (time between consecutive order receipts) in years and working days?",
        "question_vi": "Trong mô hình EOQ cơ bản, công thức tính thời gian chu kỳ T (khoảng thời gian giữa hai lần nhận hàng liên tiếp) tính theo năm và ngày làm việc là gì?",
        "options_en": [
            "T = Q* / D in years, or T = (Q* / D) * (Annual Working Days)",
            "T = D / Q*",
            "T = Q* * D * 365",
            "T = K / h"
        ],
        "options_vi": [
            "T = Q* / D (tính theo năm), hoặc T = (Q* / D) * (Số ngày làm việc trong năm)",
            "T = D / Q*",
            "T = Q* * D * 365",
            "T = K / h"
        ],
        "correct_answer": 0,
        "explanation_en": "Cycle length T represents the time required to deplete one batch Q* at consumption rate D. For ACT: T = 573.2/6000 = 0.0955 years = 23.88 working days.",
        "explanation_vi": "Chu kỳ T là thời gian tiêu thụ hết một lô hàng Q* với tốc độ D. Với ACT: T = 573.2 / 6,000 = 0.0955 năm, tương đương gần 24 ngày làm việc."
    })

    questions.append({
        "id": "QUES-166",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Purchase Cost Neutrality in Basic EOQ",
        "difficulty": "Intermediate",
        "question_en": "Why is the annual purchase acquisition cost (c * D = $20 * 6,000 = $120,000) omitted from the objective function when deriving Wilson's formula?",
        "question_vi": "Vì sao chi phí mua hàng hàng năm (c x D = $20 x 6,000 = $120,000) lại được lược bỏ khỏi hàm mục tiêu khi tìm công thức Wilson?",
        "options_en": [
            "Because unit price c is constant and total annual demand D is fixed, making c*D a constant whose derivative with respect to Q is exactly zero",
            "Because Eversafe donates all tires to ACT free of charge",
            "Because purchasing costs are paid by the government",
            "Because accounting rules forbid tracking purchase expenses"
        ],
        "options_vi": [
            "Vì đơn giá c là cố định và tổng nhu cầu D không đổi, nên c*D là một hằng số có đạo hàm theo biến quyết định Q bằng đúng 0",
            "Vì hãng Eversafe tài trợ miễn phí toàn bộ lốp xe cho ACT",
            "Vì chi phí mua hàng do chính phủ chi trả",
            "Vì chuẩn mực kế toán cấm theo dõi các chi phí thu mua"
        ],
        "correct_answer": 0,
        "explanation_en": "Since c*D is constant regardless of batch size Q, d(c*D)/dQ = 0. It shifts the curve vertically but has zero impact on the optimal location of Q*.",
        "explanation_vi": "Do c*D là hằng số bất biến theo kích thước lô Q, đạo hàm của nó bằng 0, không ảnh hưởng đến vị trí cực trị Q* của hàm tổng chi phí."
    })

    questions.append({
        "id": "QUES-167",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Lead Time Greater than Cycle Time",
        "difficulty": "Intermediate",
        "question_en": "If delivery lead time L exceeds the inventory cycle time T (L > T), how must the Reorder Point (ROP) formula be adjusted?",
        "question_vi": "Nếu thời gian giao hàng L lớn hơn thời gian một chu kỳ tồn kho T (L > T), công thức Điểm đặt hàng lại (ROP) cần được điều chỉnh như thế nào?",
        "options_en": [
            "ROP must be evaluated based on the effective lead time L_e = L - m*T, where m is the number of open replenishment orders already in transit",
            "The company must immediately cancel all customer sales",
            "ROP is multiplied by negative one",
            "Orders can only be placed when warehouse stock reaches exactly zero"
        ],
        "options_vi": [
            "ROP phải được tính toán dựa trên thời gian giao hàng hiệu dụng L_e = L - m*T, trong đó m là số lượng đơn hàng đang trên đường vận chuyển",
            "Công ty phải hủy bỏ ngay lập tức toàn bộ doanh số bán hàng",
            "ROP được nhân với số âm một",
            "Chỉ được phát lệnh đặt hàng khi tồn kho trong kho chạm đúng mức 0"
        ],
        "correct_answer": 0,
        "explanation_en": "When lead time spans multiple cycles, inventory position (on-hand + on-order) must be used rather than physical on-hand stock.",
        "explanation_vi": "Khi thời gian giao hàng kéo dài qua nhiều chu kỳ, hệ thống ERP phải tính theo Vị thế Tồn kho (Inventory Position = Tồn thực tế + Hàng đang về) để so với ROP."
    })

    questions.append({
        "id": "QUES-168",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Excel Solver Integer Restraint on Q",
        "difficulty": "Intermediate",
        "question_en": "When formulating the basic EOQ model for ACT in Excel Solver, what constraint should be added to ensure the order quantity Q is practical for dispatching?",
        "question_vi": "Khi thiết lập mô hình EOQ cơ bản cho ACT trong Excel Solver, ràng buộc nào nên được thêm vào để đảm bảo lượng đặt hàng Q khả thi trong thực tế vận hành?",
        "options_en": [
            "An Integer ('int') constraint on the decision variable cell Q (e.g., forcing Q to be 573 rather than 573.21)",
            "A constraint forcing Q to be equal to zero",
            "A constraint requiring Q to be greater than 10,000",
            "A constraint requiring holding cost to be zero"
        ],
        "options_vi": [
            "Ràng buộc Số nguyên ('int') trên ô biến quyết định Q (ép Q nhận giá trị nguyên 573 thay vì 573.21 chiếc lốp lẻ)",
            "Ràng buộc ép Q phải bằng đúng 0",
            "Ràng buộc đòi hỏi Q phải lớn hơn 10,000",
            "Ràng buộc đòi hỏi chi phí lưu kho phải bằng 0"
        ],
        "correct_answer": 0,
        "explanation_en": "Physical goods like tires cannot be ordered in fractional units; adding the 'int' constraint in Solver yields a clean integer batch size.",
        "explanation_vi": "Hàng hóa vật lý như lốp xe không thể xé lẻ thập phân; thêm ràng buộc 'int' trong Solver giúp tìm ra kích thước lô nguyên chẵn."
    })

    questions.append({
        "id": "QUES-169",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "QM for Windows EOQ Report",
        "difficulty": "Intermediate",
        "question_en": "In QM for Windows Inventory module for the basic EOQ model, what key outputs are automatically generated upon clicking 'Solve'?",
        "question_vi": "Trong module Inventory của phần mềm QM for Windows, những kết quả đầu ra chủ yếu nào được tự động tạo ra ngay khi nhấn 'Solve' cho bài toán EOQ cơ bản?",
        "options_en": [
            "Optimal Order Quantity (Q*), Maximum Inventory, Average Inventory, Orders Per Year, Annual Setup Cost, Annual Holding Cost, and Total Variable Cost",
            "A list of recommended stock market stock purchases",
            "A printable map of highway truck routes",
            "An employee performance evaluation form"
        ],
        "options_vi": [
            "Lượng đặt hàng tối ưu (Q*), Tồn kho cực đại, Tồn kho bình quân, Số lần đặt hàng/năm, Chi phí đặt hàng năm, Chi phí lưu kho năm và Tổng chi phí biến đổi",
            "Danh sách gợi ý mua cổ phiếu trên thị trường chứng khoán",
            "Bản đồ in màu các tuyến đường cao tốc xe tải chạy",
            "Biểu mẫu đánh giá hiệu quả làm việc của nhân viên"
        ],
        "correct_answer": 0,
        "explanation_en": "QM for Windows outputs a complete cost and operational summary: Q*, average inventory (Q/2), order count (D/Q), setup cost, holding cost, and TVC.",
        "explanation_vi": "QM for Windows tự động xuất báo cáo toàn diện: Lô tối ưu Q*, tồn kho bình quân, số lần đặt, chi phí đặt, chi phí giữ hàng và đồ thị giao điểm chi phí."
    })

    questions.append({
        "id": "QUES-170",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Cost of Estimating Parameters Inaccurately",
        "difficulty": "Intermediate",
        "question_en": "If ACT's setup cost K was mistakenly estimated at $230 instead of $115 (a 100% estimation error), by what percentage does the resulting calculated Q* deviate from true optimal?",
        "question_vi": "Nếu chi phí đặt hàng K của ACT bị ước tính nhầm là $230 thay vì $115 (sai số ước lượng 100%), quy mô lô tính ra Q* sẽ bị lệch bao nhiêu % so với điểm tối ưu thực tế?",
        "options_en": [
            "It is approximately 41.4% larger than optimal (sqrt(2) = 1.414), while TVC increases by only ~6% due to the flat bottom curve",
            "It increases by 1,000%",
            "It drops to zero",
            "It has zero deviation"
        ],
        "options_vi": [
            "Nó chỉ lớn hơn tối ưu khoảng 41.4% (do căn bậc hai sqrt(2) = 1.414), trong khi tổng chi phí TVC chỉ tăng thêm khoảng ~6% nhờ đặc tính đáy phẳng",
            "Nó tăng lên 1,000%",
            "Nó giảm xuống bằng 0",
            "Nó hoàn toàn không bị sai lệch chút nào"
        ],
        "correct_answer": 0,
        "explanation_en": "The square root dampens parameter errors: a 100% error in K causes only a sqrt(2) - 1 = 41.4% error in Q*, and the resulting cost penalty on TVC is only ~6%.",
        "explanation_vi": "Căn bậc hai làm suy giảm sai số tham số: K sai gấp đôi thì Q* chỉ lệch 41.4%, và tổn thất chi phí thực tế chỉ tăng thêm khoảng 6%."
    })

    # Advanced (Q171 - Q175)
    questions.append({
        "id": "QUES-171",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "BA Requirements for Pallet Rounding",
        "difficulty": "Advanced",
        "question_en": "In the ACT case, Q* is mathematically 573.2 tires. If Eversafe delivers tires on wooden pallets holding exactly 50 tires each, how should a Business Analyst specify the ERP batch-sizing business rule?",
        "question_vi": "Trong case ACT, Q* tính ra là 573.2 lốp. Nếu hãng Eversafe giao lốp trên các pallet gỗ chứa đúng 50 chiếc/pallet, BA nên chỉ định quy tắc nghiệp vụ định cỡ lô trong ERP như thế nào?",
        "options_en": [
            "The system shall round the calculated EOQ to the nearest multiple of the packaging unit (50 units), comparing total costs at 550 tires (11 pallets) vs 600 tires (12 pallets) and selecting the lower total cost",
            "The system shall order partial pallets with tires rolling loose in the truck bed",
            "The system shall force Eversafe to redesign its pallets to hold 573.2 tires",
            "The system shall cancel all tire sales immediately"
        ],
        "options_vi": [
            "Hệ thống phải làm tròn EOQ tính toán theo bội số của quy cách đóng gói (50 chiếc), so sánh tổng chi phí giữa 550 lốp (11 pallet) và 600 lốp (12 pallet) và chọn mức chi phí thấp hơn",
            "Hệ thống cho phép giao pallet dở dang để lốp xe lăn lóc tự do trên sàn xe tải",
            "Hệ thống bắt buộc Eversafe phải thiết kế lại pallet chứa đúng 573.2 chiếc lốp",
            "Hệ thống hủy bỏ ngay lập tức toàn bộ hoạt động bán lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "Practical ERP business rules enforce packaging multiples (Pallet Rounding Rules) by evaluating integer multiples around Q* (550 vs 600) to maintain logistics handling efficiency.",
        "explanation_vi": "Quy tắc nghiệp vụ ERP chuẩn áp dụng làm tròn theo bội số pallet: so sánh chi phí tại 550 lốp và 600 lốp để chọn phương án tối ưu, thuận tiện cho việc bốc xếp xe nâng."
    })

    questions.append({
        "id": "QUES-172",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Safety Stock under Stochastic Demand",
        "difficulty": "Advanced",
        "question_en": "If ACT's monthly demand is normally distributed with mean 500 tires and standard deviation sigma = 50 tires, how does the Reorder Point formula expand beyond deterministic d * L?",
        "question_vi": "Nếu nhu cầu tháng của ACT tuân theo phân phối chuẩn với trung bình 500 lốp và độ lệch chuẩn sigma = 50 lốp, công thức ROP mở rộng vượt ra ngoài d x L như thế nào?",
        "options_en": [
            "ROP = d * L + Safety_Stock, where Safety_Stock = z * sigma_L (z is the standard normal factor for the target cycle service level)",
            "ROP = d * L minus the CEO's bonus",
            "ROP = 0 because uncertainty cannot be modeled in ERP",
            "ROP is divided by the square root of 365"
        ],
        "options_vi": [
            "ROP = d * L + Tồn_Kho_An_Toàn, trong đó Tồn_Kho_An_Toàn = z * sigma_L (với z là hệ số phân phối chuẩn tương ứng với mức dịch vụ chu kỳ mong muốn)",
            "ROP = d * L trừ đi tiền thưởng của giám đốc điều hành",
            "ROP = 0 vì sự không chắc chắn không thể mô hình hóa trong ERP",
            "ROP được chia cho căn bậc hai của 365"
        ],
        "correct_answer": 0,
        "explanation_en": "Under demand uncertainty during lead time L, safety stock SS = z * sigma_L buffers against demand spikes, preventing stockouts up to the specified service level probability.",
        "explanation_vi": "Khi nhu cầu bất định trong thời gian giao hàng, điểm đặt hàng lại ROP được cộng thêm tồn kho an toàn SS = z * sigma_L để chống sốc nhu cầu và bảo đảm mức dịch vụ cam kết."
    })

    questions.append({
        "id": "QUES-173",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "ERP Material Master Sourcing Configuration",
        "difficulty": "Advanced",
        "question_en": "In SAP S/4HANA (or equivalent enterprise ERP), what lot-sizing procedure code corresponds to the Wilson Economic Order Quantity model?",
        "question_vi": "Trong SAP S/4HANA (hoặc ERP doanh nghiệp tương đương), mã quy trình định cỡ lô (Lot-Sizing Procedure) nào tương ứng với mô hình Lượng Đặt Hàng Kinh Tế Wilson?",
        "options_en": [
            "Optimum / Economic Lot Size (e.g., Procedure 'WI' or periodic balancing procedures based on Harris-Wilson algorithms)",
            "Lot-for-Lot (EX) ordering exact net requirement without batching",
            "Fixed Order Quantity (FX) hardcoded to a static number",
            "Replenish to Maximum Stock Level (HB)"
        ],
        "options_vi": [
            "Định cỡ lô Tối ưu / Kinh tế (Optimum Lot Size - như mã 'WI' hoặc các quy trình cân đối chi phí động dựa trên thuật toán Harris-Wilson)",
            "Lot-for-Lot (EX) - Đặt hàng đúng theo nhu cầu tịnh không gom lô",
            "Định cỡ lô Cố định (FX) - Luôn đặt đúng một con số tĩnh cứng",
            "Bổ sung lên mức tồn kho tối đa (HB)"
        ],
        "correct_answer": 0,
        "explanation_en": "SAP MRP uses optimum lot-sizing procedures (e.g., Groff heuristic, Least Unit Cost, or Harris-Wilson) configured in the Material Master MRP 1 view.",
        "explanation_vi": "Trong SAP, view MRP 1 của hồ sơ vật tư cho phép chọn phương pháp định cỡ lô kinh tế (Optimum Lot Size) để hệ thống tự động cân đối chi phí lưu kho và đặt hàng."
    })

    questions.append({
        "id": "QUES-174",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Inflationary Holding Cost Adjustment",
        "difficulty": "Advanced",
        "question_en": "During rapid inflation where the replacement cost of tires rises 20% mid-year, how does an ERP inventory controller prevent the system from underestimating holding costs?",
        "question_vi": "Trong thời kỳ lạm phát cao khi giá thay thế của lốp xe tăng 20% vào giữa năm, người quản trị tồn kho ERP cần làm gì để ngăn hệ thống ước tính thấp chi phí lưu kho?",
        "options_en": [
            "Update the Material Master valuation price and index carrying rate h dynamically to current replacement cost c_replacement rather than historical purchase price",
            "Pretend inflation does not exist and keep using 5-year-old cost data",
            "Stop purchasing tires completely",
            "Charge retail dealers a 500% late payment fee"
        ],
        "options_vi": [
            "Cập nhật giá định giá trong Material Master và điều chỉnh chi phí tồn trữ h theo giá thay thế thị trường mới c_replacement thay vì giá mua trong lịch sử",
            "Coi như lạm phát không tồn tại và tiếp tục dùng số liệu chi phí từ 5 năm trước",
            "Ngừng hoàn toàn việc mua lốp xe về bán",
            "Thu phí phạt thanh toán trễ hạn 500% đối với các đại lý bán lẻ"
        ],
        "correct_answer": 0,
        "explanation_en": "Holding cost reflects current capital opportunity and replacement valuation. Failing to update c leads to undersized holding charges and over-ordering during inflation.",
        "explanation_vi": "Chi phí vốn tính trên giá trị tài sản hiện hành; nếu không cập nhật đơn giá mới vào ERP, hệ thống sẽ tính thiếu chi phí lưu kho và đặt các lô hàng quá lớn gây đọng vốn."
    })

    questions.append({
        "id": "QUES-175",
        "exam_id": "EXAM-07",
        "chapter_id": "chap-04",
        "topic": "Warehouse Storage Space Capacity Constraint",
        "difficulty": "Advanced",
        "question_en": "If ACT's tire warehouse has a physical capacity ceiling of 400 tires due to floor space limits, how does this alter the optimal basic EOQ policy Q* = 573?",
        "question_vi": "Nếu kho lốp của ACT có trần sức chứa vật lý tối đa là 400 chiếc do giới hạn diện tích mặt sàn, điều này làm thay đổi chính sách EOQ tối ưu Q* = 573 như thế nào?",
        "options_en": [
            "The physical constraint forces the feasible order quantity down to Q = 400 tires (the active boundary constraint), increasing annual variable cost slightly to $2,565",
            "The warehouse automatically expands its concrete walls",
            "Tires must be stacked on public sidewalks outside the warehouse",
            "The EOQ formula ceases to exist mathematically"
        ],
        "options_vi": [
            "Ràng buộc vật lý buộc lượng đặt hàng khả thi phải giảm xuống Q = 400 lốp (ràng buộc biên kích hoạt), làm tổng chi phí biến đổi tăng nhẹ lên $2,565/năm",
            "Nhà kho sẽ tự động mở rộng các bức tường bê tông",
            "Lốp xe phải được xếp đống ngoài vỉa hè công cộng trước cửa kho",
            "Công thức EOQ bị biến mất hoàn toàn về mặt toán học"
        ],
        "correct_answer": 0,
        "explanation_en": "When optimal unconstrained Q* violates a storage ceiling (573 > 400), convexity ensures that the ceiling itself (Q = 400) is the constrained optimum.",
        "explanation_vi": "Do tính chất lồi của hàm chi phí, khi nghiệm tối ưu Q* = 573 vượt quá sức chứa kho 400 lốp, điểm khả thi tốt nhất chính là điểm chạm trần Q = 400 lốp."
    })

    return questions
