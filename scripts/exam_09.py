# -*- coding: utf-8 -*-
# EXAM 09: Economic Production Quantity (EPQ) & Gradual Replenishment (chap-05)
# 25 Questions: Q201 to Q225 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q201 - Q210)
    questions.append({
        "id": "QUES-201",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Gradual Replenishment Premise",
        "difficulty": "Basic",
        "question_en": "What operational condition makes the Gradual Replenishment (EPQ) model necessary instead of the basic EOQ model?",
        "question_vi": "Điều kiện vận hành thực tế nào đòi hỏi phải áp dụng mô hình Bổ sung dần (EPQ) thay vì mô hình EOQ cơ bản?",
        "options_en": [
            "Items are manufactured internally and arrive continuously at a finite daily production rate p, rather than arriving instantaneously all at once from an outside vendor",
            "Goods are purchased from an overseas supplier who delivers by air cargo",
            "Warehouse employees work only 1 hour per week",
            "The product can only be manufactured during a full moon"
        ],
        "options_vi": [
            "Sản phẩm được tự sản xuất nội bộ và nhập kho dần dần theo một tốc độ sản xuất hữu hạn p, chứ không phải giao trọn gói tức thời cùng một lúc từ nhà cung ứng bên ngoài",
            "Hàng hóa được mua từ nhà cung cấp nước ngoài giao bằng đường hàng không",
            "Nhân viên nhà kho chỉ làm việc 1 giờ mỗi tuần",
            "Sản phẩm chỉ có thể sản xuất vào những đêm trăng tròn"
        ],
        "correct_answer": 0,
        "explanation_en": "Basic EOQ assumes infinite replenishment speed (instant drop). EPQ models in-house manufacturing where output builds up gradually over the production run duration.",
        "explanation_vi": "EOQ cơ bản giả định hàng về ngay tức khắc. EPQ dành cho sản xuất nội bộ: hàng hoàn thành được đưa dần vào kho theo nhịp độ sản xuất hữu hạn của xưởng máy."
    })

    questions.append({
        "id": "QUES-202",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Production vs Demand Rate Condition",
        "difficulty": "Basic",
        "question_en": "In the Gradual Replenishment model, what mathematical condition must hold between daily production rate p and daily demand rate d?",
        "question_vi": "Trong mô hình Bổ sung dần, điều kiện toán học bắt buộc nào phải thỏa mãn giữa tốc độ sản xuất hàng ngày p và tốc độ nhu cầu hàng ngày d?",
        "options_en": [
            "Production rate p must be strictly greater than demand rate d (p > d)",
            "Production rate p must be exactly zero",
            "Demand rate d must be ten times greater than p",
            "Production rate must equal negative demand"
        ],
        "options_vi": [
            "Tốc độ sản xuất p bắt buộc phải lớn hơn nghiêm ngặt tốc độ tiêu thụ d (p > d)",
            "Tốc độ sản xuất p bắt buộc phải bằng đúng 0",
            "Tốc độ nhu cầu d phải lớn gấp 10 lần tốc độ sản xuất p",
            "Tốc độ sản xuất phải bằng số âm của nhu cầu"
        ],
        "correct_answer": 0,
        "explanation_en": "If p <= d, the production facility can never satisfy demand and inventory will never accumulate, resulting in continuous shortages.",
        "explanation_vi": "Nếu tốc độ sản xuất p nhỏ hơn hoặc bằng nhu cầu d, phân xưởng không bao giờ tích lũy được hàng tồn kho và dây chuyền sẽ bị đói vật tư liên tục."
    })

    questions.append({
        "id": "QUES-203",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Case Profile",
        "difficulty": "Basic",
        "question_en": "In the SOCA case study, what product does the company manufacture in-house for assembly into its television sets?",
        "question_vi": "Trong case study SOCA, công ty tự sản xuất nội bộ linh kiện gì để lắp ráp vào các bộ máy tivi của mình?",
        "options_en": [
            "Internal audio speakers",
            "Glass cathode ray display tubes",
            "Wooden cabinet furniture frames",
            "Plastic remote controls"
        ],
        "options_vi": [
            "Cụm loa âm thanh bên trong tivi (Audio speakers)",
            "Đèn hình thủy tinh cathode ray",
            "Khung vỏ gỗ trang trí tivi",
            "Thiết bị điều khiển từ xa bằng nhựa"
        ],
        "correct_answer": 0,
        "explanation_en": "SOCA operates an internal fabrication line that produces speakers for its television set assembly plant.",
        "explanation_vi": "SOCA vận hành một phân xưởng tự sản xuất loa để cấp cho dây chuyền lắp ráp tivi hoàn chỉnh."
    })

    questions.append({
        "id": "QUES-204",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Daily Demand & Production Rates",
        "difficulty": "Basic",
        "question_en": "What are the daily demand rate d and daily production rate p in the SOCA case study?",
        "question_vi": "Tốc độ nhu cầu tiêu thụ hàng ngày d và tốc độ sản xuất hàng ngày p trong case study SOCA là bao nhiêu?",
        "options_en": [
            "Daily demand d = 1,000 speakers/day; Daily production p = 3,000 speakers/day",
            "Daily demand d = 3,000 speakers/day; Daily production p = 1,000 speakers/day",
            "Both d and p equal 5,000 speakers/day",
            "Daily demand d = 500 speakers/day; Daily production p = 500 speakers/day"
        ],
        "options_vi": [
            "Nhu cầu hàng ngày d = 1,000 loa/ngày; Năng lực sản xuất p = 3,000 loa/ngày",
            "Nhu cầu hàng ngày d = 3,000 loa/ngày; Năng lực sản xuất p = 1,000 loa/ngày",
            "Cả d và p đều bằng 5,000 loa/ngày",
            "Nhu cầu hàng ngày d = 500 loa/ngày; Năng lực sản xuất p = 500 loa/ngày"
        ],
        "correct_answer": 0,
        "explanation_en": "SOCA TV assembly consumes d = 1,000 speakers/day, while the speaker manufacturing line produces p = 3,000 speakers/day when operating.",
        "explanation_vi": "Dây chuyền lắp ráp tivi cần d = 1,000 loa/ngày; xưởng loa khi vận hành sản xuất được p = 3,000 loa/ngày (gấp 3 lần tốc độ dùng)."
    })

    questions.append({
        "id": "QUES-205",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Annual Demand",
        "difficulty": "Basic",
        "question_en": "With 250 working days per year, what is SOCA's total annual demand D for speakers?",
        "question_vi": "Với 250 ngày làm việc mỗi năm, tổng nhu cầu hàng năm D về loa của SOCA là bao nhiêu?",
        "options_en": [
            "250,000 speakers per year (1,000 speakers/day x 250 days)",
            "750,000 speakers per year",
            "30,000 speakers per year",
            "50,000 speakers per year"
        ],
        "options_vi": [
            "250,000 chiếc loa mỗi năm (1,000 loa/ngày x 250 ngày làm việc)",
            "750,000 chiếc loa mỗi năm",
            "30,000 chiếc loa mỗi năm",
            "50,000 chiếc loa mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Annual demand D = daily demand (1,000) * working days (250) = 250,000 speakers per year.",
        "explanation_vi": "Nhu cầu năm D = 1,000 loa/ngày x 250 ngày làm việc = 250,000 chiếc loa/năm."
    })

    questions.append({
        "id": "QUES-206",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Cost Parameters",
        "difficulty": "Basic",
        "question_en": "What are SOCA's cost parameters for unit production cost c, setup cost K, and unit holding cost h?",
        "question_vi": "Các thông số chi phí của SOCA gồm chi phí sản xuất đơn vị c, chi phí thiết lập K và chi phí lưu kho đơn vị h là bao nhiêu?",
        "options_en": [
            "c = $12 per speaker; K = $12,000 per setup; h = $3.60 per speaker in inventory per year",
            "c = $20; K = $115; h = $4.20",
            "c = $1; K = $100; h = $0.50",
            "c = $50; K = $5,000; h = $10.00"
        ],
        "options_vi": [
            "c = $12 trên mỗi loa; K = $12,000 cho mỗi lần thiết lập dây chuyền; h = $3.60 trên mỗi loa lưu kho mỗi năm",
            "c = $20; K = $115; h = $4.20",
            "c = $1; K = $100; h = $0.50",
            "c = $50; K = $5,000; h = $10.00"
        ],
        "correct_answer": 0,
        "explanation_en": "The SOCA case specifies: c = $12/unit, setup cost K = $12,000 per run, and unit holding cost h = $3.60/unit-year.",
        "explanation_vi": "Đề bài SOCA nêu rõ: giá thành xuất xưởng c = $12, chi phí thiết lập máy K = $12,000/lần, chi phí lưu kho h = $3.60/loa/năm."
    })

    questions.append({
        "id": "QUES-207",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Gradual Replenishment Damping Factor",
        "difficulty": "Basic",
        "question_en": "In the SOCA case, what is the numerical value of the gradual replenishment factor (1 - d / p)?",
        "question_vi": "Trong case SOCA, giá trị số của hệ số điều chỉnh bổ sung dần (1 - d / p) là bao nhiêu?",
        "options_en": [
            "2 / 3 (approximately 0.6667, calculated as 1 - 1,000 / 3,000)",
            "1 / 3 (0.3333)",
            "1.0 (no adjustment)",
            "3.0"
        ],
        "options_vi": [
            "2 / 3 (khoảng 0.6667, tính bằng 1 - 1,000 / 3,000)",
            "1 / 3 (0.3333)",
            "1.0 (không điều chỉnh)",
            "3.0"
        ],
        "correct_answer": 0,
        "explanation_en": "Factor = 1 - (1,000 / 3,000) = 1 - 1/3 = 2/3. This scales down inventory accumulation because 1/3 of daily output is immediately assembled.",
        "explanation_vi": "Hệ số bổ sung dần = 1 - (1,000 / 3,000) = 2/3. Điều này phản ánh việc 1/3 sản lượng vừa ra lò đã được rút ngay sang lắp tivi."
    })

    questions.append({
        "id": "QUES-208",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "EPQ Optimal Lot Size Formula",
        "difficulty": "Basic",
        "question_en": "What is the optimal production lot size formula Q* for the Economic Production Quantity (EPQ) model?",
        "question_vi": "Công thức xác định quy mô lô sản xuất tối ưu Q* trong mô hình Lượng Sản Xuất Kinh Tế (EPQ) là gì?",
        "options_en": [
            "Q* = sqrt((2 * K * D) / (h * (1 - d / p)))",
            "Q* = sqrt((2 * K * D) / h) * (1 - d / p)",
            "Q* = sqrt((2 * K * D * h) / (1 - d / p))",
            "Q* = (2 * K * D) / (h * p)"
        ],
        "options_vi": [
            "Q* = sqrt((2 * K * D) / (h * (1 - d / p)))",
            "Q* = sqrt((2 * K * D) / h) * (1 - d / p)",
            "Q* = sqrt((2 * K * D * h) / (1 - d / p))",
            "Q* = (2 * K * D) / (h * p)"
        ],
        "correct_answer": 0,
        "explanation_en": "Because effective holding cost is dampened by (1 - d/p), it appears in the denominator under the root: Q* = sqrt((2*K*D) / [h*(1 - d/p)]).",
        "explanation_vi": "Do chi phí lưu kho thực tế được giảm trừ bởi hệ số (1 - d/p), thừa số này nằm dưới mẫu số trong dấu căn: Q* = sqrt(2KD / [h(1 - d/p)])."
    })

    questions.append({
        "id": "QUES-209",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Optimal EPQ Q* Calculation",
        "difficulty": "Basic",
        "question_en": "What is the optimal production lot size Q* for SOCA calculated via the EPQ formula?",
        "question_vi": "Quy mô lô sản xuất tối ưu Q* của SOCA tính toán theo công thức EPQ là bao nhiêu chiếc loa?",
        "options_en": [
            "50,000 speakers per production run",
            "30,000 speakers",
            "100,000 speakers",
            "10,000 speakers"
        ],
        "options_vi": [
            "50,000 chiếc loa cho mỗi đợt sản xuất",
            "30,000 chiếc loa",
            "100,000 chiếc loa",
            "10,000 chiếc loa"
        ],
        "correct_answer": 0,
        "explanation_en": "Q* = sqrt((2 * 12,000 * 250,000) / [3.60 * (2/3)]) = sqrt(6,000,000,000 / 2.40) = sqrt(2,500,000,000) = 50,000 speakers.",
        "explanation_vi": "Q* = căn((2 x 12,000 x 250,000) / [3.60 x (2/3)]) = căn(6 tỷ / 2.40) = căn(2.5 tỷ) = 50,000 chiếc loa."
    })

    questions.append({
        "id": "QUES-210",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Maximum Inventory Formula",
        "difficulty": "Basic",
        "question_en": "What is the formula for Maximum Inventory Level in the EPQ model?",
        "question_vi": "Công thức xác định Mức Tồn Kho Cực Đại trong mô hình EPQ là gì?",
        "options_en": [
            "Maximum Inventory = Q * (1 - d / p)",
            "Maximum Inventory = Q",
            "Maximum Inventory = Q / 2",
            "Maximum Inventory = Q * (d / p)"
        ],
        "options_vi": [
            "Mức Tồn kho Cực đại = Q * (1 - d / p)",
            "Mức Tồn kho Cực đại = Q",
            "Mức Tồn kho Cực đại = Q / 2",
            "Mức Tồn kho Cực đại = Q * (d / p)"
        ],
        "correct_answer": 0,
        "explanation_en": "Production duration is t_p = Q/p. Net accumulation is (p - d). Max inventory = t_p * (p - d) = (Q/p)*(p - d) = Q*(1 - d/p).",
        "explanation_vi": "Thời gian sản xuất t_p = Q/p. Tốc độ tích lũy ròng là (p - d). Tồn kho đỉnh = (Q/p) x (p - d) = Q x (1 - d/p)."
    })

    # Intermediate (Q211 - Q220)
    questions.append({
        "id": "QUES-211",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Current Policy Metrics",
        "difficulty": "Intermediate",
        "question_en": "Under SOCA's historical policy of producing Q = 30,000 speakers per run, what were its production duration, maximum inventory, and average inventory?",
        "question_vi": "Theo chính sách lịch sử của SOCA khi sản xuất lô Q = 30,000 loa/đợt, thời gian chạy máy, tồn kho cực đại và tồn kho bình quân là bao nhiêu?",
        "options_en": [
            "Production run = 10 working days; Maximum inventory = 20,000 speakers; Average inventory = 10,000 speakers",
            "Production run = 30 days; Maximum inventory = 30,000; Average inventory = 15,000",
            "Production run = 1 day; Maximum inventory = 3,000; Average inventory = 1,500",
            "Production run = 20 days; Maximum inventory = 10,000; Average inventory = 5,000"
        ],
        "options_vi": [
            "Thời gian chạy máy = 10 ngày làm việc; Tồn kho cực đại = 20,000 loa; Tồn kho bình quân = 10,000 loa",
            "Thời gian chạy máy = 30 ngày; Tồn kho cực đại = 30,000; Tồn kho bình quân = 15,000",
            "Thời gian chạy máy = 1 ngày; Tồn kho cực đại = 3,000; Tồn kho bình quân = 1,500",
            "Thời gian chạy máy = 20 ngày; Tồn kho cực đại = 10,000; Tồn kho bình quân = 5,000"
        ],
        "correct_answer": 0,
        "explanation_en": "Run time = 30,000 / 3,000 = 10 days. Max inventory = 30,000 * (1 - 1/3) = 20,000 speakers. Average inventory = 20,000 / 2 = 10,000 speakers.",
        "explanation_vi": "Thời gian chạy máy = 30,000 / 3,000 = 10 ngày. Tồn đỉnh = 30,000 x (2/3) = 20,000 loa. Tồn bình quân = 20,000 / 2 = 10,000 loa."
    })

    questions.append({
        "id": "QUES-212",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Current Annual Variable Cost",
        "difficulty": "Intermediate",
        "question_en": "What was SOCA's total variable inventory cost TVC under its historical Q = 30,000 policy?",
        "question_vi": "Tổng chi phí biến đổi tồn kho TVC của SOCA theo chính sách lịch sử Q = 30,000 là bao nhiêu?",
        "options_en": [
            "$136,000 per year (Setup: $100,000 + Holding: $36,000)",
            "$120,000 per year",
            "$3,000,000 per year",
            "$72,000 per year"
        ],
        "options_vi": [
            "$136,000 mỗi năm (Thiết lập máy: $100,000 + Lưu kho: $36,000)",
            "$120,000 mỗi năm",
            "$3,000,000 mỗi năm",
            "$72,000 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Setups = 250,000 / 30,000 = 8.33 runs. Annual Setup = 8.33 * $12,000 = $100,000. Annual Holding = $3.60 * 10,000 = $36,000. TVC = $136,000.",
        "explanation_vi": "Số lần chạy = 250,000 / 30,000 = 8.33 đợt. Chi phí thiết lập = $100,000. Chi phí lưu kho = $3.60 x 10,000 = $36,000. Tổng TVC = $136,000/năm."
    })

    questions.append({
        "id": "QUES-213",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Optimal Policy Run and Cycle Time",
        "difficulty": "Intermediate",
        "question_en": "Under SOCA's optimal EPQ policy of Q* = 50,000 speakers, what are the production run duration t_p and total cycle length T?",
        "question_vi": "Theo chính sách EPQ tối ưu Q* = 50,000 loa của SOCA, thời gian chạy máy t_p và tổng chiều dài một chu kỳ T là bao nhiêu?",
        "options_en": [
            "Production run t_p = 16.67 working days; Total cycle length T = 50 working days (5 production runs per year)",
            "Production run = 50 days; Total cycle = 100 days",
            "Production run = 10 days; Total cycle = 30 days",
            "Production run = 250 days (continuous manufacturing)"
        ],
        "options_vi": [
            "Thời gian chạy máy t_p = 16.67 ngày làm việc; Tổng chu kỳ T = 50 ngày làm việc (5 đợt sản xuất trong năm)",
            "Thời gian chạy máy = 50 ngày; Tổng chu kỳ = 100 ngày",
            "Thời gian chạy máy = 10 ngày; Tổng chu kỳ = 30 ngày",
            "Thời gian chạy máy = 250 ngày (sản xuất liên tục cả năm)"
        ],
        "correct_answer": 0,
        "explanation_en": "Run time t_p = 50,000 / 3,000 = 16.67 days. Cycle time T = 50,000 / 1,000 = 50 days. Runs per year = 250 / 50 = exactly 5 runs per year.",
        "explanation_vi": "Chạy máy t_p = 50,000 / 3,000 = 16.67 ngày. Chu kỳ T = 50,000 / 1,000 = 50 ngày. Một năm chạy đúng 250 / 50 = 5 đợt sản xuất."
    })

    questions.append({
        "id": "QUES-214",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Optimal Inventory Levels",
        "difficulty": "Intermediate",
        "question_en": "Under SOCA's optimal Q* = 50,000 policy, what are the Maximum Inventory Level and Average Inventory Level?",
        "question_vi": "Theo chính sách tối ưu Q* = 50,000 của SOCA, Mức Tồn Kho Cực Đại và Mức Tồn Kho Bình Quân là bao nhiêu chiếc loa?",
        "options_en": [
            "Maximum Inventory = 33,333.33 speakers; Average Inventory = 16,666.67 speakers",
            "Maximum Inventory = 50,000 speakers; Average Inventory = 25,000 speakers",
            "Maximum Inventory = 20,000 speakers; Average Inventory = 10,000 speakers",
            "Maximum Inventory = 10,000 speakers; Average Inventory = 5,000 speakers"
        ],
        "options_vi": [
            "Tồn kho Cực đại = 33,333.33 chiếc loa; Tồn kho Bình quân = 16,666.67 chiếc loa",
            "Tồn kho Cực đại = 50,000 chiếc loa; Tồn kho Bình quân = 25,000 chiếc loa",
            "Tồn kho Cực đại = 20,000 chiếc loa; Tồn kho Bình quân = 10,000 chiếc loa",
            "Tồn kho Cực đại = 10,000 chiếc loa; Tồn kho Bình quân = 5,000 chiếc loa"
        ],
        "correct_answer": 0,
        "explanation_en": "Max inventory = 50,000 * (1 - 1/3) = 33,333.33 speakers. Average inventory = 33,333.33 / 2 = 16,666.67 speakers.",
        "explanation_vi": "Tồn đỉnh = 50,000 x (2/3) = 33,333.33 loa. Tồn bình quân = 33,333.33 / 2 = 16,666.67 chiếc loa."
    })

    questions.append({
        "id": "QUES-215",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Optimal Total Variable Cost",
        "difficulty": "Intermediate",
        "question_en": "What is SOCA's Total Variable Cost TVC* under the optimal EPQ policy of Q* = 50,000 speakers?",
        "question_vi": "Tổng chi phí biến đổi tồn kho TVC* của SOCA theo chính sách EPQ tối ưu Q* = 50,000 chiếc loa là bao nhiêu?",
        "options_en": [
            "$120,000 per year (Annual Setup: $60,000 + Annual Holding: $60,000)",
            "$136,000 per year",
            "$100,000 per year",
            "$60,000 per year"
        ],
        "options_vi": [
            "$120,000 mỗi năm (Chi phí Thiết lập: $60,000 + Chi phí Lưu kho: $60,000)",
            "$136,000 mỗi năm",
            "$100,000 mỗi năm",
            "$60,000 mỗi năm"
        ],
        "correct_answer": 0,
        "explanation_en": "Setups = 5 runs * $12,000 = $60,000. Holding = $3.60 * 16,666.67 = $60,000. TVC* = $60,000 + $60,000 = $120,000 per year.",
        "explanation_vi": "Chi phí thiết lập = 5 x $12,000 = $60,000. Chi phí lưu kho = $3.60 x 16,666.67 = $60,000. Tổng TVC* = $120,000/năm (cân bằng hoàn hảo)."
    })

    questions.append({
        "id": "QUES-216",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "SOCA Net Annual Savings",
        "difficulty": "Intermediate",
        "question_en": "How much money does SOCA save annually by adjusting its production lot size from Q = 30,000 to optimal Q* = 50,000?",
        "question_vi": "SOCA tiết kiệm được bao nhiêu tiền mỗi năm khi điều chỉnh quy mô lô sản xuất từ Q = 30,000 lên lô tối ưu Q* = 50,000?",
        "options_en": [
            "$16,000 per year (an 11.8% reduction in variable inventory costs)",
            "$50,000 per year",
            "$36,000 per year",
            "$0 (both lot sizes cost the same)"
        ],
        "options_vi": [
            "$16,000 mỗi năm (giảm 11.8% chi phí biến đổi tồn kho)",
            "$50,000 mỗi năm",
            "$36,000 mỗi năm",
            "$0 (cả hai quy mô lô đều tốn chi phí như nhau)"
        ],
        "correct_answer": 0,
        "explanation_en": "Savings = Current TVC ($136,000) - Optimal TVC ($120,000) = $16,000 per year net savings.",
        "explanation_vi": "Khoản tiết kiệm ròng hàng năm = $136,000 - $120,000 = $16,000/năm (giảm 11.8% chi phí)."
    })

    questions.append({
        "id": "QUES-217",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Facility Utilization Ratio",
        "difficulty": "Intermediate",
        "question_en": "What fraction of the working year are SOCA's speaker production facilities actively operating to satisfy television assembly?",
        "question_vi": "Phân xưởng sản xuất loa của SOCA hoạt động sản xuất trong bao nhiêu phần thời gian làm việc của năm?",
        "options_en": [
            "Exactly 1 / 3 of the time (d / p = 1,000 / 3,000 = 33.3%), leaving 2/3 of the time available for other production uses",
            "100% of the time (continuous production)",
            "50% of the time",
            "10% of the time"
        ],
        "options_vi": [
            "Đúng 1 / 3 thời gian trong năm (d / p = 1,000 / 3,000 = 33.3%), để trống 2/3 thời gian còn lại cho các mục đích sản xuất khác",
            "100% thời gian (sản xuất liên tục không ngừng)",
            "50% thời gian",
            "10% thời gian"
        ],
        "correct_answer": 0,
        "explanation_en": "Because production rate p is three times demand rate d, the facility operates 1/3 of the time (16.67 days on, 33.33 days off per 50-day cycle).",
        "explanation_vi": "Do tốc độ sản xuất gấp 3 lần tốc độ dùng, xưởng chỉ cần chạy 1/3 thời gian (chạy 16.67 ngày, nghỉ 33.33 ngày trong mỗi chu kỳ 50 ngày)."
    })

    questions.append({
        "id": "QUES-218",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Convergence to Basic EOQ as p -> Infinity",
        "difficulty": "Intermediate",
        "question_en": "What happens to the EPQ formula Q* = sqrt(2KD / [h*(1 - d/p)]) as production rate p approaches infinity (p -> infinity)?",
        "question_vi": "Điều gì xảy ra với công thức EPQ Q* = sqrt(2KD / [h*(1 - d/p)]) khi tốc độ sản xuất p tiến tới vô cùng lớn (p -> vô cùng)?",
        "options_en": [
            "The ratio d / p approaches 0, (1 - d / p) approaches 1, and the EPQ formula collapses mathematically into the Basic Wilson EOQ formula",
            "The lot size Q* becomes zero",
            "The formula becomes mathematically undefined and crashes",
            "Holding cost increases to infinity"
        ],
        "options_vi": [
            "Tỷ số d / p tiến dần về 0, hệ số (1 - d / p) tiến về 1, và công thức EPQ tự động thu gọn về đúng công thức EOQ cơ bản của Wilson",
            "Quy mô lô Q* giảm về bằng 0",
            "Công thức trở nên vô nghĩa về mặt toán học và bị lỗi",
            "Chi phí lưu kho tăng vọt lên vô cực"
        ],
        "correct_answer": 0,
        "explanation_en": "As p -> infinity, replenishment becomes instantaneous (the basic EOQ assumption). Thus, basic EOQ is a limiting special case of EPQ.",
        "explanation_vi": "Khi p tiến tới vô cùng, việc bổ sung diễn ra tức thời (giả định của EOQ). Do đó EOQ cơ bản chính là một trường hợp giới hạn đặc biệt của EPQ."
    })

    questions.append({
        "id": "QUES-219",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Excel Solver Settings for SOCA",
        "difficulty": "Intermediate",
        "question_en": "In setting up Excel Solver for the SOCA gradual replenishment problem (Slides 137-141), how is the changing cell configured?",
        "question_vi": "Khi cài đặt Excel Solver cho bài toán bổ sung dần của SOCA (Slide 137-141), ô biến đổi (Changing Variable Cell) được cấu hình như thế nào?",
        "options_en": [
            "The single decision variable cell represents production lot size Q, using the GRG Nonlinear engine to minimize Total Variable Cost cell",
            "All cells in column A are selected as changing cells",
            "The Simplex LP engine is used with 12 decision variables",
            "Daily demand d is set as the changing variable"
        ],
        "options_vi": [
            "Ô biến quyết định duy nhất đại diện cho quy mô lô sản xuất Q, sử dụng bộ giải GRG Nonlinear để cực tiểu hóa ô Tổng Chi phí Biến đổi",
            "Toàn bộ các ô trên cột A được chọn làm ô biến đổi",
            "Bộ giải Simplex LP được chọn với 12 biến quyết định",
            "Nhu cầu hàng ngày d được chọn làm biến quyết định"
        ],
        "correct_answer": 0,
        "explanation_en": "As shown in Figure 5.12-5.13, Solver changes cell Q (Lot Size) to minimize TVC = K*(D/Q) + h*(Q/2)*(1 - d/p) using GRG Nonlinear.",
        "explanation_vi": "Theo hướng dẫn giáo trình, Solver thay đổi ô Q để cực tiểu hóa ô TVC phi tuyến thông qua giải thuật GRG Nonlinear."
    })

    questions.append({
        "id": "QUES-220",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "QM for Windows Production Order Quantity (POQ) Module",
        "difficulty": "Intermediate",
        "question_en": "In QM for Windows, which inventory model option is selected to solve SOCA's gradual replenishment problem?",
        "question_vi": "Trong phần mềm QM for Windows, tùy chọn mô hình tồn kho nào được chọn để giải bài toán bổ sung dần của SOCA?",
        "options_en": [
            "Production Order Quantity (POQ) / Non-instantaneous Delivery Model",
            "Standard EOQ with instantaneous delivery",
            "Linear Programming Transportation Model",
            "ABC Inventory Analysis"
        ],
        "options_vi": [
            "Mô hình Lượng Đặt Hàng Sản Xuất (POQ) / Giao hàng không tức thời (Non-instantaneous Delivery)",
            "Mô hình EOQ chuẩn với giao hàng tức thời",
            "Mô hình Vận tải Quy hoạch Tuyến tính",
            "Phân tích Tồn kho ABC"
        ],
        "correct_answer": 0,
        "explanation_en": "QM for Windows terms this the 'Production Order Quantity' (POQ) model, prompting for Demand rate, Setup cost, Holding cost, and Production rate.",
        "explanation_vi": "Trong QM for Windows, mô hình này mang tên Production Order Quantity (POQ), có thêm ô nhập tốc độ sản xuất hàng ngày p bên cạnh d."
    })

    # Advanced (Q221 - Q225)
    questions.append({
        "id": "QUES-221",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Multi-Product Production Line Scheduling",
        "difficulty": "Advanced",
        "question_en": "SOCA's speaker line is idle for 33.33 days in every 50-day cycle (2/3 of the year). How should an ERP Production Planning (PP) Business Analyst exploit this idle window?",
        "question_vi": "Dây chuyền loa của SOCA ngừng chạy trong 33.33 ngày ở mỗi chu kỳ 50 ngày (chiếm 2/3 thời gian trong năm). Một BA phân hệ Kế hoạch Sản xuất (PP) nên khai thác khoảng thời gian trống này như thế nào?",
        "options_en": [
            "Sequence multiple distinct speaker models (e.g., soundbar speakers, subwoofer drivers) across a shared Economic Lot Scheduling Problem (ELSP) cycle, and schedule preventive machine maintenance",
            "Demolish 2/3 of the factory building to save lighting electricity",
            "Instruct television assembly lines to run 24 hours a day with zero workers",
            "Permanently sell the speaker machines to a competing electronics brand"
        ],
        "options_vi": [
            "Lên lịch luân phiên sản xuất nhiều dòng loa khác nhau (như loa soundbar, củ loa trầm) trên cùng dây chuyền (bài toán ELSP), kết hợp bố trí lịch bảo dưỡng máy móc định kỳ",
            "Phá dỡ 2/3 diện tích nhà xưởng để tiết kiệm tiền điện thắp sáng",
            "Bắt dây chuyền lắp ráp tivi chạy 24/24 không cần công nhân",
            "Bán đứt máy móc sản xuất loa cho thương hiệu điện tử đối thủ"
        ],
        "correct_answer": 0,
        "explanation_en": "Because capacity utilization is 33.3%, the line can accommodate other product families via Economic Lot Scheduling (ELSP), synchronizing multiple batch runs across the shared facility.",
        "explanation_vi": "Công suất còn trống 66.7% cho phép BA lập lịch sản xuất đa sản phẩm (ELSP): luân phiên sản xuất các dòng loa khác nhau và bảo trì máy trong các ngày nghỉ."
    })

    questions.append({
        "id": "QUES-222",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Single-Minute Exchange of Die (SMED) Integration",
        "difficulty": "Advanced",
        "question_en": "If SOCA invests in Lean SMED (Single-Minute Exchange of Die) engineering, reducing changeover setup cost K from $12,000 down to $1,200, what happens to optimal batch size Q* and agility?",
        "question_vi": "Nếu SOCA đầu tư cải tiến Lean SMED, cắt giảm chi phí thiết lập máy K từ $12,000 xuống còn $1,200, điều gì sẽ xảy ra với quy mô lô tối ưu Q* và độ linh hoạt sản xuất?",
        "options_en": [
            "Optimal lot size Q* drops by a factor of sqrt(10) from 50,000 down to ~15,811 speakers, slashing peak inventory by 68% and dramatically shortening manufacturing lead times",
            "Optimal lot size Q* increases to 500,000 speakers",
            "The production line ceases to operate completely",
            "Holding cost h drops to zero"
        ],
        "options_vi": [
            "Quy mô lô tối ưu Q* giảm căn(10) lần từ 50,000 xuống còn ~15,811 loa, giúp giảm tới 68% tồn kho đỉnh và rút ngắn đáng kể chu kỳ sản xuất",
            "Quy mô lô tối ưu Q* tăng vọt lên 500,000 loa",
            "Dây chuyền sản xuất bị đình trệ hoàn toàn",
            "Chi phí lưu kho h tự động giảm về bằng 0"
        ],
        "correct_answer": 0,
        "explanation_en": "Lean SMED reduces setup cost K. By Wilson's relation, cutting K tenfold reduces optimal batch size to Q* = 50,000 / sqrt(10) = 15,811, enabling high-mix, low-inventory agile flow.",
        "explanation_vi": "Triết lý Lean SMED: giảm chi phí thiết lập K xuống 10 lần giúp giảm quy mô lô xuống còn 15,811 loa, giúp giải phóng vốn lưu động và tăng độ linh hoạt đáp ứng thị trường."
    })

    questions.append({
        "id": "QUES-223",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "ERP Production Order Document Lifecycle",
        "difficulty": "Advanced",
        "question_en": "In an ERP system (e.g., SAP PP), how is the EPQ batch of 50,000 speakers executed transactionally on the factory floor?",
        "question_vi": "Trong hệ thống ERP (như SAP PP), lô sản xuất EPQ 50,000 loa được thực thi giao dịch như thế nào trên mặt bằng nhà xưởng?",
        "options_en": [
            "Planned Order generated by MRP -> Converted to Production Order -> Components issued (Goods Issue) -> Operations confirmed -> Finished speakers received into inventory (Goods Receipt)",
            "Purchase Requisition sent directly to overseas vendors",
            "Sales Order billed directly to retail consumers before production begins",
            "Employee paychecks printed before materials arrive"
        ],
        "options_vi": [
            "Lệnh Kế hoạch (Planned Order) sinh từ MRP -> Chuyển thành Lệnh Sản xuất (Production Order) -> Xuất linh kiện (Goods Issue) -> Xác nhận công đoạn (Confirmation) -> Nhập kho thành phẩm (Goods Receipt)",
            "Yêu cầu Mua hàng gửi thẳng cho nhà cung cấp nước ngoài",
            "Hóa đơn Bán hàng đòi tiền người tiêu dùng trước khi sản xuất",
            "In phiếu lương nhân viên trước khi nguyên vật liệu về xưởng"
        ],
        "correct_answer": 0,
        "explanation_en": "The ERP manufacturing cycle: Planned Order -> Production Order Release -> Material Staging & Goods Issue -> Routing Confirmations -> Goods Receipt of 50,000 speakers.",
        "explanation_vi": "Vòng đời sản xuất chuẩn trong ERP: Planned Order -> Production Order -> Goods Issue nguyên liệu -> Báo công đoạn (Confirmation) -> Nhập kho thành phẩm hoàn thành."
    })

    questions.append({
        "id": "QUES-224",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Scrap and Defect Rates in EPQ",
        "difficulty": "Advanced",
        "question_en": "If SOCA's speaker manufacturing process has a constant 5% defective scrap rate (scrap fraction alpha = 0.05), how must the planned production lot size Q_p be adjusted?",
        "question_vi": "Nếu quy trình sản xuất loa của SOCA có tỷ lệ phế phẩm hỏng không thể phục hồi là 5% (alpha = 0.05), quy mô lô sản xuất kế hoạch Q_p cần được điều chỉnh như thế nào?",
        "options_en": [
            "Q_p must be increased to Q* / (1 - alpha) = 50,000 / 0.95 = 52,632 speakers to guarantee 50,000 good output units emerge from the final QA gate",
            "Q_p must be decreased by 50% to save copper",
            "Defective speakers must be hidden inside television sets",
            "Production rate p must be set to zero"
        ],
        "options_vi": [
            "Q_p phải tăng lên mức Q* / (1 - alpha) = 50,000 / 0.95 = 52,632 chiếc loa để bảo đảm sau khi loại bỏ 5% phế phẩm thì vẫn thu được đúng 50,000 loa đạt chuẩn",
            "Q_p phải giảm đi 50% để tiết kiệm đồng",
            "Giấu các loa hỏng vào bên trong thùng tivi giao cho khách",
            "Tốc độ sản xuất p bắt buộc phải hạ về 0"
        ],
        "correct_answer": 0,
        "explanation_en": "Yield loss requires inflating the gross production batch: Gross Lot = Net Requirement / (1 - Scrap_Rate) = 50,000 / 0.95 = 52,632 units.",
        "explanation_vi": "Tỷ lệ hao hụt phế phẩm đòi hỏi hệ thống ERP phải tự động tính lượng sản xuất thô (Gross): 50,000 / (1 - 0.05) = 52,632 chiếc loa để bù đắp hao hụt."
    })

    questions.append({
        "id": "QUES-225",
        "exam_id": "EXAM-09",
        "chapter_id": "chap-05",
        "topic": "Just-In-Time (JIT) Kanban vs EPQ Batching",
        "difficulty": "Advanced",
        "question_en": "How does a Just-In-Time (JIT) pull system (e.g., electronic Kanban) challenge the traditional EPQ batching approach in an integrated manufacturing environment?",
        "question_vi": "Hệ thống kéo Đúng Thời Điểm (Just-In-Time - JIT / Kanban điện tử) thách thức phương pháp gom lô sản xuất EPQ truyền thống trong môi trường sản xuất tích hợp như thế nào?",
        "options_en": [
            "JIT aims to eliminate setup times (K -> 0), driving batch sizes toward 1 and eliminating the saw-tooth inventory cycle altogether in favor of continuous pull flow",
            "JIT mandates producing 1,000,000 units in every production run",
            "JIT eliminates the need for television speakers entirely",
            "JIT requires storing all inventory on public delivery trucks"
        ],
        "options_vi": [
            "JIT hướng tới triệt tiêu thời gian thiết lập máy (K -> 0), kéo quy mô lô về 1 sản phẩm và xóa bỏ hoàn toàn chu kỳ tồn kho răng cưa để thay thế bằng luồng kéo liên tục",
            "JIT bắt buộc phải sản xuất 1,000,000 sản phẩm trong mỗi đợt chạy máy",
            "JIT loại bỏ hoàn toàn nhu cầu lắp loa vào tivi",
            "JIT yêu cầu phải lưu trữ toàn bộ hàng tồn kho trên xe tải ngoài đường"
        ],
        "correct_answer": 0,
        "explanation_en": "While EPQ accepts setup cost K as a fixed constraint, JIT/Lean attacks K directly. As K -> 0, EPQ Q* shrinks to single-piece flow, eliminating intermediate WIP buffers.",
        "explanation_vi": "EPQ coi chi phí thiết lập K là cố định; triết lý JIT/Kanban tìm cách kéo K về 0, khi đó Q* tiến về 1, loại bỏ hoàn toàn kho đệm bán thành phẩm WIP giữa các công đoạn."
    })

    return questions
