# -*- coding: utf-8 -*-
# EXAM 02: LP Transportation Models & P&T Company Case (chap-01)
# 25 Questions: Q026 to Q050 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q026 - Q035)
    questions.append({
        "id": "QUES-026",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Transportation LP Fundamentals",
        "difficulty": "Basic",
        "question_en": "What is the defining characteristic of decision variable x_ij in the P&T Co. transportation model?",
        "question_vi": "Đặc điểm định nghĩa của biến quyết định x_ij trong mô hình vận tải của công ty P&T là gì?",
        "options_en": [
            "The number of truckloads of canned peas shipped from cannery i to warehouse j",
            "The total monetary profit earned by selling peas at retail store j",
            "The number of days required for truck driver i to inspect warehouse j",
            "The percentage discount offered to grocery wholesalers in region j"
        ],
        "options_vi": [
            "Số chuyến xe tải chở đậu đóng hộp được vận chuyển từ nhà máy đóng hộp i đến kho hàng j",
            "Tổng lợi nhuận tiền tệ thu được khi bán đậu tại cửa hàng bán lẻ j",
            "Số ngày cần thiết để tài xế xe tải i đến kiểm tra nhà kho j",
            "Tỷ lệ phần trăm chiết khấu dành cho các đại lý bán buôn tạp hóa tại khu vực j"
        ],
        "correct_answer": 0,
        "explanation_en": "In the P&T model, x_ij represents the physical volume (truckloads) transported from each cannery origin i to warehouse destination j.",
        "explanation_vi": "Trong mô hình P&T, x_ij đại diện cho khối lượng vật lý (số chuyến xe tải) được điều chuyển từ nhà máy i đến kho hàng j."
    })

    questions.append({
        "id": "QUES-027",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Feasible Solutions Property",
        "difficulty": "Basic",
        "question_en": "According to the Feasible Solutions Property, when does a standard transportation problem possess feasible solutions?",
        "question_vi": "Theo Tính chất Nghiệm Khả thi, khi nào một bài toán vận tải chuẩn tắc chắc chắn có nghiệm khả thi?",
        "options_en": [
            "When the sum of all available supplies exactly equals the sum of all required demands",
            "When all unit shipping costs are negative numbers",
            "When the number of supply origins exceeds 100 facilities",
            "When every warehouse is located within 5 miles of a cannery"
        ],
        "options_vi": [
            "Khi tổng lượng cung cấp từ tất cả các nguồn bằng đúng tổng lượng nhu cầu của tất cả các điểm đích",
            "Khi tất cả cước phí vận chuyển đơn vị đều mang giá trị âm",
            "Khi số lượng các nhà máy nguồn vượt quá 100 cơ sở",
            "Khi mọi nhà kho đều nằm trong bán kính 5 dặm quanh nhà máy đóng hộp"
        ],
        "correct_answer": 0,
        "explanation_en": "The Feasible Solutions Property requires Sum(Supply_i) = Sum(Demand_j) so all equality constraints can be satisfied simultaneously.",
        "explanation_vi": "Tính chất nghiệm khả thi yêu cầu Tổng Cung = Tổng Cầu để hệ phương trình ràng buộc đẳng thức có nghiệm."
    })

    questions.append({
        "id": "QUES-028",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Network Parameters",
        "difficulty": "Basic",
        "question_en": "In the P&T Company case, what is the total system supply across Bellingham, Eugene, and Albert Lea?",
        "question_vi": "Trong case study công ty P&T, tổng lượng cung toàn hệ thống từ Bellingham, Eugene và Albert Lea là bao nhiêu?",
        "options_en": [
            "300 truckloads (75 + 125 + 100)",
            "500 truckloads",
            "150 truckloads",
            "1,000 truckloads"
        ],
        "options_vi": [
            "300 chuyến xe tải (75 + 125 + 100)",
            "500 chuyến xe tải",
            "150 chuyến xe tải",
            "1,000 chuyến xe tải"
        ],
        "correct_answer": 0,
        "explanation_en": "Bellingham (75) + Eugene (125) + Albert Lea (100) = 300 truckloads, exactly matching total warehouse demand.",
        "explanation_vi": "Tổng năng lực sản xuất của 3 nhà máy là 75 + 125 + 100 = 300 chuyến xe tải, khớp hoàn hảo với tổng nhu cầu của 4 kho hàng."
    })

    questions.append({
        "id": "QUES-029",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Requirements Assumption",
        "difficulty": "Basic",
        "question_en": "What is the practical implication of the 'Requirements Assumption' in the P&T transportation model?",
        "question_vi": "Ý nghĩa thực tiễn của 'Giả định Nhu cầu và Cung ứng' (Requirements Assumption) trong mô hình vận tải P&T là gì?",
        "options_en": [
            "All output produced by each cannery must be shipped, and each warehouse must receive its exact allocated quota",
            "Canneries are allowed to dump unsold peas into local rivers",
            "Warehouses may order unlimited additional truckloads without paying freight",
            "Truck drivers decide their own daily delivery routes based on weather"
        ],
        "options_vi": [
            "Toàn bộ sản lượng của mỗi nhà máy bắt buộc phải xuất xưởng hết, và mỗi nhà kho phải tiếp nhận đúng định ngạch nhu cầu",
            "Các nhà máy được phép đổ đậu thừa không bán được xuống các con sông địa phương",
            "Các kho hàng có thể tùy ý đặt thêm không giới hạn các chuyến xe tải mà không cần trả tiền cước",
            "Tài xế xe tải tự quyết định tuyến đường giao hàng hàng ngày dựa vào thời tiết"
        ],
        "correct_answer": 0,
        "explanation_en": "The Requirements Assumption enforces strict equality constraints: Sum_j(x_ij) = s_i for all sources, and Sum_i(x_ij) = d_j for all destinations.",
        "explanation_vi": "Giả định này buộc các ràng buộc phải là dấu bằng: tổng lượng hàng rời khỏi nhà máy bằng đúng sản lượng, và tổng lượng hàng đến kho bằng đúng nhu cầu."
    })

    questions.append({
        "id": "QUES-030",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Network Graph",
        "difficulty": "Basic",
        "question_en": "In the graphical network representation of the P&T transportation problem, what do the nodes and directed arcs represent?",
        "question_vi": "Trong đồ thị mạng lưới biểu diễn bài toán vận tải P&T, các nút (nodes) và các cung có hướng (arcs) đại diện cho điều gì?",
        "options_en": [
            "Nodes represent canneries and warehouses; directed arcs represent shipping lanes with associated unit costs",
            "Nodes represent individual retail consumers; arcs represent telephone calls",
            "Nodes represent bank accounts; arcs represent tax audits",
            "Nodes represent diesel fuel stations; arcs represent railroad tracks"
        ],
        "options_vi": [
            "Các nút đại diện cho nhà máy đóng hộp và nhà kho; các cung có hướng đại diện cho các tuyến vận chuyển kèm cước phí đơn vị",
            "Các nút đại diện cho người tiêu dùng bán lẻ; các cung đại diện cho các cuộc gọi điện thoại",
            "Các nút đại diện cho tài khoản ngân hàng; các cung đại diện cho các cuộc kiểm toán thuế",
            "Các nút đại diện cho trạm xăng dầu; các cung đại diện cho đường ray xe lửa"
        ],
        "correct_answer": 0,
        "explanation_en": "The network graph displays supply nodes on the left, demand nodes on the right, and directed arcs connecting them with flow variables x_ij and unit costs c_ij.",
        "explanation_vi": "Đồ thị mạng lưới đặt các nút nguồn bên trái, nút đích bên phải và nối bằng các cung có hướng thể hiện lượng luân chuyển x_ij và cước phí c_ij."
    })

    questions.append({
        "id": "QUES-031",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Heuristic Cost",
        "difficulty": "Basic",
        "question_en": "What was the total shipping cost incurred by P&T Co. when using their historical, intuitive allocation approach?",
        "question_vi": "Tổng chi phí vận tải của công ty P&T khi sử dụng phương pháp phân bổ theo thói quen lịch sử là bao nhiêu?",
        "options_en": [
            "$179,850",
            "$152,535",
            "$300,000",
            "$95,200"
        ],
        "options_vi": [
            "$179,850",
            "$152,535",
            "$300,000",
            "$95,200"
        ],
        "correct_answer": 0,
        "explanation_en": "P&T's traditional intuitive rule-of-thumb shipping plan generated a total freight bill of $179,850.",
        "explanation_vi": "Kế hoạch vận chuyển theo thói quen truyền thống của P&T làm phát sinh tổng cước phí là $179,850."
    })

    questions.append({
        "id": "QUES-032",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Optimal Cost",
        "difficulty": "Basic",
        "question_en": "What was the optimal shipping cost achieved when P&T Co. solved the problem using Linear Programming?",
        "question_vi": "Tổng chi phí vận chuyển tối ưu đạt được khi công ty P&T giải bài toán bằng Quy hoạch Tuyến tính là bao nhiêu?",
        "options_en": [
            "$152,535",
            "$179,850",
            "$125,000",
            "$168,400"
        ],
        "options_vi": [
            "$152,535",
            "$179,850",
            "$125,000",
            "$168,400"
        ],
        "correct_answer": 0,
        "explanation_en": "The optimal LP solution yielded a minimum total shipping cost of $152,535.",
        "explanation_vi": "Nghiệm tối ưu từ bài toán quy hoạch tuyến tính đạt tổng chi phí tối thiểu là $152,535."
    })

    questions.append({
        "id": "QUES-033",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Net Savings",
        "difficulty": "Basic",
        "question_en": "How much money did P&T Co. save annually by adopting the LP transportation model over their intuitive method?",
        "question_vi": "Công ty P&T đã tiết kiệm được bao nhiêu tiền hàng năm khi áp dụng mô hình vận tải LP thay vì phương pháp cảm tính?",
        "options_en": [
            "$27,315 per year (a 15.2% reduction in freight costs)",
            "$5,000 per year",
            "$100,000 per year",
            "$0 (the costs were identical)"
        ],
        "options_vi": [
            "$27,315 mỗi năm (giảm 15.2% chi phí vận chuyển)",
            "$5,000 mỗi năm",
            "$100,000 mỗi năm",
            "$0 (hai phương pháp cho chi phí y hệt nhau)"
        ],
        "correct_answer": 0,
        "explanation_en": "Savings = $179,850 - $152,535 = $27,315 per year, proving the substantial business value of operations research.",
        "explanation_vi": "Khoản tiết kiệm ròng = $179,850 - $152,535 = $27,315/năm, minh chứng cho sức mạnh tối ưu hóa chi phí của mô hình toán trong ERP."
    })

    questions.append({
        "id": "QUES-034",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Excel Solver Setup for LP",
        "difficulty": "Basic",
        "question_en": "Which solving engine must be selected in Microsoft Excel Solver to optimize the P&T transportation problem?",
        "question_vi": "Công cụ giải (Solving Method) nào trong Microsoft Excel Solver phải được chọn để giải tối ưu bài toán vận tải P&T?",
        "options_en": [
            "Simplex LP",
            "GRG Nonlinear",
            "Evolutionary Algorithm",
            "Monte Carlo Simulation"
        ],
        "options_vi": [
            "Simplex LP (Đơn hình tuyến tính)",
            "GRG Nonlinear (Phi tuyến)",
            "Evolutionary Algorithm (Thuật toán di truyền)",
            "Mô phỏng Monte Carlo"
        ],
        "correct_answer": 0,
        "explanation_en": "Because both the objective function and all constraints are strictly linear, the Simplex LP engine must be selected for guaranteed global optimality.",
        "explanation_vi": "Do hàm mục tiêu và toàn bộ các ràng buộc đều là bậc nhất tuyến tính, ta phải chọn bộ giải Simplex LP để đảm bảo nghiệm tối ưu toàn cục."
    })

    questions.append({
        "id": "QUES-035",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Non-negativity Constraints",
        "difficulty": "Basic",
        "question_en": "Why must the non-negativity constraint (x_ij >= 0) be enforced in transportation linear programming?",
        "question_vi": "Vì sao ràng buộc không âm (x_ij >= 0) bắt buộc phải được áp dụng trong quy hoạch tuyến tính bài toán vận tải?",
        "options_en": [
            "To prevent the mathematical model from shipping negative truckloads of goods (which is physically impossible)",
            "To force truck drivers to drive only during daylight hours",
            "To ensure that all grocery stores sell canned peas at a profit",
            "To prevent the computer operating system from overheating"
        ],
        "options_vi": [
            "Để ngăn mô hình toán học đề xuất các chuyến xe tải chở số lượng âm (điều phi lý trong thực tế vận hành)",
            "Để buộc tài xế xe tải chỉ được lái xe vào ban ngày",
            "Để đảm bảo mọi cửa hàng tạp hóa bán đậu đóng hộp đều có lãi",
            "Để ngăn ngừa hệ điều hành máy tính không bị quá nóng"
        ],
        "correct_answer": 0,
        "explanation_en": "Negative flows (x_ij < 0) are physically meaningless; non-negativity ensures only valid positive quantities are dispatched.",
        "explanation_vi": "Lượng hàng vận chuyển không thể mang giá trị âm; điều kiện x_ij >= 0 đảm bảo giải pháp đưa ra hoàn toàn khả thi trong thực tế."
    })

    # Intermediate (Q036 - Q045)
    questions.append({
        "id": "QUES-036",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "LP Algebraic Formulation",
        "difficulty": "Intermediate",
        "question_en": "In the algebraic formulation of the P&T Co. problem, how many decision variables and constraints exist?",
        "question_vi": "Trong mô hình đại số của bài toán công ty P&T, có bao nhiêu biến quyết định và bao nhiêu phương trình ràng buộc?",
        "options_en": [
            "12 decision variables (3 canneries x 4 warehouses) and 7 functional constraints (3 supply + 4 demand)",
            "7 decision variables and 12 functional constraints",
            "300 decision variables and 300 functional constraints",
            "1 decision variable and 1 constraint"
        ],
        "options_vi": [
            "12 biến quyết định (3 nhà máy x 4 nhà kho) và 7 ràng buộc hàm chức năng (3 cung + 4 cầu)",
            "7 biến quyết định và 12 ràng buộc chức năng",
            "300 biến quyết định và 300 ràng buộc chức năng",
            "1 biến quyết định và 1 ràng buộc"
        ],
        "correct_answer": 0,
        "explanation_en": "3 origins x 4 destinations = 12 arcs (decision variables x_ij). There are 3 supply equality constraints and 4 demand equality constraints (total 7 constraints).",
        "explanation_vi": "Có 3 nguồn x 4 đích = 12 biến quyết định x_ij. Số ràng buộc chức năng gồm 3 ràng buộc công suất nhà máy và 4 ràng buộc nhu cầu kho (tổng cộng 7 ràng buộc)."
    })

    questions.append({
        "id": "QUES-037",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Bellingham Optimal Allocation",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for P&T Co., where are the 75 truckloads from the Bellingham cannery allocated?",
        "question_vi": "Trong phương án tối ưu của P&T Co., 75 chuyến xe tải từ nhà máy Bellingham được phân bổ đi đâu?",
        "options_en": [
            "All 75 truckloads are shipped to Albuquerque (x14 = 75), with 0 truckloads sent to Sacramento, Salt Lake City, or Rapid City",
            "All 75 truckloads are shipped to Sacramento (x11 = 75)",
            "Equally split: 25 truckloads each to Sacramento, Salt Lake City, and Rapid City",
            "50 truckloads to Rapid City and 25 truckloads to Salt Lake City"
        ],
        "options_vi": [
            "Toàn bộ 75 chuyến xe tải được chuyển đến Albuquerque (x14 = 75), không gửi chuyến nào đến Sacramento, Salt Lake City hay Rapid City",
            "Toàn bộ 75 chuyến xe tải được chuyển đến Sacramento (x11 = 75)",
            "Chia đều: 25 chuyến cho mỗi kho Sacramento, Salt Lake City và Rapid City",
            "50 chuyến chuyển đến Rapid City và 25 chuyến chuyển đến Salt Lake City"
        ],
        "correct_answer": 0,
        "explanation_en": "Counter-intuitively, the optimal LP solution dispatches all 75 truckloads from Bellingham to Albuquerque to liberate Eugene's and Albert Lea's lower-cost shipping options for northern warehouses.",
        "explanation_vi": "Khác với suy đoán trực giác, mô hình tối ưu điều phối toàn bộ 75 xe từ Bellingham đến Albuquerque để nhường các tuyến cước rẻ hơn từ Eugene và Albert Lea cho các kho phía bắc."
    })

    questions.append({
        "id": "QUES-038",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Counter-Intuitive Dispatching",
        "difficulty": "Intermediate",
        "question_en": "Why did P&T's intuitive management historically ship Bellingham peas to Sacramento ($464) rather than Albuquerque ($867)?",
        "question_vi": "Vì sao ban giám đốc P&T trước đây lại có thói quen gửi đậu từ Bellingham đến Sacramento ($464) thay vì Albuquerque ($867)?",
        "options_en": [
            "They fell into the greedy heuristic trap of looking only at local arc costs ($464 < $867) rather than global multi-echelon network interactions",
            "Sacramento offered higher cash bribes to cannery managers",
            "The road to Albuquerque was permanently blocked by snow",
            "Bellingham peas were disliked by customers in New Mexico"
        ],
        "options_vi": [
            "Họ rơi vào bẫy tư duy cục bộ 'tham lam' (greedy heuristic), chỉ nhìn vào chi phí từng cung riêng lẻ ($464 < $867) thay vì xem xét sự tương tác tổng thể toàn mạng lưới",
            "Kho Sacramento hối lộ tiền mặt nhiều hơn cho quản đốc nhà máy",
            "Đường đến Albuquerque bị tuyết chặn vĩnh viễn không thể đi",
            "Khách hàng tại New Mexico không thích ăn đậu đóng hộp từ Bellingham"
        ],
        "options_vi": [
            "Họ rơi vào bẫy tư duy cục bộ (greedy heuristic), chỉ nhìn chi phí đơn lẻ ($464 < $867) thay vì tương tác toàn mạng lưới",
            "Kho Sacramento trả giá mua đậu cao hơn các kho khác",
            "Tuyến đường đi Albuquerque không có trạm tiếp nhiên liệu",
            "Công ty ưu tiên bán hàng tại bang gần trước"
        ],
        "correct_answer": 0,
        "explanation_en": "Heuristic decision-makers focus on minimizing individual lane costs, missing that Eugene shipping to Sacramento ($352) saves far more money across the combined system.",
        "explanation_vi": "Tư duy trực giác mắc sai lầm tối ưu hóa cục bộ, không nhận ra rằng để Eugene chuyển về Sacramento ($352) sẽ giúp tổng chi phí toàn mạng lưới giảm sâu hơn nhiều."
    })

    questions.append({
        "id": "QUES-039",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Excel SUMPRODUCT in Transportation",
        "difficulty": "Intermediate",
        "question_en": "In setting up the objective function for P&T Co. in Excel, what formula is typically placed in the Total Cost target cell?",
        "question_vi": "Khi thiết lập hàm mục tiêu cho công ty P&T trong Excel, công thức nào thường được nhập vào ô Tổng Chi phí mục tiêu?",
        "options_en": [
            "=SUMPRODUCT(Unit_Cost_Matrix, Shipped_Quantity_Matrix)",
            "=AVERAGE(Unit_Cost_Matrix)",
            "=COUNTIF(Shipped_Quantity_Matrix, \">0\")",
            "=STDEV.S(Shipped_Quantity_Matrix)"
        ],
        "options_vi": [
            "=SUMPRODUCT(Ma_Tran_Cuoc_Phi, Ma_Tran_San_Luong_Chuyen)",
            "=AVERAGE(Ma_Tran_Cuoc_Phi)",
            "=COUNTIF(Ma_Tran_San_Luong_Chuyen, \">0\")",
            "=STDEV.S(Ma_Tran_San_Luong_Chuyen)"
        ],
        "correct_answer": 0,
        "explanation_en": "SUMPRODUCT multiplies each unit cost c_ij by its corresponding shipped decision variable x_ij and sums all products to calculate total freight cost Z.",
        "explanation_vi": "Hàm SUMPRODUCT nhân từng ô cước phí c_ij với biến quyết định số chuyến xe x_ij tương ứng và cộng tổng lại để tính hàm mục tiêu Z."
    })

    questions.append({
        "id": "QUES-040",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Eugene Dispatch Allocation",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for P&T Co., how is Eugene's total capacity of 125 truckloads distributed?",
        "question_vi": "Trong phương án tối ưu của P&T Co., tổng công suất 125 chuyến xe tải của nhà máy Eugene được phân bổ như thế nào?",
        "options_en": [
            "80 truckloads to Sacramento and 45 truckloads to Salt Lake City",
            "125 truckloads to Albuquerque",
            "70 truckloads to Rapid City and 55 truckloads to Sacramento",
            "125 truckloads to Salt Lake City"
        ],
        "options_vi": [
            "80 chuyến đến Sacramento và 45 chuyến đến Salt Lake City",
            "125 chuyến đến Albuquerque",
            "70 chuyến đến Rapid City và 55 chuyến đến Sacramento",
            "125 chuyến đến Salt Lake City"
        ],
        "correct_answer": 0,
        "explanation_en": "Eugene satisfies Sacramento's entire demand (80 truckloads at $352) and ships its remaining 45 truckloads to Salt Lake City at $416 (80 + 45 = 125).",
        "explanation_vi": "Eugene đáp ứng toàn bộ nhu cầu của kho Sacramento (80 chuyến với giá cước $352) và chuyển nốt 45 chuyến sang Salt Lake City với cước $416."
    })

    questions.append({
        "id": "QUES-041",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Albert Lea Dispatch Allocation",
        "difficulty": "Intermediate",
        "question_en": "In the optimal solution for P&T Co., how is Albert Lea's output of 100 truckloads distributed?",
        "question_vi": "Trong phương án tối ưu của P&T Co., sản lượng 100 chuyến xe tải của nhà máy Albert Lea được phân bổ như thế nào?",
        "options_en": [
            "20 truckloads to Salt Lake City, 70 to Rapid City, and 10 to Albuquerque",
            "100 truckloads to Sacramento",
            "50 truckloads to Rapid City and 50 to Salt Lake City",
            "100 truckloads to Rapid City"
        ],
        "options_vi": [
            "20 chuyến đến Salt Lake City, 70 chuyến đến Rapid City và 10 chuyến đến Albuquerque",
            "100 chuyến đến Sacramento",
            "50 chuyến đến Rapid City và 50 chuyến đến Salt Lake City",
            "100 chuyến đến Rapid City"
        ],
        "correct_answer": 0,
        "explanation_en": "Albert Lea sends 70 truckloads to Rapid City ($388), 20 to Salt Lake City ($682), and 10 to Albuquerque ($685), summing to 100 truckloads.",
        "explanation_vi": "Albert Lea chuyển 70 chuyến cho Rapid City ($388), 20 chuyến cho Salt Lake City ($682) và 10 chuyến cho Albuquerque ($685), vừa đủ 100 xe."
    })

    questions.append({
        "id": "QUES-042",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Degeneracy in Transportation LP",
        "difficulty": "Intermediate",
        "question_en": "What does 'Degeneracy' mean in the context of a transportation simplex basic solution?",
        "question_vi": "'Suy biến' (Degeneracy) trong nghiệm cơ sở của phương pháp đơn hình vận tải có nghĩa là gì?",
        "options_en": [
            "The number of basic (positive allocation) cells in the solution is strictly less than (m + n - 1)",
            "The total shipping cost is greater than $1,000,000",
            "The warehouse roof has collapsed and destroyed the goods",
            "All shipping lanes have identical unit costs"
        ],
        "options_vi": [
            "Số lượng ô cơ sở (ô được phân bổ lượng hàng dương) nhỏ hơn nghiêm ngặt giá trị (m + n - 1)",
            "Tổng chi phí vận chuyển vượt quá $1,000,000",
            "Mái nhà kho bị sập làm hư hỏng hàng hóa",
            "Mọi tuyến đường vận chuyển đều có đơn giá cước y hệt nhau"
        ],
        "correct_answer": 0,
        "explanation_en": "A standard transportation basis requires exactly m + n - 1 basic variables. If fewer positive variables exist, the tableau is degenerate, requiring an artificial zero allocation (epsilon) to evaluate stepping-stone loops.",
        "explanation_vi": "Một phương án cơ sở chuẩn có đúng m + n - 1 ô chọn. Nếu số ô chọn ít hơn mức này, bài toán rơi vào trạng thái suy biến và cần bổ sung ô 0 giả định để tìm hệ số thế vị."
    })

    questions.append({
        "id": "QUES-043",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "QM for Windows Transportation Module",
        "difficulty": "Intermediate",
        "question_en": "When using QM for Windows to solve the P&T transportation model, what starting method can be chosen to find an initial basic feasible solution?",
        "question_vi": "Khi sử dụng QM for Windows để giải bài toán vận tải P&T, phương pháp khởi tạo nào có thể được chọn để tìm phương án cơ sở khả thi ban đầu?",
        "options_en": [
            "Vogel's Approximation Method (VAM), Northwest Corner Rule, or Minimum Cost Method",
            "Newton-Raphson Gradient Descent",
            "Random Number Sampling",
            "Binary Tree Search"
        ],
        "options_vi": [
            "Phương pháp xấp xỉ Vogel (VAM), Quy tắc góc Tây Bắc (Northwest Corner), hoặc Phương pháp cước phí nhỏ nhất (Minimum Cost)",
            "Phương pháp giảm gradient Newton-Raphson",
            "Lấy mẫu số ngẫu nhiên Monte Carlo",
            "Tìm kiếm trên cây nhị phân"
        ],
        "correct_answer": 0,
        "explanation_en": "QM for Windows allows users to pick Northwest Corner, Minimum Cost, or Vogel's Approximation Method (VAM) as the starting heuristic before executing stepping-stone iterations.",
        "explanation_vi": "QM for Windows hỗ trợ các thuật toán tìm nghiệm xuất phát kinh điển: Góc Tây Bắc, Chi phí nhỏ nhất và Xấp xỉ Vogel (VAM) trước khi lặp đơn hình tối ưu."
    })

    questions.append({
        "id": "QUES-044",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Transportation Shadow Prices",
        "difficulty": "Intermediate",
        "question_en": "In transportation LP sensitivity analysis, what does the shadow price (dual value) of a warehouse demand constraint represent?",
        "question_vi": "Trong phân tích độ nhạy bài toán vận tải, giá bóng (giá trị đối ngẫu) của ràng buộc nhu cầu tại một nhà kho đại diện cho điều gì?",
        "options_en": [
            "The marginal increase in total system freight cost if that warehouse's demand increases by one additional truckload",
            "The physical rental price per square foot of warehouse floor space",
            "The salary paid to the warehouse night watchman",
            "The retail price premium charged to grocery store consumers"
        ],
        "options_vi": [
            "Mức tăng biên tế của tổng chi phí vận tải toàn hệ thống nếu nhu cầu tại nhà kho đó tăng thêm một chuyến xe tải",
            "Giá thuê tính trên mỗi mét vuông mặt sàn nhà kho",
            "Tiền lương trả cho nhân viên bảo vệ ca đêm tại kho",
            "Khoản phụ thu bán lẻ áp cho người tiêu dùng tại siêu thị"
        ],
        "correct_answer": 0,
        "explanation_en": "A constraint's shadow price indicates the rate of change in the objective function per unit increase in the constraint's right-hand-side value.",
        "explanation_vi": "Giá bóng của ràng buộc cho biết hàm mục tiêu tổng chi phí sẽ tăng (hoặc giảm) bao nhiêu khi vế phải ràng buộc tăng thêm 1 đơn vị."
    })

    questions.append({
        "id": "QUES-045",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Homework Link to Texago Case",
        "difficulty": "Intermediate",
        "question_en": "Why does the course syllabus assign the Texago Corp. Site Selection Problem as homework immediately following the P&T Co. lecture in Week 1?",
        "question_vi": "Vì sao đề cương môn học lại giao Case study chọn vị trí nhà máy Texago Corp. làm bài tập lớn ngay sau bài giảng P&T Co. ở Tuần 1?",
        "options_en": [
            "Because evaluating each candidate refinery location in Texago requires solving multi-echelon transportation LP models identical in mathematical structure to P&T Co.",
            "Because Texago produces canned vegetables identical to P&T Co.",
            "Because P&T and Texago are owned by the exact same family business",
            "To test whether students know how to purchase petroleum stocks"
        ],
        "options_vi": [
            "Vì việc đánh giá từng địa điểm nhà máy tiềm năng của Texago đòi hỏi giải các bài toán quy hoạch tuyến tính vận tải đa tầng có cấu trúc toán học tương tự như P&T Co.",
            "Vì Texago cũng sản xuất đậu đóng hộp giống như công ty P&T",
            "Vì P&T và Texago thuộc quyền sở hữu của cùng một gia đình",
            "Để kiểm tra xem sinh viên có biết cách đầu tư cổ phiếu ngành dầu khí hay không"
        ],
        "correct_answer": 0,
        "explanation_en": "The Texago case applies transportation LP in a two-stage decision: shipping crude oil to refineries and finished products to distribution centers for candidate plant locations.",
        "explanation_vi": "Case Texago nâng cấp bài toán vận tải lên mạng lưới hai tầng: vận chuyển dầu thô đến nhà máy và vận chuyển sản phẩm đến trung tâm phân phối để lựa chọn vị trí tối ưu."
    })

    # Advanced (Q046 - Q050)
    questions.append({
        "id": "QUES-046",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "BA Acceptance Criteria for LP",
        "difficulty": "Advanced",
        "question_en": "A Business Analyst is drafting Acceptance Criteria (AC) for an automated freight allocation module based on P&T's model. Which criteria ensures operational validity in User Acceptance Testing (UAT)?",
        "question_vi": "Một Business Analyst đang soạn thảo Tiêu chí Chấp nhận (Acceptance Criteria - AC) cho phân hệ điều phối vận tải tự động dựa trên mô hình P&T. Tiêu chí nào sau đây đảm bảo tính hợp lệ vận hành khi kiểm thử UAT?",
        "options_en": [
            "Given supply vector S and demand vector D, When optimization runs, Then sum of shipped loads from each cannery must equal its capacity, all warehouse demands must be 100% met, and total cost must be <= benchmark heuristic",
            "The system shall display a green button regardless of whether constraints are violated",
            "The algorithm must run in zero seconds and eliminate all freight drivers",
            "All shipments must be routed exclusively through Sacramento regardless of cost"
        ],
        "options_vi": [
            "Cho trước vectơ cung S và vectơ cầu D, Khi thuật toán tối ưu chạy, Thì tổng lượng xuất từ mỗi nhà máy phải bằng đúng công suất, toàn bộ nhu cầu kho phải được đáp ứng 100%, và tổng chi phí phải <= chi phí lịch sử",
            "Hệ thống phải hiển thị nút bấm màu xanh bất kể các ràng buộc có bị vi phạm hay không",
            "Thuật toán phải chạy trong 0 giây và sa thải toàn bộ đội ngũ tài xế",
            "Mọi lô hàng bắt buộc phải đi qua Sacramento bất kể chi phí cao hay thấp"
        ],
        "correct_answer": 0,
        "explanation_en": "Rigorous BA acceptance criteria specify given preconditions, execution events, and verifiable business rules (capacity adherence, demand fulfillment, cost optimality).",
        "explanation_vi": "Tiêu chí chấp nhận chuẩn Given-When-Then kiểm chứng chính xác việc tuân thủ ràng buộc công suất, thỏa mãn đủ nhu cầu và đạt hiệu quả tối ưu chi phí."
    })

    questions.append({
        "id": "QUES-047",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Integrity of Transport Simplex vs General LP",
        "difficulty": "Advanced",
        "question_en": "Why does solving a transportation problem with integer supplies and demands via the Simplex LP method guarantee integer optimal shipment values without branch-and-bound?",
        "question_vi": "Vì sao khi giải bài toán vận tải có lượng cung và cầu nguyên bằng phương pháp Simplex LP thì nghiệm tối ưu luôn tự động nhận giá trị nguyên mà không cần dùng thuật toán nhánh cận (Branch-and-Bound)?",
        "options_en": [
            "Due to the Total Unimodularity (TUM) property of the transportation constraint coefficient matrix",
            "Because Excel Solver automatically rounds all numbers to the nearest hundred",
            "Because truck drivers refuse to transport fractional cans of peas",
            "Because linear programming is incapable of calculating decimal fractions"
        ],
        "options_vi": [
            "Do tính chất Hoàn toàn Đơn mô-đun (Total Unimodularity - TUM) của ma trận hệ số ràng buộc trong bài toán vận tải",
            "Do Excel Solver tự động làm tròn tất cả các số về hàng trăm gần nhất",
            "Do các tài xế xe tải từ chối chở các hộp đậu bị cắt lẻ phân số",
            "Do quy hoạch tuyến tính không có khả năng tính toán số thập phân"
        ],
        "correct_answer": 0,
        "explanation_en": "The constraint matrix of a bipartite network flow problem is totally unimodular (all subdeterminants are 0, 1, or -1). By Cramer's rule, basic solutions are purely integer if RHS values are integer.",
        "explanation_vi": "Ma trận hệ số bài toán vận tải có tính chất đơn mô-đun hoàn toàn (TUM). Định thức con luôn là 0 hoặc ±1, do đó nghiệm cơ sở luôn là số nguyên nếu cung và cầu là số nguyên."
    })

    questions.append({
        "id": "QUES-048",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "Transport Cost Non-linearity in Practice",
        "difficulty": "Advanced",
        "question_en": "In real-world logistics, shipping rates often feature Full Truckload (FTL) discounts and Less-Than-Truckload (LTL) step-functions. How does this violate pure LP assumptions, and how should a BA address it?",
        "question_vi": "Trong thực tế logistics, cước vận chuyển thường có bậc giá nguyên chuyến (FTL) và lẻ chuyến (LTL). Điều này vi phạm giả định LP nào, và một Business Analyst nên xử lý ra sao?",
        "options_en": [
            "It violates Cost Proportionality; the BA should formulate piecewise linear cost curves or mixed-integer programming (MIP) with fixed-charge binary variables",
            "It violates the Requirements Assumption; the BA should shut down two factories",
            "It violates Non-Negativity; the BA should instruct warehouses to return goods",
            "It has no impact; standard linear simplex natively handles staircase curves without adjustment"
        ],
        "options_vi": [
            "Vi phạm Giả định Tỷ lệ thuận của chi phí; BA cần thiết lập mô hình đường cong chi phí từng đoạn hoặc Quy hoạch nguyên hỗn hợp (MIP) với biến nhị phân chi phí cố định",
            "Vi phạm Giả định Nhu cầu; BA nên đề xuất đóng cửa hai nhà máy",
            "Vi phạm Giả định Không âm; BA nên hướng dẫn kho hàng gửi trả lại hàng",
            "Không có ảnh hưởng gì; thuật toán đơn hình tuyến tính tự động giải quyết các đường cong bậc thang"
        ],
        "correct_answer": 0,
        "explanation_en": "Pure LP assumes c_ij * x_ij is strictly linear. Quantity step-breaks require mixed-integer linear programming (MILP) with binary indicators for truck activations.",
        "explanation_vi": "Quy hoạch tuyến tính thuần túy giả định chi phí tỷ lệ thuận đều. Cước bậc thang FTL/LTL đòi hỏi mô hình MIP sử dụng biến nhị phân kích hoạt chi phí chuyến xe."
    })

    questions.append({
        "id": "QUES-049",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "P&T Sensitivity Analysis",
        "difficulty": "Advanced",
        "question_en": "If Bellingham's cannery output increases from 75 to 85 truckloads while Albuquerque's demand increases simultaneously from 85 to 95 truckloads, how will the optimal shipment pattern change?",
        "question_vi": "Nếu sản lượng của Bellingham tăng từ 75 lên 85 chuyến xe và nhu cầu tại Albuquerque cũng tăng đồng thời từ 85 lên 95 chuyến xe, phương án vận chuyển tối ưu sẽ thay đổi thế nào?",
        "options_en": [
            "All 10 additional truckloads will flow directly from Bellingham to Albuquerque (x14 increases to 85), maintaining optimal basis topology with total cost increasing by 10 * $867 = $8,670",
            "The entire network collapses and all shipments must be rerouted through Eugene",
            "Total costs will decrease because Albuquerque is closer to Mexico",
            "Albert Lea will be forced to shut down operations permanently"
        ],
        "options_vi": [
            "Toàn bộ 10 chuyến xe tăng thêm sẽ được điều chuyển thẳng từ Bellingham đến Albuquerque (x14 tăng lên 85), giữ nguyên cấu trúc cơ sở với tổng chi phí tăng đúng 10 * $867 = $8,670",
            "Toàn bộ mạng lưới bị đổ vỡ và mọi lô hàng phải chuyển hướng đi qua Eugene",
            "Tổng chi phí sẽ giảm đi vì Albuquerque nằm gần biên giới",
            "Nhà máy Albert Lea sẽ bị buộc phải đóng cửa vĩnh viễn"
        ],
        "correct_answer": 0,
        "explanation_en": "Because Bellingham already ships exclusively to Albuquerque and Albuquerque still needs unmet supply, the dual ray accommodates the 10-unit balanced expansion directly at marginal cost c14 = $867.",
        "explanation_vi": "Vì Bellingham đang chuyển toàn bộ sản lượng cho Albuquerque và Albuquerque vẫn cần thêm hàng, 10 xe tăng thêm đi thẳng trên tuyến này với chi phí biên 10 * $867 = $8,670."
    })

    questions.append({
        "id": "QUES-050",
        "exam_id": "EXAM-02",
        "chapter_id": "chap-01",
        "topic": "ERP Master Data Configuration for Transportation",
        "difficulty": "Advanced",
        "question_en": "In an ERP Transportation Management (TM) implementation for P&T Co., what master data entities must be configured before running automated load-planning optimization?",
        "question_vi": "Khi triển khai module Quản trị Vận tải (TM) cho P&T Co., những thực thể dữ liệu chủ (Master Data) nào bắt buộc phải được thiết lập trước khi chạy thuật toán tối ưu hóa?",
        "options_en": [
            "Transportation Zones, Shipping Points, Plant Locations, Carrier Freight Rate Tables, Vehicle Capacities, and Customer Ship-To Addresses",
            "Employee birth certificates and factory cafeteria daily menus",
            "Corporate marketing slogans and social media follower counts",
            "Historical stock ticker prices from the 1920s"
        ],
        "options_vi": [
            "Vùng Vận chuyển (Transportation Zones), Điểm Xuất hàng, Vị trí Nhà máy, Biểu cước Hãng vận tải, Tải trọng Phương tiện và Địa chỉ Giao hàng của Khách hàng",
            "Giấy khai sinh của nhân viên và thực đơn bữa trưa nhà ăn của công nhân",
            "Khẩu hiệu tiếp thị của công ty và số lượng người theo dõi trên mạng xã hội",
            "Giá cổ phiếu niêm yết trong lịch sử từ những năm 1920"
        ],
        "correct_answer": 0,
        "explanation_en": "ERP TM engines require precise geospatial master data: origins (plants/shipping points), destinations (customer ship-to), distance matrices, vehicle types, and freight tariff rate tables.",
        "explanation_vi": "Hệ thống TM cần dữ liệu chủ địa lý và vận hành chuẩn xác: tọa độ nhà máy, địa chỉ kho nhận, ma trận khoảng cách cước phí, loại phương tiện và bảng giá cước nhà xe."
    })

    return questions
