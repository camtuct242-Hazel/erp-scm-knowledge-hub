import json

flashcards = [
    # Chapter 1 Flashcards
    {
        'id': 'CARD-001',
        'chapter_id': 'chap-01',
        'category': 'Definition',
        'front_en': 'What is Enterprise Resource Planning (ERP)?',
        'front_vi': 'Hệ thống ERP (Enterprise Resource Planning) là gì?',
        'back_en': 'An integrated suite of business applications running on a common database that manages and automates end-to-end business processes across procurement, manufacturing, inventory, sales, finance, and HR.',
        'back_vi': 'Bộ phần mềm quản trị doanh nghiệp hợp nhất chạy trên cơ sở dữ liệu chung, tự động hóa và kết nối liền mạch toàn bộ các quy trình nghiệp vụ từ mua hàng, sản xuất, kho vận, bán hàng, tài chính đến nhân sự.',
        'example': 'SAP S/4HANA connects sales orders directly to material requirements planning (MRP) and financial ledgers.'
    },
    {
        'id': 'CARD-002',
        'chapter_id': 'chap-01',
        'category': 'Model',
        'front_en': 'What are the two foundational assumptions of a standard Linear Programming Transportation Problem?',
        'front_vi': 'Hai giả định nền tảng của Bài toán Vận tải Tuyến tính chuẩn tắc là gì?',
        'back_en': '1. Requirements Assumption: Total supply from each origin must be distributed, and total demand at each destination must be received.\n2. Feasible Solutions Property: Total Supply must equal Total Demand (Sum(Supply) = Sum(Demand)).',
        'back_vi': '1. Giả định Nhu cầu & Cung cấp (Requirements Assumption): Toàn bộ lượng cung tại nguồn phải được vận chuyển hết, và toàn bộ nhu cầu tại đích phải được thỏa mãn đủ.\n2. Tính chất Nghiệm Khả thi: Tổng Cung bắt buộc phải bằng Tổng Cầu.',
        'example': 'P&T Co. has 3 canneries with supply 300 truckloads and 4 warehouses with demand 300 truckloads.'
    },
    {
        'id': 'CARD-003',
        'chapter_id': 'chap-01',
        'category': 'Formula',
        'front_en': 'What is the objective function formula of a standard Transportation Problem?',
        'front_vi': 'Công thức hàm mục tiêu của Bài toán Vận tải chuẩn tắc là gì?',
        'back_en': 'Minimize Z = Sum_i=1..m Sum_j=1..n (c_ij * x_ij), where c_ij is the unit shipping cost from source i to destination j, and x_ij is the quantity shipped.',
        'back_vi': 'Min Z = Tổng_i=1..m Tổng_j=1..n (c_ij * x_ij), trong đó c_ij là cước phí đơn vị từ nguồn i đến đích j, và x_ij là lượng hàng vận chuyển.',
        'example': 'P&T Co: Min Z = 464*x11 + 513*x12 + ... + 685*x34.'
    },
    {
        'id': 'CARD-004',
        'chapter_id': 'chap-01',
        'category': 'Distinction',
        'front_en': 'How does Excel Solver differ from QM for Windows in solving transportation problems?',
        'front_vi': 'Excel Solver khác biệt thế nào với QM for Windows khi giải bài toán vận tải?',
        'back_en': 'Excel Solver requires manual cell formula design, SUMPRODUCT cost links, and explicit constraint bounds using the Simplex LP engine. QM for Windows provides pre-structured matrix forms with automated stepping-stone iterations.',
        'back_vi': 'Excel Solver đòi hỏi người dùng tự thiết lập bảng tính, công thức hàm mục tiêu (SUMPRODUCT) và khai báo ràng buộc trong hộp thoại Solver. QM for Windows cung cấp biểu mẫu nhập ma trận định sẵn và tự động xuất các bảng đơn hình.',
        'example': 'In Excel Solver, set Solving Method to Simplex LP and check "Make Unconstrained Variables Non-Negative".'
    },
    {
        'id': 'CARD-005',
        'chapter_id': 'chap-01',
        'category': 'Business Rule',
        'front_en': 'In the P&T Co. case, what was the financial benefit of transitioning from intuitive allocation to LP optimization?',
        'front_vi': 'Trong case study P&T Co., lợi ích tài chính khi chuyển từ phân bổ cảm tính sang tối ưu hóa quy hoạch tuyến tính là gì?',
        'back_en': 'Total freight cost was reduced from $179,850 (intuitive heuristic) down to $152,535 (LP optimal), generating an immediate net saving of $27,315 (15.2% cost reduction).',
        'back_vi': 'Tổng chi phí vận tải giảm từ $179,850 (phân bổ theo thói quen) xuống còn $152,535 (nghiệm tối ưu LP), tiết kiệm ròng $27,315 (giảm 15.2% chi phí).',
        'example': 'The CEO reduced distribution expenses without altering warehouse sales or cannery outputs.'
    },

    # Chapter 2 Flashcards
    {
        'id': 'CARD-006',
        'chapter_id': 'chap-02',
        'category': 'Model',
        'front_en': 'How do you formulate a transportation problem when Total Supply > Total Demand?',
        'front_vi': 'Làm thế nào để mô hình hóa bài toán vận tải khi Tổng Cung > Tổng Cầu?',
        'back_en': 'Create an artificial "Dummy Destination" with demand equal to the surplus (Supply - Demand) and set all unit shipping costs from all sources to this dummy destination to $0.',
        'back_vi': 'Thêm một "Điểm đến Giả định" (Dummy Destination) có nhu cầu bằng đúng lượng cung dư thừa (Tổng Cung - Tổng Cầu) và gán cước phí vận chuyển từ tất cả các nguồn đến điểm giả định này bằng $0.',
        'example': 'Metro Water District: 3 rivers supply 16M acre-feet, 4 cities need 12.5M. Dummy demand = 3.5M with $0 cost.'
    },
    {
        'id': 'CARD-007',
        'chapter_id': 'chap-02',
        'category': 'Business Rule',
        'front_en': 'What does an allocation to a Dummy Destination represent in business practice?',
        'front_vi': 'Một lượng hàng phân bổ vào Điểm đến Giả định đại diện cho điều gì trong thực tế kinh doanh?',
        'back_en': 'It represents unutilized, idle production capacity or surplus inventory retained at that supply origin without incurring outbound shipping expenses.',
        'back_vi': 'Đại diện cho công suất nhàn rỗi không huy động hoặc lượng hàng tồn kho giữ lại tại điểm nguồn mà không phát sinh chi phí vận chuyển xuất kho.',
        'example': 'Water from Sacron River allocated to the dummy destination means water left in the reservoir.'
    },
    {
        'id': 'CARD-008',
        'chapter_id': 'chap-02',
        'category': 'Model',
        'front_en': 'How do you handle a prohibited shipping route or infeasible combination in a transportation tableau?',
        'front_vi': 'Làm thế nào để xử lý tuyến vận chuyển bị cấm hoặc kết hợp không khả thi trong bảng vận tải?',
        'back_en': 'Assign a prohibitively large unit cost M (Big-M, e.g., $999,999) to that route, or enforce an explicit constraint in Solver setting x_ij = 0.',
        'back_vi': 'Gán một hệ số chi phí phạt cực lớn M (Big-M, ví dụ $999,999) cho tuyến đường đó, hoặc đặt ràng buộc trực tiếp trong Solver x_ij = 0.',
        'example': 'In Better Products Co. (Case 2.1), Plant 2 cannot manufacture Product 3, so c23 = M.'
    },
    {
        'id': 'CARD-009',
        'chapter_id': 'chap-02',
        'category': 'Distinction',
        'front_en': 'In the Energetic Co. case, why can electricity needs only be satisfied by the electricity utility source?',
        'front_vi': 'Trong case Energetic Co., vì sao nhu cầu điện chỉ có thể được đáp ứng bởi nguồn điện lưới?',
        'back_en': 'Solar heaters and natural gas burners produce thermal energy for water/space heating but cannot generate electricity under building equipment constraints, so their costs to electricity are set to M.',
        'back_vi': 'Hệ thống năng lượng mặt trời và bình gas chỉ tạo ra nhiệt năng sưởi ấm và đun nước chứ không thể phát điện trong cấu hình tòa nhà, nên chi phí cấp cho điện bị gán bằng M.',
        'example': 'c(Gas, Electricity) = M; c(Solar, Electricity) = M.'
    },
    {
        'id': 'CARD-010',
        'chapter_id': 'chap-02',
        'category': 'Formula',
        'front_en': 'How do you formulate a transportation problem when Total Demand > Total Supply?',
        'front_vi': 'Làm thế nào để thiết lập bài toán vận tải khi Tổng Cầu > Tổng Cung?',
        'back_en': 'Introduce an artificial "Dummy Source" with capacity equal to the deficit (Demand - Supply). If minimizing shortage penalties, assign unit costs equal to lost contribution margin or unmet penalty.',
        'back_vi': 'Đưa thêm một "Nguồn Giả định" (Dummy Source) có lượng cung bằng lượng thiếu hụt (Tổng Cầu - Tổng Cung). Gán chi phí bằng 0 nếu chỉ cân bằng, hoặc bằng lợi nhuận biên bị mất nếu muốn giảm thiểu thiệt hại.',
        'example': 'Better Products (Case 2.1) had capacity 195 units vs sales demand 120 units.'
    },

    # Chapter 3 Flashcards
    {
        'id': 'CARD-011',
        'chapter_id': 'chap-03',
        'category': 'Model',
        'front_en': 'How are unstable demand ranges [Min, Max] modeled in the Middletown School District problem?',
        'front_vi': 'Khoảng nhu cầu dao động [Min, Max] được mô hình hóa như thế nào trong bài toán Middletown School District?',
        'back_en': 'Each destination j is constrained by two linear inequalities: Sum_i (x_ij) >= Min_j (Lower Bound) and Sum_i (x_ij) <= Max_j (Upper Bound).',
        'back_vi': 'Mỗi điểm đích j được khống chế bởi 2 bất đẳng thức tuyến tính: Tổng_i (x_ij) >= Min_j (Cận dưới) và Tổng_i (x_ij) <= Max_j (Cận trên).',
        'example': 'School 1: 1,200 <= x11 + x21 + ... + x91 <= 1,800 students.'
    },
    {
        'id': 'CARD-012',
        'chapter_id': 'chap-03',
        'category': 'Model',
        'front_en': 'How is a Profit Maximization transportation problem converted for minimization solvers?',
        'front_vi': 'Làm thế nào để chuyển đổi bài toán vận tải Tối đa hóa Lợi nhuận sang dạng cực tiểu hóa chi phí?',
        'back_en': 'Subtract each unit profit P_ij from the maximum profit value in the table: c_ij = P_max - P_ij. Solving for Min Sum(c_ij * x_ij) yields the exact profit-maximizing solution.',
        'back_vi': 'Lấy lợi nhuận lớn nhất trong bảng trừ đi từng hệ số lợi nhuận: c_ij = P_max - P_ij. Khi đó cực tiểu hóa chi phí cơ hội sẽ tương đương với cực đại hóa tổng lợi nhuận.',
        'example': 'In Nifty Co., max profit is $59. Cost c32 = 59 - 59 = 0; c22 = 59 - 18 = 41.'
    },
    {
        'id': 'CARD-013',
        'chapter_id': 'chap-03',
        'category': 'Definition',
        'front_en': 'What is an Assignment Problem?',
        'front_vi': 'Bài toán Phân công (Assignment Problem) là gì?',
        'back_en': 'A special 0-1 integer linear programming problem where n assignees are matched to n tasks on a strict one-to-one basis, ensuring each task has exactly one assignee and each assignee has one task.',
        'back_vi': 'Bài toán quy hoạch tuyến tính nguyên nhị phân 0-1 đặc biệt, trong đó n đối tượng được ghép đôi với n nhiệm vụ theo nguyên tắc 1-kèm-1 (mỗi việc 1 người, mỗi người 1 việc) với chi phí thấp nhất.',
        'example': 'Better Products Case 2.2: Assigning each plant to distinct products with zero product splitting.'
    },
    {
        'id': 'CARD-014',
        'chapter_id': 'chap-03',
        'category': 'Model',
        'front_en': 'What is the computational complexity of the Hungarian Method?',
        'front_vi': 'Độ phức tạp tính toán của Phương pháp Hungarian (Kuhn-Munkres) là bao nhiêu?',
        'back_en': 'O(n^3) polynomial time, executing iterative row and column reductions and minimal line covering of zeros.',
        'back_vi': 'Thời gian đa thức bậc ba O(n^3), thực hiện qua các bước giảm trừ hàng, giảm trừ cột và phủ các số 0 bằng số đường thẳng tối thiểu.',
        'example': 'Solves large nxn assignment matrix problems far faster than general branch-and-bound integer programming.'
    },
    {
        'id': 'CARD-015',
        'chapter_id': 'chap-03',
        'category': 'Distinction',
        'front_en': 'Why did Better Products Co. management transition from Case 2.1 to Case 2.2 (prohibiting product splitting)?',
        'front_vi': 'Vì sao ban lãnh đạo Better Products Co. chuyển từ Case 2.1 sang Case 2.2 (cấm chia nhỏ sản phẩm)?',
        'back_en': 'Product splitting introduced heavy hidden costs: duplicated tooling changeovers, fragmented shipments, administrative overhead, and complex quality tracking.',
        'back_vi': 'Việc chia nhỏ sản phẩm cho nhiều nhà máy sản xuất gây ra chi phí ẩn nặng nề: nhân đôi chi phí thiết lập máy (tooling), xé lẻ vận chuyển, phát sinh thủ tục quản lý và khó kiểm soát chất lượng đồng nhất.',
        'example': 'Manufacturing Product 1 in both Plant 1 and Plant 3 incurred dual machine setups.'
    },

    # Chapter 4 Flashcards
    {
        'id': 'CARD-016',
        'chapter_id': 'chap-04',
        'category': 'Definition',
        'front_en': 'What are the four primary cost components of inventory models?',
        'front_vi': 'Bốn thành phần chi phí cốt lõi của mô hình quản trị tồn kho là gì?',
        'back_en': '1. Acquisition Cost (c)\n2. Setup / Ordering Cost (K)\n3. Holding / Carrying Cost (h)\n4. Shortage / Stockout Cost (p)',
        'back_vi': '1. Chi phí Mua hàng / Giá vốn (c)\n2. Chi phí Thiết lập / Đặt hàng (K)\n3. Chi phí Tồn trữ / Lưu kho (h)\n4. Chi phí Thiếu hàng / Phạt hết hàng (p)',
        'example': 'ACT Case: c = $20, K = $115, h = $4.20/tire/yr, p = $7.50/tire/yr.'
    },
    {
        'id': 'CARD-017',
        'chapter_id': 'chap-04',
        'category': 'Formula',
        'front_en': 'What is the Basic EOQ formula for optimal order quantity Q*?',
        'front_vi': 'Công thức EOQ cơ bản xác định lượng đặt hàng tối ưu Q* là gì?',
        'back_en': 'Q* = sqrt((2 * K * D) / h), where D = annual demand rate, K = setup/order cost, and h = annual holding cost per unit.',
        'back_vi': 'Q* = sqrt((2 * K * D) / h), với D là nhu cầu hàng năm, K là chi phí mỗi lần đặt hàng, và h là chi phí lưu kho 1 đơn vị trong 1 năm.',
        'example': 'ACT: Q* = sqrt((2 * 115 * 6000) / 4.20) = sqrt(328,571.43) = 573.2 tires.'
    },
    {
        'id': 'CARD-018',
        'chapter_id': 'chap-04',
        'category': 'Business Rule',
        'front_en': 'At the optimal EOQ lot size Q*, what is the relationship between Annual Holding Cost and Annual Setup Cost?',
        'front_vi': 'Tại điểm đặt hàng tối ưu EOQ Q*, mối quan hệ giữa Chi phí Lưu kho hàng năm và Chi phí Đặt hàng hàng năm là gì?',
        'back_en': 'They are exactly equal! Annual Holding Cost (h * Q/2) = Annual Setup Cost (K * D/Q). This represents the mathematical minimum of Total Variable Cost (TVC).',
        'back_vi': 'Chúng hoàn toàn bằng nhau! Chi phí Lưu kho hàng năm (h * Q/2) = Chi phí Đặt hàng hàng năm (K * D/Q). Đây là giao điểm cực tiểu hóa Tổng Chi phí Biến đổi (TVC).',
        'example': 'At ACT with Q=573: Setup Cost = $1,203.74, Holding Cost = $1,203.74.'
    },
    {
        'id': 'CARD-019',
        'chapter_id': 'chap-04',
        'category': 'Formula',
        'front_en': 'What is the Reorder Point (ROP) formula under constant demand and deterministic lead time?',
        'front_vi': 'Công thức Điểm Đặt Hàng Lại (ROP) trong điều kiện nhu cầu ổn định và thời gian giao hàng xác định là gì?',
        'back_en': 'ROP = d * L, where d is the daily demand rate (D / working days) and L is the replenishment lead time in working days.',
        'back_vi': 'ROP = d * L, trong đó d là nhu cầu sử dụng mỗi ngày và L là thời gian giao hàng (Lead Time) tính theo ngày làm việc.',
        'example': 'ACT: d = 20 tires/day, L = 9 days -> ROP = 20 * 9 = 180 tires.'
    },
    {
        'id': 'CARD-020',
        'chapter_id': 'chap-04',
        'category': 'Distinction',
        'front_en': 'Why must Excel Solver use the GRG Non-Linear engine rather than Simplex LP for the EOQ model?',
        'front_vi': 'Vì sao Excel Solver phải sử dụng bộ giải GRG Non-Linear thay vì Simplex LP cho bài toán EOQ?',
        'back_en': 'Because the EOQ cost function contains K * (D / Q), which has the decision variable Q in the denominator (Q^-1), making the objective function curved and nonlinear.',
        'back_vi': 'Vì hàm chi phí EOQ chứa thành phần K * (D / Q), có biến quyết định Q nằm ở mẫu số (bậc -1), làm hàm mục tiêu có dạng đường cong phi tuyến.',
        'example': 'Selecting Simplex LP causes Solver to throw an error: "The linearity conditions required by this LP Solver are not satisfied".'
    },

    # Chapter 5 Flashcards
    {
        'id': 'CARD-021',
        'chapter_id': 'chap-05',
        'category': 'Model',
        'front_en': 'What are the two key decision variables in the EOQ model with Planned Shortages?',
        'front_vi': 'Hai biến quyết định chính trong mô hình EOQ có Thiếu hụt Kế hoạch (Planned Shortages) là gì?',
        'back_en': '1. Q: The total batch replenishment order quantity.\n2. S: The maximum shortage level (maximum backorder quantity accumulated at the end of cycle).',
        'back_vi': '1. Q: Quy mô lô đặt hàng bổ sung tổng thể.\n2. S: Mức thiếu hụt tối đa (lượng đơn hàng nợ tích lũy lớn nhất tại thời điểm cuối chu kỳ).',
        'example': 'ACT: Q* = 716 tires, S* = 257 tires. Maximum inventory held = Q* - S* = 459 tires.'
    },
    {
        'id': 'CARD-022',
        'chapter_id': 'chap-05',
        'category': 'Formula',
        'front_en': 'What is the optimal order quantity formula Q* with Planned Shortages?',
        'front_vi': 'Công thức xác định lượng đặt hàng tối ưu Q* khi có Thiếu hụt Kế hoạch là gì?',
        'back_en': 'Q* = sqrt((2*K*D)/h) * sqrt((p + h) / p). The multiplier sqrt((p+h)/p) is always > 1, so Q* is larger than basic EOQ.',
        'back_vi': 'Q* = sqrt((2*K*D)/h) * sqrt((p + h) / p). Thừa số sqrt((p+h)/p) luôn lớn hơn 1, nên lượng đặt hàng Q* luôn lớn hơn so với EOQ cơ bản.',
        'example': 'ACT: Basic EOQ = 573.2. Multiplier = sqrt((7.5+4.2)/7.5) = 1.249 -> Q* = 716 tires.'
    },
    {
        'id': 'CARD-023',
        'chapter_id': 'chap-05',
        'category': 'Business Rule',
        'front_en': 'Why does an enterprise choose to allow Planned Shortages (Backorders)?',
        'front_vi': 'Vì sao doanh nghiệp lại chủ động lựa chọn chính sách Thiếu hụt Kế hoạch?',
        'back_en': 'Because maximum physical inventory drops from Q to (Q - S), substantially reducing annual holding costs. When holding cost savings exceed backorder penalties, TVC drops.',
        'back_vi': 'Vì mức tồn kho vật lý cực đại giảm từ Q xuống còn (Q - S), giúp cắt giảm mạnh chi phí lưu kho vốn. Khi phần tiết kiệm lưu kho lớn hơn chi phí phạt thiếu hàng, tổng chi phí TVC sẽ giảm sâu.',
        'example': 'ACT reduced annual variable inventory cost from $2,407 down to $1,927 (saving nearly 20% more).'
    },
    {
        'id': 'CARD-024',
        'chapter_id': 'chap-05',
        'category': 'Model',
        'front_en': 'In the Quantity Discount model, why is Annual Purchase Cost included in Total Cost TC(Q)?',
        'front_vi': 'Trong mô hình Chiết khấu theo số lượng, vì sao Chi phí Mua hàng hàng năm lại phải đưa vào Tổng chi phí TC(Q)?',
        'back_en': 'Because unit price c(Q) varies across quantity discount tiers, so c*D is no longer a fixed constant. Total expenditure must compare purchase discounts against increased holding costs.',
        'back_vi': 'Vì đơn giá mua c(Q) thay đổi theo từng mức số lượng, khiến c*D không còn là hằng số cố định. Doanh nghiệp phải cân đối giữa số tiền tiết kiệm nhờ giá mua rẻ với chi phí lưu kho tăng cao.',
        'example': 'TC(Q) = c(Q)*D + K*(D/Q) + h(Q)*(Q/2).'
    },
    {
        'id': 'CARD-025',
        'chapter_id': 'chap-05',
        'category': 'Business Rule',
        'front_en': 'In the ACT Quantity Discount case, why was ordering Q = 750 tires the optimal decision?',
        'front_vi': 'Trong case Chiết khấu số lượng của ACT, vì sao đặt đúng Q = 750 lốp lại là quyết định tối ưu?',
        'back_en': 'Tier 2 unconstrained EOQ was 576 (infeasible). Evaluating at the 750 breakpoint gave TC = $121,279.25, which was lower than Tier 1 ($122,407) and Tier 2 breakpoint at 2000 ($122,061).',
        'back_vi': 'EOQ lý thuyết ở Mức 2 là 576 (nằm ngoài dải 750-1,999). Đánh giá tại điểm ngưỡng breakpoint Q = 750 cho tổng chi phí $121,279.25, thấp hơn Mức 1 ($122,407) và ngưỡng 2,000 lốp ($122,061).',
        'example': 'ACT captured the 1% discount while minimizing additional warehouse holding buildup.'
    },
    {
        'id': 'CARD-026',
        'chapter_id': 'chap-05',
        'category': 'Formula',
        'front_en': 'What is the Economic Production Quantity (EPQ) formula for gradual replenishment?',
        'front_vi': 'Công thức Lượng Sản Xuất Kinh Tế (EPQ) cho bài toán bổ sung dần là gì?',
        'back_en': 'Q* = sqrt((2 * K * D) / (h * (1 - d / p))), where p is daily production rate and d is daily consumption rate.',
        'back_vi': 'Q* = sqrt((2 * K * D) / (h * (1 - d / p))), trong đó p là tốc độ sản xuất hàng ngày và d là tốc độ tiêu thụ hàng ngày của dây chuyền.',
        'example': 'SOCA: d = 1,000, p = 3,000 -> 1 - d/p = 2/3. Q* = sqrt((2 * 12000 * 250000) / (3.60 * 2/3)) = 50,000 speakers.'
    },
    {
        'id': 'CARD-027',
        'chapter_id': 'chap-05',
        'category': 'Distinction',
        'front_en': 'Why is maximum inventory in EPQ less than the production batch size Q?',
        'front_vi': 'Vì sao mức tồn kho cực đại trong mô hình EPQ luôn nhỏ hơn quy mô lô sản xuất Q?',
        'back_en': 'Because during the production run, units are simultaneously withdrawn for downstream consumption at rate d. Max inventory is only Q * (1 - d/p).',
        'back_vi': 'Vì trong suốt thời gian máy đang chạy sản xuất, một phần sản phẩm đã được rút ra đồng thời để phục vụ lắp ráp với tốc độ d. Mức tồn kho cực đại chỉ đạt Q * (1 - d/p).',
        'example': 'SOCA: Q = 30,000 produced over 10 days, but 10,000 consumed during those 10 days -> Max inventory = 20,000.'
    },
    {
        'id': 'CARD-028',
        'chapter_id': 'chap-05',
        'category': 'Business Rule',
        'front_en': 'What annual savings did SOCA achieve by moving from Q = 30,000 to optimal EPQ Q* = 50,000?',
        'front_vi': 'SOCA tiết kiệm được bao nhiêu chi phí mỗi năm khi chuyển từ lô Q = 30,000 sang lô tối ưu Q* = 50,000?',
        'back_en': 'Total variable inventory cost dropped from $136,000/year to $120,000/year, achieving an annual net savings of $16,000 (11.8% cost reduction).',
        'back_vi': 'Tổng chi phí biến đổi tồn kho giảm từ $136,000/năm xuống còn $120,000/năm, mang lại khoản tiết kiệm ròng $16,000/năm (giảm 11.8%).',
        'example': 'Setup costs dropped from $100k to $60k, while holding costs rose from $36k to $60k, balancing at optimal parity.'
    },

    # Chapter 6 Flashcards
    {
        'id': 'CARD-029',
        'chapter_id': 'chap-06',
        'category': 'Model',
        'front_en': 'How do ERP Transportation Management (TM) and Extended Warehouse Management (EWM) integrate?',
        'front_vi': 'Module Vận tải (TM) và Quản trị Kho mở rộng (EWM) trong ERP tích hợp với nhau như thế nào?',
        'back_en': 'EWM manages staging bays, dock doors, pick/pack/ship and putaway operations, while TM optimizes multi-modal freight consolidation, carrier selection, route planning, and shipment freight billing.',
        'back_vi': 'EWM quản lý khu vực tập kết hàng (staging), cửa xuất nhập hàng (dock door), quy trình lấy hàng/đóng gói/dán nhãn, trong khi TM tối ưu hóa gom chuyến xe, chọn hãng vận tải, lập tuyến đường và quyết toán cước phí.',
        'example': 'SAP TM passes Freight Orders to SAP EWM for wave picking and truck loading execution.'
    },
    {
        'id': 'CARD-030',
        'chapter_id': 'chap-06',
        'category': 'Distinction',
        'front_en': 'From a Business Analyst perspective, what is the key difference between functional requirements and business rules in ERP inventory optimization?',
        'front_vi': 'Dưới góc nhìn Business Analyst, sự khác biệt then chốt giữa yêu cầu chức năng (FR) và quy tắc nghiệp vụ (BR) trong tối ưu hóa tồn kho ERP là gì?',
        'back_en': 'A functional requirement defines what the system must do (e.g., "The system shall calculate ROP and trigger automated purchase requisition"), whereas a business rule defines organizational logic or constraints (e.g., "Planned shortages are prohibited on Class A medical items").',
        'back_vi': 'Yêu cầu chức năng (FR) mô tả hệ thống phải làm gì (ví dụ: "Hệ thống phải tự động tính ROP và sinh Purchase Requisition"), trong khi Quy tắc nghiệp vụ (BR) xác định chính sách hoặc ràng buộc tổ chức (ví dụ: "Nghiêm cấm để xảy ra nợ hàng đối với mặt hàng y tế nhóm A").',
        'example': 'FR: Display EOQ recommendation. BR: Supplier order must be a multiple of pallet size (50 units).'
    }
]

with open('outputs/data/flashcards.json', 'w', encoding='utf-8') as f:
    json.dump(flashcards, f, ensure_ascii=False, indent=2)

print(f'Successfully exported {len(flashcards)} flashcards to outputs/data/flashcards.json')
