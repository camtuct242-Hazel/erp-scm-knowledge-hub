import os

chap2_content = """# CHƯƠNG 02: CÁC BIẾN THỂ BÀI TOÁN VẬN TẢI & RÀNG BUỘC THỰC TẾ
## CHAPTER 02: TRANSPORTATION PROBLEM VARIATIONS & REAL-WORLD CONSTRAINTS

---

## 1. Tổng quan Chương học (Chapter Overview)

### 1.1 Giới thiệu bối cảnh (Introduction)
Trong thực tế quản trị chuỗi cung ứng của các doanh nghiệp, điều kiện cân bằng lý tưởng giữa tổng năng lực cung ứng và tổng nhu cầu tiêu thụ hiếm khi xuất hiện. Doanh nghiệp thường xuyên hoạt động trong tình trạng dư thừa năng lực sản xuất (Total Supply > Total Demand) hoặc thiếu hụt nguồn cung trước các đợt bùng nổ nhu cầu thị trường (Total Supply < Total Demand). Bên cạnh đó, mạng lưới logistics thực tế luôn chịu sự chi phối của các rào cản kỹ thuật, địa lý, chính sách pháp lý hoặc hợp đồng độc quyền khiến một số tuyến đường vận chuyển bị cấm chỉ định hoặc bất khả thi.

Chương này trang bị các kỹ thuật nâng cao để mô hình hóa và xử lý các biến thể bài toán vận tải phức tạp: kỹ thuật khởi tạo nguồn/đích ảo (**Dummy Source / Dummy Destination**), phương pháp xử lý tuyến đường cấm (**Prohibited Routes**) bằng hệ số phạt cực lớn (**Big-M Method**), và bài toán phân bổ năng lực sản xuất thực tế dựa trên trường hợp kinh điển **Metro Water District**, **Energetic Company** và **Better Products Company (Case 2.1)**.

### 1.2 Mục tiêu học tập (Learning Objectives)
1. **Phát hiện và phân loại** các trường hợp bài toán vận tải không cân bằng (Unbalanced Transportation Problems).
2. **Thiết lập kỹ thuật điểm ảo**: Tạo điểm đến giả (Dummy Destination) khi Cung > Cầu và điểm nguồn giả (Dummy Source) khi Cầu > Cung với chi phí bằng 0 hoặc chi phí phạt thiếu hàng.
3. **Áp dụng phương pháp Big-M** để loại bỏ các tuyến đường vận chuyển bị cấm hoặc các cặp ghép nhà máy - sản phẩm không tương thích về mặt công nghệ.
4. **Mô hình hóa và giải quyết** bài toán phân bổ công suất nhà máy trong Case Study Better Products 2.1 bằng Excel Solver.
5. **Đặc tả yêu cầu Business Analyst (BA)** cho phân hệ Quản trị Vận tải (TMS) và Kế hoạch Sản xuất (PP) để tự động xử lý năng lực dư thừa và cảnh báo vi phạm tuyến đường.

### 1.3 Mối quan hệ liên chương (Relationship with Other Chapters)
- Phát triển trực tiếp từ nền tảng bài toán vận tải cân bằng ở **Chương 1**.
- Chuẩn bị cơ sở toán học cho **Chương 3** (ràng buộc khoảng nhu cầu [Min, Max] và phân công nguyên khối 0-1).
- Kết nối với việc thiết lập quy tắc Master Data và kiểm soát tuyến đường trong hệ thống ERP ở **Chương 6**.

---

## 2. Các Khái niệm Cốt lõi (Core Concepts)

### 2.1 Bài toán Vận tải Không cân bằng (Unbalanced Transportation Problem)
- **Cung vượt Cầu (Supply > Demand):** Tổng sản lượng khả dụng của các nhà máy lớn hơn tổng dung lượng thị trường ($\sum s_i > \sum d_j$). Doanh nghiệp có năng lực sản xuất nhàn rỗi (Excess / Idle Capacity). Để chuyển bài toán về dạng chuẩn tắc, ta bổ sung một **Điểm đến ảo (Dummy Destination)** đại diện cho phần công suất không được huy động, với nhu cầu:
  $$d_{\text{Dummy}} = \sum_{i=1}^m s_i - \sum_{j=1}^n d_j$$
  Chi phí vận chuyển đến điểm ảo thường gán bằng $0$ ($c_{i,\text{Dummy}} = 0$) nếu công suất nhàn rỗi không phát sinh thêm chi phí phạt.
- **Cầu vượt Cung (Demand > Supply):** Nhu cầu thị trường vượt quá tổng năng lực cung ứng của toàn mạng lưới ($\sum d_j > \sum s_i$). Tình trạng thiếu hụt hàng hóa (Shortage) xuất hiện. Doanh nghiệp phải bổ sung một **Nguồn cung ảo (Dummy Source)** với năng lực:
  $$s_{\text{Dummy}} = \sum_{j=1}^n d_j - \sum_{i=1}^m s_i$$
  Chi phí vận chuyển từ nguồn ảo đến các điểm tiêu thụ ($c_{\text{Dummy},j}$) phản ánh chi phí cơ hội bị mất hoặc tiền phạt do vi phạm cam kết giao hàng (Shortage Penalty Cost).

### 2.2 Tuyến đường Cấm & Phương pháp Big-M (Prohibited Routes & Big-M Method)
Trong mạng lưới thực tế, một số tuyến vận chuyển $i \to j$ không thể thực hiện được do:
1. Phương tiện vận tải không đáp ứng tiêu chuẩn kỹ thuật (ví dụ: đường hẹp không cho xe container vào).
2. Quy định địa phương hoặc lệnh cấm tải theo giờ.
3. Dây chuyền tại nhà máy $i$ không có khuôn mẫu hoặc công nghệ để sản xuất sản phẩm $j$.

Để ngăn chặn thuật toán tối ưu hóa phân bổ bất kỳ khối lượng hàng nào vào tuyến cấm mà không làm phá vỡ cấu trúc ma trận của bài toán quy hoạch tuyến tính, ta gán cho tuyến cấm đó một **chi phí vận chuyển đơn vị cực lớn ($c_{ij} = M$)**, trong đó $M$ là một hằng số dương vượt trội so với mọi chi phí thực tế trong hệ thống ($M \gg \max c_{ij}$). Thuật toán Simplex LP với hàm mục tiêu cực tiểu hóa chi phí sẽ tự động ép $x_{ij} = 0$.

---

## 3. Thuật ngữ Kỹ thuật & Phân biệt Khái niệm (Key Terminologies)

| Thuật ngữ Tiếng Anh | Thuật ngữ Tiếng Việt | Định nghĩa & Ý nghĩa Nghiệp vụ |
|---|---|---|
| **Dummy Destination** | Điểm đến giả / Điểm đến ảo | Điểm nhận ảo tạo ra để hấp thụ toàn bộ phần công suất cung dư thừa của hệ thống. |
| **Dummy Source** | Điểm nguồn giả / Nguồn cung ảo | Điểm cung ảo tạo ra để đại diện cho lượng nhu cầu bị bỏ lỡ (Shortage) khi thiếu cung. |
| **Idle Capacity** | Năng lực sản xuất nhàn rỗi | Khối lượng công suất máy móc không được khai thác do thiếu đơn hàng thị trường. |
| **Prohibited Route** | Tuyến đường bị cấm | Tuyến vận tải không được phép lưu thông do giới hạn kỹ thuật, địa lý hoặc pháp lý. |
| **Big-M Method** | Phương pháp M lớn | Kỹ thuật đặt hệ số phạt kinh tế vô cùng lớn để triệt tiêu biến phân bổ trên tuyến cấm. |
| **Capacity Allocation** | Phân bổ năng lực sản xuất | Hoạch định việc giao nhiệm vụ sản xuất từng dòng sản phẩm cho từng nhà máy. |

---

## 4. Mô hình, Khung lý thuyết & Phương pháp Định lượng (Models & Quantitative Methods)

```mermaid
graph TD
    subgraph SupplySide["Cung Ứng (Tổng Cung = 195)"]
        P1["Nhà máy 1 (Cung 75)"]
        P2["Nhà máy 2 (Cung 75)"]
        P3["Nhà máy 3 (Cung 45)"]
    end
    
    subgraph DemandSide["Nhu Cầu Thực & Điểm Ảo (Tổng Cầu = 195)"]
        D1["SP 1 (Cầu 20)"]
        D2["SP 2 (Cầu 30)"]
        D3["SP 3 (Cầu 30)"]
        D4["SP 4 (Cầu 40)"]
        Dummy["Dummy Demand (Ảo 75)"]
    end

    P1 --> D1
    P1 --> D2
    P1 --> D3
    P1 --> D4
    P1 --> Dummy
    
    P2 --> D1
    P2 --> D2
    P2 -.->|Tuyến cấm c23 = M| D3
    P2 --> D4
    P2 --> Dummy
    
    P3 --> D1
    P3 --> D2
    P3 --> D3
    P3 --> D4
    P3 --> Dummy
```

### 4.1 Mô hình Toán học: Bài toán Phân bổ Better Products (Case 2.1)
Công ty Better Products sở hữu 3 nhà máy có công suất dư thừa, chuẩn bị sản xuất 4 sản phẩm mới:
- **Năng lực cung ứng của các nhà máy:**
  - Nhà máy 1: $s_1 = 75\text{ đơn vị/ngày}$
  - Nhà máy 2: $s_2 = 75\text{ đơn vị/ngày}$
  - Nhà máy 3: $s_3 = 45\text{ đơn vị/ngày}$
  - **Tổng cung khả dụng:** $75 + 75 + 45 = \mathbf{195\text{ đơn vị/ngày}}$
- **Nhu cầu tiêu thụ của 4 sản phẩm:**
  - Sản phẩm 1: $d_1 = 20\text{ đơn vị/ngày}$
  - Sản phẩm 2: $d_2 = 30\text{ đơn vị/ngày}$
  - Sản phẩm 3: $d_3 = 30\text{ đơn vị/ngày}$
  - Sản phẩm 4: $d_4 = 40\text{ đơn vị/ngày}$
  - **Tổng nhu cầu thực tế:** $20 + 30 + 30 + 40 = \mathbf{120\text{ đơn vị/ngày}}$
- **Khởi tạo Dummy Destination:** Vì Tổng cung (195) > Tổng cầu (120), ta bổ sung một sản phẩm giả (Dummy Product 5) với nhu cầu:
  $$d_{\text{Dummy}} = 195 - 120 = \mathbf{75\text{ đơn vị/ngày}}$$
  Chi phí phân bổ vào Dummy bằng 0 ($c_{i,\text{Dummy}} = 0$).

#### Bảng chi phí sản xuất đơn vị và Tuyến cấm:
Do giới hạn công nghệ, **Nhà máy 2 không thể sản xuất Sản phẩm 3**. Ta gán $c_{23} = M = \$10.000$.

| Nhà máy \ Sản phẩm | SP 1 ($d_1=20$) | SP 2 ($d_2=30$) | SP 3 ($d_3=30$) | SP 4 ($d_4=40$) | Dummy ($d_5=75$) | Khả năng cung ($s_i$) |
|---|---|---|---|---|---|---|
| **Nhà máy 1** | \$41 | \$27 | \$28 | \$24 | \$0 | **75** |
| **Nhà máy 2** | \$40 | \$29 | **M (\$10.000)** | \$23 | \$0 | **75** |
| **Nhà máy 3** | \$37 | \$30 | \$27 | \$21 | \$0 | **45** |

### 4.2 Lời giải Tối ưu Toán học (Optimal LP Solution)
Thiết lập bài toán trên Excel Solver với 15 biến quyết định $x_{ij} \ge 0$, hàm mục tiêu cực tiểu hóa chi phí.

| Nhà máy | Phân bổ Sản phẩm ($x_{ij}^*$) | Chi phí đơn vị | Thành tiền |
|---|---|---|---|
| **Nhà máy 1** | Sản phẩm 2: $30\text{ đơn vị}$<br/>Sản phẩm 4: $40\text{ đơn vị}$<br/>Dummy: $5\text{ đơn vị}$ | \$27<br/>\$24<br/>\$0 | $30 \times 27 = \$810$<br/>$40 \times 24 = \$960$<br/>$5 \times 0 = \$0$ |
| **Nhà máy 2** | Sản phẩm 1: $20\text{ đơn vị}$<br/>Dummy: $55\text{ đơn vị}$ | \$40<br/>\$0 | $20 \times 40 = \$800$<br/>$55 \times 0 = \$0$ |
| **Nhà máy 3** | Sản phẩm 3: $30\text{ đơn vị}$<br/>Dummy: $15\text{ đơn vị}$ | \$27<br/>\$0 | $30 \times 27 = \$810$<br/>$15 \times 0 = \$0$ |
| **Tổng cộng** | **Sản xuất đủ 120 đơn vị thực tế** | | **$Z^* = \$3.260/\text{ngày}$** |

#### Đánh giá giải pháp:
- Tuyến cấm Nhà máy 2 $\to$ Sản phẩm 3 có $x_{23}^* = 0$ (phương pháp Big-M hoạt động hoàn hảo).
- Năng lực nhàn rỗi 75 đơn vị được phân bổ cụ thể: Nhà máy 1 dư 5 đơn vị, Nhà máy 2 dư 55 đơn vị, Nhà máy 3 dư 15 đơn vị.

---

## 5. Quy trình Nghiệp vụ (Business Processes)

```mermaid
flowchart TD
    A["Kiểm tra Tổng Cung vs. Tổng Cầu"] --> B{"So sánh Cung & Cầu"}
    B -->|Cung = Cầu| C["Chạy mô hình vận tải tiêu chuẩn"]
    B -->|Cung > Cầu| D["Thêm Dummy Destination<br/>Nhu cầu = Cung - Cầu<br/>Chi phí = 0"]
    B -->|Cầu > Cung| E["Thêm Dummy Source<br/>Cung = Cầu - Cung<br/>Chi phí = Phạt thiếu hàng"]
    D --> F["Kiểm tra ràng buộc cấm kỹ thuật"]
    E --> F
    C --> F
    F --> G{"Có tuyến cấm không?"}
    G -->|Có| H["Gán cước phí Big-M (M >> max cij)"]
    G -->|Không| I["Thực thi Solver Simplex LP"]
    H --> I
    I --> J["Xuất kế hoạch sản xuất & điều chuyển"]
```

---

## 6. Minh họa Trực quan (Visual Learning)

```mermaid
classDiagram
    class TransportationModel {
        +int total_supply
        +int total_demand
        +check_balance()
        +add_dummy_destination()
        +add_dummy_source()
        +apply_big_m(source_id, dest_id)
        +solve_simplex_lp()
    }
    class SupplyNode {
        +String plant_id
        +double capacity
    }
    class DemandNode {
        +String product_id
        +double required_units
    }
    TransportationModel "1" *-- "many" SupplyNode : contains
    TransportationModel "1" *-- "many" DemandNode : contains
```

---

## 7. Ví dụ Thực tế Doanh nghiệp (Practical Business Examples)

### 7.1 Ví dụ Giáo trình: Metro Water District
Huyện Thủy lợi Metro Water District khai thác nước từ 3 dòng sông (Colombo, Sacron, Calorie) với tổng công suất cung ứng $16\text{ triệu m}^3$, cung cấp nước tưới cho 4 khu đô thị lân cận với tổng nhu cầu là $12,5\text{ triệu m}^3$. Bằng cách bổ sung một khu đô thị giả định (Dummy District) có nhu cầu hấp thụ $3,5\text{ triệu m}^3$ nước thặng dư với chi phí dẫn nước bằng $0$, ban quản lý thủy lợi đã xây dựng được lịch trình dẫn nước tối ưu chi phí mà vẫn giữ lại nguồn nước dự trữ an toàn tại các hồ chứa đầu nguồn.

### 7.2 Ví dụ Giáo trình: Energetic Company
Tập đoàn Năng lượng Energetic Co. sở hữu các trạm phát điện chạy bằng than, khí đốt và năng lượng mặt trời. Do hạn chế về mặt đường dây tải điện cao thế kết nối vùng, trạm phát điện mặt trời không thể cấp tải trực tiếp cho trạm biến áp trung tâm số 2. Việc đưa hệ số chi phí Big-M vào ma trận điều độ đã ngăn chặn hoàn toàn nguy cơ quá tải đường dây trong khi vẫn đảm bảo huy động tối đa nguồn năng lượng sạch.

---

## 8. Ứng dụng trong Hệ thống ERP (ERP Applications)

- **Cấu hình Năng lực Nhà máy trong SAP PP (Production Planning):**
  - Giao dịch `CR01` / `CR02` (Work Center): Định nghĩa năng lực khả dụng (Available Capacity).
  - Khái niệm Dummy trong ERP: Khi lập kế hoạch tổng thể (SOP - Sales and Operations Planning), phần công suất không được sử dụng được ghi nhận vào tài khoản chi phí nhàn rỗi (Under-utilization / Idle Capacity Variance) trên phân hệ Kiểm soát chi phí (CO).
- **Chặn tuyến vận tải trong SAP TM (Transportation Management):**
  - Chức năng `Incompatibility Rules` (Quy tắc không tương thích): Cho phép cấu hình hệ thống cấm điều phối một loại phương tiện cụ thể cho một tuyến đường hoặc ngăn không cho vận chuyển chung một số loại hóa chất độc hại với thực phẩm.

---

## 9. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (Business Analyst Perspective)

### 9.1 Yêu cầu Chức năng (Functional Requirements - FR)
- `FR-VAR-01`: Hệ thống PHẢI tự động phát hiện tình trạng chênh lệch giữa tổng năng lực cung ứng và tổng nhu cầu đơn hàng để tự động khởi tạo bản ghi giả định (Dummy Record) trong bảng tính toán trung gian.
- `FR-VAR-02`: Hệ thống PHẢI cung cấp bảng ma trận quy tắc cấm (Restriction Matrix) cho phép người dùng nghiệp vụ đánh dấu các cặp [Nhà máy - Sản phẩm] không hợp lệ mà không cần can thiệp chỉnh sửa code.

### 9.2 Quy tắc Nghiệp vụ (Business Rules - BR)
- `BR-CAP-01`: Chi phí nhàn rỗi (Idle cost) của các nhà máy mặc định bằng 0, trừ khi có thỏa thuận công đoàn quy định mức trợ cấp ngừng việc tối thiểu cho công nhân theo giờ.
- `BR-CAP-02`: Giá trị của hệ số phạt $M$ trong thuật toán PHẢI lớn hơn ít nhất 100 lần so với chi phí vận tải lớn nhất trong cơ sở dữ liệu hiện hành.

### 9.3 Tiêu chí Nghiệm thu (UAT Acceptance Criteria)
- **Kịch bản:** Kiểm tra tuyến cấm Nhà máy 2 $\to$ Sản phẩm 3.
  - *Given* Cấu hình tuyến Nhà máy 2 - Sản phẩm 3 có thuộc tính `Prohibited = True`.
  - *When* Chạy tiến trình tối ưu hóa MRP/Transportation Run.
  - *Then* Sản lượng phân bổ $x_{23}$ bắt buộc phải bằng đúng 0; hệ thống không được phát sinh lỗi phân kỳ thuật toán.

---

## 10. Phân tích Phản biện & Đánh đổi Chiến lược (Critical Analysis)

- **Chi phí ẩn của năng lực nhàn rỗi:** Mô hình toán học thường xem chi phí của điểm ảo là \$0. Tuy nhiên trong thực tế kinh doanh, năng lực máy móc bị bỏ trống vẫn phát sinh chi phí khấu hao tài sản cố định (Depreciation) và chi phí duy tu bảo dưỡng. Doanh nghiệp cần chủ động tìm kiếm các đơn hàng gia công ngoài (OEM/Contract Manufacturing) để lấp đầy công suất này.
- **Rủi ro số học khi chọn giá trị M:** Nếu chọn giá trị $M$ quá nhỏ, thuật toán có thể chấp nhận chọn tuyến cấm khi chi phí chung tăng cao. Ngược lại, nếu chọn $M$ quá lớn (ví dụ: $10^{15}$), hệ thống có thể gặp lỗi số học tràn số hoặc làm mất tính chính xác do sai số làm tròn (Floating Point Rounding Error) trong thuật toán Simplex.

---

## 11. Tóm tắt Chương học (Chapter Summary)
1. Bài toán vận tải thực tế hầu hết là không cân bằng; kỹ thuật bổ sung Dummy Source hoặc Dummy Destination giúp đưa mô hình về dạng chuẩn tắc.
2. Tuyến đường cấm hoặc giới hạn kỹ thuật được xử lý linh hoạt và triệt để bằng phương pháp Big-M.
3. Case Study Better Products 2.1 chứng minh tính hiệu quả của mô hình trong việc phân bổ công suất nhà máy dư thừa, đem lại mức chi phí vận hành tối ưu \$3.260/ngày.
4. Chuyên viên BA cần thiết kế các quy tắc nghiệp vụ linh hoạt (Incompatibility Rules) trong hệ thống ERP để phản ánh chính xác các giới hạn vật lý của nhà xưởng.

---

## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Khi tổng năng lực cung ứng của các nhà máy lớn hơn tổng nhu cầu thị trường ($\sum s_i > \sum d_j$), kỹ thuật nào sau đây được áp dụng để cân bằng bài toán?
   - A. Thêm một nguồn cung ảo (Dummy Source) với năng lực bằng hiệu số Cung - Cầu.
   - B. Thêm một điểm đến ảo (Dummy Destination) với nhu cầu bằng hiệu số Cung - Cầu và chi phí đơn vị thường bằng 0.
   - C. Cắt giảm ngẫu nhiên công suất của các nhà máy.
   - D. Nhân đôi nhu cầu của tất cả các điểm tiêu thụ.
   - *Đáp án đúng:* **B**.

2. **Câu hỏi:** Trong phương pháp Big-M để xử lý tuyến đường cấm, bản chất của tham số $M$ là gì?
   - A. Là số lượng hàng hóa tối đa được phép vận chuyển trên tuyến.
   - B. Là một hằng số dương cực lớn đóng vai trò là mức phạt kinh tế để ép biến quyết định tương ứng về giá trị 0 trong hàm cực tiểu hóa chi phí.
   - C. Là thời gian giao hàng tối thiểu tính bằng phút.
   - D. Là hệ số chiết khấu giá cước vận tải.
   - *Đáp án đúng:* **B**.
"""

with open("outputs/content/chapters/CHAP_02.md", "w", encoding="utf-8") as f:
    f.write(chap2_content)

print("Saved outputs/content/chapters/CHAP_02.md")
