import json

case_studies = [
    {
        "id": "CASE-01",
        "title": {
            "vi": "Vụ việc Texago Corp: Lựa chọn địa điểm xây dựng nhà máy lọc dầu",
            "en": "The Texago Corp. Site Selection Problem"
        },
        "industry": {
            "vi": "Dầu khí & Hóa dầu (Petroleum Refining)",
            "en": "Petroleum & Refining"
        },
        "model_type": {
            "vi": "Mô hình Vận tải Tuyến tính Hai Tầng (Two-Echelon LP Transportation Model)",
            "en": "Two-Echelon Linear Programming Transportation Model"
        },
        "summary": {
            "vi": "Texago cần lựa chọn 1 trong 3 địa điểm tiềm năng (Los Angeles, Galveston, St. Louis) để xây dựng nhà máy lọc dầu mới công suất 120 triệu thùng/năm, tối thiểu hóa tổng chi phí vận chuyển dầu thô, chi phí vận hành nhà máy và chi phí phân phối thành phẩm.",
            "en": "Texago must select 1 of 3 candidate sites (Los Angeles, Galveston, St. Louis) to construct a new 120 million barrel/year refinery, minimizing total crude transport, refinery operating, and finished distribution costs."
        },
        "candidate_sites": [
            {
                "site": "Los Angeles, CA",
                "operating_cost": 620,
                "crude_transport_cost": 410,
                "finished_transport_cost": 410,
                "total_variable_cost": 1440,
                "rank": 3,
                "recommendation": False
            },
            {
                "site": "Galveston, TX",
                "operating_cost": 570,
                "crude_transport_cost": 360,
                "finished_transport_cost": 450,
                "total_variable_cost": 1380,
                "rank": 2,
                "recommendation": False
            },
            {
                "site": "St. Louis, MO",
                "operating_cost": 530,
                "crude_transport_cost": 440,
                "finished_transport_cost": 360,
                "total_variable_cost": 1330,
                "rank": 1,
                "recommendation": True,
                "savings_vs_worst": 110
            }
        ],
        "key_takeaways": {
            "vi": "St. Louis là vị trí tối ưu với tổng chi phí thấp nhất ($1.330 triệu USD/năm), tiết kiệm $110 triệu USD/năm so với Los Angeles. Mô hình chứng minh việc tối ưu hóa mạng lưới chuỗi cung ứng phải xem xét chi phí toàn chuỗi (end-to-end), không thể chỉ xét riêng chi phí vận hành đơn lẻ.",
            "en": "St. Louis is the optimal site with the lowest total annual cost ($1,330M/year), saving $110M/year compared to Los Angeles. Demonstrates that SCM network optimization requires end-to-end evaluation rather than isolated site cost analysis."
        },
        "markdown_file": "outputs/content/case-studies/CASE_01_TEXAGO.md"
    },
    {
        "id": "CASE-02",
        "title": {
            "vi": "Công ty Better Products: Phân bổ nhà máy sản xuất sản phẩm mới",
            "en": "Assigning Plants to Products (Better Products Company)"
        },
        "industry": {
            "vi": "Sản xuất hàng tiêu dùng (Consumer Goods Manufacturing)",
            "en": "Consumer Goods Manufacturing"
        },
        "model_type": {
            "vi": "Vận tải không cân bằng có cung ảo & Phân công nhị phân 0-1",
            "en": "Unbalanced Transportation with Dummy Demand & Binary 0-1 Assignment"
        },
        "summary": {
            "vi": "Phân bổ 4 sản phẩm mới vào 3 nhà máy có công suất dư thừa (tổng cung 195 > tổng cầu 120). Case 2.1 cho phép chia tách sản phẩm giữa các nhà máy; Case 2.2 yêu cầu phân công nguyên khối (mỗi sản phẩm chỉ sản xuất tại đúng một nhà máy duy nhất).",
            "en": "Allocating 4 new products into 3 manufacturing plants with excess capacity (supply 195 > demand 120). Case 2.1 permits product splitting; Case 2.2 imposes un-split binary 0-1 dedication."
        },
        "scenarios": [
            {
                "name": "Case 2.1 - Product Splitting Permitted",
                "total_cost": 3260,
                "assignments": [
                    {"plant": "Plant 1 (Capacity 75)", "assignments": "Prod 2: 30, Prod 4: 40, Dummy: 5"},
                    {"plant": "Plant 2 (Capacity 75)", "assignments": "Prod 1: 20, Prod 2: 0, Prod 3: Prohibited, Dummy: 55"},
                    {"plant": "Plant 3 (Capacity 45)", "assignments": "Prod 3: 30, Dummy: 15"}
                ]
            },
            {
                "name": "Case 2.2 - No Splitting (0-1 Assignment)",
                "total_cost": 3290,
                "assignments": [
                    {"subplant": "Plant 1a", "assigned_to": "Product 4 (Demand 40)"},
                    {"subplant": "Plant 1b", "assigned_to": "Product 3 (Demand 30)"},
                    {"subplant": "Plant 2a", "assigned_to": "Product 1 (Demand 20)"},
                    {"subplant": "Plant 2b", "assigned_to": "Product 2 (Demand 30)"},
                    {"subplant": "Plant 3", "assigned_to": "Dummy Demand"}
                ],
                "split_penalty": 30
            }
        ],
        "key_takeaways": {
            "vi": "Ràng buộc không chia nhỏ sản phẩm (Case 2.2) làm chi phí tăng nhẹ $30/ngày ($3.290 vs $3.260), nhưng giảm thiểu chi phí chuyển đổi dây chuyền (changeover costs), giảm rủi ro chất lượng và đơn giản hóa điều hành sản xuất trên hệ thống ERP.",
            "en": "Prohibiting product splitting (Case 2.2) incurs a modest cost premium of $30/day ($3,290 vs $3,260), but eliminates line changeovers, reduces quality variance, and simplifies production scheduling in ERP."
        },
        "markdown_file": "outputs/content/case-studies/CASE_02_BETTER_PRODUCTS.md"
    },
    {
        "id": "CASE-03",
        "title": {
            "vi": "Tập đoàn Atlantic Coast Tire (ACT): Quản trị chi phí và tồn kho lốp xe",
            "en": "The Atlantic Coast Tire Corp. (ACT) Problem"
        },
        "industry": {
            "vi": "Phụ tùng ô tô & Phân phối bán buôn (Automotive Aftermarket Distribution)",
            "en": "Automotive Aftermarket & Tire Distribution"
        },
        "model_type": {
            "vi": "Mô hình EOQ cơ bản, EOQ thiếu hàng có kế hoạch & EOQ chiết khấu số lượng",
            "en": "Basic EOQ, EOQ with Planned Shortages, and EOQ with Quantity Discounts"
        },
        "summary": {
            "vi": "ACT phân phối lốp xe bán chạy (D = 6.000 lốp/năm, K = $115, h = $4,20). Đánh giá sự chuyển đổi từ chính sách đặt hàng trực giác (Q = 1.000) sang EOQ cơ bản (Q* = 573), EOQ thiếu hàng (p = $7,50 -> Q* = 716, S* = 257) và EOQ chiết khấu mua hàng số lượng lớn.",
            "en": "ACT distributes passenger tires (D = 6,000/yr, K = $115, h = $4.20). Evaluates transition from intuitive lot size (Q = 1,000) to Basic EOQ (Q* = 573), Planned Shortages (Q* = 716, S* = 257), and Quantity Discounts."
        },
        "policies": [
            {
                "name": "Chính sách hiện tại (Current Guesswork)",
                "lot_size": 1000,
                "tvc": 2790.00,
                "notes": "Đặt hàng trực quan không có cơ sở khoa học"
            },
            {
                "name": "Mô hình EOQ cơ bản (Basic EOQ)",
                "lot_size": 573,
                "tvc": 2407.48,
                "savings": 382.52,
                "notes": "Tiết kiệm 13.7% chi phí biến đổi"
            },
            {
                "name": "Mô hình EOQ cho phép thiếu hàng (Planned Shortages)",
                "lot_size": 716,
                "shortage": 257,
                "tvc": 1927.56,
                "savings": 862.44,
                "notes": "Tiết kiệm 30.9% chi phí biến đổi"
            },
            {
                "name": "Mô hình chiết khấu số lượng (Quantity Discounts)",
                "lot_size": 750,
                "unit_cost": 19.80,
                "total_cost": 121279.25,
                "savings": 1128.23,
                "notes": "Tối ưu hóa tổng chi phí bao gồm cả giá mua"
            }
        ],
        "key_takeaways": {
            "vi": "Mô hình toán học hóa giúp ACT tiết kiệm hàng ngàn USD chi phí vận hành hàng năm. Đặc biệt, khi nhà cung cấp đưa ra chiết khấu theo số lượng, điểm đặt hàng tối ưu chuyển dịch sang điểm phá vỡ giá (price breakpoint) Q = 750 chiếc.",
            "en": "Mathematical inventory modeling delivers significant bottom-line cost reduction. With quantity discounts, the optimal order policy shifts to the price breakpoint Q = 750 tires."
        },
        "markdown_file": "outputs/content/case-studies/CASE_03_ACT_TIRE.md"
    },
    {
        "id": "CASE-04",
        "title": {
            "vi": "Công ty SOCA: Bài toán sản xuất và bổ sung hàng dần dần (EPQ)",
            "en": "The SOCA Problem (Gradual Replenishment / EPQ)"
        },
        "industry": {
            "vi": "Sản xuất linh kiện điện tử & TV (Consumer Electronics Manufacturing)",
            "en": "Consumer Electronics Manufacturing"
        },
        "model_type": {
            "vi": "Mô hình Cỡ Lô Sản Xuất Kinh Tế (Economic Production Quantity - EPQ)",
            "en": "Economic Production Quantity (EPQ) Model"
        },
        "summary": {
            "vi": "SOCA tự sản xuất linh kiện loa phục vụ lắp ráp TV (d = 1.000/ngày, p = 3.000/ngày, D = 250.000/năm, K = $12.000/lần setup, h = $3,60/năm). So sánh chính sách hiện tại (Q = 30.000) với cỡ lô tối ưu EPQ (Q* = 50.000).",
            "en": "SOCA manufactures speakers for TV assembly (d = 1,000/day, p = 3,000/day, D = 250,000/yr, K = $12,000/setup, h = $3.60/yr). Compares current policy (Q = 30,000) with EPQ optimum (Q* = 50,000)."
        },
        "comparison": {
            "current": {
                "lot_size": 30000,
                "runs_per_year": 8.33,
                "production_days": 10.0,
                "idle_days": 20.0,
                "max_inventory": 20000,
                "avg_inventory": 10000,
                "annual_setup_cost": 100000.0,
                "annual_holding_cost": 36000.0,
                "total_variable_cost": 136000.0
            },
            "optimal": {
                "lot_size": 50000,
                "runs_per_year": 5.0,
                "production_days": 16.67,
                "idle_days": 33.33,
                "max_inventory": 33333.33,
                "avg_inventory": 16666.67,
                "annual_setup_cost": 60000.0,
                "annual_holding_cost": 60000.0,
                "total_variable_cost": 120000.0
            },
            "annual_savings": 16000.0,
            "percentage_saving": 11.76
        },
        "key_takeaways": {
            "vi": "Tăng kích cỡ lô từ 30.000 lên 50.000 chiếc giúp cân bằng chính xác chi phí thiết lập và lưu kho ($60.000 = $60.000), tiết kiệm ròng $16.000/năm và giải phóng các khối thời gian rảnh rỗi dài hơn (33,33 ngày so với 20 ngày) cho dây chuyền.",
            "en": "Increasing lot size from 30,000 to 50,000 units precisely balances setup and holding costs ($60,000 = $60,000), saving $16,000 annually and extending available downtime for other production runs."
        },
        "markdown_file": "outputs/content/case-studies/CASE_04_SOCA.md"
    }
]

with open("outputs/data/case-studies.json", "w", encoding="utf-8") as f:
    json.dump(case_studies, f, ensure_ascii=False, indent=2)

print("Saved outputs/data/case-studies.json with 4 cases.")
