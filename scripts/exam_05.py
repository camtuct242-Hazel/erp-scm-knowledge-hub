# -*- coding: utf-8 -*-
# EXAM 05: Demand Bounds, Profit Maximization & Assignment Problems (chap-03)
# 25 Questions: Q101 to Q125 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q101 - Q110)
    questions.append({
        "id": "QUES-101",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Demand Range Concept",
        "difficulty": "Basic",
        "question_en": "In the Middletown School District problem, why are school enrollments modeled as ranges [Min, Max] rather than fixed numbers?",
        "question_vi": "Trong bài toán Middletown School District, vì sao số lượng học sinh mỗi trường được mô hình hóa dưới dạng khoảng [Tối thiểu, Tối đa] thay vì một con số cố định?",
        "options_en": [
            "To allow operational flexibility between minimum viable class sizes and maximum physical classroom capacities",
            "Because the school principal does not know how to count students",
            "To encourage students to skip school whenever they want",
            "Because school buses cannot operate unless enrollment changes daily"
        ],
        "options_vi": [
            "Để tạo sự linh hoạt trong điều hành giữa quy mô lớp học tối thiểu cần duy trì và sức chứa phòng học tối đa của cơ sở vật chất",
            "Vì hiệu trưởng nhà trường không biết cách kiểm đếm số lượng học sinh",
            "Để khuyến khích học sinh tự do trốn học bất cứ khi nào các em muốn",
            "Vì xe buýt đưa đón học sinh không thể chạy nếu sĩ số không thay đổi mỗi ngày"
        ],
        "correct_answer": 0,
        "explanation_en": "Facilities operate within capacity limits: a minimum threshold to justify staffing, and a maximum ceiling determined by physical classrooms.",
        "explanation_vi": "Cơ sở vật chất trường học có cận dưới để bảo đảm hiệu quả mở lớp và cận trên do giới hạn phòng học thực tế."
    })

    questions.append({
        "id": "QUES-102",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Middletown Student Population",
        "difficulty": "Basic",
        "question_en": "In the Middletown School District case, what is the total number of high school students residing across the 9 residential tracts?",
        "question_vi": "Trong case Middletown School District, tổng số học sinh trung học cư trú tại 9 phân khu dân cư là bao nhiêu?",
        "options_en": [
            "4,100 students (500+400+450+400+500+450+450+400+500)",
            "10,000 students",
            "1,200 students",
            "300 students"
        ],
        "options_vi": [
            "4,100 học sinh (500+400+450+400+500+450+450+400+500)",
            "10,000 học sinh",
            "1,200 học sinh",
            "300 học sinh"
        ],
        "correct_answer": 0,
        "explanation_en": "Summing the student counts across all 9 tracts yields exactly 4,100 students.",
        "explanation_vi": "Cộng dồn số học sinh ở cả 9 khu vực dân cư cho kết quả chính xác là 4,100 học sinh."
    })

    questions.append({
        "id": "QUES-103",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Middletown Objective Function",
        "difficulty": "Basic",
        "question_en": "What is the primary objective of management in the Middletown School District problem?",
        "question_vi": "Mục tiêu trọng tâm của ban quản lý học khu trong bài toán Middletown School District là gì?",
        "options_en": [
            "Minimize the total student travel distance (in student-miles) to attend school",
            "Maximize the price of school cafeteria lunch meals",
            "Minimize the number of teachers employed by the city",
            "Ensure all students attend School 1 exclusively"
        ],
        "options_vi": [
            "Cực tiểu hóa tổng quãng đường di chuyển của học sinh (tính bằng học sinh - dặm) khi đến trường",
            "Cực đại hóa giá bán suất ăn trưa tại căng-tin trường học",
            "Cực tiểu hóa số lượng giáo viên được thành phố tuyển dụng",
            "Bắt buộc toàn bộ học sinh phải học tập duy nhất tại Trường 1"
        ],
        "correct_answer": 0,
        "explanation_en": "The school board's explicit goal is minimizing the total distance students must travel to school.",
        "explanation_vi": "Hội đồng học khu đặt mục tiêu giảm thiểu tối đa quãng đường đi lại của học sinh nhằm tiết kiệm thời gian và chi phí xe buýt."
    })

    questions.append({
        "id": "QUES-104",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Middletown Capacity Feasibility",
        "difficulty": "Basic",
        "question_en": "In Middletown, how do the aggregate minimum and maximum capacities of the 3 schools compare to the 4,100 student population?",
        "question_vi": "Ở Middletown, tổng công suất tối thiểu và tối đa của 3 trường so với 4,100 học sinh có mối tương quan thế nào?",
        "options_en": [
            "Sum of Min = 3,300 <= 4,100 <= Sum of Max = 5,000, confirming the existence of feasible solutions",
            "Total minimum capacity exceeds 10,000, causing severe shortage",
            "Total maximum capacity is only 2,000, leaving 2,100 students without school",
            "All three schools have zero capacity"
        ],
        "options_vi": [
            "Tổng công suất Tối thiểu = 3,300 <= 4,100 <= Tổng công suất Tối đa = 5,000, khẳng định bài toán luôn có nghiệm khả thi",
            "Tổng công suất tối thiểu vượt quá 10,000, gây thừa chỗ nghiêm trọng",
            "Tổng công suất tối đa chỉ đạt 2,000, khiến 2,100 học sinh không có chỗ học",
            "Cả ba trường học đều có công suất tiếp nhận bằng 0"
        ],
        "correct_answer": 0,
        "explanation_en": "Min sum = 1,200 + 1,100 + 1,000 = 3,300 <= 4,100 <= Max sum = 1,800 + 1,700 + 1,500 = 5,000, satisfying feasibility bounds.",
        "explanation_vi": "Tổng cận dưới = 3,300 <= 4,100 <= Tổng cận trên = 5,000, đảm bảo bài toán nằm trong miền khả thi để tìm nghiệm tối ưu."
    })

    questions.append({
        "id": "QUES-105",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Profit Maximization Objective",
        "difficulty": "Basic",
        "question_en": "How does the objective function of the Nifty Company case differ from the classical P&T Co. problem?",
        "question_vi": "Hàm mục tiêu của case study Nifty Company khác biệt căn bản như thế nào so với bài toán P&T Co. cổ điển?",
        "options_en": [
            "Nifty Co. seeks to MAXIMIZE total net profit from commercial sales rather than minimize transportation costs",
            "Nifty Co. seeks to minimize the number of factory machines",
            "Nifty Co. seeks to maximize employee vacation days",
            "There is no difference; both minimize freight shipping costs"
        ],
        "options_vi": [
            "Nifty Co. hướng tới CỰC ĐẠI HÓA tổng lợi nhuận thương mại ròng thay vì cực tiểu hóa chi phí vận chuyển",
            "Nifty Co. tìm cách cực tiểu hóa số lượng máy móc trong nhà máy",
            "Nifty Co. tìm cách cực đại hóa số ngày nghỉ phép của công nhân",
            "Không có sự khác biệt; cả hai bài toán đều cực tiểu hóa chi phí vận chuyển"
        ],
        "correct_answer": 0,
        "explanation_en": "Nifty Co. has unit profit margins P_ij and customer order options; the goal is maximizing Total Profit Z = Sum(P_ij * x_ij).",
        "explanation_vi": "Nifty Co. có ma trận lợi nhuận đơn vị P_ij; mục tiêu doanh nghiệp chuyển từ cắt giảm chi phí sang tối đa hóa lợi nhuận kinh doanh."
    })

    questions.append({
        "id": "QUES-106",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Profit-to-Cost Transformation",
        "difficulty": "Basic",
        "question_en": "What mathematical transformation converts a profit maximization problem (Max Sum(P_ij * x_ij)) into an equivalent cost minimization problem?",
        "question_vi": "Phép biến đổi toán học nào chuyển đổi bài toán cực đại hóa lợi nhuận (Max Tổng P_ij * x_ij) thành bài toán cực tiểu hóa chi phí tương đương?",
        "options_en": [
            "Define equivalent unit costs as c_ij = P_max - P_ij, where P_max is the maximum profit value in the tableau",
            "Multiply all profit numbers by -100 and add 1,000",
            "Divide every profit figure by zero",
            "Square all numbers in the profit table"
        ],
        "options_vi": [
            "Định nghĩa chi phí đơn vị tương đương c_ij = P_max - P_ij, trong đó P_max là giá trị lợi nhuận lớn nhất trong toàn bảng",
            "Nhân toàn bộ các số lợi nhuận với -100 rồi cộng thêm 1,000",
            "Chia tất cả các con số lợi nhuận cho 0",
            "Bình phương tất cả các con số trong bảng lợi nhuận"
        ],
        "correct_answer": 0,
        "explanation_en": "Minimizing opportunity cost (P_max - P_ij) is mathematically equivalent to maximizing profit, allowing standard transportation simplex solvers to run without alteration.",
        "explanation_vi": "Cực tiểu hóa chi phí cơ hội c_ij = P_max - P_ij tương đương hoàn toàn với cực đại hóa lợi nhuận, giúp sử dụng được các phần mềm giải vận tải tiêu chuẩn."
    })

    questions.append({
        "id": "QUES-107",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Assignment Problem Definition",
        "difficulty": "Basic",
        "question_en": "What defines a pure Assignment Problem in operations research?",
        "question_vi": "Điều gì định nghĩa một Bài toán Phân công (Assignment Problem) thuần túy trong nghiên cứu vận hành?",
        "options_en": [
            "Allocating n assignees to n tasks on a strict one-to-one basis such that each task is performed by exactly one assignee",
            "Distributing 1,000 tons of gravel across 50 highways",
            "Hiring temporary contract workers without assigning them any tasks",
            "Selling factory inventory at an online public auction"
        ],
        "options_vi": [
            "Phân bổ n đối tượng cho n nhiệm vụ theo nguyên tắc 1-kèm-1 chặt chẽ sao cho mỗi công việc do đúng một đối tượng đảm nhận",
            "Phân phối 1,000 tấn đá sỏi trên 50 tuyến đường cao tốc",
            "Tuyển dụng công nhân thời vụ nhưng không giao cho họ bất kỳ công việc nào",
            "Bán đấu giá tài sản tồn kho của nhà máy trên sàn trực tuyến"
        ],
        "correct_answer": 0,
        "explanation_en": "The assignment problem matches assignees to tasks one-to-one, represented mathematically with binary decision variables x_ij in {0, 1}.",
        "explanation_vi": "Bài toán phân công ghép cặp 1-kèm-1 giữa đối tượng và công việc, sử dụng biến nhị phân x_ij thuộc {0, 1}."
    })

    questions.append({
        "id": "QUES-108",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Hungarian Method Algorithm",
        "difficulty": "Basic",
        "question_en": "Which famous polynomial-time combinatorial algorithm is designed specifically to solve the Assignment Problem?",
        "question_vi": "Thuật toán tổ hợp thời gian đa thức nổi tiếng nào được thiết kế chuyên biệt để giải Bài toán Phân công?",
        "options_en": [
            "The Hungarian Method (Kuhn-Munkres algorithm)",
            "Dijkstra's Shortest Path Algorithm",
            "Binary Search Tree Traversal",
            "Bubble Sort Algorithm"
        ],
        "options_vi": [
            "Phương pháp Hungarian (Thuật toán Kuhn-Munkres)",
            "Thuật toán đường đi ngắn nhất Dijkstra",
            "Duyệt cây tìm kiếm nhị phân",
            "Thuật toán sắp xếp nổi bọt (Bubble Sort)"
        ],
        "correct_answer": 0,
        "explanation_en": "The Hungarian method solves bipartite matching assignment problems in O(n^3) time using matrix row and column reductions.",
        "explanation_vi": "Phương pháp Hungarian giải quyết bài toán phân công nhị phân trong thời gian đa thức O(n^3) thông qua các phép biến đổi giảm trừ ma trận."
    })

    questions.append({
        "id": "QUES-109",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Better Products Case 2.2 Difference",
        "difficulty": "Basic",
        "question_en": "What is the key constraint that differentiates Better Products Case 2.2 from Case 2.1?",
        "question_vi": "Ràng buộc then chốt nào phân biệt Better Products Case 2.2 với Case 2.1?",
        "options_en": [
            "Product splitting is strictly prohibited: each new product must be assigned to exactly one manufacturing plant",
            "Plant 1 is permanently demolished",
            "All four products must be manufactured in China",
            "There are zero production costs for any product"
        ],
        "options_vi": [
            "Nghiêm cấm chia nhỏ sản phẩm (No product splitting): mỗi sản phẩm mới bắt buộc phải sản xuất tại duy nhất một nhà máy",
            "Nhà máy 1 bị phá dỡ hoàn toàn",
            "Cả bốn sản phẩm bắt buộc phải được sản xuất tại Trung Quốc",
            "Không phát sinh bất kỳ chi phí sản xuất nào cho tất cả sản phẩm"
        ],
        "correct_answer": 0,
        "explanation_en": "Case 2.2 prohibits product splitting to eliminate hidden changeover, tooling, and multi-facility coordination overhead.",
        "explanation_vi": "Case 2.2 cấm chia nhỏ sản phẩm để triệt tiêu chi phí ẩn do chuyển đổi máy móc trùng lặp và phân tán đơn hàng."
    })

    questions.append({
        "id": "QUES-110",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Better Products Case 2.2 Capacities",
        "difficulty": "Basic",
        "question_en": "In Better Products Case 2.2, what are the allowed product assignment limits for Plants 1, 2, and 3?",
        "question_vi": "Trong Better Products Case 2.2, hạn mức phân công sản phẩm được phép cho các Nhà máy 1, 2 và 3 là bao nhiêu?",
        "options_en": [
            "Plant 1 can produce up to 2 products; Plant 2 can produce 1 product; Plant 3 can produce 1 product (Total = 4 products)",
            "Each plant can produce exactly 4 products",
            "Plant 3 can produce 3 products and Plants 1 & 2 produce 0",
            "None of the plants are allowed to produce any products"
        ],
        "options_vi": [
            "Nhà máy 1 sản xuất tối đa 2 sản phẩm; Nhà máy 2 sản xuất 1 sản phẩm; Nhà máy 3 sản xuất 1 sản phẩm (Tổng cộng = 4 sản phẩm)",
            "Mỗi nhà máy đều sản xuất được đúng 4 sản phẩm",
            "Nhà máy 3 sản xuất 3 sản phẩm và Nhà máy 1 & 2 không sản xuất gì",
            "Không có nhà máy nào được phép sản xuất bất kỳ sản phẩm nào"
        ],
        "correct_answer": 0,
        "explanation_en": "Since there are 4 products and 3 plants, Plants 1 and 2 have capacity to make two, but the optimal assignment allocates 2 to Plant 1, 1 to Plant 2, and 1 to Plant 3.",
        "explanation_vi": "4 sản phẩm phân bổ cho 3 nhà máy: Nhà máy 1 nhận 2 sản phẩm, Nhà máy 2 nhận 1 sản phẩm, và Nhà máy 3 nhận 1 sản phẩm."
    })

    # Intermediate (Q111 - Q120)
    questions.append({
        "id": "QUES-111",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Splitting Plant 1 for Hungarian Tableau",
        "difficulty": "Intermediate",
        "question_en": "To solve Better Products Case 2.2 using the standard square Hungarian assignment method, how must Plant 1 be represented?",
        "question_vi": "Để giải Better Products Case 2.2 bằng bảng phân công Hungarian hình vuông chuẩn, Nhà máy 1 phải được biểu diễn như thế nào?",
        "options_en": [
            "Split Plant 1 into two identical sub-plants (Plant 1A and Plant 1B), each with an assignment capacity of 1, creating a 4x4 cost matrix",
            "Delete Plant 1 and hire an outside contract manufacturer",
            "Combine Plant 1 and Plant 2 into a single megawatt facility",
            "Multiply all costs of Plant 1 by two"
        ],
        "options_vi": [
            "Tách Nhà máy 1 thành hai nhà máy con giống nhau (Nhà máy 1A và Nhà máy 1B), mỗi nhà máy có năng lực gán bằng 1, tạo thành ma trận vuông 4x4",
            "Xóa bỏ Nhà máy 1 và thuê ngoài gia công sản xuất",
            "Gộp Nhà máy 1 và Nhà máy 2 thành một siêu nhà máy duy nhất",
            "Nhân đôi toàn bộ các mức chi phí của Nhà máy 1"
        ],
        "correct_answer": 0,
        "explanation_en": "Since the Hungarian algorithm requires an nxn matrix with unit supplies, a facility with capacity 2 is split into two identical rows of capacity 1.",
        "explanation_vi": "Thuật toán Hungarian đòi hỏi ma trận vuông nxn với mỗi đối tượng có công suất bằng 1, do đó nhà máy có công suất 2 được tách thành hai dòng giống hệt nhau (1A và 1B)."
    })

    questions.append({
        "id": "QUES-112",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Better Products Case 2.2 Optimal Cost",
        "difficulty": "Intermediate",
        "question_en": "What is the optimal product assignment and minimum daily cost in Better Products Case 2.2?",
        "question_vi": "Phương án phân công sản phẩm tối ưu và tổng chi phí hàng ngày tối thiểu trong Better Products Case 2.2 là gì?",
        "options_en": [
            "Plant 1 produces Products 2 & 3; Plant 2 produces Product 4; Plant 3 produces Product 1 (Total Cost = $810 + $840 + $920 + $740 = $3,310/day)",
            "Plant 1 produces Products 1 & 4; Plant 2 produces Product 2; Plant 3 produces Product 3 (Total Cost = $5,000/day)",
            "All four products produced at Plant 1 (Total Cost = $3,430/day)",
            "Plant 2 produces Product 3 at prohibited cost"
        ],
        "options_vi": [
            "Nhà máy 1 sản xuất Sản phẩm 2 & 3; Nhà máy 2 sản xuất Sản phẩm 4; Nhà máy 3 sản xuất Sản phẩm 1 (Tổng chi phí = $810 + $840 + $920 + $740 = $3,310/ngày)",
            "Nhà máy 1 sản xuất Sản phẩm 1 & 4; Nhà máy 2 sản xuất Sản phẩm 2; Nhà máy 3 sản xuất Sản phẩm 3 (Tổng chi phí = $5,000/ngày)",
            "Toàn bộ 4 sản phẩm đều giao cho Nhà máy 1 sản xuất (Tổng chi phí = $3,430/ngày)",
            "Nhà máy 2 sản xuất Sản phẩm 3 với chi phí phạt"
        ],
        "correct_answer": 0,
        "explanation_en": "The optimal binary assignment gives: Plant 1 -> Prod 2 ($810) & Prod 3 ($840); Plant 2 -> Prod 4 ($920); Plant 3 -> Prod 1 ($740). Sum = $3,310 per day.",
        "explanation_vi": "Phương án gán tối ưu nhị phân: Nhà máy 1 làm SP 2 ($810) và SP 3 ($840); Nhà máy 2 làm SP 4 ($920); Nhà máy 3 làm SP 1 ($740). Tổng cước = $3,310/ngày."
    })

    questions.append({
        "id": "QUES-113",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Cost of Prohibiting Product Splitting",
        "difficulty": "Intermediate",
        "question_en": "Comparing Better Products Case 2.1 (splitting allowed) with Case 2.2 (splitting prohibited), why does the visible variable cost appear higher in Case 2.2?",
        "question_vi": "So sánh Better Products Case 2.1 (cho phép chia nhỏ) với Case 2.2 (cấm chia nhỏ), vì sao chi phí biến đổi bề nổi lại có vẻ cao hơn trong Case 2.2?",
        "options_en": [
            "Prohibiting product splitting adds integer 0-1 constraints, shrinking the feasible solution space; however, it eliminates massive unmodeled setup and logistics overhead",
            "Because workers demand triple pay when product splitting is prohibited",
            "Because Case 2.2 includes corporate tax and Case 2.1 does not",
            "Because machine oil becomes more expensive"
        ],
        "options_vi": [
            "Việc cấm chia nhỏ bổ sung thêm các ràng buộc nguyên 0-1 làm thu hẹp miền nghiệm khả thi; tuy nhiên nó loại bỏ được các chi phí ẩn rất lớn về thiết lập máy và điều phối",
            "Vì công nhân đòi tăng lương gấp 3 lần khi không được chia nhỏ sản phẩm",
            "Vì Case 2.2 tính thêm thuế doanh nghiệp còn Case 2.1 thì không tính",
            "Vì dầu bôi trơn máy móc trở nên đắt đỏ hơn"
        ],
        "correct_answer": 0,
        "explanation_en": "Integer restrictions constrain optimization, raising direct costs, but this trade-off is justified by eliminating hidden changeover and administrative coordination expenses.",
        "explanation_vi": "Ràng buộc nguyên làm miền nghiệm hẹp lại khiến chi phí trực tiếp tăng nhẹ, nhưng bù lại giúp doanh nghiệp loại bỏ các chi phí ẩn khổng lồ về chuyển đổi máy và quản lý."
    })

    questions.append({
        "id": "QUES-114",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Hungarian Method Step 1",
        "difficulty": "Intermediate",
        "question_en": "What is the initial mathematical step in the Hungarian Method after constructing the square cost matrix?",
        "question_vi": "Bước toán học khởi đầu trong Phương pháp Hungarian sau khi đã lập xong ma trận chi phí hình vuông là gì?",
        "options_en": [
            "Row Reduction: Subtract the minimum element in each row from all elements in that row",
            "Multiply all matrix elements by negative one",
            "Add 1,000 to the bottom-right corner cell",
            "Take the square root of every number in the matrix"
        ],
        "options_vi": [
            "Giảm trừ Hàng (Row Reduction): Trừ giá trị phần tử nhỏ nhất trong mỗi hàng cho tất cả các phần tử nằm trên hàng đó",
            "Nhân toàn bộ các phần tử trong ma trận với số âm 1",
            "Cộng thêm 1,000 vào ô góc dưới cùng bên phải",
            "Lấy căn bậc hai của tất cả các con số có trong ma trận"
        ],
        "correct_answer": 0,
        "explanation_en": "The Hungarian method starts with Row Reduction (subtracting row minima), followed by Column Reduction (subtracting column minima) to expose zero opportunity costs.",
        "explanation_vi": "Thuật toán Hungarian bắt đầu bằng phép Giảm trừ Hàng (trừ số nhỏ nhất mỗi hàng), tiếp theo là Giảm trừ Cột để tạo ra các số 0 chi phí cơ hội."
    })

    questions.append({
        "id": "QUES-115",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Hungarian Method Line Covering Test",
        "difficulty": "Intermediate",
        "question_en": "In the Hungarian algorithm, how do you verify if the current matrix contains an optimal assignment?",
        "question_vi": "Trong thuật toán Hungarian, làm thế nào để kiểm tra xem ma trận hiện tại đã đạt phương án phân công tối ưu hay chưa?",
        "options_en": [
            "Determine the minimum number of horizontal and vertical lines needed to cover all zeros; if this number equals n (the matrix dimension), an optimal assignment is found",
            "Check if all matrix entries are negative",
            "Check if the sum of all cells exceeds 10,000",
            "Count how many diagonal lines can be drawn across the sheet"
        ],
        "options_vi": [
            "Xác định số lượng đường thẳng ngang và dọc tối thiểu cần thiết để phủ kín toàn bộ các số 0; nếu số đường này đúng bằng n (kích thước ma trận) thì đã đạt nghiệm tối ưu",
            "Kiểm tra xem toàn bộ các phần tử trong ma trận đã chuyển thành số âm hay chưa",
            "Kiểm tra xem tổng giá trị của toàn bộ các ô có vượt quá 10,000 hay không",
            "Đếm số đường chéo có thể kẻ qua trang giấy"
        ],
        "correct_answer": 0,
        "explanation_en": "By König's theorem, an optimal assignment exists when the maximum matching (minimum lines to cover all zeros) equals the dimension n.",
        "explanation_vi": "Theo định lý König, nghiệm tối ưu xuất hiện khi số đường thẳng tối thiểu dùng để phủ hết các số 0 bằng đúng bậc n của ma trận."
    })

    questions.append({
        "id": "QUES-116",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Nifty Co. Plant Capacities",
        "difficulty": "Intermediate",
        "question_en": "In the Nifty Company case, what is the total production output available across Plants 1, 2, and 3?",
        "question_vi": "Trong case Nifty Company, tổng sản lượng có thể sản xuất của 3 Nhà máy 1, 2 và 3 là bao nhiêu?",
        "options_en": [
            "20,000 units (Plant 1: 8,000; Plant 2: 5,000; Plant 3: 7,000)",
            "30,000 units",
            "12,000 units",
            "50,000 units"
        ],
        "options_vi": [
            "20,000 đơn vị (Nhà máy 1: 8,000; Nhà máy 2: 5,000; Nhà máy 3: 7,000)",
            "30,000 đơn vị",
            "12,000 đơn vị",
            "50,000 đơn vị"
        ],
        "correct_answer": 0,
        "explanation_en": "Plant 1 (8,000) + Plant 2 (5,000) + Plant 3 (7,000) = 20,000 total available production quantity.",
        "explanation_vi": "Tổng năng lực sản xuất của 3 nhà máy là 8,000 + 5,000 + 7,000 = 20,000 đơn vị."
    })

    questions.append({
        "id": "QUES-117",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Nifty Co. Demand Range Imbalance",
        "difficulty": "Intermediate",
        "question_en": "In Nifty Co., total plant supply is 20,000 units, while customer requested purchases total 30,000 units and minimum purchases total 12,000 units. How is this demand interval formulated in LP?",
        "question_vi": "Ở Nifty Co., tổng cung là 20,000 đơn vị, trong khi nhu cầu tối đa yêu cầu là 30,000 và cam kết mua tối thiểu là 12,000. Khoảng nhu cầu này được thiết lập trong LP thế nào?",
        "options_en": [
            "For each customer j: Minimum_Purchase_j <= Sum_i (x_ij) <= Requested_Purchase_j, with total supply constrained to Sum_j (x_ij) <= Capacity_i",
            "All customers are forced to receive 20,000 units each",
            "Customers with minimum purchases are banned from buying products",
            "The model ignores customer demand and ships to warehouses randomly"
        ],
        "options_vi": [
            "Với mỗi khách hàng j: Mức_Mua_Tối_Thiểu_j <= Tổng_i (x_ij) <= Mức_Mua_Yêu_Cầu_j, với tổng cung khống chế bởi Tổng_j (x_ij) <= Công_Suất_i",
            "Toàn bộ khách hàng bị ép buộc phải tiếp nhận mỗi người 20,000 đơn vị",
            "Khách hàng có cam kết mua tối thiểu bị cấm mua hàng",
            "Mô hình bỏ qua nhu cầu khách hàng và giao hàng ngẫu nhiên vào các kho"
        ],
        "correct_answer": 0,
        "explanation_en": "Each customer j has two bounding constraints: a lower bound (minimum contract commitment) and an upper bound (maximum requested order size).",
        "explanation_vi": "Mỗi khách hàng có hai chặn ràng buộc: cận dưới là hợp đồng cam kết tối thiểu và cận trên là hạn mức nhu cầu tối đa."
    })

    questions.append({
        "id": "QUES-118",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Network Simplex Efficiency",
        "difficulty": "Intermediate",
        "question_en": "Why is the Network Simplex method significantly faster than general matrix simplex for large enterprise distribution graphs?",
        "question_vi": "Vì sao phương pháp Đơn hình Mạng lưới (Network Simplex) lại nhanh hơn vượt trội so với đơn hình ma trận tổng quát cho các đồ thị phân phối lớn?",
        "options_en": [
            "It maintains the simplex basis as a directed spanning tree, performing pivot steps via tree updates rather than computing expensive matrix inverses",
            "It skips all mathematical calculations and guesses the answer",
            "It requires specialized quantum supercomputers to run",
            "It only works on networks with fewer than three nodes"
        ],
        "options_vi": [
            "Nó duy trì cơ sở đơn hình dưới dạng cây khung có hướng (spanning tree), thực hiện các phép xoay đơn hình bằng cách cập nhật đồ thị cây thay vì nghịch đảo ma trận tốn kém",
            "Nó bỏ qua toàn bộ phép tính toán học và đoán mò kết quả",
            "Nó bắt buộc phải chạy trên các siêu máy tính lượng tử chuyên dụng",
            "Nó chỉ hoạt động được trên các mạng lưới có ít hơn ba nút"
        ],
        "correct_answer": 0,
        "explanation_en": "Network simplex maintains a spanning tree basis data structure. Pivot operations correspond to adding an arc to form a cycle and pruning an exiting arc, running in near-linear time.",
        "explanation_vi": "Đơn hình mạng lưới lưu cơ sở bằng cây khung. Mỗi bước xoay chỉ là thao tác thêm cạnh tạo chu trình và bẻ nhánh cây, đạt tốc độ cực nhanh mà không cần nghịch đảo ma trận."
    })

    questions.append({
        "id": "QUES-119",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Middletown Redistricting Equity",
        "difficulty": "Intermediate",
        "question_en": "In Middletown School District, why did management choose average student distance rather than total bus fuel expenditure as the objective metric?",
        "question_vi": "Trong học khu Middletown, vì sao ban quản lý lại chọn quãng đường học sinh trung bình thay vì tổng tiền xăng xe buýt làm chỉ số hàm mục tiêu?",
        "options_en": [
            "To prioritize student welfare, equitable travel times, and pedestrian safety across all socioeconomic residential tracts",
            "Because bus fuel is completely free of charge in Middletown",
            "Because school buses are powered by sails",
            "To deliberately make high school students walk longer distances"
        ],
        "options_vi": [
            "Để ưu tiên phúc lợi của học sinh, đảm bảo sự công bằng về thời gian đi lại và an toàn giao thông cho mọi phân khu dân cư",
            "Vì tiền xăng xe buýt được miễn phí hoàn toàn tại Middletown",
            "Vì xe buýt trường học chạy bằng sức gió cánh buồm",
            "Để cố tình bắt học sinh trung học phải đi bộ quãng đường xa hơn"
        ],
        "correct_answer": 0,
        "explanation_en": "Minimizing student-miles directly reflects student quality-of-life, family convenience, and transit safety, which public school boards prioritize over pure fiscal metrics.",
        "explanation_vi": "Hàm mục tiêu học sinh - dặm phản ánh sự công bằng xã hội và an toàn cho học sinh, tiêu chí hàng đầu của các tổ chức giáo dục công lập."
    })

    questions.append({
        "id": "QUES-120",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Binary Integer Programming in Excel Solver",
        "difficulty": "Intermediate",
        "question_en": "When solving Better Products Case 2.2 in Excel Solver, what constraint type must be added to the decision variable cells?",
        "question_vi": "Khi giải Better Products Case 2.2 trong Excel Solver, kiểu ràng buộc nào bắt buộc phải thêm vào các ô biến quyết định?",
        "options_en": [
            "The 'bin' (Binary) constraint, forcing all decision variables to be strictly 0 or 1",
            "The 'int' (Integer) constraint with upper bound 1,000",
            "The 'dif' (AllDifferent) constraint",
            "No constraint; continuous fractions are completely acceptable"
        ],
        "options_vi": [
            "Ràng buộc 'bin' (Nhị phân), ép tất cả các biến quyết định chỉ được phép nhận giá trị 0 hoặc 1",
            "Ràng buộc 'int' (Số nguyên) với cận trên là 1,000",
            "Ràng buộc 'dif' (Tất cả khác nhau)",
            "Không cần ràng buộc gì; các giá trị phân số thập phân hoàn toàn được chấp nhận"
        ],
        "correct_answer": 0,
        "explanation_en": "Binary variables (bin in Excel Solver) restrict each plant-product pairing to either active (1) or inactive (0), guaranteeing zero product splitting.",
        "explanation_vi": "Ràng buộc 'bin' trong Solver ép biến nhận giá trị 0 hoặc 1, bảo đảm mỗi sản phẩm chỉ được gán trọn vẹn cho đúng một nhà máy."
    })

    # Advanced (Q121 - Q125)
    questions.append({
        "id": "QUES-121",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "BA Change Management: Splitting vs Discrete",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is presenting Better Products Case 2.1 vs 2.2 to the Executive Committee. How should the BA articulate the strategic business case for accepting a higher visible direct cost in Case 2.2?",
        "question_vi": "Một Business Analyst đang trình bày so sánh Case 2.1 và 2.2 cho Hội đồng Quản trị Better Products. BA nên diễn giải luận điểm kinh doanh chiến lược nào để thuyết phục HĐQT chấp nhận chi phí trực tiếp có vẻ cao hơn trong Case 2.2?",
        "options_en": [
            "Case 2.2 eliminates unbudgeted multi-plant changeover costs, duplicated tooling investments, split-shipment logistics friction, and quality inconsistency across factories",
            "Case 2.2 is mathematically simpler and requires fewer computer processors",
            "Case 2.1 violates federal antitrust monopoly laws",
            "Case 2.2 allows the company to fire all plant quality inspectors"
        ],
        "options_vi": [
            "Case 2.2 loại bỏ các chi phí chuyển đổi máy ngoài dự toán, tránh phải đầu tư khuôn mẫu (tooling) trùng lặp tại nhiều nhà máy, triệt tiêu rủi ro đơn hàng xé lẻ và đồng nhất chất lượng sản phẩm",
            "Case 2.2 đơn giản hơn về mặt toán học và đòi hỏi ít chip xử lý máy tính hơn",
            "Case 2.1 vi phạm luật chống độc quyền liên bang",
            "Case 2.2 cho phép công ty sa thải toàn bộ nhân viên kiểm soát chất lượng"
        ],
        "correct_answer": 0,
        "explanation_en": "A seasoned BA looks beyond spreadsheet LP direct costs, identifying that product splitting incurs hidden capital tooling replication, quality variance, and double freight handling.",
        "explanation_vi": "BA chuyên nghiệp nhìn thấu chi phí ẩn đằng sau các con số: chia nhỏ sản phẩm sẽ phải mua 2 bộ khuôn gá, tốn 2 lần chỉnh máy và khó truy xuất nguồn gốc khi có sản phẩm lỗi."
    })

    questions.append({
        "id": "QUES-122",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Dual Gap in Integer Programming",
        "difficulty": "Advanced",
        "question_en": "Why does solving the LP relaxation of Better Products Case 2.2 (allowing fractional assignments between 0 and 1) NOT guarantee an integer solution like P&T Co. did?",
        "question_vi": "Vì sao việc giải bài toán nới lỏng LP của Better Products Case 2.2 (cho phép biến nhận giá trị phân số từ 0 đến 1) lại KHÔNG tự động đảm bảo nghiệm nguyên như bài toán P&T Co.?",
        "options_en": [
            "Because plant capacities and assignment task bounds differ, creating non-unimodular constraint intersections that can produce fractional extreme points in LP relaxation",
            "Because Excel Solver is broken",
            "Because four products cannot be divided by three plants evenly",
            "Because the Hungarian method is only valid for quadratic equations"
        ],
        "options_vi": [
            "Vì năng lực gán của các nhà máy không đồng nhất (2, 1, 1), phá vỡ cấu trúc ma trận đơn mô-đun thuần túy và làm xuất hiện các điểm cực biên phân số trong bài toán nới lỏng",
            "Vì bộ giải Excel Solver bị lỗi thuật toán",
            "Vì bốn sản phẩm không thể chia đều cho ba nhà máy",
            "Vì phương pháp Hungarian chỉ áp dụng được cho phương trình bậc hai"
        ],
        "correct_answer": 0,
        "explanation_en": "When supply/demand capacities are asymmetric, generalized network formulations lose total unimodularity unless expanded into symmetric bipartite matchings, requiring branch-and-bound.",
        "explanation_vi": "Khi công suất phân bổ không đều (nhà máy 1 nhận 2 việc, các nhà máy khác nhận 1), nếu không nhân đôi dòng nhà máy 1 thì ma trận mất tính đơn mô-đun và sinh ra nghiệm phân số."
    })

    questions.append({
        "id": "QUES-123",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Multi-Criteria Profit-Service Optimization",
        "difficulty": "Advanced",
        "question_en": "In Nifty Co., Customer 4 has zero minimum purchase commitment but requested up to 8,000 units. If management suspects Customer 4 will become a strategic enterprise client next year, how should a BA modify the LP formulation?",
        "question_vi": "Ở Nifty Co., Khách hàng 4 có cam kết mua tối thiểu bằng 0 nhưng yêu cầu tối đa tới 8,000 đơn vị. Nếu ban giám đốc nhận định Khách hàng 4 là đối tác chiến lược tương lai, BA nên sửa đổi mô hình LP như thế nào?",
        "options_en": [
            "Impose an artificial strategic minimum purchase floor (e.g., Sum_i x_i4 >= 4,000) or apply an intangible customer-lifetime-value (LTV) bonus to Customer 4's profit coefficients",
            "Ban Customer 4 from ever buying products again",
            "Give all 20,000 units of company production to Customer 4 for free",
            "Force Customer 4 to purchase Plant 2"
        ],
        "options_vi": [
            "Thiết lập một sàn cam kết tối thiểu chiến lược (ví dụ Tổng_i x_i4 >= 4,000) hoặc cộng thêm hệ số giá trị trọn đời khách hàng (LTV) vào tỷ suất lợi nhuận của Khách hàng 4",
            "Cấm Khách hàng 4 không bao giờ được mua hàng của công ty nữa",
            "Tặng không toàn bộ 20,000 đơn vị sản phẩm của công ty cho Khách hàng 4",
            "Bắt buộc Khách hàng 4 phải mua lại Nhà máy 2"
        ],
        "correct_answer": 0,
        "explanation_en": "Pure short-term profit maximization might allocate zero units to Customer 4; a BA aligns mathematical constraints with long-term strategic relationship goals by enforcing allocation floors.",
        "explanation_vi": "Nếu chỉ tối đa hóa lợi nhuận ngắn hạn, khách hàng 4 có thể bị gạt ra 0 đơn vị. BA thông minh sẽ đặt sàn sản lượng tối thiểu để bảo vệ mối quan hệ chiến lược dài hạn."
    })

    questions.append({
        "id": "QUES-124",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "Combinatorial Scalability in Assignment",
        "difficulty": "Advanced",
        "question_en": "If Better Products expands to 50 manufacturing plants and 50 new products with strict 1-to-1 assignments, how many possible assignment permutations exist, and why is the Hungarian algorithm essential?",
        "question_vi": "Nếu Better Products mở rộng lên 50 nhà máy và 50 sản phẩm mới với nguyên tắc gán 1-kèm-1, có bao nhiêu hoán vị có thể xảy ra, và vì sao thuật toán Hungarian là thiết yếu?",
        "options_en": [
            "There are 50! (factorial) permutations (approx 3 x 10^64), making brute-force enumeration impossible; the Hungarian algorithm solves it in polynomial O(n^3) time",
            "There are only 50 combinations, which can be checked by hand in 5 minutes",
            "There are 2,500 combinations",
            "Zero permutations exist because large problems cannot have solutions"
        ],
        "options_vi": [
            "Có tới 50! (giai thừa) hoán vị (khoảng 3 x 10^64), khiến việc vét cạn thử sai là bất khả thi; thuật toán Hungarian giải quyết bài toán trong thời gian đa thức O(n^3) chỉ trong vài giây",
            "Chỉ có đúng 50 phương án kết hợp, có thể kiểm tra thủ công bằng tay trong 5 phút",
            "Có đúng 2,500 phương án kết hợp",
            "Không tồn tại hoán vị nào vì các bài toán quy mô lớn không thể có nghiệm"
        ],
        "correct_answer": 0,
        "explanation_en": "50! is an astronomical number exceeding the atoms in a galaxy. Combinatorial optimization algorithms like Hungarian/Kuhn-Munkres cut through combinatorial explosion in polynomial time.",
        "explanation_vi": "50! là con số khổng lồ vượt qua số nguyên tử trong dải ngân hà. Thuật toán Hungarian giúp giải quyết bùng nổ tổ hợp này chỉ trong tích tắc nhờ thời gian đa thức O(n^3)."
    })

    questions.append({
        "id": "QUES-125",
        "exam_id": "EXAM-05",
        "chapter_id": "chap-03",
        "topic": "ERP System Integration of School Assignment Models",
        "difficulty": "Advanced",
        "question_en": "When operationalizing Middletown's school boundary redistricting in a municipal ERP / GIS system, how are tract boundary assignments translated into student transportation rosters?",
        "question_vi": "Khi vận hành hóa phương án phân tuyến trường học Middletown trong hệ thống ERP/GIS đô thị, kết quả gán phân khu được chuyển đổi thành danh sách điều phối học sinh như thế nào?",
        "options_en": [
            "GIS student residential addresses within each tract are joined with the optimized school assignment ID, automatically generating school bus stop routes, driver manifests, and school enrollment rosters",
            "Students are instructed to find their own way to schools using compasses",
            "School principals choose students based on foot races",
            "The ERP system randomly re-assigns students every Monday morning"
        ],
        "options_vi": [
            "Tọa độ địa chỉ cư trú của học sinh trong từng phân khu được liên kết với mã trường học tối ưu, tự động sinh lộ trình điểm đón xe buýt, danh sách tài xế và danh sách điểm danh lớp học",
            "Học sinh tự tìm đường đến trường bằng cách sử dụng la bàn cầm tay",
            "Hiệu trưởng nhà trường chọn học sinh thông qua các cuộc thi chạy bộ",
            "Hệ thống ERP tự động phân lại trường ngẫu nhiên vào mỗi sáng thứ Hai"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP integration couples mathematical optimization outputs with geospatial address master data to produce daily transportation manifests, bus routing, and academic registrations.",
        "explanation_vi": "Tích hợp ERP/GIS chuyển kết quả phân tuyến thành lộ trình xe buýt chi tiết, điểm đón trả học sinh và đồng bộ hồ sơ nhập học điện tử cho từng em."
    })

    return questions
