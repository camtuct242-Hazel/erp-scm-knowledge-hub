# -*- coding: utf-8 -*-
# EXAM 03: Unbalanced Transportation & Dummy Node Modeling (chap-02)
# 25 Questions: Q051 to Q075 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q051 - Q060)
    questions.append({
        "id": "QUES-051",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Unbalanced Transportation Concept",
        "difficulty": "Basic",
        "question_en": "What mathematical issue arises in a transportation problem when total supply does NOT equal total demand?",
        "question_vi": "Vấn đề toán học nào nảy sinh trong bài toán vận tải khi tổng lượng cung KHÔNG bằng tổng lượng cầu?",
        "options_en": [
            "The standard equality constraints contradict each other, violating the Feasible Solutions Property",
            "The computer running the software will physically crash",
            "All unit shipping costs automatically double",
            "All factory production must be cancelled immediately"
        ],
        "options_vi": [
            "Các phương trình ràng buộc dấu bằng mâu thuẫn lẫn nhau, vi phạm Tính chất Nghiệm Khả thi",
            "Máy tính đang chạy phần mềm sẽ bị sập nguồn vật lý",
            "Mọi cước phí vận chuyển đơn vị tự động tăng gấp đôi",
            "Toàn bộ hoạt động sản xuất của nhà máy phải bị hủy bỏ ngay lập tức"
        ],
        "correct_answer": 0,
        "explanation_en": "If Sum(Supply) != Sum(Demand), a system composed strictly of equality constraints has no feasible solution, requiring dummy nodes to restore mathematical balance.",
        "explanation_vi": "Khi Tổng Cung khác Tổng Cầu, hệ phương trình ràng buộc đẳng thức không thể thỏa mãn đồng thời, bắt buộc phải bổ sung điểm giả định để cân bằng."
    })

    questions.append({
        "id": "QUES-052",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dummy Destination Rule",
        "difficulty": "Basic",
        "question_en": "When Total Supply exceeds Total Demand (Sum(Supply) > Sum(Demand)), what mathematical entity is added to balance the tableau?",
        "question_vi": "Khi Tổng Cung lớn hơn Tổng Cầu (Tổng Cung > Tổng Cầu), thực thể toán học nào được bổ sung để cân bằng bảng vận tải?",
        "options_en": [
            "A Dummy Destination with demand equal to the surplus and unit shipping costs of $0",
            "A Dummy Source with negative capacity",
            "A third-party freight trucking company",
            "An extra row of random negative integers"
        ],
        "options_vi": [
            "Một Điểm đến Giả định (Dummy Destination) có nhu cầu bằng đúng lượng cung dư thừa và cước phí đơn vị bằng $0",
            "Một Nguồn Giả định có công suất âm",
            "Một công ty vận tải xe tải trung gian",
            "Một hàng bổ sung chứa các số nguyên âm ngẫu nhiên"
        ],
        "correct_answer": 0,
        "explanation_en": "A dummy destination acts as a virtual sink absorbing surplus capacity at zero cost, ensuring Sum(Supply) = Sum(Demand).",
        "explanation_vi": "Điểm đến giả định tiếp nhận lượng công suất dư thừa với chi phí bằng $0, khôi phục điều kiện Tổng Cung = Tổng Cầu."
    })

    questions.append({
        "id": "QUES-053",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Metro Water District Supplies",
        "difficulty": "Basic",
        "question_en": "In the Metro Water District case, what is the total water supply available across the Colombo, Sacron, and Calorie rivers?",
        "question_vi": "Trong case study Metro Water District, tổng lượng nước có thể cung cấp từ 3 con sông Colombo, Sacron và Calorie là bao nhiêu?",
        "options_en": [
            "16 million acre-feet (5 + 6 + 5)",
            "12.5 million acre-feet",
            "3.5 million acre-feet",
            "25 million acre-feet"
        ],
        "options_vi": [
            "16 triệu acre-feet (5 + 6 + 5)",
            "12.5 triệu acre-feet",
            "3.5 triệu acre-feet",
            "25 triệu acre-feet"
        ],
        "correct_answer": 0,
        "explanation_en": "Colombo (5) + Sacron (6) + Calorie (5) = 16 million acre-feet of available river water.",
        "explanation_vi": "Năng lực cung của 3 con sông là 5 + 6 + 5 = 16 triệu acre-feet nước."
    })

    questions.append({
        "id": "QUES-054",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-02",
        "topic": "Metro Water District Demands",
        "difficulty": "Basic",
        "question_en": "In the Metro Water District case, what is the total water demand needed across Berdoo, Los Devils, San Go, and Hollyglass?",
        "question_vi": "Trong case study Metro Water District, tổng nhu cầu nước của 4 thành phố Berdoo, Los Devils, San Go và Hollyglass là bao nhiêu?",
        "options_en": [
            "12.5 million acre-feet (2 + 5 + 4 + 1.5)",
            "16 million acre-feet",
            "3.5 million acre-feet",
            "10 million acre-feet"
        ],
        "options_vi": [
            "12.5 triệu acre-feet (2 + 5 + 4 + 1.5)",
            "16 triệu acre-feet",
            "3.5 triệu acre-feet",
            "10 triệu acre-feet"
        ],
        "correct_answer": 0,
        "explanation_en": "Berdoo (2) + Los Devils (5) + San Go (4) + Hollyglass (1.5) = 12.5 million acre-feet total demand.",
        "explanation_vi": "Nhu cầu của 4 thành phố là 2 + 5 + 4 + 1.5 = 12.5 triệu acre-feet nước."
    })

    questions.append({
        "id": "QUES-055",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Metro Water Surplus",
        "difficulty": "Basic",
        "question_en": "What is the required demand capacity assigned to the Dummy Destination in the Metro Water District problem?",
        "question_vi": "Nhu cầu được gán cho Điểm đến Giả định trong bài toán Metro Water District là bao nhiêu?",
        "options_en": [
            "3.5 million acre-feet (16 - 12.5)",
            "16 million acre-feet",
            "12.5 million acre-feet",
            "0 acre-feet"
        ],
        "options_vi": [
            "3.5 triệu acre-feet (16 - 12.5)",
            "16 triệu acre-feet",
            "12.5 triệu acre-feet",
            "0 acre-feet"
        ],
        "correct_answer": 0,
        "explanation_en": "Surplus supply = 16 - 12.5 = 3.5 million acre-feet. The dummy destination is assigned this exact quantity.",
        "explanation_vi": "Lượng cung dư thừa = 16 - 12.5 = 3.5 triệu acre-feet. Đây chính là nhu cầu của điểm đến giả định."
    })

    questions.append({
        "id": "QUES-056",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dummy Source Rule",
        "difficulty": "Basic",
        "question_en": "When Total Demand exceeds Total Supply (Sum(Demand) > Sum(Supply)), what mathematical entity must be introduced?",
        "question_vi": "Khi Tổng Cầu vượt quá Tổng Cung (Tổng Cầu > Tổng Cung), thực thể toán học nào bắt buộc phải được bổ sung?",
        "options_en": [
            "A Dummy Source with supply capacity equal to the shortage deficit",
            "A Dummy Destination with infinite demand",
            "A bank loan credit constraint",
            "An export tariff penalty on retail customers"
        ],
        "options_vi": [
            "Một Nguồn Giả định (Dummy Source) có lượng cung bằng đúng lượng thiếu hụt của thị trường",
            "Một Điểm đến Giả định có nhu cầu vô hạn",
            "Một ràng buộc hạn mức vay vốn ngân hàng",
            "Một mức thuế xuất khẩu áp lên người tiêu dùng bán lẻ"
        ],
        "correct_answer": 0,
        "explanation_en": "When demand outstrips supply, an artificial Dummy Source supplies the deficit so all destination demands are algebraically met.",
        "explanation_vi": "Khi cầu vượt cung, một Nguồn Giả định được thêm vào với lượng cung bằng phần thiếu hụt để hệ phương trình đẳng thức cân bằng."
    })

    questions.append({
        "id": "QUES-057",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dummy Shipping Cost",
        "difficulty": "Basic",
        "question_en": "Why are unit shipping costs to a Dummy Destination typically set to $0?",
        "question_vi": "Vì sao cước phí vận chuyển đơn vị đến Điểm đến Giả định thường được đặt bằng $0?",
        "options_en": [
            "Because goods allocated to the dummy destination are not actually shipped; they remain as unutilized capacity at the source",
            "Because the government subsidizes all highway transportation",
            "Because truck drivers work for free when visiting dummy warehouses",
            "To prevent the computer software from calculating square roots"
        ],
        "options_vi": [
            "Vì lượng hàng phân bổ cho điểm giả định không được vận chuyển trong thực tế; chúng đại diện cho công suất chưa huy động tại nguồn",
            "Vì chính phủ tài trợ 100% cước phí vận chuyển đường bộ",
            "Vì tài xế xe tải không nhận thù lao khi đến nhà kho giả định",
            "Để ngăn phần mềm máy tính không phải tính căn bậc hai"
        ],
        "correct_answer": 0,
        "explanation_en": "Allocations to a dummy destination reflect unused plant capacity left in situ, incurring zero outbound freight expense.",
        "explanation_vi": "Hàng phân bổ vào điểm giả định chính là công suất nhà máy để nhàn rỗi, không phát sinh bất kỳ chi phí chuyên chở nào."
    })

    questions.append({
        "id": "QUES-058",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Metro Water Prohibited Route",
        "difficulty": "Basic",
        "question_en": "In the Metro Water District case, which city CANNOT receive water from the Calorie River due to geographical aqueduct constraints?",
        "question_vi": "Trong case study Metro Water District, thành phố nào KHÔNG THỂ tiếp nhận nước từ sông Calorie do hạn chế địa lý của hệ thống dẫn nước?",
        "options_en": [
            "Hollyglass",
            "Berdoo",
            "Los Devils",
            "San Go"
        ],
        "options_vi": [
            "Hollyglass",
            "Berdoo",
            "Los Devils",
            "San Go"
        ],
        "correct_answer": 0,
        "explanation_en": "The textbook explicitly states: 'with the exception that no provision has been made to supply Hollyglass with Calorie River water.'",
        "explanation_vi": "Giáo trình nêu rõ: không có đường ống dẫn nước nào được thiết kế để cấp nước từ sông Calorie cho thành phố Hollyglass."
    })

    questions.append({
        "id": "QUES-059",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Handling Prohibited Route in Metro Water",
        "difficulty": "Basic",
        "question_en": "How is the prohibited aqueduct route from Calorie River to Hollyglass represented mathematically in the transportation matrix?",
        "question_vi": "Tuyến đường ống cấm từ sông Calorie đến Hollyglass được thể hiện toán học như thế nào trong ma trận vận tải?",
        "options_en": [
            "By setting the unit cost to a prohibitively large penalty M (e.g., $999,999) or omitting the variable x_Calorie,Hollyglass",
            "By setting the cost to -$100",
            "By doubling Hollyglass's water demand",
            "By deleting the Calorie River from the database"
        ],
        "options_vi": [
            "Bằng cách gán cước phí đơn vị bằng một số phạt M cực lớn (ví dụ $999,999) hoặc loại bỏ biến x_Calorie,Hollyglass khỏi mô hình",
            "Bằng cách gán cước phí bằng -$100",
            "Bằng cách nhân đôi nhu cầu nước của thành phố Hollyglass",
            "Bằng cách xóa luôn sông Calorie khỏi cơ sở dữ liệu"
        ],
        "correct_answer": 0,
        "explanation_en": "Assigning Big-M ensures that cost minimization algorithms will never assign positive flow along an infeasible path.",
        "explanation_vi": "Gán chi phí M cực lớn khiến hàm mục tiêu chi phí phạt rất nặng, buộc thuật toán loại bỏ hoàn toàn tuyến cấm này khỏi nghiệm."
    })

    questions.append({
        "id": "QUES-060",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Water Allocation Unit",
        "difficulty": "Basic",
        "question_en": "What measurement unit is used for water volumes and freight costs in the Metro Water District case study?",
        "question_vi": "Đơn vị đo lường nào được sử dụng cho khối lượng nước và cước phí trong case study Metro Water District?",
        "options_en": [
            "Millions of acre-feet for water volumes, and dollars per acre-foot for costs",
            "Gallons and cents",
            "Liters and Euros",
            "Barrels and British Pounds"
        ],
        "options_vi": [
            "Triệu acre-feet cho thể tích nước, và Đô la trên mỗi acre-foot cho chi phí",
            "Gallon và cent",
            "Lít và Euro",
            "Thùng (Barrels) và Bảng Anh"
        ],
        "correct_answer": 0,
        "explanation_en": "The case uses millions of acre-feet for quantities and $/acre-foot for transportation costs.",
        "explanation_vi": "Số liệu case dùng đơn vị triệu acre-feet nước và chi phí $/acre-foot."
    })

    # Intermediate (Q061 - Q070)
    questions.append({
        "id": "QUES-061",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Metro Water Optimal Allocation",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for Metro Water District, from which river source is the 3.5 million acre-feet of unutilized surplus water retained?",
        "question_vi": "Trong phương án tối ưu của Metro Water District, 3.5 triệu acre-feet nước dư thừa không khai thác được giữ lại tại con sông nào?",
        "options_en": [
            "The Calorie River retains 2.5M acre-feet and Colombo retains 1M acre-feet in the dummy allocation",
            "The Sacron River retains all 3.5M acre-feet",
            "Hollyglass retains all water in its municipal reservoir",
            "All three rivers are 100% drained with zero surplus retained"
        ],
        "options_vi": [
            "Sông Calorie giữ lại 2.5 triệu acre-feet và sông Colombo giữ lại 1 triệu acre-feet (phân bổ cho Dummy)",
            "Sông Sacron giữ lại toàn bộ 3.5 triệu acre-feet",
            "Thành phố Hollyglass giữ lại toàn bộ nước trong hồ chứa đô thị",
            "Cả 3 con sông đều bị khai thác cạn kiệt 100% không còn dư thừa"
        ],
        "correct_answer": 0,
        "explanation_en": "Solving the Metro Water LP model shows that Calorie River (due to high unit costs and the Hollyglass restriction) and Colombo leave water unextracted.",
        "explanation_vi": "Giải mô hình LP cho thấy sông Calorie (do cước cao và bị cấm cấp cho Hollyglass) và Colombo có chi phí biên kém hấp dẫn nhất nên được phân bổ vào Dummy."
    })

    questions.append({
        "id": "QUES-062",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dummy Destination with Storage Costs",
        "difficulty": "Intermediate",
        "question_en": "If retaining surplus inventory at a factory incurs an inventory holding charge, how should the Dummy Destination cost coefficients be modified?",
        "question_vi": "Nếu việc giữ lại hàng hóa dư thừa tại nhà máy làm phát sinh chi phí lưu kho, các hệ số chi phí đến Điểm đến Giả định cần được điều chỉnh như thế nào?",
        "options_en": [
            "Set c_i,Dummy equal to the unit holding cost h_i of retaining inventory at plant i, rather than $0",
            "Set all shipping costs to negative numbers",
            "Multiply all customer demands by 10",
            "Delete the dummy destination and force plants to overproduce"
        ],
        "options_vi": [
            "Gán c_i,Dummy bằng đúng chi phí lưu kho đơn vị h_i khi giữ hàng lại tại nhà máy i, thay vì để bằng $0",
            "Gán tất cả cước phí vận chuyển thành số âm",
            "Nhân toàn bộ nhu cầu của khách hàng lên 10 lần",
            "Xóa bỏ điểm giả định và ép các nhà máy phải sản xuất dư thừa"
        ],
        "correct_answer": 0,
        "explanation_en": "When idling or storing excess capacity has differential holding costs across plants, assigning c_i,Dummy = h_i ensures Solver idles the cheapest facility first.",
        "explanation_vi": "Khi chi phí lưu kho tại các nhà máy khác nhau, việc gán c_i,Dummy = h_i giúp Solver ưu tiên để tồn kho tại nhà máy có chi phí rẻ nhất."
    })

    questions.append({
        "id": "QUES-063",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dummy Source with Penalty Costs",
        "difficulty": "Intermediate",
        "question_en": "When Total Demand > Total Supply, why might a company assign distinct penalty costs to the Dummy Source cells instead of $0?",
        "question_vi": "Khi Tổng Cầu > Tổng Cung, vì sao doanh nghiệp lại có thể gán các mức chi phí phạt khác nhau cho Nguồn Giả định thay vì để bằng $0?",
        "options_en": [
            "To reflect varying customer profit margins or contractual stockout penalties, ensuring vital VIP customers are prioritized for physical deliveries",
            "To artificially increase corporate revenue on the balance sheet",
            "To prevent delivery trucks from consuming fuel",
            "Because the tax authorities mandate negative shipping tariffs"
        ],
        "options_vi": [
            "Để phản ánh sự chênh lệch về tỷ suất lợi nhuận hoặc mức phạt trễ hạn giữa các khách hàng, đảm bảo khách hàng VIP được ưu tiên giao hàng thực tế",
            "Để làm tăng doanh thu ảo trên bảng cân đối kế toán",
            "Để ngăn xe tải giao hàng không tiêu hao nhiên liệu",
            "Vì cơ quan thuế bắt buộc phải áp dụng biểu cước vận chuyển âm"
        ],
        "correct_answer": 0,
        "explanation_en": "Assigning high penalty costs to dummy source cells for high-priority customers forces the optimizer to satisfy their demands using real physical supply first.",
        "explanation_vi": "Gán chi phí phạt cao cho ô nguồn giả định của khách hàng ưu tiên sẽ buộc thuật toán phân bổ hàng thực cho họ trước để tránh bị phạt nặng."
    })

    questions.append({
        "id": "QUES-064",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Inequality vs Equality Formulation",
        "difficulty": "Intermediate",
        "question_en": "In Excel Solver, how can an unbalanced transportation problem with Total Supply > Total Demand be solved WITHOUT adding a Dummy Destination column?",
        "question_vi": "Trong Excel Solver, làm thế nào để giải bài toán vận tải không cân bằng khi Tổng Cung > Tổng Cầu mà KHÔNG CẦN thêm cột Điểm đến Giả định?",
        "options_en": [
            "Formulate the supply constraints as less-than-or-equal-to inequalities (Sum_j x_ij <= s_i) while keeping demand constraints as strict equalities (Sum_i x_ij = d_j)",
            "Change all cell numbers to Roman numerals",
            "Set the objective function to Maximize rather than Minimize",
            "Delete all supply constraints entirely"
        ],
        "options_vi": [
            "Thiết lập các ràng buộc cung dưới dạng bất đẳng thức nhỏ hơn hoặc bằng (Tổng_j x_ij <= s_i) trong khi vẫn giữ ràng buộc cầu là dấu bằng (Tổng_i x_ij = d_j)",
            "Chuyển toàn bộ các chữ số trên bảng tính sang chữ số La Mã",
            "Đặt hàm mục tiêu thành Cực đại hóa (Maximize) thay vì Cực tiểu hóa",
            "Xóa bỏ hoàn toàn toàn bộ các ràng buộc cung cấp"
        ],
        "correct_answer": 0,
        "explanation_en": "In general linear programming, supply surplus is natively handled by inequality constraints (Supply row Sum <= Capacity), where slack variables represent dummy allocations.",
        "explanation_vi": "Trong quy hoạch tuyến tính, bất đẳng thức <= cho phép xuất lượng hàng nhỏ hơn hoặc bằng công suất, biến bù (slack) tự động đóng vai trò điểm giả định."
    })

    questions.append({
        "id": "QUES-065",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Big-M Magnitude Guidelines",
        "difficulty": "Intermediate",
        "question_en": "When using the Big-M method in Excel Solver to prohibit a transportation route, what risk arises if M is chosen to be excessively astronomical (e.g., 10^30)?",
        "question_vi": "Khi sử dụng phương pháp số M lớn trong Excel Solver để cấm một tuyến vận chuyển, rủi ro nào xảy ra nếu chọn giá trị M quá khổng lồ (ví dụ 10^30)?",
        "options_en": [
            "Numerical instability, round-off errors, and floating-point overflow during simplex matrix inversion",
            "The computer screen will catch fire",
            "Excel will automatically delete the user's email inbox",
            "The shipping trucks will refuse to start their engines"
        ],
        "options_vi": [
            "Lỗi mất ổn định số học, sai số làm tròn và tràn số dấu phẩy động (floating-point overflow) trong quá trình nghịch đảo ma trận đơn hình",
            "Màn hình máy tính sẽ bị bốc cháy",
            "Excel sẽ tự động xóa sạch hộp thư điện tử của người dùng",
            "Các xe tải vận chuyển sẽ từ chối khởi động động cơ"
        ],
        "correct_answer": 0,
        "explanation_en": "Excessively large M values distort floating-point precision, causing numerical degeneracy. M should be chosen just significantly larger than the maximum genuine cost (e.g., 10x-100x max cost).",
        "explanation_vi": "Chọn số M quá lớn gây sai số làm tròn số học trên máy tính. Chỉ cần chọn M lớn gấp 10-100 lần chi phí lớn nhất trong bảng là đủ để chặn tuyến."
    })

    questions.append({
        "id": "QUES-066",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Better Products Case 2.1 Imbalance",
        "difficulty": "Intermediate",
        "question_en": "In Better Products Co. (Case 2.1), what is the total available daily plant capacity versus total required daily product demand?",
        "question_vi": "Trong case Better Products Co. (Case 2.1), tổng công suất nhà máy hàng ngày so với tổng nhu cầu sản phẩm cần sản xuất hàng ngày là bao nhiêu?",
        "options_en": [
            "Total plant capacity is 195 units/day (75 + 75 + 45), while required production demand is 120 units/day (20 + 30 + 30 + 40)",
            "Plant capacity is 120 units/day and demand is 195 units/day",
            "Both capacity and demand are exactly 300 units/day",
            "Capacity is 75 units/day and demand is 500 units/day"
        ],
        "options_vi": [
            "Tổng công suất nhà máy là 195 đơn vị/ngày (75 + 75 + 45), trong khi tổng nhu cầu sản xuất là 120 đơn vị/ngày (20 + 30 + 30 + 40)",
            "Công suất nhà máy là 120 đơn vị/ngày và nhu cầu là 195 đơn vị/ngày",
            "Cả công suất và nhu cầu đều bằng đúng 300 đơn vị/ngày",
            "Công suất là 75 đơn vị/ngày và nhu cầu là 500 đơn vị/ngày"
        ],
        "correct_answer": 0,
        "explanation_en": "Plant 1 (75) + Plant 2 (75) + Plant 3 (45) = 195 units/day. Products 1-4 demand = 20 + 30 + 30 + 40 = 120 units/day. Surplus capacity = 75 units/day.",
        "explanation_vi": "3 nhà máy có công suất 75 + 75 + 45 = 195 đơn vị/ngày; 4 sản phẩm cần 20 + 30 + 30 + 40 = 120 đơn vị/ngày. Dư thừa công suất 75 đơn vị/ngày."
    })

    questions.append({
        "id": "QUES-067",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Better Products Case 2.1 Formulation",
        "difficulty": "Intermediate",
        "question_en": "How is the 75-unit surplus capacity balanced in the Better Products Case 2.1 transportation tableau?",
        "question_vi": "Lượng công suất dư thừa 75 đơn vị được cân bằng như thế nào trong bảng vận tải của Better Products Case 2.1?",
        "options_en": [
            "By adding a Dummy Product column with demand of 75 units/day and unit costs of $0 across all three plants",
            "By forcing Plant 3 to shut down permanently",
            "By increasing Product 1 demand from 20 to 95 units/day",
            "By adding three new manufacturing facilities"
        ],
        "options_vi": [
            "Bằng cách thêm một cột Sản phẩm Giả định (Dummy Product) có nhu cầu 75 đơn vị/ngày và cước phí đơn vị bằng $0 cho cả 3 nhà máy",
            "Bằng cách bắt buộc Nhà máy 3 phải đóng cửa vĩnh viễn",
            "Bằng cách tăng nhu cầu của Sản phẩm 1 từ 20 lên 95 đơn vị/ngày",
            "Bằng cách xây dựng thêm ba nhà máy sản xuất mới"
        ],
        "correct_answer": 0,
        "explanation_en": "The 75-unit surplus capacity across the plants is absorbed by an artificial 'Dummy Product' destination with $0 cost.",
        "explanation_vi": "Công suất nhàn rỗi 75 đơn vị được hấp thụ bởi cột Sản phẩm Giả định với chi phí $0."
    })

    questions.append({
        "id": "QUES-068",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Better Products Case 2.1 Prohibited Route",
        "difficulty": "Intermediate",
        "question_en": "In Better Products Case 2.1, what technical manufacturing restriction is imposed on Plant 2?",
        "question_vi": "Trong Better Products Case 2.1, ràng buộc kỹ thuật sản xuất nào bị áp đặt lên Nhà máy 2?",
        "options_en": [
            "Plant 2 cannot produce Product 3, requiring cell (Plant 2, Product 3) to be assigned Big-M cost or constrained to zero",
            "Plant 2 is prohibited from hiring night-shift workers",
            "Plant 2 must produce only Product 1 and nothing else",
            "Plant 2 must ship all output to Sacramento"
        ],
        "options_vi": [
            "Nhà máy 2 không thể sản xuất Sản phẩm 3, đòi hỏi ô (Nhà máy 2, Sản phẩm 3) phải gán chi phí Big-M hoặc chặn biến bằng 0",
            "Nhà máy 2 bị cấm thuê công nhân làm ca đêm",
            "Nhà máy 2 chỉ được phép sản xuất Sản phẩm 1 và không làm gì khác",
            "Nhà máy 2 phải chuyển toàn bộ sản lượng về Sacramento"
        ],
        "correct_answer": 0,
        "explanation_en": "The case states Plant 2 cannot manufacture Product 3 due to tooling limitations, enforced via penalty cost M.",
        "explanation_vi": "Đề bài quy định Nhà máy 2 không có công nghệ để sản xuất Sản phẩm 3, do đó c23 = M để loại bỏ khả năng này."
    })

    questions.append({
        "id": "QUES-069",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Dual Value of Dummy Constraints",
        "difficulty": "Intermediate",
        "question_en": "In an unbalanced problem where Total Supply > Total Demand, what is the shadow price (dual value) of the Dummy Destination constraint?",
        "question_vi": "Trong bài toán không cân bằng có Tổng Cung > Tổng Cầu, giá bóng (giá trị đối ngẫu) của ràng buộc Điểm đến Giả định luôn bằng bao nhiêu?",
        "options_en": [
            "$0, because absorbing one additional unit of surplus supply incurs zero marginal system cost",
            "$1,000,000",
            "Equal to the price of gold on international markets",
            "-100"
        ],
        "options_vi": [
            "$0, vì việc tiếp nhận thêm một đơn vị cung dư thừa không làm phát sinh thêm bất kỳ chi phí biên nào cho hệ thống",
            "$1,000,000",
            "Bằng giá vàng trên thị trường quốc tế",
            "-100"
        ],
        "correct_answer": 0,
        "explanation_en": "Because dummy shipping costs are zero and excess capacity is slack, expanding dummy demand has a zero marginal cost impact.",
        "explanation_vi": "Do cước phí đến điểm giả định bằng 0 và công suất đang dư thừa, việc nới lỏng thêm 1 đơn vị giả định có chi phí biên bằng $0."
    })

    questions.append({
        "id": "QUES-070",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "ERP Capacity Planning Integration",
        "difficulty": "Intermediate",
        "question_en": "How does an ERP Capacity Requirements Planning (CRP) module utilize the outputs of a balanced transportation tableau?",
        "question_vi": "Phân hệ Hoạch định Nhu cầu Năng lực (CRP) trong ERP sử dụng kết quả đầu ra của bảng vận tải cân bằng như thế nào?",
        "options_en": [
            "It converts plant allocations into machine work center hours and schedules labor shifts to fulfill production quotas",
            "It immediately terminates factory maintenance technicians",
            "It prints retail price tags for supermarket display shelves",
            "It cancels all open purchase orders for raw materials"
        ],
        "options_vi": [
            "Quy đổi sản lượng phân bổ tại từng nhà máy thành số giờ làm việc tại các trung tâm máy và lên lịch ca kíp công nhân",
            "Sa thải ngay lập tức đội ngũ kỹ thuật viên bảo trì nhà máy",
            "In tem giá bán lẻ để dán lên kệ trưng bày tại siêu thị",
            "Hủy bỏ toàn bộ các đơn đặt mua nguyên vật liệu thô đang mở"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP CRP takes optimized plant production allocations and explodes them into required work center machine hours and labor staffing schedules.",
        "explanation_vi": "Module CRP lấy sản lượng tối ưu phân bổ cho từng xưởng để tính toán định mức giờ máy và bố trí ca kíp nhân công phù hợp."
    })

    # Advanced (Q071 - Q075)
    questions.append({
        "id": "QUES-071",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "BA Requirements for Idle Plant Capacity",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is defining business rules for handling surplus plant capacity in an ERP supply chain module. Which business rule best operationalizes the dummy allocation?",
        "question_vi": "Một Business Analyst đang định nghĩa quy tắc nghiệp vụ để xử lý công suất nhà máy nhàn rỗi trong phân hệ ERP SCM. Quy tắc nghiệp vụ nào sau đây vận hành hóa tốt nhất lượng phân bổ giả định?",
        "options_en": [
            "When optimization allocates volume to Dummy_Sink, the system shall flag the corresponding plant work centers as 'Planned Idle Capacity' and block automated raw material replenishment orders for that volume",
            "The system shall instruct plant managers to manufacture unrequested goods and store them in outdoor parking lots",
            "The system shall automatically bill end customers for goods that were never manufactured",
            "The system shall shut down the entire enterprise network whenever surplus capacity is detected"
        ],
        "options_vi": [
            "Khi thuật toán tối ưu phân bổ sản lượng vào Dummy_Sink, hệ thống phải gắn cờ trung tâm máy của nhà máy tương ứng là 'Công suất Nhàn rỗi Kế hoạch' và chặn các đơn mua nguyên vật liệu tự động cho phần sản lượng này",
            "Hệ thống yêu cầu quản đốc tiếp tục sản xuất hàng không ai mua và đem chất đống ngoài bãi đỗ xe",
            "Hệ thống tự động phát hành hóa đơn đòi tiền khách hàng cho các sản phẩm chưa từng được sản xuất",
            "Hệ thống tắt toàn bộ mạng lưới doanh nghiệp bất cứ khi nào phát hiện có công suất dư thừa"
        ],
        "correct_answer": 0,
        "explanation_en": "A robust BA business rule translates mathematical dummy slack into concrete operational controls: preventing unwanted procurement and planning preventive machine maintenance.",
        "explanation_vi": "Quy tắc nghiệp vụ chặt chẽ chuyển đổi biến ảo toán học thành hành động thực tế: không mua nguyên liệu thừa và tận dụng giờ máy nhàn rỗi để bảo dưỡng máy móc."
    })

    questions.append({
        "id": "QUES-072",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Multi-Facility Capacity Rationing",
        "difficulty": "Advanced",
        "question_en": "In a severe shortage crisis where Total Demand exceeds Total Supply by 30%, which multi-objective optimization criteria should a BA specify to ensure commercial equity?",
        "question_vi": "Trong cuộc khủng hoảng thiếu hụt nghiêm trọng khi Tổng Cầu vượt Tổng Cung tới 30%, tiêu chí tối ưu hóa đa mục tiêu nào một BA nên chỉ định để đảm bảo tính công bằng thương mại?",
        "options_en": [
            "Incorporate a Max-Min fairness objective or proportional rationing constraints ensuring every customer region receives at least alpha% of their base demand",
            "Allocate 100% of supply to the nearest warehouse and 0% to all other regions",
            "Distribute goods based on a random lottery drawn by warehouse workers",
            "Stop all shipments completely until customer demand drops to zero"
        ],
        "options_vi": [
            "Bổ sung hàm mục tiêu công bằng Max-Min hoặc ràng buộc phân bổ tỷ lệ đảm bảo mỗi khu vực khách hàng nhận được tối thiểu alpha% nhu cầu cơ sở của họ",
            "Phân bổ 100% hàng cho kho gần nhất và bỏ mặc 0% cho tất cả các vùng khác",
            "Phân phối hàng hóa dựa trên kết quả bốc thăm xổ số ngẫu nhiên của nhân viên kho",
            "Dừng toàn bộ các chuyến giao hàng cho đến khi nhu cầu của khách hàng tự giảm về 0"
        ],
        "options_vi": [
            "Bổ sung mục tiêu công bằng Max-Min hoặc ràng buộc tỷ lệ đảm bảo mỗi vùng nhận tối thiểu alpha% nhu cầu cơ sở",
            "Giao 100% cho kho gần nhất và 0% cho các nơi khác",
            "Bốc thăm ngẫu nhiên người nhận hàng",
            "Ngừng bán hàng vô thời hạn"
        ],
        "correct_answer": 0,
        "explanation_en": "Unconstrained cost minimization under shortages can starve distant customers completely; fair-share proportional rationing constraints protect enterprise customer relationships.",
        "explanation_vi": "Nếu chỉ tối thiểu chi phí khi thiếu hàng, các khách hàng ở xa sẽ bị bỏ đói 100%. Ràng buộc phân bổ tỷ lệ công bằng giúp bảo vệ mối quan hệ khách hàng dài hạn."
    })

    questions.append({
        "id": "QUES-073",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Degeneracy Induced by Dummy Sinks",
        "difficulty": "Advanced",
        "question_en": "Why do transportation tableaus with Dummy Destinations frequently encounter algorithmic degeneracy during stepping-stone iterations?",
        "question_vi": "Vì sao bảng vận tải có Điểm đến Giả định thường dễ gặp phải hiện tượng suy biến thuật toán trong quá trình lặp stepping-stone?",
        "options_en": [
            "Because multiple supply origins share identical $0 unit costs to the dummy destination, frequently causing simultaneous basic variable dropouts",
            "Because dummy destinations contain corrupt data bytes",
            "Because Excel cannot divide zero by zero",
            "Because truck drivers refuse to transport non-existent merchandise"
        ],
        "options_vi": [
            "Vì nhiều nguồn cung cùng có chung cước phí bằng $0 đến điểm giả định, dễ dẫn đến việc nhiều biến cơ sở đồng thời về 0 trong cùng một bước lặp đơn hình",
            "Vì các điểm đến giả định chứa các byte dữ liệu bị lỗi",
            "Vì Excel không thể thực hiện phép chia 0 cho 0",
            "Vì tài xế xe tải từ chối vận chuyển những lô hàng không có thật"
        ],
        "correct_answer": 0,
        "explanation_en": "Ties in reduced costs and zero coefficients across dummy columns frequently lead to simultaneous basic dropouts, reducing positive basic cells below (m + n - 1).",
        "explanation_vi": "Cước phí 0 đồng nhất ở cột giả định tạo ra các phương án hòa chi phí, khiến nhiều ô cơ sở cùng triệt tiêu về 0, làm phát sinh suy biến."
    })

    questions.append({
        "id": "QUES-074",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "Environmental Water Allocation Trade-offs",
        "difficulty": "Advanced",
        "question_en": "In the Metro Water District case, if state environmental regulators mandate that at least 1.5 million acre-feet of Sacron River flow must remain in the natural delta, how is this modeled?",
        "question_vi": "Trong case Metro Water District, nếu cơ quan bảo vệ môi trường quy định bắt buộc phải giữ lại tối thiểu 1.5 triệu acre-feet nước sông Sacron cho vùng đồng bằng tự nhiên, điều này được mô hình hóa như thế nào?",
        "options_en": [
            "Add a lower bound constraint on the allocation to the dummy destination: x_Sacron,Dummy >= 1.5 (or reduce Sacron's exportable capacity to 4.5M)",
            "Increase Hollyglass's water bill by 50%",
            "Impose Big-M cost on all rivers",
            "Cancel all water deliveries to Berdoo and Los Devils"
        ],
        "options_vi": [
            "Thêm ràng buộc cận dưới cho biến phân bổ vào điểm giả định: x_Sacron,Dummy >= 1.5 (hoặc giảm công suất khai thác khả dụng của Sacron xuống còn 4.5 triệu)",
            "Tăng hóa đơn tiền nước của thành phố Hollyglass thêm 50%",
            "Áp dụng cước phí phạt Big-M lên toàn bộ các con sông",
            "Hủy bỏ toàn bộ việc cấp nước cho Berdoo và Los Devils"
        ],
        "correct_answer": 0,
        "explanation_en": "Mandatory unextracted ecological flow is modeled by setting a minimum allocation threshold on the dummy slack variable (x_Sacron,Dummy >= 1.5) or derating supply.",
        "explanation_vi": "Duy trì dòng chảy sinh thái bắt buộc được mô hình hóa bằng cách đặt cận dưới cho biến giả định (x_Sacron,Dummy >= 1.5) hoặc trừ trực tiếp vào công suất cấp."
    })

    questions.append({
        "id": "QUES-075",
        "exam_id": "EXAM-03",
        "chapter_id": "chap-02",
        "topic": "ERP Integration of Plant Allocation Constraints",
        "difficulty": "Advanced",
        "question_en": "When integrating Better Products Case 2.1 into an ERP system (e.g., SAP S/4HANA PP-PI), how should the prohibition of Product 3 on Plant 2 be configured?",
        "question_vi": "Khi tích hợp bài toán Better Products Case 2.1 vào hệ thống ERP (như SAP S/4HANA PP), lệnh cấm sản xuất Sản phẩm 3 tại Nhà máy 2 cần được cấu hình như thế nào?",
        "options_en": [
            "By deliberately omitting a Production Version and Routing linkage for Material 3 at Plant 2's plant-specific Material Master view",
            "By setting the selling price of Product 3 to zero in the sales catalog",
            "By deleting Plant 2's physical mailing address from the vendor database",
            "By locking all user logins belonging to Plant 2's factory workers"
        ],
        "options_vi": [
            "Bằng cách chủ động không tạo Định mức/Phiên bản Sản xuất (Production Version) và Quy trình Công nghệ (Routing) cho Sản phẩm 3 tại view Nhà máy 2 trong Material Master",
            "Bằng cách đặt giá bán của Sản phẩm 3 bằng 0 trong danh mục bán hàng",
            "Bằng cách xóa địa chỉ gửi thư của Nhà máy 2 khỏi danh bạ nhà cung ứng",
            "Bằng cách khóa toàn bộ tài khoản đăng nhập của công nhân Nhà máy 2"
        ],
        "correct_answer": 0,
        "explanation_en": "In SAP, a plant cannot manufacture a material if no valid Production Version (BOM + Routing link) exists for that material in that specific plant code.",
        "explanation_vi": "Trong ERP, việc cấm sản xuất một mặt hàng tại một nhà máy được kiểm soát chặt chẽ bằng cách không tạo Phiên bản sản xuất (Production Version) cho mã vật tư đó tại nhà máy đó."
    })

    return questions
