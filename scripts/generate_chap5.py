import os

chap5_content = r"""# CHƯƠNG 05: CÁC BIẾN THỂ MÔ HÌNH QUẢN TRỊ TỒN KHO THỰC TẾ
## CHAPTER 05: DETERMINISTIC INVENTORY MODELS UNDER COMPLEX BUSINESS CONDITIONS

---

## 1. Tổng quan Chương học (Chapter Overview)

### 1.1 Giới thiệu bối cảnh (Introduction)
Mặc dù mô hình EOQ cơ bản (Chương 4) mang lại những hiểu biết trực giác sâu sắc về sự cân bằng chi phí, các giả định lý tưởng của nó hiếm khi phản ánh trọn vẹn sự phức tạp của thế giới kinh doanh:
1. Doanh nghiệp bán hàng công nghiệp (B2B) hoặc sản phẩm độc quyền có thể thỏa thuận để khách hàng chấp nhận nhận hàng trễ hạn (**Planned Shortages / Backorders**) nhằm giảm quy mô tồn kho đệm.
2. Các nhà cung cấp luôn đưa ra chính sách giá khuyến khích mua số lượng lớn (**Quantity Discounts**), phá vỡ giả định giá mua đơn vị ($c$) là hằng số cố định.
3. Trong môi trường tự sản xuất nội bộ, hàng hóa không thể xuất hiện tức thời trong kho trong chớp mắt mà được tạo ra dần dần với một tốc độ sản xuất hữu hạn (**Gradual Replenishment / Economic Production Quantity - EPQ**).

Chương này đi sâu vào 3 biến thể toán học kinh điển nhằm mở rộng mô hình tồn kho tất định: Mô hình cho phép thiếu hàng có kế hoạch (kiểm chứng qua số liệu mở rộng của **Atlantic Coast Tire**), Mô hình chiết khấu số lượng theo bậc thang giá, và Mô hình sản xuất kinh tế bổ sung dần dần qua tình huống chuyên sâu của **Công ty Sản xuất TV SOCA**.

### 1.2 Mục tiêu học tập (Learning Objectives)
1. **Dẫn xuất và làm chủ công thức EOQ cho phép thiếu hàng**: Tính toán quy mô lô tối ưu ($Q^*$), mức thiếu hụt cực đại ($S^*$) và mức tồn kho đỉnh ($Q^* - S^*$).
2. **Nắm vững thuật toán 3 bước giải bài toán Chiết khấu số lượng** (Quantity Discounts) và kiểm tra tính khả thi tại các điểm phá vỡ giá (Price Breakpoints).
3. **Phân tích cơ chế hoạt động của Mô hình EPQ (Bổ sung dần)**: Chứng minh tại sao tồn kho cực đại chỉ đạt $I_{\max} = Q(1 - d/p)$ và dẫn xuất công thức cỡ lô sản xuất tối ưu.
4. **Giải quyết triệt để tình huống SOCA**: Lượng hóa khoản tiết kiệm \$16.000/năm và tối ưu hóa thời gian chạy máy (16,67 ngày chạy, 33,33 ngày nghỉ).
5. **Đặc tả yêu cầu Business Analyst (BA)** cho các phân hệ Mua hàng (MM) và Sản xuất (PP) trên nền tảng ERP để cấu hình đúng các điều kiện thương mại và quy trình kiểm soát lô hàng.

### 1.3 Mối quan hệ liên chương (Relationship with Other Chapters)
- Phát triển trực tiếp từ nền tảng lý thuyết cân bằng chi phí của **Chương 4**.
- Cung cấp các công thức định cỡ lô (Lot-Sizing Procedures) phục vụ trực tiếp cho vòng lặp chạy Hoạch định Nhu cầu Nguyên vật liệu (MRP) trong kiến trúc tích hợp hệ sinh thái ERP ở **Chương 6**.

---

## 2. Các Khái niệm Cốt lõi (Core Concepts)

### 2.1 Biến thể 1: Thiếu hàng Có Kế hoạch (Planned Shortages / Backorders)
- **Bản chất:** Khi kho hết hàng, khách hàng không bỏ đi sang đối thủ cạnh tranh mà đồng ý chờ đợi (Backorder). Lô hàng tiếp theo khi cập bến sẽ ưu tiên bù đắp ngay lập tức cho các đơn hàng nợ tồn này trước khi đưa lượng hàng còn lại vào kho dự trữ.
- **Chi phí phát sinh:** Doanh nghiệp chịu thêm chi phí phạt thiếu hàng $p$ (\$/đơn vị nợ/năm) để bù đắp việc chiết khấu bồi thường hoặc chi phí quản lý đơn hàng trễ.
- **Hàm ý kinh tế:** Bằng cách chấp nhận một lượng thiếu hàng nhất định, doanh nghiệp cắt giảm được đáng kể mức tồn kho đỉnh ($I_{\max} = Q - S < Q$), từ đó giảm chi phí lưu kho vốn rất đắt đỏ.

### 2.2 Biến thể 2: Chiết khấu Mua hàng Theo Số lượng (Quantity Discounts)
- **Bản chất:** Nhà cung cấp đưa ra biểu giá bậc thang: Mua càng nhiều, đơn giá $c$ càng giảm. Biểu giá phổ biến nhất là chiết khấu toàn bộ đơn vị (All-Units Quantity Discount):
  $$c = \begin{cases} c_1 & \text{nếu } 0 \le Q < q_1 \\ c_2 & \text{nếu } q_1 \le Q < q_2 \quad (c_2 < c_1) \\ c_3 & \text{nếu } Q \ge q_2 \quad (c_3 < c_2) \end{cases}$$
- **Hàm ý kinh tế:** Giá mua $c$ thay đổi dẫn đến chi phí mua hàng hàng năm ($c \times D$) không còn là hằng số cố định. Ta bắt buộc phải cực tiểu hóa **Tổng chi phí toàn diện (Total Cost - TC)** bao gồm cả chi phí mua hàng:
  $$\text{TC}(Q) = cD + K\frac{D}{Q} + h\frac{Q}{2}$$

### 2.3 Biến thể 3: Bổ sung Hàng Dần dần (Gradual Replenishment / EPQ)
- **Bản chất:** Hàng hóa được sản xuất tại xưởng nội bộ với tốc độ $p$ (đơn vị/ngày). Dây chuyền tiêu thụ hoặc thị trường đồng thời rút hàng với tốc độ $d$ (đơn vị/ngày), với điều kiện năng lực sản xuất phải lớn hơn tốc độ tiêu thụ ($p > d$).
- **Động thái tồn kho:** Trong giai đoạn nhà xưởng đang chạy máy, hàng vừa được bổ sung vừa bị tiêu thụ, do đó tồn kho chỉ tích lũy với tốc độ ròng là $(p - d)$. Khi lô hàng sản xuất đủ $Q$ đơn vị, máy móc ngừng chạy để phục vụ sản phẩm khác; tồn kho sau đó giảm dần với tốc độ tiêu thụ $-d$ cho đến khi chạm 0.

---

## 3. Thuật ngữ Kỹ thuật & Phân biệt Khái niệm (Key Terminologies)

| Thuật ngữ Tiếng Anh | Thuật ngữ Tiếng Việt | Định nghĩa & Ý nghĩa Nghiệp vụ |
|---|---|---|
| **Backorder** | Đơn hàng nợ / Giao bù sau | Đơn đặt hàng của khách phát sinh khi kho đã hết hàng, cam kết giao bù ngay khi có đợt hàng mới. |
| **Lost Sale** | Đơn hàng bị mất vĩnh viễn | Khách hàng hủy đơn bỏ đi khi thấy hết hàng (doanh nghiệp mất hoàn toàn doanh thu và lợi nhuận). |
| **Price Breakpoint ($q_i$)** | Điểm phá vỡ giá | Mức số lượng đặt hàng tối thiểu bắt đầu được áp dụng khung đơn giá ưu đãi rẻ hơn. |
| **Economic Production Quantity (EPQ)** | Cỡ lô sản xuất kinh tế | Quy mô lô chạy máy tối ưu trong điều kiện bổ sung dần dần với tốc độ hữu hạn. |
| **Production Run Time ($t_p$)** | Thời gian chạy một đợt máy | Khoảng thời gian phân xưởng vận hành liên tục để sản xuất đủ một lô $Q$: $t_p = Q/p$. |
| **Idle Run Time ($t_d$)** | Thời gian trống giữa hai đợt | Khoảng thời gian máy móc ngừng sản xuất mặt hàng này và chuyển sang sản phẩm khác: $t_d = I_{\max}/d$. |

---

## 4. Mô hình, Khung lý thuyết & Phương pháp Định lượng (Models & Quantitative Methods)

```mermaid
graph TD
    subgraph EPQDiagram["Chu Kỳ Bổ Sung Dần (SOCA Case Study: EPQ Model)"]
        direction TB
        Start["Bắt đầu sản xuất (t = 0)"] -->|Tốc độ tích lũy ròng (p - d)| Peak["Tồn kho cực đại Imax = Q(1 - d/p)"]
        Peak -->|Ngừng máy: Tiêu thụ thuần túy (-d)| Zero["Hết hàng (Kho chạm đáy = 0)"]
        Zero --> Start
    end
```

### 4.1 Biến thể 1: Công thức Thiếu hàng Có Kế hoạch (Backorders)
- Gọi $S$ là mức thiếu hụt tối đa cho phép vào cuối chu kỳ.
- Tồn kho cực đại: $I_{\max} = Q - S$.
- Tồn kho bình quân dương: $I_{\text{avg}} = \frac{(Q - S)^2}{2Q}$.
- Lượng thiếu hàng bình quân: $S_{\text{avg}} = \frac{S^2}{2Q}$.
- **Hàm Tổng chi phí biến đổi:**
  $$\text{TVC}(Q, S) = K\frac{D}{Q} + h\frac{(Q - S)^2}{2Q} + p\frac{S^2}{2Q}$$
- **Nghiệm tối ưu:**
  $$\mathbf{Q^* = \sqrt{\frac{2KD}{h}} \times \sqrt{\frac{p + h}{p}} = Q^*_{\text{EOQ}} \times \sqrt{\frac{p + h}{p}}}$$
  $$\mathbf{S^* = Q^* \times \left(\frac{h}{p + h}\right)}$$
  $$\mathbf{I_{\max}^* = Q^* - S^* = Q^* \times \left(\frac{p}{p + h}\right)}$$

#### Ứng dụng số liệu Atlantic Coast Tire (ACT):
- $D = 6.000$, $K = \$115$, $h = \$4,20$. Chi phí phạt thiếu hàng: $p = \$7,50/\text{lốp/năm}$.
- Hệ số điều chỉnh thiếu hàng:
  $$\sqrt{\frac{p + h}{p}} = \sqrt{\frac{7,50 + 4,20}{7,50}} = \sqrt{\frac{11,70}{7,50}} = \sqrt{1,56} \approx 1,249$$
- **Cỡ lô tối ưu:**
  $$Q^* = 573,21 \times 1,249 = \mathbf{716\text{ lốp}}$$
- **Lượng thiếu hàng tối đa ($S^*$):**
  $$S^* = 716 \times \left(\frac{4,20}{7,50 + 4,20}\right) = 716 \times \frac{4,20}{11,70} = \mathbf{257\text{ lốp}}$$
- **Tồn kho cực đại thực tế:**
  $$I_{\max}^* = 716 - 257 = \mathbf{459\text{ lốp}}$$
- **Tổng chi phí biến đổi:**
  $$\text{TVC}^* = 115 \frac{6.000}{716} + 4,20 \frac{459^2}{2 \times 716} + 7,50 \frac{257^2}{2 \times 716} = 963,69 + 617,87 + 346,00 = \mathbf{\$1.927,56/\text{năm}}$$
  *(So với EOQ cơ bản \$2.407,48, chính sách cho phép thiếu hàng giúp ACT tiết kiệm thêm **\$479,92/năm**; so với mức ban đầu \$2.790, tiết kiệm tới **\$862,44/năm** tương đương **30,9%**).*

---

### 4.2 Biến thể 2: Thuật toán Chiết khấu Số lượng (Quantity Discounts)
Nhà cung cấp lốp xe đưa ra biểu giá bậc thang cho ACT ($D = 6.000, K = \$115, I = 21\% \implies h = 0,21 \times c$):
- Bậc 1: $0 \le Q < 750 \implies c_1 = \$20,00 \implies h_1 = \$4,20 \implies Q_1^* = 573$ (Khả thi vì $573 < 750$).
- Bậc 2: $750 \le Q < 2.000 \implies c_2 = \$19,80 \implies h_2 = \$4,158 \implies Q_2^* = \sqrt{\frac{2 \times 115 \times 6000}{4,158}} = 576$ (Không khả thi vì $576 < 750$). Bắt buộc phải điều chỉnh về điểm phá vỡ giá: **$Q_2 = 750$**.
- Bậc 3: $Q \ge 2.000 \implies c_3 = \$19,60 \implies h_3 = \$4,116 \implies Q_3^* = 579$ (Không khả thi). Bắt buộc phải điều chỉnh về điểm phá vỡ giá: **$Q_3 = 2.000$**.

#### Bảng so sánh Tổng chi phí toàn diện (Total Cost - TC):
| Khung Chiết Khấu | Kích Cỡ Lô ($Q$) | Đơn Giá ($c$) | Chi Phí Mua ($c \times D$) | Chi Phí Biến Đổi ($\text{TVC}$) | Tổng Chi Phí Toàn Diện ($\text{TC}$) | Kết Luận |
|---|---|---|---|---|---|---|
| **Bậc 1 ($Q < 750$)** | $573$ | \$20,00 | \$120.000,00 | \$2.407,48 | \$122.407,48 | Không chọn |
| **Bậc 2 ($750 \le Q < 2000$)** | **750** | **\$19,80** | **\$118.800,00** | **\$2.479,25** | **\$121.279,25** | **Tối ưu nhất (Chọn)** |
| **Bậc 3 ($Q \ge 2000$)** | $2.000$ | \$19,60 | \$117.600,00 | \$4.461,00 | \$122.061,00 | Bị chi phí lưu kho quá cao làm triệt tiêu lợi thế giá rẻ |

*(Kết luận: Điểm đặt hàng tối ưu là **$Q = 750$ chiếc**, giúp công ty tiết kiệm ròng **\$1.128,23/năm** so với việc mua theo mức EOQ gốc \$20).*

---

### 4.3 Biến thể 3: Bổ sung Dần dần & Tình huống Chuyên sâu SOCA (Case 4)
- Tốc độ tiêu thụ: $d = 1.000\text{ loa/ngày}$.
- Tốc độ sản xuất: $p = 3.000\text{ loa/ngày}$.
- Số ngày làm việc: $250\text{ ngày/năm} \implies D = 250.000\text{ loa/năm}$.
- Chi phí thiết lập máy: $K = \$12.000/\text{lần setup}$.
- Chi phí lưu kho: $h = \$3,60/\text{loa/năm}$.

#### Công thức EPQ:
$$\mathbf{Q^* = \sqrt{\frac{2KD}{h\left(1 - \frac{d}{p}\right)}}}$$

Vì $1 - d/p = 1 - 1.000/3.000 = 2/3$:
$$Q^* = \sqrt{\frac{2 \times 12.000 \times 250.000}{3,60 \times \frac{2}{3}}} = \sqrt{\frac{6.000.000.000}{2,40}} = \sqrt{2.500.000.000} = \mathbf{50.000\text{ loa}}$$

#### So sánh Chính sách Hiện tại ($Q = 30.000$) vs. Tối ưu EPQ ($Q^* = 50.000$):
- **Chính sách hiện tại ($Q = 30.000$):**
  - Số đợt setup: $N = 250.000 / 30.000 = 8,33\text{ lần/năm}$.
  - Chi phí setup: $12.000 \times 8,333 = \mathbf{\$100.000/\text{năm}}$.
  - Tồn kho cực đại: $I_{\max} = 30.000 \times (2/3) = 20.000\text{ loa}$.
  - Tồn kho bình quân: $10.000\text{ loa} \implies \text{Chi phí lưu kho} = 3,60 \times 10.000 = \mathbf{\$36.000/\text{năm}}$.
  - Tổng chi phí biến đổi: $\text{TVC}_{\text{Hiện tại}} = 100.000 + 36.000 = \mathbf{\$136.000/\text{năm}}$.
- **Chính sách tối ưu EPQ ($Q^* = 50.000$):**
  - Số đợt setup: $N^* = 250.000 / 50.000 = \mathbf{5\text{ lần/năm}}$.
  - Chi phí setup: $12.000 \times 5 = \mathbf{\$60.000/\text{năm}}$.
  - Tồn kho cực đại: $I_{\max}^* = 50.000 \times (2/3) = \mathbf{33.333\text{ loa}}$.
  - Tồn kho bình quân: $16.667\text{ loa} \implies \text{Chi phí lưu kho} = 3,60 \times 16.666,67 = \mathbf{\$60.000/\text{năm}}$.
  - Tổng chi phí biến đổi tối ưu: $\text{TVC}^* = 60.000 + 60.000 = \mathbf{\$120.000/\text{năm}}$.
- **Kết quả kinh tế:** Tiết kiệm ròng **\$16.000/năm (giảm 11,76%)**, đồng thời kéo dài thời gian máy móc rảnh rỗi giữa 2 đợt chạy từ $20\text{ ngày}$ lên tới **$33,33\text{ ngày}$**, tạo dư địa rất lớn cho việc sản xuất các linh kiện khác.

---

## 5. Quy trình Nghiệp vụ (Business Processes)

```mermaid
flowchart TD
    A["Kiểm tra nguồn gốc hàng bổ sung"] --> B{"Tự sản xuất hay Mua ngoài?"}
    B -->|Tự sản xuất nội bộ| C["Mô hình EPQ: Xác định tốc độ p & d<br/>Tính Q* = sqrt(2KD / [h(1 - d/p)])"]
    B -->|Mua ngoài từ Vendor| D{"Có chiết khấu theo số lượng không?"}
    D -->|Có biểu giá chiết khấu| E["Thuật toán Chiết khấu:<br/>Tính EOQ từng bậc & Kiểm tra Breakpoint"]
    D -->|Không chiết khấu| F{"Khách hàng có chấp nhận Backorder?"}
    F -->|Có chấp nhận thiếu hàng| G["Mô hình Backorder:<br/>Tính Q* = Q_eoq * sqrt((p+h)/p)"]
    F -->|Không chấp nhận| H["Mô hình EOQ cơ bản"]
    C --> I["Thiết lập tham số Lot Size trên ERP Master Data"]
    E --> I
    G --> I
    H --> I
```

---

## 6. Minh họa Trực quan (Visual Learning)

```mermaid
classDiagram
    class InventoryModel {
        +double annual_demand_D
        +double setup_cost_K
        +double holding_cost_h
        +calculate_optimal_lot()
    }
    class BasicEOQ {
        +calculate_eoq()
    }
    class BackorderEOQ {
        +double shortage_cost_p
        +calculate_max_backorder()
    }
    class QuantityDiscountEOQ {
        +List price_tiers
        +evaluate_breakpoints()
    }
    class EPQModel {
        +double production_rate_p
        +double daily_demand_d
        +calculate_epq()
        +get_production_duration()
    }
    InventoryModel <|-- BasicEOQ
    InventoryModel <|-- BackorderEOQ
    InventoryModel <|-- QuantityDiscountEOQ
    InventoryModel <|-- EPQModel
```

---

## 7. Ví dụ Thực tế Doanh nghiệp (Practical Business Examples)

### 7.1 Tình huống Thực tế: Công ty Nhựa Rạng Đông
Nhà máy ép nhựa tự gia công nắp chai nước ngọt cho Pepsi với tốc độ đùn ép của máy là 20.000 nắp/ngày ($p$). Dây chuyền chiết rót của khách hàng tiêu thụ 5.000 nắp/ngày ($d$). Chi phí mỗi lần thay khuôn dập ($K$) là 8.000.000 VNĐ. Chi phí lưu kho $h$ là 200 VNĐ/nắp/năm. Nếu áp dụng công thức EOQ thông thường bỏ qua yếu tố bổ sung dần, doanh nghiệp sẽ tính sai kích cỡ lô và đánh giá quá cao diện tích kho cần thiết, dẫn đến việc thuê thừa mặt bằng kho chứa bên ngoài.

---

## 8. Ứng dụng trong Hệ thống ERP (ERP Applications)

- **Cấu hình Bậc giá Chiết khấu trong SAP MM:**
  - Giao dịch `ME11` / `ME12` (Purchasing Info Record - PIR): Cấu hình bảng điều kiện giá `Scales` (Condition Type `PB00`). Hệ thống sẽ tự động đối chiếu số lượng trên Purchase Order với các ngưỡng Breakpoint để áp mức đơn giá ưu đãi rẻ nhất.
- **Cấu hình Đơn hàng Nợ (Backorder Processing - BOP) trong SAP SD/aATP:**
  - Chức năng Advanced Available-to-Promise (aATP): Cho phép phân loại đơn hàng theo các mức ưu tiên `Win`, `Gain`, `Redistribute`, `Fill`, `Lose` để tự động gán hàng mới về bù đắp cho các đơn Backorder tồn đọng theo thuật toán đã định trước.

---

## 9. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (Business Analyst Perspective)

### 9.1 Yêu cầu Chức năng (Functional Requirements - FR)
- `FR-EPQ-01`: Hệ thống PHẢI hỗ trợ lưu trữ tốc độ sản xuất danh định ($p$) trên Work Center Master và tự động tính toán hệ số bù trừ $(1 - d/p)$ khi chạy quy tắc định cỡ lô sản xuất EPQ.
- `FR-QD-01`: Khi tạo Purchase Order, hệ thống PHẢI hiển thị thông báo gợi ý (Pop-up Advice) cho Buyer nếu chỉ cần mua thêm một lượng nhỏ hàng hóa để chạm ngưỡng Breakpoint được giảm giá.

### 9.2 Quy tắc Nghiệp vụ (Business Rules - BR)
- `BR-BO-01`: Chỉ cho phép cấu hình tính năng thiếu hàng Backorder cho các nhóm khách hàng chiến lược thuộc Hạng A có ký phụ lục thỏa thuận chấp nhận thời gian chờ; không áp dụng cho khách hàng vãng lai.
- `BR-EPQ-01`: Kích cỡ lô sản xuất $Q$ tính theo EPQ không được vượt quá dung tích vật lý tối đa của khu vực đệm đầu chuyền lắp ráp ($I_{\max} \le \text{Storage Bin Limit}$).

### 9.3 Tiêu chí Nghiệm thu (UAT Acceptance Criteria)
- **Kịch bản:** Kiểm thử gợi ý chiết khấu số lượng cho nhà cung cấp ACT.
  - *Given* Buyer tạo đơn mua hàng số lượng 720 chiếc lốp với đơn giá \$20.
  - *When* Nhấn nút "Kiểm tra Tối ưu Giá" (Price Check).
  - *Then* Hệ thống hiển thị cảnh báo: *"Nếu tăng số lượng lên 750 chiếc, đơn giá giảm còn \$19,80; tổng giá trị đơn hàng tiết kiệm được \$850; bạn có muốn cập nhật số lượng không?"*

---

## 10. Phân tích Phản biện & Đánh đổi Chiến lược (Critical Analysis)

- **Cái bẫy của Chiết khấu Số lượng (The Bulk Purchase Trap):** Nhiều nhà quản lý mua hàng thường bị mê hoặc bởi mức đơn giá rẻ ở các bậc chiết khấu lớn mà quên mất rằng hàng hóa dư thừa sẽ chiếm dụng vốn lưu động (Working Capital) và làm phát sinh chi phí kho bãi khổng lồ, thậm chí dẫn đến nguy cơ hàng bị biến chất hoặc hết hạn sử dụng (Obsolescence). Bảng so sánh của ACT chứng minh tại sao bậc 3 ($Q = 2.000$) tuy giá rẻ nhất (\$19,60) nhưng lại có tổng chi phí cao hơn bậc 2 (\$19,80).
- **Rủi ro niềm tin khách hàng trong Mô hình Backorder:** Mặc dù về mặt toán học, chấp nhận nợ hàng giúp tiết kiệm chi phí, nhưng trong thời đại thương mại điện tử cạnh tranh khốc liệt, khách hàng có thể hủy đơn và không bao giờ quay lại nếu phải chờ đợi. Chi phí thiếu hàng vô hình (Reputational Loss) luôn lớn hơn rất nhiều so với con số ước lượng trên sổ sách kế toán.

---

## 11. Tóm tắt Chương học (Chapter Summary)
1. Mô hình thiếu hàng có kế hoạch giúp giảm mức tồn kho đỉnh ($I_{\max} = Q - S$), tiết kiệm chi phí lưu kho khi chi phí phạt $p$ không quá lớn.
2. Mô hình chiết khấu số lượng đòi hỏi phải so sánh Tổng chi phí toàn diện (TC) bao gồm cả giá trị mua hàng tại các điểm phá vỡ giá (Breakpoints).
3. Mô hình bổ sung dần (EPQ) phản ánh chân thực môi trường tự chế tạo; tình huống SOCA minh chứng việc tăng lô hàng lên $50.000$ chiếc giúp cân bằng hoàn hảo chi phí thiết lập và lưu kho ở mức \$60.000, tiết kiệm \$16.000/năm.
4. Chuyên viên BA cần khéo léo kết hợp các điều kiện ràng buộc thương mại và kỹ thuật vào Master Data của hệ thống ERP để bảo vệ doanh nghiệp khỏi các quyết định mua sắm hoặc sản xuất thiếu căn cứ khoa học.

---

## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Trong mô hình bổ sung dần (EPQ - Gradual Replenishment), tại sao mức tồn kho cực đại ($I_{\max}$) luôn nhỏ hơn kích cỡ lô sản xuất ($Q$)?
   - A. Do hàng bị hao hụt và hỏng hóc trong quá trình gia công.
   - B. Do trong suốt thời gian dây chuyền đang chạy sản xuất để tạo ra lô $Q$, hàng hóa thành phẩm cũng đồng thời liên tục bị rút ra để tiêu thụ.
   - C. Do nhà xưởng không có đủ chỗ chứa.
   - D. Do công nhân đình công giữa ca.
   - *Đáp án đúng:* **B**.

2. **Câu hỏi:** Trong tình huống Atlantic Coast Tire (ACT) áp dụng chính sách chiết khấu số lượng, tại sao phương án đặt $Q = 2.000$ chiếc với đơn giá rẻ nhất (\$19,60) lại không được lựa chọn làm điểm tối ưu?
   - A. Vì nhà cung cấp không đủ năng lực giao 2.000 chiếc.
   - B. Vì chi phí lưu kho phát sinh do ôm lượng hàng tồn khổng lồ (\$4.461) đã vượt trội và triệt tiêu hoàn toàn khoản tiết kiệm được từ việc giảm giá mua.
   - C. Vì lốp xe bị hết hạn sau 1 tháng.
   - D. Vì hệ thống ERP không cho phép nhập số lượng trên 1.000.
   - *Đáp án đúng:* **B**.
"""

with open("outputs/content/chapters/CHAP_05.md", "w", encoding="utf-8") as f:
    f.write(chap5_content)

print("Saved outputs/content/chapters/CHAP_05.md")
