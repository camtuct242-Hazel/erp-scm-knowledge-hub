# -*- coding: utf-8 -*-
# EXAM 10: Enterprise ERP Integration, Decision Modeling & BA Practice (chap-06)
# 25 Questions: Q226 to Q250 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    questions = []

    # Basic (Q226 - Q235)
    questions.append({
        "id": "QUES-226",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "BA Role in ERP Projects",
        "difficulty": "Basic",
        "question_en": "What is the primary role of a Business Analyst (BA) during an enterprise ERP implementation project?",
        "question_vi": "Vai trò cốt lõi của một Business Analyst (BA) trong dự án triển khai hệ thống ERP doanh nghiệp là gì?",
        "options_en": [
            "To bridge the gap between business stakeholders and technical developers by analyzing business processes, eliciting requirements, and validating system solutions",
            "To write low-level machine assembly code for database servers",
            "To manage the physical loading of trucks at warehouse docks",
            "To invest corporate funds in foreign real estate markets"
        ],
        "options_vi": [
            "Làm cầu nối giữa các bên liên quan nghiệp vụ và đội ngũ phát triển kỹ thuật bằng cách phân tích quy trình, khơi gợi yêu cầu và nghiệm thu giải pháp hệ thống",
            "Viết mã nguồn hợp ngữ máy cấp thấp cho các máy chủ cơ sở dữ liệu",
            "Trực tiếp bốc vác hàng hóa lên các xe tải tại cửa kho",
            "Đầu tư vốn của công ty vào các thị trường bất động sản nước ngoài"
        ],
        "correct_answer": 0,
        "explanation_en": "The BA acts as the critical translator between business operations and IT implementation, ensuring functional software solves real enterprise operational problems.",
        "explanation_vi": "BA đóng vai trò thông dịch viên nghiệp vụ - kỹ thuật: thấu hiểu nỗi đau quy trình, chuyển hóa thành yêu cầu phần mềm và đảm bảo hệ thống giải quyết đúng bài toán kinh doanh."
    })

    questions.append({
        "id": "QUES-227",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "As-Is vs To-Be Process Modeling",
        "difficulty": "Basic",
        "question_en": "In business process re-engineering, what is the difference between an 'As-Is' process map and a 'To-Be' process map?",
        "question_vi": "Trong tái cấu trúc quy trình nghiệp vụ, sự khác biệt giữa sơ đồ quy trình 'As-Is' (Hiện trạng) và 'To-Be' (Tương lai) là gì?",
        "options_en": [
            "The As-Is map depicts current baseline operational workflows (with all inefficiencies), while the To-Be map models the optimized future state enabled by the new ERP system",
            "As-Is is written in English, while To-Be is written in Latin",
            "As-Is is used only for finance, while To-Be is used only for marketing",
            "There is no difference; both terms refer to the same document"
        ],
        "options_vi": [
            "Sơ đồ As-Is mô tả quy trình vận hành hiện tại (kèm theo các điểm nghẽn và lãng phí), trong khi sơ đồ To-Be mô hình hóa quy trình tương lai tối ưu sau khi đưa ERP vào vận hành",
            "As-Is được viết bằng tiếng Anh, còn To-Be được viết bằng tiếng Latin",
            "As-Is chỉ dùng cho kế toán, còn To-Be chỉ dùng cho tiếp thị",
            "Không có sự khác biệt; cả hai thuật ngữ đều chỉ cùng một văn bản"
        ],
        "correct_answer": 0,
        "explanation_en": "As-Is documents current reality to uncover pain points; To-Be designs streamlined, standardized target workflows aligned with ERP capabilities.",
        "explanation_vi": "As-Is ghi nhận hiện trạng để bóc tách nút thắt; To-Be thiết kế quy trình chuẩn hóa đích đến sau khi tích hợp phần mềm ERP."
    })

    questions.append({
        "id": "QUES-228",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "BPMN Standard Notation",
        "difficulty": "Basic",
        "question_en": "Which international modeling notation is most widely utilized by Business Analysts to document enterprise workflows?",
        "question_vi": "Ký hiệu mô hình hóa quốc tế nào được các Business Analyst sử dụng rộng rãi nhất để tài liệu hóa các luồng quy trình nghiệp vụ doanh nghiệp?",
        "options_en": [
            "BPMN 2.0 (Business Process Model and Notation)",
            "HTML5 Web Layout Tags",
            "Musical Sheet Notation",
            "Morse Code Telegraph Dots"
        ],
        "options_vi": [
            "BPMN 2.0 (Business Process Model and Notation)",
            "Các thẻ bố cục trang web HTML5",
            "Ký xướng âm khuông nhạc",
            "Mã điện tín Morse"
        ],
        "correct_answer": 0,
        "explanation_en": "BPMN 2.0 provides standardized visual semantics (events, activities, gateways, swimlanes, data objects) understood by both business users and software architects.",
        "explanation_vi": "BPMN 2.0 là chuẩn quốc tế biểu diễn quy trình với các sự kiện (Events), hoạt động (Tasks), cổng rẽ nhánh (Gateways) và làn trách nhiệm (Swimlanes)."
    })

    questions.append({
        "id": "QUES-229",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Stakeholder RACI Matrix",
        "difficulty": "Basic",
        "question_en": "What do the four letters in a RACI Stakeholder Responsibility Matrix stand for?",
        "question_vi": "Bốn chữ cái trong Ma trận Trách nhiệm RACI đại diện cho những vai trò nào?",
        "options_en": [
            "Responsible, Accountable, Consulted, and Informed",
            "Rapid, Accurate, Concise, and Intelligent",
            "Routing, Allocation, Calculation, and Inspection",
            "Receiving, Assembly, Costing, and Inventory"
        ],
        "options_vi": [
            "Responsible (Người thực thi), Accountable (Người chịu trách nhiệm giải trình cuối cùng), Consulted (Người được tham vấn), và Informed (Người được thông báo)",
            "Rapid (Nhanh chóng), Accurate (Chính xác), Concise (Súc tích), và Intelligent (Thông minh)",
            "Routing (Lập tuyến), Allocation (Phân bổ), Calculation (Tính toán), và Inspection (Kiểm định)",
            "Receiving (Nhận hàng), Assembly (Lắp ráp), Costing (Tính giá thành), và Inventory (Tồn kho)"
        ],
        "correct_answer": 0,
        "explanation_en": "RACI clarifies governance: Responsible (does the work), Accountable (approves/owns outcome), Consulted (provides two-way input), Informed (one-way update).",
        "explanation_vi": "Ma trận RACI phân định rõ quyền hạn: R (trực tiếp làm), A (chịu trách nhiệm tối hậu), C (tham vấn chuyên môn), I (nhận thông báo tiến độ)."
    })

    questions.append({
        "id": "QUES-230",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Functional vs Non-Functional Requirements",
        "difficulty": "Basic",
        "question_en": "Which of the following is an example of a Non-Functional Requirement (NFR) in an ERP Transportation Management module?",
        "question_vi": "Yêu cầu nào sau đây là ví dụ điển hình về Yêu cầu Phi Chức Năng (Non-Functional Requirement - NFR) trong phân hệ Quản trị Vận tải ERP?",
        "options_en": [
            "The network optimization engine shall compute the optimal freight allocation for a 50-node network within 5 seconds under peak system load",
            "The system shall display the truck driver's name on the shipping dispatch order",
            "The system shall multiply shipped units by unit shipping cost to calculate total cost",
            "The system shall send an email notification to warehouse clerks upon goods arrival"
        ],
        "options_vi": [
            "Bộ giải tối ưu hóa mạng lưới phải tính toán xong phương án phân bổ cước cho đồ thị 50 nút trong vòng dưới 5 giây dưới tải cao điểm",
            "Hệ thống phải hiển thị tên của tài xế xe tải trên phiếu điều phối giao hàng",
            "Hệ thống phải nhân số lượng hàng vận chuyển với đơn giá cước để tính tổng chi phí",
            "Hệ thống phải gửi email thông báo cho thủ kho ngay khi hàng về đến nơi"
        ],
        "correct_answer": 0,
        "explanation_en": "NFRs define quality attributes such as performance, response latency, scalability, security, and uptime availability rather than discrete transactional behaviors.",
        "explanation_vi": "NFR quy định phẩm chất vận hành hệ thống như tốc độ xử lý (dưới 5 giây), độ bảo mật, tính sẵn sàng và khả năng chịu tải."
    })

    questions.append({
        "id": "QUES-231",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "User Story Structure",
        "difficulty": "Basic",
        "question_en": "What is the standard Agile template for drafting a user-centric requirement in ERP development?",
        "question_vi": "Mẫu cấu trúc Agile chuẩn mực để viết một User Story hướng người dùng trong dự án phát triển ERP là gì?",
        "options_en": [
            "As a [Role], I want [Feature / Action], So that [Business Value / Benefit]",
            "If [Error occurs], Then [Restart computer], Otherwise [Shutdown]",
            "To Whom It May Concern: Please fix the warehouse software immediately",
            "Dear Supplier, We need 1,000 tires delivered tomorrow morning"
        ],
        "options_vi": [
            "As a [Vai trò người dùng], I want [Tính năng / Hành động mong muốn], So that [Giá trị / Lợi ích nghiệp vụ đạt được]",
            "If [Có lỗi xảy ra], Then [Khởi động lại máy tính], Otherwise [Tắt nguồn]",
            "Kính gửi các bên liên quan: Xin vui lòng sửa phần mềm nhà kho ngay lập tức",
            "Kính gửi Nhà cung cấp: Chúng tôi cần giao 1,000 chiếc lốp vào sáng mai"
        ],
        "correct_answer": 0,
        "explanation_en": "The classic Agile User Story format connects the user persona (As a...), the software capability (I want...), and the measurable business outcome (So that...).",
        "explanation_vi": "User Story chuẩn: 'Với tư cách là [Vai trò], tôi muốn [Tính năng], để [Lợi ích nghiệp vụ]' giúp đội ngũ kỹ thuật hiểu rõ động lực của người dùng."
    })

    questions.append({
        "id": "QUES-232",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Acceptance Criteria (Gherkin)",
        "difficulty": "Basic",
        "question_en": "Which syntax framework is commonly utilized by Business Analysts to structure testable Acceptance Criteria for automated testing?",
        "question_vi": "Cú pháp nào thường được các Business Analyst sử dụng để cấu trúc Tiêu chí Chấp nhận (Acceptance Criteria) phục vụ kiểm thử tự động?",
        "options_en": [
            "Given [Preconditions], When [Trigger Event / Action], Then [Expected Verifiable Outcome]",
            "Select * From Database Where Row = 1",
            "Try... Catch... Finally",
            "Once upon a time... And they lived happily ever after"
        ],
        "options_vi": [
            "Given [Điều kiện tiền đề], When [Sự kiện kích hoạt / Hành động], Then [Kết quả kỳ vọng có thể kiểm chứng]",
            "Select * From Database Where Row = 1",
            "Try... Catch... Finally",
            "Ngày xửa ngày xưa... Và họ sống hạnh phúc mãi mãi về sau"
        ],
        "correct_answer": 0,
        "explanation_en": "Gherkin syntax (Given-When-Then) provides unambiguous, executable specifications for Behavior-Driven Development (BDD) and UAT sign-off.",
        "explanation_vi": "Cú pháp Gherkin (Given-When-Then) mô tả rõ bối cảnh xuất phát, hành động thao tác và kết quả đầu ra cần kiểm chứng, làm căn cứ nghiệm thu UAT."
    })

    questions.append({
        "id": "QUES-233",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "User Acceptance Testing (UAT)",
        "difficulty": "Basic",
        "question_en": "What is the primary objective of User Acceptance Testing (UAT) in an enterprise ERP release?",
        "question_vi": "Mục tiêu trọng tâm của Kiểm thử Chấp nhận Người dùng (User Acceptance Testing - UAT) trong một đợt phát hành ERP là gì?",
        "options_en": [
            "To enable actual business end-users to validate that the configured system executes daily end-to-end operational scenarios in accordance with business requirements before go-live",
            "To test the physical strength of warehouse concrete floors",
            "To rewrite the software program from scratch",
            "To measure the typing speed of office administrative assistants"
        ],
        "options_vi": [
            "Cho phép người dùng nghiệp vụ trực tiếp kiểm chứng hệ thống đã cấu hình có thực thi trôi chảy các kịch bản vận hành thực tế đúng theo yêu cầu trước khi Go-live hay không",
            "Kiểm tra độ chịu lực của sàn bê tông nhà kho",
            "Lập trình lại toàn bộ phần mềm từ đầu",
            "Đo tốc độ gõ bàn phím của nhân viên văn thư"
        ],
        "correct_answer": 0,
        "explanation_en": "UAT is the final quality milestone where business process owners execute real-world scenarios to grant formal sign-off for production deployment.",
        "explanation_vi": "UAT là bước nghiệm thu then chốt: các trưởng bộ phận nghiệp vụ trực tiếp thao tác trên các kịch bản thực tế để ký biên bản nghiệm thu trước khi vận hành chính thức."
    })

    questions.append({
        "id": "QUES-234",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Data Cleansing in ERP Migration",
        "difficulty": "Basic",
        "question_en": "Why is 'Data Cleansing' an indispensable prerequisite when migrating legacy inventory files into an enterprise ERP database?",
        "question_vi": "Vì sao 'Làm sạch Dữ liệu' (Data Cleansing) là tiền đề không thể thiếu khi chuyển đổi dữ liệu tồn kho từ file cũ sang cơ sở dữ liệu ERP mới?",
        "options_en": [
            "Legacy files frequently contain duplicate material numbers, obsolete items, inconsistent units of measure, and corrupt supplier records that would paralyze ERP automated MRP and optimization engines",
            "Because computers cannot read uppercase letters",
            "To delete all customer order histories to hide past corporate revenue",
            "Because older hard drives have dust on their plastic casings"
        ],
        "options_vi": [
            "Các file cũ thường chứa mã vật tư trùng lặp, mặt hàng lỗi thời, đơn vị tính không nhất quán và thông tin nhà cung cấp sai lệch có thể làm tê liệt thuật toán MRP và tối ưu của ERP",
            "Vì máy tính không thể đọc được các chữ cái viết hoa",
            "Để xóa toàn bộ lịch sử đơn hàng nhằm che giấu doanh thu quá khứ",
            "Vì các ổ cứng cũ bị bám bụi bẩn trên vỏ nhựa bên ngoài"
        ],
        "correct_answer": 0,
        "explanation_en": "Garbage in, garbage out: corrupt master data (e.g., mismatched units of measure, duplicate SKUs) crashes mathematical solvers and causes false procurement signals.",
        "explanation_vi": "'Rác vào thì rác ra': dữ liệu rác cũ (sai đơn vị tính, trùng mã SKU) sẽ làm hỏng hoàn toàn các phép tính toán tối ưu và gây rối loạn đơn mua hàng tự động."
    })

    questions.append({
        "id": "QUES-235",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Go-Live Cutover Strategy",
        "difficulty": "Basic",
        "question_en": "What is an ERP 'Cutover' plan during the final transition to production go-live?",
        "question_vi": "'Kế hoạch Chuyển đổi Vận hành' (Cutover Plan) trong giai đoạn chuyển tiếp cuối cùng sang Go-live của dự án ERP là gì?",
        "options_en": [
            "A meticulously scheduled sequence of black-out steps to freeze legacy transactions, extract final financial and inventory balances, load delta data, and open the new ERP system for business",
            "A plan to cut internet cables with scissors",
            "A corporate party celebrating the end of software licensing contracts",
            "An executive meeting to slash departmental employee salaries"
        ],
        "options_vi": [
            "Trình tự các bước chi tiết được lên lịch chính xác để đóng băng giao dịch trên hệ thống cũ, chốt số dư tồn kho và tài chính, nạp dữ liệu chốt kỳ và kích hoạt mở hệ thống ERP mới",
            "Kế hoạch dùng kéo cắt đứt các đường dây cáp mạng internet",
            "Một bữa tiệc liên hoan mừng hết hạn hợp đồng bản quyền phần mềm",
            "Cuộc họp ban giám đốc để cắt giảm lương nhân viên các phòng ban"
        ],
        "correct_answer": 0,
        "explanation_en": "Cutover orchestrates the final transition window: transactional freeze, master data delta load, opening inventory count upload, and operational handoff.",
        "explanation_vi": "Cutover là kế hoạch tác chiến chuyển đổi: chốt sổ hệ thống cũ, nạp số dư tồn kho thực tế chốt kỳ vào ERP, kiểm tra đối soát và phát lệnh mở hệ thống."
    })

    # Intermediate (Q236 - Q245)
    questions.append({
        "id": "QUES-236",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Texago Two-Echelon Supply Chain",
        "difficulty": "Intermediate",
        "question_en": "In the Texago Corporation Site Selection problem (Case 1), how are the two distinct transportation echelons coupled in the enterprise decision model?",
        "question_vi": "Trong bài toán Chọn vị trí nhà máy của Texago Corporation (Case 1), hai tầng vận tải riêng biệt được ghép nối với nhau như thế nào trong mô hình ra quyết định doanh nghiệp?",
        "options_en": [
            "Echelon 1 ships crude oil from oil fields/imports to refineries (360M barrels total); Echelon 2 ships refined finished products from refineries to regional distribution centers (360M barrels total)",
            "Echelon 1 produces television sets and Echelon 2 produces truck tires",
            "Echelon 1 ships peas to Albuquerque and Echelon 2 delivers water to Hollyglass",
            "There is only one echelon; crude oil is pumped directly into retail consumer vehicles"
        ],
        "options_vi": [
            "Tầng 1 vận chuyển dầu thô từ các mỏ nội địa và nhập khẩu đến các nhà máy lọc dầu (tổng 360 triệu thùng); Tầng 2 vận chuyển sản phẩm xăng dầu thành phẩm từ nhà máy đến các kho phân phối (tổng 360 triệu thùng)",
            "Tầng 1 sản xuất máy tivi và Tầng 2 sản xuất lốp xe tải",
            "Tầng 1 chở đậu đóng hộp đến Albuquerque và Tầng 2 cấp nước cho Hollyglass",
            "Chỉ có một tầng duy nhất; dầu thô chưa lọc được bơm thẳng vào bình xăng xe ô tô"
        ],
        "correct_answer": 0,
        "explanation_en": "Texago models a multi-echelon supply chain: crude oil routing (inbound) + refinery processing (operations) + finished product distribution (outbound).",
        "explanation_vi": "Mô hình Texago liên kết hai tầng chuỗi cung ứng: vận chuyển dầu thô đầu vào (inbound) -> lọc dầu tại nhà máy -> phân phối thành phẩm đầu ra (outbound) tới các kho khu vực."
    })

    questions.append({
        "id": "QUES-237",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Texago Capital Cost Exclusion",
        "difficulty": "Intermediate",
        "question_en": "In the Texago case study text, why are capital refinery construction costs excluded from the site selection decision evaluation?",
        "question_vi": "Trong văn bản case study Texago, vì sao chi phí vốn xây dựng nhà máy lọc dầu (Capital Costs) lại được loại trừ khỏi quyết định lựa chọn địa điểm?",
        "options_en": [
            "Because management determined that capital construction expenditures would be essentially identical across all three potential candidate sites",
            "Because the federal government constructs all petroleum refineries for free",
            "Because Texago plans to build the refinery entirely out of wood",
            "Because capital costs are considered illegal under GAAP accounting"
        ],
        "options_vi": [
            "Vì ban lãnh đạo xác định rằng chi phí đầu tư xây dựng cơ bản sẽ cơ bản là tương đương nhau tại bất kỳ địa điểm tiềm năng nào trong số ba địa điểm",
            "Vì chính phủ liên bang xây dựng miễn phí toàn bộ các nhà máy lọc dầu",
            "Vì Texago có kế hoạch xây dựng nhà máy hoàn toàn bằng gỗ",
            "Vì chi phí vốn bị coi là bất hợp pháp theo chuẩn mực kế toán GAAP"
        ],
        "correct_answer": 0,
        "explanation_en": "The case explicitly states: 'Capital costs are not a factor since they would be essentially the same at any of the potential sites.' Thus, only differential variable operating and shipping costs matter.",
        "explanation_vi": "Đề bài khẳng định chi phí xây dựng cơ bản tương đương nhau tại cả 3 nơi, do đó chỉ có chi phí vận hành hàng năm và cước phí vận tải hai tầng là những yếu tố phân hóa quyết định."
    })

    questions.append({
        "id": "QUES-238",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Texago Supplementary JPG Data Role",
        "difficulty": "Intermediate",
        "question_en": "What critical data did the supplementary reference artifact ('Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg') provide that was missing from the student textbook PDF?",
        "question_vi": "Hiện vật bổ sung ('Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg') đã cung cấp dữ liệu trọng yếu nào mà file PDF giáo trình sinh viên bị thiếu sót?",
        "options_en": [
            "The finished product freight matrix from all 6 refineries to 4 distribution centers AND the exact required demand vector (Pittsburgh: 100, Atlanta: 80, Kansas City: 80, San Francisco: 100 million barrels = 360M total)",
            "The personal home phone numbers of refinery plant managers",
            "The chemical molecular weight of crude oil hydrocarbons",
            "A photograph of an offshore oil drilling rig"
        ],
        "options_vi": [
            "Ma trận cước vận chuyển thành phẩm từ cả 6 nhà máy đến 4 trung tâm phân phối VÀ vectơ nhu cầu chính xác của 4 kho (Pittsburgh: 100, Atlanta: 80, Kansas City: 80, San Francisco: 100 triệu thùng = tổng 360 triệu)",
            "Số điện thoại nhà riêng của các giám đốc nhà máy lọc dầu",
            "Trọng lượng phân tử hóa học của các hydrocacbon trong dầu thô",
            "Một bức ảnh chụp giàn khoan dầu ngoài khơi"
        ],
        "correct_answer": 0,
        "explanation_en": "The textbook PDF omitted the distribution center demands. The JPG artifact restored the 100-80-80-100 demand requirements, balancing total demand (360M) with refinery output (360M).",
        "explanation_vi": "File PDF gốc bị in thiếu dòng nhu cầu của 4 kho hàng. Bức ảnh JPG bổ sung chính xác nhu cầu 100-80-80-100 triệu thùng, giúp bài toán cân bằng Tổng Cung = Tổng Cầu = 360 triệu thùng."
    })

    questions.append({
        "id": "QUES-239",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Texago Candidate Site Characteristics",
        "difficulty": "Intermediate",
        "question_en": "In Texago, what are the primary strategic advantages and annual operating costs of St. Louis, Missouri?",
        "question_vi": "Trong case Texago, những lợi thế chiến lược chính và chi phí vận hành hàng năm của địa điểm St. Louis, Missouri là gì?",
        "options_en": [
            "Lowest annual operating cost ($530M), centrally located for inland distribution centers, and ready access to crude via the Mississippi River",
            "Direct Pacific Ocean tanker terminal access from Alaska",
            "Zero operating cost and infinite free crude oil",
            "Located next door to corporate headquarters in Galveston"
        ],
        "options_vi": [
            "Chi phí vận hành hàng năm thấp nhất ($530 triệu), vị trí trung tâm thuận tiện tỏa đi các kho nội địa, và tiếp cận nguồn dầu thô dễ dàng qua sà lan sông Mississippi",
            "Cảng biển nước sâu trực tiếp đón tàu chở dầu từ Alaska qua Thái Bình Dương",
            "Chi phí vận hành bằng 0 và nguồn dầu thô miễn phí vô hạn",
            "Nằm sát ngay cạnh trụ sở chính của tập đoàn tại Galveston"
        ],
        "options_vi": [
            "Chi phí vận hành thấp nhất ($530M), vị trí trung tâm nội địa, tiếp cận dầu thô qua sông Mississippi",
            "Đón tàu dầu từ Alaska qua Thái Bình Dương",
            "Chi phí vận hành bằng 0",
            "Nằm cạnh trụ sở chính ở Galveston"
        ],
        "correct_answer": 0,
        "explanation_en": "Table 2.6 and Table 2.8.3 establish St. Louis has the lowest operational overhead ($530M vs $570M Galveston, $620M LA) and central inland river access.",
        "explanation_vi": "Bảng 2.6 và 2.8.3 xác định St. Louis có chi phí vận hành thấp nhất ($530 triệu so với $570 triệu ở Galveston và $620 triệu ở LA), lại có lợi thế giao thông thủy sông Mississippi."
    })

    questions.append({
        "id": "QUES-240",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Texago Decision Analysis Procedure",
        "difficulty": "Intermediate",
        "question_en": "What is the complete three-step analytical procedure to determine the optimal refinery location for Texago?",
        "question_vi": "Quy trình phân tích 3 bước hoàn chỉnh để xác định vị trí nhà máy lọc dầu tối ưu cho Texago là gì?",
        "options_en": [
            "For each candidate site (LA, Galveston, St. Louis): 1. Solve crude transportation LP; 2. Solve finished product transportation LP; 3. Add Annual Operating Cost to find Total Variable Cost and select minimum",
            "Flip a three-sided coin to choose randomly",
            "Build all three refineries simultaneously to triple output",
            "Choose Los Angeles because it has the most movie theaters"
        ],
        "options_vi": [
            "Với mỗi địa điểm tiềm năng (LA, Galveston, St. Louis): 1. Giải bài toán vận tải dầu thô LP; 2. Giải bài toán vận tải thành phẩm LP; 3. Cộng thêm Chi phí Vận hành Hàng năm để tìm Tổng Chi phí Biến đổi và chọn điểm nhỏ nhất",
            "Tung đồng xu 3 mặt để lựa chọn ngẫu nhiên",
            "Xây dựng cùng lúc cả 3 nhà máy để tăng gấp 3 lần sản lượng",
            "Chọn Los Angeles vì ở đó có nhiều rạp chiếu phim nhất"
        ],
        "correct_answer": 0,
        "explanation_en": "Total system cost must be computed for all 3 scenarios: Total Cost = Inbound Crude Shipping + Outbound Product Shipping + Annual Operating Cost. The lowest total cost wins.",
        "explanation_vi": "Đánh giá toàn diện 3 kịch bản: Tổng Chi Phí = Cước vận chuyển dầu thô + Cước vận chuyển xăng dầu thành phẩm + Chi phí vận hành nhà máy. Địa điểm có tổng chi phí nhỏ nhất sẽ được chọn."
    })

    questions.append({
        "id": "QUES-241",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Master Data Governance",
        "difficulty": "Intermediate",
        "question_en": "What is the primary responsibility of a Master Data Governance (MDG) council in an enterprise ERP ecosystem?",
        "question_vi": "Trách nhiệm hàng đầu của hội đồng Quản trị Dữ liệu Chủ (Master Data Governance - MDG) trong hệ sinh thái ERP doanh nghiệp là gì?",
        "options_en": [
            "To establish standardized definitions, validation workflows, ownership, and maintenance policies for enterprise-wide records (materials, customers, vendors)",
            "To repair physical computer keyboards and mice",
            "To dictate which brand of coffee is brewed in company cafeterias",
            "To personally inspect every delivery truck tire using a magnifying glass"
        ],
        "options_vi": [
            "Thiết lập định nghĩa chuẩn hóa, quy trình phê duyệt kiểm thực, quyền sở hữu dữ liệu và quy chế cập nhật các bản ghi dùng chung (vật tư, khách hàng, nhà cung cấp)",
            "Sửa chữa bàn phím và chuột máy tính bị hỏng",
            "Chỉ định thương hiệu cà phê được pha trong căng-tin công ty",
            "Trực tiếp dùng kính lúp kiểm tra từng chiếc lốp xe tải giao hàng"
        ],
        "correct_answer": 0,
        "explanation_en": "MDG prevents data entropy by enforcing strict authoring workflows, naming conventions, and deduplication rules across cross-functional ERP modules.",
        "explanation_vi": "Hội đồng MDG ngăn ngừa sự hỗn loạn dữ liệu: quy định định dạng chuẩn, phê duyệt mã vật tư mới, chuẩn hóa đơn vị tính và ngăn chặn tạo trùng lặp hồ sơ."
    })

    questions.append({
        "id": "QUES-242",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Role-Based Access Control (RBAC)",
        "difficulty": "Intermediate",
        "question_en": "Why is Segregation of Duties (SoD) enforced via Role-Based Access Control (RBAC) in ERP procurement workflows?",
        "question_vi": "Vì sao nguyên tắc Phân tách Trách nhiệm (Segregation of Duties - SoD) bắt buộc phải được áp dụng qua phân quyền RBAC trong quy trình mua hàng ERP?",
        "options_en": [
            "To prevent internal fraud and embezzlement by ensuring that an employee who creates a Purchase Order cannot also approve the order, receive physical goods, or release vendor payment",
            "To ensure that all employees have identical system passwords",
            "To allow warehouse clerks to alter financial tax reports without authorization",
            "To slow down business operations so workers can leave work early"
        ],
        "options_vi": [
            "Để ngăn ngừa gian lận và biển thủ nội bộ bằng cách bảo đảm rằng nhân viên tạo Đơn Mua Hàng không thể tự phê duyệt đơn, không được kiêm nhiệm nhận hàng vào kho hay chuẩn chi lệnh thanh toán",
            "Để đảm bảo mọi nhân viên trong công ty đều dùng chung một mật khẩu hệ thống",
            "Để cho phép thủ kho có thể tùy ý sửa đổi báo cáo thuế mà không cần phê duyệt",
            "Để làm chậm hoạt động kinh doanh giúp công nhân được về sớm"
        ],
        "correct_answer": 0,
        "explanation_en": "Segregation of Duties (SoD) is a foundational internal audit control (e.g., SOX): separating creation, approval, physical custody, and cash disbursement functions.",
        "explanation_vi": "Phân tách trách nhiệm SoD là yêu cầu kiểm soát nội bộ bắt buộc: người lập đơn không thể tự duyệt, người giữ hàng trong kho không được kiêm nhiệm ký ủy nhiệm chi chuyển tiền."
    })

    questions.append({
        "id": "QUES-243",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Electronic Data Interchange (EDI)",
        "difficulty": "Intermediate",
        "question_en": "Which standard ANSI X12 / EDIFACT electronic transaction set is universally transmitted between wholesalers (like ACT) and manufacturers (like Eversafe) to place purchase orders?",
        "question_vi": "Bộ thông điệp điện tử chuẩn ANSI X12 / EDIFACT nào được truyền phổ biến giữa các nhà bán buôn (như ACT) và nhà sản xuất (như Eversafe) để đặt mua hàng?",
        "options_en": [
            "EDI 850 (Purchase Order) / EDIFACT ORDERS",
            "EDI 810 (Invoice)",
            "EDI 214 (Transportation Carrier Shipment Status Message)",
            "EDI 997 (Functional Acknowledgment)"
        ],
        "options_vi": [
            "EDI 850 (Purchase Order) / EDIFACT ORDERS",
            "EDI 810 (Hóa đơn tài chính - Invoice)",
            "EDI 214 (Thông điệp trạng thái định vị vận chuyển của hãng xe)",
            "EDI 997 (Xác nhận kỹ thuật đã nhận thông điệp)"
        ],
        "correct_answer": 0,
        "explanation_en": "EDI 850 is the standardized electronic Purchase Order payload carrying line items, quantities, agreed contract prices, and shipping instructions.",
        "explanation_vi": "EDI 850 là thông điệp Đơn Đặt Hàng Mua điện tử chuẩn quốc tế truyền trực tiếp từ hệ thống ERP của người mua sang hệ thống của người bán."
    })

    questions.append({
        "id": "QUES-244",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Real-Time Inventory Visibility (ATP)",
        "difficulty": "Intermediate",
        "question_en": "When a sales representative enters a large tire order into ERP, what three inventory categories does the system evaluate to confirm Available-to-Promise (ATP)?",
        "question_vi": "Khi nhân viên kinh doanh nhập một đơn hàng lốp xe lớn vào ERP, ba phân loại tồn kho nào được hệ thống đối soát để xác nhận Khả năng Cam kết Giao hàng (ATP)?",
        "options_en": [
            "Unrestricted physical on-hand stock, planned incoming goods receipts (open purchase orders / production orders), minus already committed reservations from prior customer sales orders",
            "Damaged scrap goods, employee personal cars, and warehouse trash bins",
            "Tires that were sold five years ago",
            "Future customer orders that have not yet been placed"
        ],
        "options_vi": [
            "Tồn kho khả dụng thực tế trong kho, các lô hàng dự kiến sẽ về (đơn mua hàng PO mở / lệnh sản xuất đang chạy), trừ đi lượng hàng đã cam kết giữ chỗ cho các đơn bán hàng trước",
            "Hàng phế phẩm bị hỏng, xe ô tô cá nhân của nhân viên và thùng rác nhà kho",
            "Số lượng lốp xe đã bán từ 5 năm trước",
            "Các đơn hàng tương lai của khách hàng mà hiện tại khách chưa hề đặt"
        ],
        "correct_answer": 0,
        "explanation_en": "ATP dynamically calculates: ATP = On-Hand Stock + Planned Inbound Replenishment - Existing Allocated Outbound Demands.",
        "explanation_vi": "Công thức kiểm tra ATP động trong ERP: Tồn kho sẵn có = Tồn kho vật lý + Lô hàng sắp nhập về - Lượng hàng đã cam kết cho các đơn bán hàng khác."
    })

    questions.append({
        "id": "QUES-245",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Analytics & Executive Dashboards",
        "difficulty": "Intermediate",
        "question_en": "What is the primary operational value of integrating an executive Business Intelligence (BI) dashboard with core ERP transactional tables?",
        "question_vi": "Giá trị vận hành hàng đầu của việc tích hợp bảng điều khiển báo cáo quản trị (BI Dashboard) với các bảng dữ liệu giao dịch cốt lõi của ERP là gì?",
        "options_en": [
            "It provides real-time executive visibility into Key Performance Indicators (KPIs) such as inventory turnover ratio, order fulfillment rates, transportation cost per ton-mile, and cash conversion cycle",
            "It automatically increases employee salaries without management review",
            "It plays classical music when truck drivers park their vehicles",
            "It deletes all overdue customer debts from the database"
        ],
        "options_vi": [
            "Cung cấp tầm nhìn thời gian thực cho ban lãnh đạo về các chỉ số hiệu suất trọng yếu (KPI) như hệ số vòng quay tồn kho, tỷ lệ hoàn tất đơn hàng, chi phí vận tải trên mỗi tấn-dặm và chu kỳ chuyển hóa tiền mặt",
            "Tự động tăng lương cho nhân viên mà không cần ban giám đốc phê duyệt",
            "Phát nhạc cổ điển mỗi khi tài xế xe tải đỗ xe vào bãi",
            "Tự động xóa sạch toàn bộ các khoản nợ quá hạn của khách hàng khỏi hệ thống"
        ],
        "correct_answer": 0,
        "explanation_en": "BI dashboards aggregate millions of granular ERP records into strategic metrics (Days Inventory Outstanding, On-Time In-Full OTD, freight variance) for proactive decision-making.",
        "explanation_vi": "Dashboard quản trị tổng hợp hàng triệu giao dịch ERP thành các chỉ số KPI trực quan (vòng quay tồn kho, tỷ lệ giao đúng hạn đủ lượng OTIF, chi phí vận tải) giúp ban giám đốc chỉ đạo kịp thời."
    })

    # Advanced (Q246 - Q250)
    questions.append({
        "id": "QUES-246",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "BA Traceability Matrix in ERP Delivery",
        "difficulty": "Advanced",
        "question_en": "Why does a Lead Business Analyst construct a Requirements Traceability Matrix (RTM) spanning Business Needs, Functional Specifications, Technical Configuration, and UAT Test Scripts?",
        "question_vi": "Vì sao một Lead Business Analyst bắt buộc phải xây dựng Ma trận Truy xuất Yêu cầu (Requirements Traceability Matrix - RTM) kết nối từ Nhu cầu Kinh doanh, Đặc tả Chức năng, Cấu hình Kỹ thuật đến Kịch bản Kiểm thử UAT?",
        "options_en": [
            "To guarantee complete bidirectional alignment, verifying that every business need is satisfied by software features and tested in UAT, while preventing gold-plating scope creep",
            "To prove that the BA worked overtime hours to justify their billing rate",
            "Because international law requires all software to have colorful matrices",
            "To replace software developers with automated spreadsheets"
        ],
        "options_vi": [
            "Để đảm bảo sự đồng bộ hai chiều toàn diện, chứng minh mọi nhu cầu kinh doanh đều được hiện thực hóa bằng tính năng phần mềm và được kiểm thử trong UAT, đồng thời ngăn chặn phát sinh tính năng thừa (scope creep)",
            "Để chứng minh BA có làm thêm giờ nhằm biện minh cho mức thù lao dự án",
            "Vì luật pháp quốc tế bắt buộc mọi phần mềm đều phải có ma trận nhiều màu sắc",
            "Để thay thế hoàn toàn các lập trình viên phần mềm bằng các bảng tính tự động"
        ],
        "correct_answer": 0,
        "explanation_en": "The RTM ensures rigorous requirement governance: ensuring 100% test coverage for legitimate business needs and eliminating unauthorized custom modifications (gold plating).",
        "explanation_vi": "Ma trận RTM bảo đảm không có yêu cầu nào bị bỏ sót trong quá trình lập trình và kiểm thử UAT, đồng thời ngăn ngừa đội ngũ kỹ thuật tự ý thêm tính năng không cần thiết làm đội chi phí."
    })

    questions.append({
        "id": "QUES-247",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Coupling Transportation LP with Inventory EOQ",
        "difficulty": "Advanced",
        "question_en": "In a holistic enterprise supply chain, why are transportation routing decisions and warehouse inventory lot-sizing decisions mathematically coupled rather than independent?",
        "question_vi": "Trong một chuỗi cung ứng doanh nghiệp tổng thể, vì sao các quyết định lập tuyến vận chuyển và quy mô lô hàng tồn kho kho bãi lại gắn kết chặt chẽ về mặt toán học chứ không hề độc lập?",
        "options_en": [
            "Order batch size Q directly determines shipping frequency and vehicle freight utilization (FTL vs LTL rates), meaning minimizing transportation in isolation inflates inventory holding costs, and vice versa",
            "Because truck drivers also work as warehouse inventory accountants",
            "Because transportation and inventory share the exact same mathematical formula",
            "There is no coupling; transportation and inventory have zero interaction in business"
        ],
        "options_vi": [
            "Quy mô lô đặt hàng Q trực tiếp quyết định tần suất vận chuyển và mức độ tận dụng tải trọng xe (cước nguyên xe FTL vs cước lẻ xe LTL), nghĩa là nếu tối ưu hóa vận chuyển riêng lẻ sẽ làm bùng nổ chi phí lưu kho và ngược lại",
            "Vì tài xế xe tải kiêm nhiệm luôn công việc kế toán kiểm kê hàng tồn kho",
            "Vì bài toán vận tải và bài toán tồn kho dùng chung một công thức toán học y hệt nhau",
            "Không có sự gắn kết nào; vận tải và tồn kho hoàn toàn không có tương tác gì trong kinh doanh"
        ],
        "correct_answer": 0,
        "explanation_en": "Transportation and inventory exhibit fundamental trade-offs: shipping Full Truckload (FTL) minimizes freight costs per unit but forces massive lot sizes Q, driving up warehouse inventory carrying costs.",
        "explanation_vi": "Đây là sự đánh đổi kinh điển trong SCM: gom đủ chuyến xe lớn (FTL) để tối ưu cước vận tải sẽ buộc quy mô lô Q phải lớn, làm tồn kho lưu bãi tăng vọt; chia nhỏ lô hàng để kho tinh gọn thì cước vận chuyển lẻ (LTL) lại đắt đỏ."
    })

    questions.append({
        "id": "QUES-248",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Post-Go-Live Operational Productivity Slump",
        "difficulty": "Advanced",
        "question_en": "During the first four weeks post-go-live, an enterprise experiences a temporary 15% drop in warehouse shipping throughput despite flawless software execution. How should a Senior BA analyze this phenomenon?",
        "question_vi": "Trong bốn tuần đầu tiên sau Go-live, doanh nghiệp bị sụt giảm tạm thời 15% năng suất xuất hàng tại kho dù phần mềm vận hành hoàn hảo không có lỗi kỹ thuật. Senior BA nên phân tích hiện tượng này như thế nào?",
        "options_en": [
            "It is the expected 'productivity dip' of the organizational learning curve as warehouse operators adapt to new handheld RF barcode workflows and transaction screens; mitigate through floor coaching and super-user support",
            "Declare the entire ERP implementation a total failure and revert to legacy paper ledgers immediately",
            "Fire all warehouse operators and replace them with contract laborers",
            "Assume the mathematical optimization engine has a hardware defect"
        ],
        "options_vi": [
            "Đây là hiện tượng 'sụt giảm năng suất tạm thời' (Productivity Dip) tự nhiên của đường cong học tập khi nhân viên kho phải thích nghi với máy quét mã vạch và màn hình giao diện mới; cần khắc phục bằng hỗ trợ cầm tay chỉ việc tại chỗ",
            "Tuyên bố dự án ERP thất bại hoàn toàn và quay trở lại dùng sổ sách giấy truyền thống ngay lập tức",
            "Sa thải toàn bộ công nhân kho và thay thế bằng lao động thời vụ",
            "Cho rằng bộ giải thuật toán tối ưu hóa bị lỗi phần cứng"
        ],
        "correct_answer": 0,
        "explanation_en": "The post-implementation productivity dip is a well-documented change management phenomenon: operational staff face cognitive friction adapting to unfamiliar ERP interfaces, resolved via on-the-ground super-user coaching.",
        "explanation_vi": "Hiện tượng sụt giảm năng suất ban đầu là quy luật tâm lý học tập tự nhiên: nhân sự thao tác chưa quen tay trên phần mềm mới. Cần duy trì đội ngũ hỗ trợ Super-User tại hiện trường thay vì hoang mang kết luận phần mềm lỗi."
    })

    questions.append({
        "id": "QUES-249",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "ERP Cloud Continuous Integration / Continuous Delivery (CI/CD)",
        "difficulty": "Advanced",
        "question_en": "In a modern SaaS Cloud ERP environment (e.g., automated bi-monthly releases), how must the enterprise testing and release governance be structured by IT leadership?",
        "question_vi": "Trong môi trường ERP Đám mây SaaS hiện đại (với các bản cập nhật tính năng tự động 2 tháng một lần từ nhà sản xuất), quy trình kiểm thử và quản trị phát hành cần được tổ chức như thế nào?",
        "options_en": [
            "Deploy automated regression test suites to validate custom integration endpoints and core business processes in a sandbox environment before each vendor cloud push goes live in production",
            "Block all vendor cloud updates permanently to prevent software changes",
            "Stop conducting all software testing and rely entirely on vendor luck",
            "Instruct employees to disconnect computers from the internet whenever an update arrives"
        ],
        "options_vi": [
            "Triển khai bộ kiểm thử hồi quy tự động (Automated Regression Testing) để kiểm chứng các cổng tích hợp riêng và quy trình cốt lõi trên môi trường Sandbox trước khi bản cập nhật của hãng được áp vào môi trường Production",
            "Khóa vĩnh viễn mọi bản cập nhật đám mây của nhà cung cấp để phần mềm không bao giờ bị thay đổi",
            "Ngừng toàn bộ công tác kiểm thử phần mềm và trông chờ hoàn toàn vào may rủi của nhà cung cấp",
            "Yêu cầu nhân viên ngắt kết nối máy tính khỏi mạng internet mỗi khi có thông báo cập nhật"
        ],
        "correct_answer": 0,
        "explanation_en": "SaaS Cloud ERP requires continuous automated regression testing: verifying that vendor platform patches do not break custom API interfaces, workflows, or reporting extensions.",
        "explanation_vi": "Cloud ERP cập nhật liên tục đòi hỏi bộ kiểm thử hồi quy tự động: bảo đảm mỗi khi hãng nâng cấp hệ thống thì các kết nối API riêng, quy trình phê duyệt nội bộ và báo cáo quản trị vẫn hoạt động ổn định."
    })

    questions.append({
        "id": "QUES-250",
        "exam_id": "EXAM-10",
        "chapter_id": "chap-06",
        "topic": "Holistic Capstone Synthesis: SCM Optimization & BA Practice",
        "difficulty": "Advanced",
        "question_en": "Synthesizing the entire course: How do scientific operations research models (Transportation LP, Hungarian Assignment, EOQ, EPQ) transform an enterprise ERP system from a passive system of record into an active decision support engine?",
        "question_vi": "Tổng hợp toàn bộ chương trình học: Các mô hình nghiên cứu vận hành khoa học (Quy hoạch Tuyến tính Vận tải, Phân công Hungarian, EOQ, EPQ) giúp chuyển đổi hệ thống ERP doanh nghiệp từ một hệ thống ghi chép thụ động thành một cỗ máy hỗ trợ ra quyết định chủ động như thế nào?",
        "options_en": [
            "By embedding prescriptive mathematical algorithms that ingest transactional master data, evaluate complex multi-facility trade-offs, and recommend provably optimal operational plans that maximize enterprise profitability and customer service",
            "By converting the ERP system into an arcade video game for factory floor workers",
            "By eliminating the need for corporate financial accounting ledgers",
            "By ensuring that all business decisions are made based on executive intuition"
        ],
        "options_vi": [
            "Bằng cách nhúng các thuật toán toán học tối ưu tự động đọc dữ liệu chủ giao dịch, phân tích đa chiều các sự đánh đổi phức tạp trên mạng lưới, và đề xuất các phương án vận hành tối ưu chuẩn xác giúp tối đa hóa lợi nhuận và mức độ phục vụ khách hàng",
            "Bằng cách biến hệ thống ERP thành một trò chơi điện tử giải trí cho công nhân nhà máy",
            "Bằng cách loại bỏ hoàn toàn sự cần thiết của các sổ cái kế toán tài chính doanh nghiệp",
            "Bằng cách đảm bảo rằng mọi quyết định kinh doanh đều được đưa ra dựa trên cảm tính trực giác của ban giám đốc"
        ],
        "correct_answer": 0,
        "explanation_en": "Mathematical optimization elevates ERP from merely recording historical transactions (System of Record) to proactively orchestrating least-cost, high-service operational execution (System of Intelligence).",
        "explanation_vi": "Mô hình định lượng biến ERP từ một công cụ nhập liệu kế toán đơn thuần (System of Record) thành một bộ não điều hành thông minh (System of Intelligence), tự động tính toán các phương án phân bổ và đặt hàng tối ưu mang lại hàng triệu đô la lợi ích kinh tế."
    })

    return questions
