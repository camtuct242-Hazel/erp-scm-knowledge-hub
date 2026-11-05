# -*- coding: utf-8 -*-
# EXAM 08: EOQ with Planned Shortages & Quantity Discounts (chap-05)
# 25 Questions: Q176 to Q200 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q176 - Q185)
    questions.append({
        "id": "QUES-176",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Planned Shortages Concept",
        "difficulty": "Basic",
        "question_en": "What is the defining premise of the EOQ model with Planned Shortages (Backorders)?",
        "question_vi": "Tiền đề định nghĩa của mô hình EOQ có Thiếu hụt Kế hoạch (Planned Shortages / Backorders) là gì?",
        "options_en": [
            "Management deliberately allows stockouts to occur at the end of each cycle because the holding cost savings from maintaining lower peak inventory exceed the shortage penalty costs",
            "Management forgets to place purchase orders on time due to human error",
            "Suppliers deliberately damage 50% of ordered products before delivery",
            "Customers refuse to accept deliveries on rainy days"
        ],
        "options_vi": [
            "Ban quản lý chủ động cho phép xảy ra tình trạng thiếu hàng cuối mỗi chu kỳ vì số tiền tiết kiệm chi phí lưu kho nhờ hạ thấp đỉnh tồn kho lớn hơn chi phí phạt thiếu hàng",
            "Ban quản lý quên không đặt hàng đúng hạn do sơ suất cá nhân",
            "Nhà cung cấp cố tình làm hỏng 50% hàng hóa trước khi giao",
            "Khách hàng từ chối nhận hàng vào những ngày trời mưa"
        ],
        "correct_answer": 0,
        "explanation_en": "Planned shortages deliberately exploit cost trade-offs: holding costs drop significantly because maximum inventory is only (Q - S) instead of Q.",
        "explanation_vi": "Doanh nghiệp chủ động cho phép nợ hàng vì mức tồn kho đỉnh giảm từ Q xuống (Q - S), giúp tiết kiệm chi phí lưu kho vượt trội so với phí phạt thiếu hàng."
    })

    questions.append({
        "id": "QUES-177",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Max Inventory with Planned Shortages",
        "difficulty": "Basic",
        "question_en": "In the EOQ model with planned shortages, if batch replenishment order size is Q and maximum backorder level is S, what is the Maximum Inventory Level held in the warehouse?",
        "question_vi": "Trong mô hình EOQ có thiếu hụt kế hoạch, nếu quy mô lô đặt hàng là Q và mức nợ hàng tối đa là S, thì Mức Tồn Kho Cực Đại trong kho là bao nhiêu?",
        "options_en": [
            "Maximum Inventory Level = Q - S",
            "Maximum Inventory Level = Q + S",
            "Maximum Inventory Level = Q * S",
            "Maximum Inventory Level = S / Q"
        ],
        "options_vi": [
            "Mức Tồn kho Cực đại = Q - S",
            "Mức Tồn kho Cực đại = Q + S",
            "Mức Tồn kho Cực đại = Q * S",
            "Mức Tồn kho Cực đại = S / Q"
        ],
        "correct_answer": 0,
        "explanation_en": "When a batch Q arrives, S units are immediately used to fulfill accumulated backorders, leaving exactly (Q - S) in physical inventory.",
        "explanation_vi": "Khi lô hàng Q vừa nhập kho, S đơn vị được dùng để trả ngay cho các đơn hàng nợ tích lũy, lượng hàng thực tế lưu lại trong kho chỉ là Q - S."
    })

    questions.append({
        "id": "QUES-178",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Optimal Lot Size with Planned Shortages Formula",
        "difficulty": "Basic",
        "question_en": "What is the optimal order quantity formula Q* for the EOQ model with Planned Shortages?",
        "question_vi": "Công thức xác định lượng đặt hàng tối ưu Q* trong mô hình EOQ có Thiếu hụt Kế hoạch là gì?",
        "options_en": [
            "Q* = sqrt((2 * K * D) / h) * sqrt((p + h) / p)",
            "Q* = sqrt((2 * K * D) / h) * sqrt(p / (p + h))",
            "Q* = (2 * K * D) / (p + h)",
            "Q* = sqrt(2 * K * D * p * h)"
        ],
        "options_vi": [
            "Q* = sqrt((2 * K * D) / h) * sqrt((p + h) / p)",
            "Q* = sqrt((2 * K * D) / h) * sqrt(p / (p + h))",
            "Q* = (2 * K * D) / (p + h)",
            "Q* = sqrt(2 * K * D * p * h)"
        ],
        "correct_answer": 0,
        "explanation_en": "The basic EOQ is multiplied by sqrt((p+h)/p), which is always > 1, meaning batch sizes Q* are systematically larger when shortages are allowed.",
        "explanation_vi": "Lô hàng tối ưu được nhân thêm thừa số sqrt((p+h)/p) > 1, có nghĩa là quy mô mỗi lần đặt Q* luôn lớn hơn so với mô hình EOQ cơ bản."
    })

    questions.append({
        "id": "QUES-179",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Optimal Shortage Level Formula",
        "difficulty": "Basic",
        "question_en": "What is the formula for the optimal maximum shortage level S* in the planned shortages model?",
        "question_vi": "Công thức xác định mức thiếu hụt tối đa tối ưu S* trong mô hình thiếu hàng có kế hoạch là gì?",
        "options_en": [
            "S* = (h / (p + h)) * Q*",
            "S* = (p / (p + h)) * Q*",
            "S* = (p + h) / h",
            "S* = Q* / 2"
        ],
        "options_vi": [
            "S* = (h / (p + h)) * Q*",
            "S* = (p / (p + h)) * Q*",
            "S* = (p + h) / h",
            "S* = Q* / 2"
        ],
        "correct_answer": 0,
        "explanation_en": "Optimal backorder level S* is proportional to the holding-to-total penalty ratio: S* = [h / (p + h)] * Q*.",
        "explanation_vi": "Mức nợ hàng tối ưu S* tỷ lệ thuận với tỷ trọng chi phí lưu kho trên tổng chi phí phạt: S* = [h / (p + h)] x Q*."
    })

    questions.append({
        "id": "QUES-180",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Planned Shortage Parameters",
        "difficulty": "Basic",
        "question_en": "In applying the Planned Shortages model to ACT (Table 5.1), what is the value of unit shortage penalty p?",
        "question_vi": "Khi áp dụng mô hình Thiếu hụt Kế hoạch cho ACT (Bảng 5.1), giá trị của chi phí phạt thiếu hụt đơn vị p là bao nhiêu?",
        "options_en": [
            "$7.50 per tire short per year",
            "$4.20 per year",
            "$115.00 per year",
            "$20.00 per year"
        ],
        "options_vi": [
            "$7.50 trên mỗi lốp nợ mỗi năm",
            "$4.20 mỗi năm",
            "$115.00 mỗi năm",
            "$20.00 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Table 5.1 specifies p = $7.50, representing annual backorder management costs, customer goodwill placation, and delayed revenue.",
        "explanation_vi": "Bảng 5.1 trong giáo trình quy định p = $7.50/lốp/năm cho chi phí phát sinh do nợ hàng."
    })

    questions.append({
        "id": "QUES-181",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Planned Shortage Optimal Q*",
        "difficulty": "Basic",
        "question_en": "For ACT with D = 6,000, K = $115, h = $4.20, and p = $7.50, what is the optimal batch order quantity Q* with planned shortages?",
        "question_vi": "Đối với ACT với D = 6,000, K = $115, h = $4.20 và p = $7.50, lượng đặt hàng tối ưu Q* khi cho phép thiếu hàng kế hoạch là bao nhiêu?",
        "options_en": [
            "716 tires (approximately 573.2 x 1.249)",
            "573 tires",
            "1,000 tires",
            "257 tires"
        ],
        "options_vi": [
            "716 lốp (khoảng 573.2 x 1.249)",
            "573 lốp",
            "1,000 lốp",
            "257 lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "Multiplier = sqrt((7.50 + 4.20) / 7.50) = sqrt(1.56) = 1.249. Q* = 573.2 * 1.249 = 715.9 -> 716 tires.",
        "explanation_vi": "Thừa số điều chỉnh = căn((7.5 + 4.2) / 7.5) = căn(1.56) = 1.249. Q* = 573.2 x 1.249 = 716 lốp."
    })

    questions.append({
        "id": "QUES-182",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Optimal Shortage S*",
        "difficulty": "Basic",
        "question_en": "For ACT under optimal planned shortages, what is the maximum backorder level S*?",
        "question_vi": "Đối với ACT theo phương án thiếu hàng tối ưu, mức nợ hàng tối đa S* là bao nhiêu?",
        "options_en": [
            "257 tires (4.20 / 11.70 x 716)",
            "459 tires",
            "716 tires",
            "0 tires"
        ],
        "options_vi": [
            "257 lốp (4.20 / 11.70 x 716)",
            "459 lốp",
            "716 lốp",
            "0 lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "S* = (h / (p + h)) * Q* = (4.20 / 11.70) * 715.9 = 0.35897 * 715.9 = 257 tires.",
        "explanation_vi": "S* = (4.20 / 11.70) x 716 = 257 chiếc lốp nợ tối đa vào cuối chu kỳ."
    })

    questions.append({
        "id": "QUES-183",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Max Physical Inventory under Planned Shortages",
        "difficulty": "Basic",
        "question_en": "What is the maximum physical inventory held in ACT's warehouse under the planned shortages model?",
        "question_vi": "Mức tồn kho vật lý cực đại thực tế được lưu trữ trong kho của ACT theo mô hình thiếu hàng có kế hoạch là bao nhiêu?",
        "options_en": [
            "459 tires (716 - 257)",
            "716 tires",
            "573 tires",
            "1,000 tires"
        ],
        "options_vi": [
            "459 lốp (716 - 257)",
            "716 lốp",
            "573 lốp",
            "1,000 lốp"
        ],
        "correct_answer": 0,
        "explanation_en": "Maximum inventory = Q* - S* = 716 - 257 = 459 tires. Notice this is substantially lower than basic EOQ peak of 573 tires.",
        "explanation_vi": "Tồn kho cực đại = Q* - S* = 716 - 257 = 459 lốp. Mức này thấp hơn rõ rệt so với đỉnh 573 lốp của EOQ cơ bản."
    })

    questions.append({
        "id": "QUES-184",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Planned Shortages TVC*",
        "difficulty": "Basic",
        "question_en": "What is ACT's Total Variable Cost TVC* under the optimal planned shortages policy?",
        "question_vi": "Tổng chi phí biến đổi tồn kho TVC* của ACT theo chính sách thiếu hàng kế hoạch tối ưu là bao nhiêu?",
        "options_en": [
            "$1,927.56 per year",
            "$2,407.48 per year",
            "$2,790.00 per year",
            "$3,500.00 per year"
        ],
        "options_vi": [
            "$1,927.56 mỗi năm",
            "$2,407.48 mỗi năm",
            "$2,790.00 mỗi năm",
            "$3,500.00 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "TVC* = $2,407.48 * sqrt(p / (p + h)) = $2,407.48 * sqrt(7.50 / 11.70) = $2,407.48 * 0.8006 = $1,927.56 per year.",
        "explanation_vi": "TVC* = $2,407.48 x căn(7.5 / 11.7) = $1,927.56/năm, tiết kiệm thêm gần 20% so với EOQ cơ bản."
    })

    questions.append({
        "id": "QUES-185",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Quantity Discount Schedule Definition",
        "difficulty": "Basic",
        "question_en": "In an all-units quantity discount pricing schedule, how does the unit price c(Q) change?",
        "question_vi": "Trong biểu giá chiết khấu toàn bộ số lượng (All-units quantity discount), đơn giá mua c(Q) thay đổi như thế nào?",
        "options_en": [
            "The reduced price applies to ALL units in the entire order once the batch size reaches or exceeds a designated volume threshold (breakpoint)",
            "The discount only applies to the single final unit purchased",
            "The unit price increases as order size grows",
            "The supplier gives away 100 free tires randomly"
        ],
        "options_vi": [
            "Mức giá giảm được áp dụng cho TOÀN BỘ các đơn vị trong cả lô hàng một khi quy mô đơn hàng đạt hoặc vượt qua ngưỡng số lượng quy định (breakpoint)",
            "Mức giá chiết khấu chỉ áp dụng cho duy nhất một đơn vị hàng cuối cùng được mua",
            "Đơn giá mua ngày càng đắt hơn khi quy mô đơn hàng càng tăng",
            "Nhà cung cấp tặng ngẫu nhiên 100 chiếc lốp miễn phí"
        ],
        "correct_answer": 0,
        "explanation_en": "In all-units discounts, qualifying for a breakpoint lowers the unit price for every single unit in that order batch.",
        "explanation_vi": "Trong chiết khấu toàn bộ số lượng, chỉ cần đơn hàng chạm ngưỡng breakpoint là toàn bộ các sản phẩm trong lô đều được hưởng đơn giá rẻ mới."
    })

    # Intermediate (Q186 - Q195)
    questions.append({
        "id": "QUES-186",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Quantity Discount Pricing Tiers",
        "difficulty": "Intermediate",
        "question_en": "According to Table 5.3 in the textbook, what are Eversafe's quantity discount price breaks for ACT?",
        "question_vi": "Theo Bảng 5.3 trong giáo trình, các mức giá chiết khấu theo số lượng mà hãng Eversafe chào cho ACT là gì?",
        "options_en": [
            "Tier 1 (0-749 tires): $20.00; Tier 2 (750-1,999 tires): $19.80 (1% off); Tier 3 (>=2,000 tires): $19.60 (2% off)",
            "Tier 1: $20.00; Tier 2: $15.00; Tier 3: $10.00",
            "Tier 1: $20.00; Tier 2: $19.00; Tier 3: $18.00",
            "All tires are $20.00 with zero discounts"
        ],
        "options_vi": [
            "Mức 1 (0-749 lốp): $20.00; Mức 2 (750-1,999 lốp): $19.80 (giảm 1%); Mức 3 (>=2,000 lốp): $19.60 (giảm 2%)",
            "Mức 1: $20.00; Mức 2: $15.00; Mức 3: $10.00",
            "Mức 1: $20.00; Mức 2: $19.00; Mức 3: $18.00",
            "Mọi đơn hàng đều có giá $20.00 không có chiết khấu nào"
        ],
        "correct_answer": 0,
        "explanation_en": "Table 5.3 defines 3 tiers: 0-749 ($20), 750-1,999 ($19.80, 1% discount), and >=2,000 ($19.60, 2% discount).",
        "explanation_vi": "Bảng 5.3 nêu rõ 3 bậc giá: 0-749 lốp giá $20; 750-1,999 lốp giá $19.80 (chiết khấu 1%); từ 2,000 lốp trở lên giá $19.60 (chiết khấu 2%)."
    })

    questions.append({
        "id": "QUES-187",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Total Cost Formula for Quantity Discounts",
        "difficulty": "Intermediate",
        "question_en": "Why must Total Cost TC(Q) = c(Q)*D + K*(D/Q) + h(Q)*(Q/2) be evaluated instead of TVC alone under quantity discounts?",
        "question_vi": "Vì sao phải đánh giá Tổng Chi Phí Toàn Phần TC(Q) = c(Q)*D + K*(D/Q) + h(Q)*(Q/2) thay vì chỉ xét riêng TVC trong mô hình chiết khấu số lượng?",
        "options_en": [
            "Because unit purchase cost c(Q) is no longer constant across tiers; annual purchase expenditure c(Q)*D changes dynamically and often dwarfs setup and holding costs",
            "Because taxes are only paid when buying in bulk",
            "Because shipping trucks charge zero freight when discounts apply",
            "Because Excel cannot compute square roots without total cost"
        ],
        "options_vi": [
            "Vì đơn giá mua c(Q) không còn là hằng số giữa các bậc giá; tổng tiền mua hàng c(Q)*D biến động mạnh và thường có quy mô lớn áp đảo chi phí đặt hàng và lưu kho",
            "Vì thuế chỉ phải nộp khi mua hàng với số lượng lớn",
            "Vì các xe tải vận chuyển miễn phí cước hoàn toàn khi có chiết khấu",
            "Vì Excel không thể tính căn bậc hai nếu thiếu tổng chi phí"
        ],
        "correct_answer": 0,
        "explanation_en": "When unit price c changes, annual purchasing cost c*D varies by thousands of dollars, making it a primary decision trade-off variable.",
        "explanation_vi": "Khi giá c giảm 1-2%, trên quy mô 6,000 lốp, doanh nghiệp tiết kiệm được $1,200 - $2,400 tiền mua hàng, do đó bắt buộc phải đưa c*D vào hàm mục tiêu."
    })

    questions.append({
        "id": "QUES-188",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Tier 2 Unconstrained EOQ Feasibility",
        "difficulty": "Intermediate",
        "question_en": "For ACT Tier 2 (c = $19.80, h = 0.21 * 19.80 = $4.158), the unconstrained formula yields Q2* = 576.1 tires. Why is this solution INFEASIBLE?",
        "question_vi": "Ở Mức giá 2 của ACT (c = $19.80, h = 0.21 x 19.80 = $4.158), công thức tự do cho Q2* = 576.1 lốp. Vì sao nghiệm này KHÔNG KHẢ THI?",
        "options_en": [
            "Because 576.1 is outside the qualifying range for Tier 2 (750 to 1,999 tires); Eversafe will not sell at $19.80 for an order of 576 tires",
            "Because Eversafe does not manufacture tires in batches of 576",
            "Because 576 is an odd number",
            "Because the ACT warehouse has collapsed"
        ],
        "options_vi": [
            "Vì 576.1 nằm ngoài dải số lượng áp dụng của Mức 2 (750 đến 1,999 lốp); Eversafe sẽ không bán giá ưu đãi $19.80 nếu chỉ đặt 576 chiếc",
            "Vì Eversafe không sản xuất lốp theo lô 576 chiếc",
            "Vì 576 là một số lẻ",
            "Vì kho hàng của ACT đã bị sập"
        ],
        "correct_answer": 0,
        "explanation_en": "To qualify for the $19.80 price, the order must be at least 750 tires. Q = 576 falls into Tier 1 ($20.00), making Q=576 at $19.80 economically invalid.",
        "explanation_vi": "Để được mua giá $19.80, đơn hàng tối thiểu phải từ 750 lốp. Đặt 576 lốp thì nhà cung cấp chỉ tính giá Mức 1 ($20.00), do đó nghiệm này không khả thi."
    })

    questions.append({
        "id": "QUES-189",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Evaluating Breakpoint at Q = 750",
        "difficulty": "Intermediate",
        "question_en": "When an unconstrained EOQ lies below the price break range (576 < 750), why must the cost be evaluated at the lower boundary (breakpoint Q = 750)?",
        "question_vi": "Khi EOQ lý thuyết nằm bên trái dải giá chiết khấu (576 < 750), vì sao ta bắt buộc phải đánh giá chi phí tại điểm ngưỡng cận dưới (breakpoint Q = 750)?",
        "options_en": [
            "Because for any Q > 576, the Total Cost curve is strictly increasing; therefore, the lowest cost within the feasible interval [750, 1999] occurs at the lowest possible quantity, Q = 750",
            "Because suppliers demand that all orders end in a zero",
            "Because 750 is the legal maximum truckload weight limit",
            "Because ACT warehouse workers only work 750 minutes per week"
        ],
        "options_vi": [
            "Vì với mọi Q > 576, đường Tổng Chi Phí là hàm đơn điệu tăng; do đó điểm có chi phí thấp nhất trong khoảng khả thi [750, 1999] chính là điểm cận dưới nhỏ nhất Q = 750",
            "Vì nhà cung cấp yêu cầu mọi đơn hàng phải có số cuối là 0",
            "Vì 750 là giới hạn tải trọng xe tải tối đa theo luật",
            "Vì công nhân kho ACT chỉ làm việc 750 phút mỗi tuần"
        ],
        "correct_answer": 0,
        "explanation_en": "By convexity, past the minimum (Q > 576), total cost rises continuously. The closest feasible point to the minimum is the left boundary breakpoint Q = 750.",
        "explanation_vi": "Do tính lồi, qua điểm cực tiểu 576 thì chi phí tăng dần. Do đó, điểm khả thi gần cực tiểu nhất và có chi phí rẻ nhất trong dải chính là ngưỡng 750 lốp."
    })

    questions.append({
        "id": "QUES-190",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Total Cost at Q = 750",
        "difficulty": "Intermediate",
        "question_en": "What is ACT's Total Annual Cost TC at the Tier 2 breakpoint Q = 750 tires?",
        "question_vi": "Tổng Chi Phí Hàng Năm TC của ACT tại điểm ngưỡng Mức 2 (Q = 750 lốp) là bao nhiêu?",
        "options_en": [
            "$121,279.25 per year (Purchase: $118,800 + Setup: $920 + Holding: $1,559.25)",
            "$122,407.48 per year",
            "$122,061.00 per year",
            "$115,000.00 per year"
        ],
        "options_vi": [
            "$121,279.25 mỗi năm (Mua hàng: $118,800 + Đặt hàng: $920 + Lưu kho: $1,559.25)",
            "$122,407.48 mỗi năm",
            "$122,061.00 mỗi năm",
            "$115,000.00 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Purchase = $19.80 * 6,000 = $118,800. Setup = $115 * (6,000/750) = $920. Holding = (0.21 * $19.80) * (750/2) = $4.158 * 375 = $1,559.25. Total TC = $121,279.25.",
        "explanation_vi": "Tiền mua = $19.80 x 6,000 = $118,800. Đặt hàng = $115 x 8 = $920. Lưu kho = $4.158 x 375 = $1,559.25. Tổng TC = $121,279.25/năm."
    })

    questions.append({
        "id": "QUES-191",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Total Cost at Q = 2,000",
        "difficulty": "Intermediate",
        "question_en": "What is ACT's Total Annual Cost TC if it orders at the Tier 3 breakpoint Q = 2,000 tires to capture the 2% discount ($19.60)?",
        "question_vi": "Tổng Chi Phí Hàng Năm TC của ACT là bao nhiêu nếu đặt tại điểm ngưỡng Mức 3 (Q = 2,000 lốp) để nhận mức chiết khấu 2% ($19.60)?",
        "options_en": [
            "$122,061.00 per year (Purchase: $117,600 + Setup: $345 + Holding: $4,116)",
            "$121,279.25 per year",
            "$122,407.48 per year",
            "$130,000.00 per year"
        ],
        "options_vi": [
            "$122,061.00 mỗi năm (Mua hàng: $117,600 + Đặt hàng: $345 + Lưu kho: $4,116)",
            "$121,279.25 mỗi năm",
            "$122,407.48 mỗi năm",
            "$130,000.00 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Purchase = $19.60 * 6,000 = $117,600. Setup = $115 * (6,000/2,000) = $345. Holding = (0.21 * $19.60) * (2,000/2) = $4.116 * 1,000 = $4,116. Total TC = $122,061.00.",
        "explanation_vi": "Tiền mua = $19.60 x 6,000 = $117,600. Đặt hàng = $115 x 3 = $345. Lưu kho = $4.116 x 1,000 = $4,116. Tổng TC = $122,061.00/năm."
    })

    questions.append({
        "id": "QUES-192",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ACT Quantity Discount Optimal Decision",
        "difficulty": "Intermediate",
        "question_en": "Comparing all three tiers for ACT: Tier 1 at Q=573 ($122,407.48), Tier 2 at Q=750 ($121,279.25), and Tier 3 at Q=2000 ($122,061.00), what is the optimal purchasing decision?",
        "question_vi": "So sánh cả 3 mức của ACT: Mức 1 tại Q=573 ($122,407.48), Mức 2 tại Q=750 ($121,279.25) và Mức 3 tại Q=2000 ($122,061.00), quyết định mua hàng tối ưu là gì?",
        "options_en": [
            "Order exactly Q = 750 tires at Tier 2 breakpoint, achieving the absolute minimum Total Annual Cost of $121,279.25",
            "Order 2,000 tires to get the biggest discount percentage",
            "Order 573 tires to keep warehouse stock lean",
            "Order 1,000 tires because it is a round number"
        ],
        "options_vi": [
            "Đặt đúng Q = 750 lốp tại điểm ngưỡng Mức 2, đạt Tổng Chi Phí Hàng Năm thấp nhất toàn cục là $121,279.25",
            "Đặt 2,000 lốp để nhận tỷ lệ phần trăm chiết khấu cao nhất",
            "Đặt 573 lốp để giữ lượng tồn kho tinh gọn",
            "Đặt 1,000 lốp vì đó là con số tròn chẵn dễ nhớ"
        ],
        "correct_answer": 0,
        "explanation_en": "Q = 750 strikes the perfect balance: it captures the 1% purchase savings while avoiding the excessive holding cost penalty incurred at Q = 2,000 ($4,116 holding).",
        "explanation_vi": "Đặt Q = 750 là quyết định tối ưu: vừa ăn được chiết khấu 1% giá mua, vừa không bị đọng vốn lưu kho quá nặng như mức 2,000 lốp (phí lưu kho vọt lên $4,116)."
    })

    questions.append({
        "id": "QUES-193",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Why Tier 3 at Q = 2,000 Was Inferior",
        "difficulty": "Intermediate",
        "question_en": "Why was the 2% discount at Q = 2,000 financially inferior to the 1% discount at Q = 750 for ACT?",
        "question_vi": "Vì sao mức chiết khấu 2% tại Q = 2,000 lại kém hiệu quả tài chính hơn mức chiết khấu 1% tại Q = 750 đối với ACT?",
        "options_en": [
            "The additional $1,200 saved in purchase price was completely overwhelmed by a $2,556.75 surge in annual inventory holding costs from storing 1,000 average tires",
            "Because Eversafe tires deteriorate after 10 days in storage",
            "Because the bank charged a penalty for writing large checks",
            "Because retail tire dealers refuse to buy tires from large orders"
        ],
        "options_vi": [
            "Khoản tiền tiết kiệm thêm $1,200 nhờ giá mua rẻ bị nuốt chửng hoàn toàn bởi khoản tăng vọt $2,556.75 của chi phí lưu kho khi phải giữ tới 1,000 lốp bình quân",
            "Vì lốp xe Eversafe bị thoái hóa sau 10 ngày lưu kho",
            "Vì ngân hàng phạt tiền khi ký séc chi trả giá trị lớn",
            "Vì các đại lý bán lẻ từ chối mua lốp từ các đơn hàng lớn"
        ],
        "correct_answer": 0,
        "explanation_en": "Holding 1,000 average tires (Q=2,000) drove holding cost to $4,116 (up from $1,559 at Q=750), exceeding the incremental $1,200 purchasing price savings.",
        "explanation_vi": "Tồn kho bình quân 1,000 lốp làm chi phí giữ hàng tăng thêm $2,556.75, lớn hơn rất nhiều so với khoản tiền $1,200 tiết kiệm thêm được từ giá mua."
    })

    questions.append({
        "id": "QUES-194",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Holding Cost as a Percentage of Discounted Price",
        "difficulty": "Intermediate",
        "question_en": "When unit purchase price c drops due to quantity discounts, why does unit holding cost h also drop in the ACT analysis?",
        "question_vi": "Khi đơn giá mua c giảm nhờ chiết khấu số lượng, vì sao chi phí lưu kho đơn vị h cũng giảm theo trong phân tích của ACT?",
        "options_en": [
            "Because holding cost is tied to capital opportunity cost and taxes, modeled as a fixed percentage rate (h = I * c = 0.21 * c)",
            "Because warehouse landlords reduce rent when goods are cheap",
            "Because insurance companies charge zero premium for discounted goods",
            "Because cheaper tires physically occupy less cubic volume in warehouse racks"
        ],
        "options_vi": [
            "Vì chi phí lưu kho gắn liền với chi phí cơ hội vốn và thuế, được mô hình hóa theo tỷ lệ phần trăm cố định trên giá trị hàng (h = I x c = 0.21 x c)",
            "Vì chủ nhà kho giảm tiền thuê mặt bằng khi hàng hóa có giá rẻ",
            "Vì các công ty bảo hiểm miễn phí bảo hiểm cho hàng mua chiết khấu",
            "Vì lốp xe giá rẻ chiếm ít thể tích không gian hơn trên kệ hàng"
        ],
        "correct_answer": 0,
        "explanation_en": "Capital carrying charges and ad valorem taxes are proportional to asset value: h(c) = 0.21 * c. As c decreases ($20 -> $19.80 -> $19.60), h drops ($4.20 -> $4.158 -> $4.116).",
        "explanation_vi": "Chi phí vốn tính trên giá trị đầu tư: h = 0.21 x c. Khi đơn giá giảm thì vốn bị chôn trong mỗi chiếc lốp giảm theo, làm h giảm tương ứng."
    })

    questions.append({
        "id": "QUES-195",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Excel Template Analytical Solver for Quantity Discounts",
        "difficulty": "Intermediate",
        "question_en": "According to Figure 5.6 in the textbook, how does the Excel analytical template determine the global optimal order quantity across multiple discount tiers?",
        "question_vi": "Theo Hình 5.6 trong giáo trình, biểu mẫu phân tích Excel xác định lượng đặt hàng tối ưu toàn cục giữa các bậc chiết khấu như thế nào?",
        "options_en": [
            "It computes the unconstrained EOQ for each tier, determines feasibility within the tier range, evaluates candidate quantities (feasible EOQs and boundary breakpoints), and picks the Minimum Total Cost",
            "It uses a random number generator to pick a tier",
            "It always selects the tier with the highest discount",
            "It averages the prices across all tiers and calculates a single EOQ"
        ],
        "options_vi": [
            "Tính EOQ lý thuyết cho từng bậc, kiểm tra tính khả thi trong dải số lượng, tính tổng chi phí cho các điểm ứng viên (EOQ khả thi và các điểm ngưỡng breakpoint), và chọn điểm có Tổng Chi Phí nhỏ nhất",
            "Dùng hàm tạo số ngẫu nhiên để chọn bậc giá",
            "Luôn luôn tự động chọn bậc giá có mức chiết khấu cao nhất",
            "Lấy trung bình cộng giá của các bậc rồi tính một số EOQ duy nhất"
        ],
        "correct_answer": 0,
        "explanation_en": "The algorithmic procedure calculates Q_k* for each tier k, checks interval feasibility, evaluates TC at all feasible EOQs and breakpoint thresholds, and selects min(TC).",
        "explanation_vi": "Quy trình chuẩn: Tính Q* cho từng mức, kiểm tra tính khả thi, đánh giá TC tại các điểm EOQ khả thi và các điểm ngưỡng breakpoint, rồi chọn min(TC)."
    })

    # Advanced (Q196 - Q200)
    questions.append({
        "id": "QUES-196",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "BA Risk Assessment of Planned Shortages",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is reviewing ACT's proposal to implement Planned Shortages (Backorders). What strategic market risk must the BA highlight to executive leadership?",
        "question_vi": "Một Business Analyst đang thẩm định đề xuất áp dụng Thiếu hàng Kế hoạch (Backorders) của ACT. Rủi ro thị trường chiến lược nào mà BA bắt buộc phải cảnh báo tới ban giám đốc?",
        "options_en": [
            "If competitor distributors offer immediate same-day delivery, retail auto service stations may cancel backorders and permanently defect to rival tire brands, destroying customer lifetime value",
            "Tires in shortage might explode in the factory",
            "The mathematical calculus formula will be banned by state regulators",
            "Tire sizes will automatically change when backordered"
        ],
        "options_vi": [
            "Nếu các nhà phân phối đối thủ giao hàng ngay trong ngày, các gara sửa xe bán lẻ có thể hủy đơn nợ và chuyển sang mua vĩnh viễn từ thương hiệu khác, phá hủy giá trị trọn đời khách hàng",
            "Lốp xe bị nợ hàng có thể bị phát nổ trong nhà máy sản xuất",
            "Công thức đạo hàm toán học sẽ bị các cơ quan quản lý bang cấm sử dụng",
            "Kích thước lốp xe sẽ tự động biến dạng khi bị đưa vào trạng thái nợ hàng"
        ],
        "correct_answer": 0,
        "explanation_en": "The backorder model assumes customer patience. In highly competitive wholesale markets, customers defect to competitors immediately upon stockout, turning backorders into fatal lost sales.",
        "explanation_vi": "Mô hình backorder giả định khách hàng kiên nhẫn chờ đợi. Trong thị trường cạnh tranh gay gắt, khách sẽ quay sang đối thủ ngay lập tức, biến đơn hàng nợ thành mất khách vĩnh viễn."
    })

    questions.append({
        "id": "QUES-197",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Incremental vs All-Units Quantity Discounts in ERP",
        "difficulty": "Advanced",
        "question_en": "How does an 'Incremental Quantity Discount' schedule differ structurally from Eversafe's 'All-Units' schedule, and how does this affect ERP pricing configuration?",
        "question_vi": "Biểu giá 'Chiết khấu Lũy tiến Từng phần' (Incremental Discount) khác biệt về cấu trúc như thế nào so với biểu giá 'Toàn bộ Số lượng' của Eversafe, và ảnh hưởng ra sao đến cấu hình ERP?",
        "options_en": [
            "Incremental discounts apply price cuts only to units purchased WITHIN each successive bracket (like progressive income tax brackets), resulting in a continuous, kinked piecewise linear cost curve without downward drops",
            "Incremental discounts charge higher prices as volume grows",
            "Incremental discounts require cash payments exclusively",
            "All-units discounts apply only to damaged goods"
        ],
        "options_vi": [
            "Chiết khấu lũy tiến chỉ áp dụng giá giảm cho các đơn vị nằm TRONG từng khoảng số lượng kế tiếp (giống như biểu thuế thu nhập lũy tiến), tạo ra đường chi phí mua liên tục có góc gấp khúc mà không bị đứt gãy sụt giảm đột ngột",
            "Chiết khấu lũy tiến tính giá ngày càng đắt hơn khi mua nhiều hơn",
            "Chiết khấu lũy tiến bắt buộc thanh toán bằng tiền mặt",
            "Chiết khấu toàn bộ số lượng chỉ áp dụng cho hàng bị lỗi"
        ],
        "correct_answer": 0,
        "explanation_en": "All-units discounts create discontinuities (sudden drops at breakpoints), which can encourage waste (ordering more to pay less total). Incremental discounts maintain continuity.",
        "explanation_vi": "Chiết khấu toàn bộ tạo ra các bước nhảy đứt gãy giá, đôi khi mua nhiều hơn lại trả ít tiền hơn. Chiết khấu lũy tiến từng phần bảo đảm tính liên tục và công bằng."
    })

    questions.append({
        "id": "QUES-198",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "ERP Purchase Info Record (PIR) Configuration",
        "difficulty": "Advanced",
        "question_en": "In SAP S/4HANA MM (Materials Management), where are vendor volume discount scales (breakpoints and stepped prices) configured?",
        "question_vi": "Trong phân hệ SAP S/4HANA MM (Quản lý Vật tư), bảng thang giá chiết khấu số lượng của nhà cung cấp (breakpoints và đơn giá bậc thang) được cấu hình ở đâu?",
        "options_en": [
            "In the Purchasing Info Record (PIR) under Condition Scales (Condition Type PB00 / PBXX)",
            "In the Employee Travel Expense ledger",
            "In the Customer Credit Rating master data",
            "In the factory electrical circuit breaker diagram"
        ],
        "options_vi": [
            "Trong Bản ghi Thông tin Mua hàng (Purchasing Info Record - PIR) tại phần Thang giá Điều kiện (Condition Scales - Loại điều kiện PB00 / PBXX)",
            "Trong sổ cái chi phí công tác của nhân viên",
            "Trong hồ sơ dữ liệu chủ hạn mức tín dụng khách hàng",
            "Trong sơ đồ cầu dao điện của nhà xưởng"
        ],
        "correct_answer": 0,
        "explanation_en": "SAP Purchasing Info Records (PIR) maintain vendor-material price condition scales. When a PO is created, SAP pricing automatically reads order quantity Q and pulls the matching tier price.",
        "explanation_vi": "Bản ghi PIR lưu trữ thang giá chiết khấu của nhà cung cấp. Khi tạo đơn PO, hệ thống tự động kiểm tra số lượng đặt Q và áp đơn giá ưu đãi tương ứng."
    })

    questions.append({
        "id": "QUES-199",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "Forward Buying and Bullwhip Induced by Discounts",
        "difficulty": "Advanced",
        "question_en": "When suppliers offer temporary trade promotions or volume quantity discounts, how does this practice induce artificial demand swings (Forward Buying) in the supply chain?",
        "question_vi": "Khi nhà cung cấp đưa ra các chương trình khuyến mãi ngắn hạn hoặc chiết khấu số lượng, hành vi này kích hoạt hiện tượng dao động nhu cầu ảo (Forward Buying) trong chuỗi cung ứng như thế nào?",
        "options_en": [
            "Distributors purchase massive forward stockpiles far exceeding real-time consumption to capture discounts, causing subsequent order droughts and amplifying the Bullwhip Effect",
            "Retail customers stop driving automobiles entirely",
            "Suppliers are forced to burn excess inventory in public",
            "Truck drivers refuse to deliver discounted tires"
        ],
        "options_vi": [
            "Các nhà phân phối mua tích trữ đầu cơ (Forward Buying) số lượng khổng lồ vượt xa nhu cầu tiêu thụ thực tế để ôm giá rẻ, dẫn đến khoảng trống cạn kiệt đơn hàng ở các kỳ sau và khuếch đại hiệu ứng Bullwhip",
            "Người tiêu dùng ngừng lái ô tô hoàn toàn",
            "Nhà cung cấp bị buộc phải đốt bỏ hàng tồn kho ngoài trời",
            "Tài xế xe tải từ chối chở các lô lốp có chiết khấu"
        ],
        "correct_answer": 0,
        "explanation_en": "Quantity discounts trigger forward buying: buyers hoard stock at discounted rates, masking true steady consumer demand and destabilizing upstream factory schedules.",
        "explanation_vi": "Chiết khấu số lượng kích thích tâm lý đầu cơ gom hàng (Forward buying), tạo ra nhu cầu giả tạo đột biến rồi sau đó là giai đoạn đứng yên, làm nhà máy sản xuất bị rối loạn kế hoạch."
    })

    questions.append({
        "id": "QUES-200",
        "exam_id": "EXAM-08",
        "chapter_id": "chap-05",
        "topic": "BA Negotiation Strategy Using EOQ Breakpoints",
        "difficulty": "Advanced",
        "question_en": "In ACT's case, Tier 3 discount (2%) requires ordering >= 2,000 tires, which incurred excessive holding costs ($122,061). How can a Senior Procurement BA use this mathematical insight in vendor negotiations?",
        "question_vi": "Trong case ACT, Mức 3 (giảm 2%) đòi hỏi đặt >= 2,000 lốp, gây chi phí lưu kho quá đắt ($122,061). Một Senior Procurement BA có thể sử dụng phát hiện toán học này trong đàm phán hợp đồng cung ứng như thế nào?",
        "options_en": [
            "Negotiate a blanket purchase order contract committing to purchase 2,000 tires annually at $19.60, but structured with call-off releases delivered in 4 staggered batches of 500 tires",
            "Threaten to sue Eversafe in federal court for offering discounts",
            "Accept the 2,000-tire delivery and store half the tires in hotel rooms",
            "Demand that Eversafe lower the price to $1.00 per tire"
        ],
        "options_vi": [
            "Đàm phán một Hợp đồng Mua sắm Khung (Blanket Purchase Order) cam kết tổng sản lượng 2,000 lốp/năm với giá $19.60, nhưng chia thành 4 đợt giao hàng nhỏ (Call-off release) mỗi đợt 500 lốp",
            "Đe dọa kiện Eversafe ra tòa án liên bang vì đã dám đưa ra chiết khấu",
            "Chấp nhận nhập 2,000 lốp một lúc rồi đem thuê phòng khách sạn để chứa lốp thừa",
            "Yêu cầu Eversafe phải hạ giá bán lốp xuống còn $1.00"
        ],
        "correct_answer": 0,
        "explanation_en": "A savvy BA negotiates contract pricing based on annual aggregate volume commitment while decoupling physical delivery lot sizes via Blanket Orders with scheduled EDI releases.",
        "explanation_vi": "BA đàm phán đỉnh cao: ký hợp đồng nguyên tắc cam kết tổng sản lượng năm để lấy đơn giá rẻ nhất ($19.60), nhưng phát lệnh giao hàng từng đợt nhỏ (Call-off) để giữ kho luôn tinh gọn."
    })

    return questions
