import os

chap4_content = r"""# CHƯƠNG 04: QUẢN TRỊ TỒN KHO KHOA HỌC & MÔ HÌNH EOQ CƠ BẢN
## CHAPTER 04: SCIENTIFIC INVENTORY MANAGEMENT & THE CLASSICAL EOQ MODEL

---

## 1. Tổng quan Chương học (Chapter Overview)

### 1.1 Giới thiệu bối cảnh (Introduction)
Hàng tồn kho (Inventory) là một trong những tài sản lưu động lớn nhất trên bảng cân đối kế toán của mọi doanh nghiệp sản xuất và phân phối, thường chiếm từ **20% đến 40% tổng tài sản**. Tuy nhiên, quản trị tồn kho là một bài toán mâu thuẫn quyền lợi nội bộ gay gắt:
- **Bộ phận Bán hàng (Sales):** Muốn tồn kho thật nhiều để không bao giờ bị thiếu hàng (Zero Stockout), tối đa hóa doanh thu và mức độ dịch vụ khách hàng.
- **Bộ phận Sản xuất (Production):** Muốn sản xuất theo các lô thật lớn để giảm tần suất thay đổi khuôn mẫu, tối ưu hóa năng suất máy móc.
- **Bộ phận Tài chính (Finance):** Muốn ép tồn kho xuống mức tối thiểu (Zero Inventory / Just-in-Time) để giải phóng dòng tiền lưu động và cắt giảm chi phí lãi vay ngân hàng.

Để hóa giải mâu thuẫn này, các phương pháp **Quản trị Tồn kho Khoa học (Scientific Inventory Management)** ra đời. Chương này tập trung vào lý thuyết nền tảng kinh điển nhất: **Mô hình Quy mô Đơn hàng Kinh tế (Economic Order Quantity - EOQ)** của Ford W. Harris (thường gọi là công thức Wilson), phân tích cơ chế đánh đổi giữa chi phí đặt hàng và chi phí lưu kho, xây dựng công thức toán học và kiểm chứng qua tình huống kinh điển của **Tập đoàn Lốp xe Atlantic Coast Tire (ACT)**.

### 1.2 Mục tiêu học tập (Learning Objectives)
1. **Phân tích 4 thành phần chi phí cơ bản** cấu thành tổng chi phí tồn kho trong doanh nghiệp ($c, K, h, p$).
2. **Chứng minh và dẫn xuất công thức EOQ cơ bản** bằng giải tích vi phân và phân tích đường cong đánh đổi chi phí (Cost Trade-off Curve).
3. **Tính toán các chỉ số vận hành then chốt**: Chu kỳ đặt hàng ($T$), số đơn hàng trong năm ($N$), và Điểm đặt hàng lại (**Reorder Point - ROP**).
4. **Giải quyết bài toán cơ sở của Atlantic Coast Tire (ACT)**, lượng hóa khoản tiết kiệm kinh tế khi chuyển đổi từ trực quan ($Q = 1.000$) sang tối ưu ($Q^* = 573$).
5. **Cài đặt bài toán trên Excel Solver** sử dụng động cơ giải phi tuyến tính **GRG Nonlinear Engine**.
6. **Thiết kế yêu cầu Business Analyst (BA)** để tham số hóa Master Data và tự động hóa đề xuất mua hàng (Purchase Requisition Proposal) trong hệ thống ERP (SAP MM).

### 1.3 Mối quan hệ liên chương (Relationship with Other Chapters)
- Là nền móng lý thuyết bắt buộc cho **Chương 5** (Các biến thể nâng cao: Thiếu hàng có kế hoạch, Chiết khấu số lượng, Bổ sung dần EPQ).
- Đóng vai trò là bài toán đối ứng với bài toán vận tải ở **Chương 1, 2, 3** (khi chi phí vận tải rẻ kích thích đặt lô lớn nhưng làm chi phí lưu kho tăng vọt).
- Kết nối trực tiếp vào luồng quy trình Procure-to-Pay (P2P) và chạy tự động MRP trong ERP tại **Chương 6**.

---

## 2. Các Khái niệm Cốt lõi (Core Concepts)

### 2.1 Bốn Thành phần Chi phí Tồn kho Cơ bản (The Four Cost Components)
Mọi mô hình quản trị tồn kho khoa học đều xây dựng trên 4 cấu phần chi phí:
1. **Chi phí mua hàng / Chi phí sản xuất đơn vị ($c$ - Unit Purchasing / Production Cost):** Giá mua từ nhà cung ứng hoặc chi phí trực tiếp tạo ra 1 đơn vị sản phẩm. Tổng chi phí mua hàng hàng năm là $c \times D$. Trong mô hình EOQ cơ bản không có chiết khấu, giá $c$ là hằng số bất kể quy mô đặt hàng $Q$, do đó là một khoản chi phí cố định (Fixed Baseline).
2. **Chi phí đặt hàng / Chi phí thiết lập máy ($K$ - Ordering / Setup Cost):** Khoản chi phí cố định phát sinh mỗi khi một đơn mua hàng được phát hành hoặc một đợt chạy máy được thiết lập, bất kể số lượng hàng trong đơn là 1 hay 1.000 chiếc. Bao gồm: chi phí hành chính lập PO, kiểm đếm tại cửa kho, chi phí dừng máy vệ sinh và lắp khuôn mới.
3. **Chi phí lưu kho / Chi phí giữ hàng ($h$ - Unit Holding / Carrying Cost):** Chi phí phát sinh để bảo quản, cất giữ 1 đơn vị hàng tồn trong kho trong thời gian 1 năm. Bao gồm: chi phí vốn vay (Cost of Capital / Interest - chiếm 60-70% của $h$), chi phí thuê diện tích kho bãi, điện điều hòa, bảo hiểm cháy nổ, nhân sự thủ kho, rủi ro rơi vỡ, hao hụt và lạc hậu công nghệ. Thường được biểu diễn dưới dạng:
   $$h = I \times c$$
   (với $I$ là tỷ lệ chi phí lưu kho hàng năm, thường từ $15\% - 30\%$).
4. **Chi phí thiếu hàng / Chi phí phạt hết hàng ($p$ - Shortage / Penalty Cost):** Khoản thiệt hại phát sinh khi khách hàng có nhu cầu nhưng kho không có sẵn hàng để phục vụ. Bao gồm: lợi nhuận bị mất do mất đơn hàng, uy tín thương hiệu suy giảm, và các khoản phạt hợp đồng do giao trễ.

### 2.2 Các Giả định Cốt lõi của Mô hình EOQ Cổ điển
Mô hình Wilson EOQ hoạt động dựa trên các giả định lý tưởng hóa:
1. Nhu cầu tiêu thụ hàng năm ($D$) là xác định và liên tục với tốc độ không đổi ($d$ đơn vị/ngày).
2. Thời gian giao hàng (Lead Time - $L$) bằng đúng $0$ hoặc là một hằng số đã biết trước hoàn hảo.
3. Lô hàng được giao và nhập kho toàn bộ trong một thời điểm duy nhất (Instantaneous Replenishment).
4. Không cho phép xảy ra tình trạng thiếu hàng (Zero Shortages Allowed / $p \to \infty$).
5. Giá mua đơn vị ($c$) là hằng số, không có chiết khấu theo số lượng.

---

## 3. Thuật ngữ Kỹ thuật & Phân biệt Khái niệm (Key Terminologies)

| Thuật ngữ Tiếng Anh | Thuật ngữ Tiếng Việt | Định nghĩa & Đặc trưng Bản chất |
|---|---|---|
| **Economic Order Quantity (EOQ)** | Quy mô đơn hàng kinh tế | Kích cỡ lô đặt hàng ($Q^*$) giúp cực tiểu hóa tổng chi phí biến đổi tồn kho hàng năm. |
| **Total Variable Cost (TVC)** | Tổng chi phí biến đổi | Tổng của chi phí đặt hàng hàng năm và chi phí lưu kho hàng năm: $\text{TVC} = \text{Setup} + \text{Holding}$. |
| **Total Cost (TC)** | Tổng chi phí tồn kho | Bao gồm cả giá trị mua hàng: $\text{TC} = cD + \text{TVC}$. |
| **Reorder Point (ROP)** | Điểm đặt hàng lại | Mức tồn kho kích hoạt việc phát hành đơn hàng mua mới: $\text{ROP} = d \times L + \text{SS}$. |
| **Safety Stock (SS)** | Tồn kho an toàn | Lượng hàng dự phòng đệm để phòng ngừa biến động ngẫu nhiên của nhu cầu và Lead Time. |
| **Lead Time ($L$)** | Thời gian giao hàng | Khoảng thời gian từ khi ký phát đơn hàng PO đến khi hàng thực tế cập cảng và nhập kho. |

---

## 4. Mô hình, Khung lý thuyết & Phương pháp Định lượng (Models & Quantitative Methods)

```mermaid
graph LR
    subgraph Sawtooth["Biểu Đồ Răng Cưa Tồn Kho Cổ Điển (Classic Saw-tooth Pattern)"]
        direction TB
        A["Nhập lô hàng Q (Tồn kho đỉnh = Q)"] -->|Tiêu thụ liên tục với tốc độ d| B["Tồn kho chạm Điểm ROP = d * L"]
        B -->|Hàng trên đường giao (Lead Time L)| C["Tồn kho chạm đáy = 0"]
        C -->|Hàng mới cập bến tức thời| A
    end
```

### 4.1 Dẫn xuất Công thức Toán học Wilson EOQ
Giả sử doanh nghiệp đặt hàng theo từng lô có quy mô $Q$ đơn vị:
- Số đơn đặt hàng cần thực hiện trong 1 năm:
  $$N = \frac{D}{Q}$$
- Chi phí đặt hàng hàng năm (Annual Ordering Cost):
  $$\text{AOC}(Q) = K \times N = K \frac{D}{Q}$$
- Vì lượng hàng tiêu thụ đều đặn từ $Q$ về $0$, mức tồn kho bình quân trong kho là:
  $$I_{\text{avg}} = \frac{Q + 0}{2} = \frac{Q}{2}$$
- Chi phí lưu kho hàng năm (Annual Holding Cost):
  $$\text{AHC}(Q) = h \times I_{\text{avg}} = h \frac{Q}{2}$$
- **Hàm Tổng chi phí biến đổi hàng năm (Total Variable Cost - TVC):**
  $$\text{TVC}(Q) = \text{AOC}(Q) + \text{AHC}(Q) = K \frac{D}{Q} + h \frac{Q}{2}$$

#### Tìm điểm cực tiểu hóa:
Lấy đạo hàm bậc nhất của $\text{TVC}$ theo $Q$ và giải phương trình $\frac{d\text{TVC}}{dQ} = 0$:
$$\frac{d\text{TVC}}{dQ} = -\frac{KD}{Q^2} + \frac{h}{2} = 0 \iff \frac{KD}{Q^2} = \frac{h}{2} \iff Q^2 = \frac{2KD}{h}$$

$$\mathbf{Q^* = \sqrt{\frac{2KD}{h}}}$$

#### Tính chất quan trọng tại điểm tối ưu:
Tại nghiệm tối ưu $Q^*$, **Chi phí đặt hàng hàng năm cân bằng chính xác với Chi phí lưu kho hàng năm**:
$$\text{AOC}(Q^*) = \text{AHC}(Q^*) \iff K\frac{D}{Q^*} = h\frac{Q^*}{2}$$
$$\implies \mathbf{\text{TVC}(Q^*) = 2 \times \text{AHC}(Q^*) = \sqrt{2KDh}}$$

### 4.2 Tình huống Nghiên cứu Thực tế: Atlantic Coast Tire (ACT) - Bài toán Cơ sở
Tập đoàn Atlantic Coast Tire (ACT) phân phối dòng lốp xe du lịch cỡ lớn với các dữ liệu kế toán chi phí thu thập được như sau:
- Nhu cầu khách hàng hàng năm: $D = 6.000\text{ lốp/năm}$ (ổn định).
- Giá mua đơn vị từ nhà sản xuất: $c = \$20,00/\text{chiếc}$.
- Chi phí đặt mỗi đơn hàng: $K = \$115,00/\text{đơn}$.
- Chi phí lưu kho đơn vị hàng năm: $h = \$4,20/\text{chiếc/năm}$ (bao gồm chi phí vốn lãi vay, bảo hiểm và kho bãi).
- Thời gian giao hàng (Lead Time): $L = 7,5\text{ ngày làm việc}$. Quy ước: 250 ngày làm việc/năm.

#### So sánh Chính sách Hiện tại vs. Chính sách EOQ Tối ưu:

1. **Chính sách hiện tại theo thói quen trực giác ($Q = 1.000\text{ lốp}$):**
   - Số đơn hàng/năm: $N = \frac{6.000}{1.000} = 6\text{ đơn/năm}$.
   - Chi phí đặt hàng: $\text{AOC} = 115 \times 6 = \mathbf{\$690,00/\text{năm}}$.
   - Tồn kho bình quân: $I_{\text{avg}} = \frac{1.000}{2} = 500\text{ lốp}$.
   - Chi phí lưu kho: $\text{AHC} = 4,20 \times 500 = \mathbf{\$2.100,00/\text{năm}}$.
   - Tổng chi phí biến đổi: $\text{TVC}_{\text{Hiện tại}} = 690 + 2.100 = \mathbf{\$2.790,00/\text{năm}}$.
   *(Nhận xét: Chi phí lưu kho cao gấp hơn 3 lần chi phí đặt hàng $\implies$ Doanh nghiệp đang ôm đồm tồn kho quá lớn!).*

2. **Chính sách Tối ưu Khoa học ($Q^*$):**
   $$Q^* = \sqrt{\frac{2 \times 115 \times 6.000}{4,20}} = \sqrt{\frac{1.380.000}{4,20}} = \sqrt{328.571,43} \approx \mathbf{573\text{ lốp}}$$
   - Số đơn hàng/năm: $N^* = \frac{6.000}{573,21} = 10,47\text{ đơn/năm}$.
   - Chi phí đặt hàng: $\text{AOC}^* = 115 \times 10,467 = \mathbf{\$1.203,74/\text{năm}}$.
   - Tồn kho bình quân: $I_{\text{avg}}^* = \frac{573,21}{2} = 286,6\text{ lốp}$.
   - Chi phí lưu kho: $\text{AHC}^* = 4,20 \times 286,60 = \mathbf{\$1.203,74/\text{năm}}$.
   - Tổng chi phí biến đổi tối ưu: $\text{TVC}^* = 1.203,74 + 1.203,74 = \mathbf{\$2.407,48/\text{năm}}$.
   
3. **Hiệu quả Kinh tế Đạt được:**
   $$\text{Tiết kiệm hàng năm} = \$2.790,00 - \$2.407,48 = \mathbf{\$382,52/\text{năm}} \quad (\mathbf{\text{Giảm } 13,71\% \text{ chi phí tồn kho}})$$

#### Tính toán Điểm đặt hàng lại (Reorder Point - ROP):
- Tốc độ tiêu thụ hàng ngày:
  $$d = \frac{D}{250\text{ ngày}} = \frac{6.000}{250} = 24\text{ lốp/ngày}$$
- Nhu cầu tiêu thụ trong thời gian Lead Time ($L = 7,5\text{ ngày}$):
  $$\text{Lead Time Demand} = d \times L = 24 \times 7,5 = 180\text{ lốp}$$
- Vì không có biến động, tồn kho an toàn $\text{SS} = 0$.
- **Điểm đặt hàng lại:**
  $$\mathbf{\text{ROP} = 180\text{ lốp}}$$
  *(Ý nghĩa: Khi số lượng lốp trong kho vật lý giảm xuống chạm đúng ngưỡng 180 chiếc, nhân viên mua hàng phải phát hành ngay đơn hàng mới với số lượng $Q^* = 573$ chiếc).*

---

## 5. Quy trình Nghiệp vụ (Business Processes)

```mermaid
sequenceDiagram
    autonumber
    participant Inv as Kho Hàng (Warehouse Inventory)
    participant ERP as Hệ thống ERP (SAP MM / MRP)
    participant Buyer as Nhân viên Mua hàng (Purchaser)
    participant Vendor as Nhà Cung Cấp (Tire Manufacturer)

    Inv->>ERP: Quét xuất kho bán hàng (Goods Issue - Mvt 601)
    ERP->>ERP: Cập nhật tồn khả dụng & Đối chiếu ngưỡng ROP = 180
    alt Tồn kho > 180
        ERP-->>Inv: Trạng thái an toàn - Không hành động
    else Tồn kho <= 180
        ERP->>Buyer: Tự động tạo Purchase Requisition (PR) với Q* = 573
        Buyer->>ERP: Duyệt PR & Chuyển thành Purchase Order (PO)
        ERP->>Vendor: Truyền đơn đặt hàng điện tử (EDI 850)
        Vendor-->>Inv: Giao hàng sau 7.5 ngày (Tồn kho vừa chạm 0)
        Inv->>ERP: Nhập kho (Goods Receipt - Mvt 101) -> Tồn kho tăng lên 573
    end
```

---

## 6. Minh họa Trực quan (Visual Learning)

```mermaid
flowchart TD
    subgraph CostCurve["Đường Cong Chi Phí Đánh Đổi (Trade-off Cost Curve)"]
        direction TB
        C1["Chi phí Lưu kho AHC = h(Q/2) - Tăng tuyến tính"] 
        C2["Chi phí Đặt hàng AOC = K(D/Q) - Giảm hyperbol"]
        C1 --- C3["Giao điểm tại Q* = 573 (Cân bằng chi phí)"]
        C2 --- C3
        C3 --> C4["Đáy cực tiểu TVC* = $2.407,48"]
    end
```

---

## 7. Ví dụ Thực tế Doanh nghiệp (Practical Business Examples)

### 7.1 Tình huống Thực tế: Chuỗi bán lẻ Dược phẩm Pharmacity
Một chuỗi nhà thuốc quản lý mặt hàng thuốc Panadol Extra. Nhu cầu cả hệ thống là 120.000 hộp/năm. Chi phí mỗi lần đặt hàng từ nhà sản xuất Sanofi là 500.000 VNĐ (chi phí kiểm nghiệm, xử lý chứng từ nhập kho GSP). Giá mua mỗi hộp là 30.000 VNĐ, chi phí lưu kho chiếm 18%/năm ($h = 5.400\text{ VNĐ/hộp/năm}$). Nếu đặt theo trực giác mỗi tháng 1 lần ($Q = 10.000$ hộp), tổng chi phí biến đổi là 33.000.000 VNĐ. Áp dụng công thức EOQ:
$$Q^* = \sqrt{\frac{2 \times 500.000 \times 120.000}{5.400}} \approx 4.714\text{ hộp}$$
Số đơn hàng tối ưu tăng lên khoảng 25 đơn/năm, giúp tổng chi phí biến đổi giảm xuống còn 25.455.000 VNĐ, tiết kiệm cho doanh nghiệp hơn 22,8% chi phí tồn trữ.

---

## 8. Ứng dụng trong Hệ thống ERP (ERP Applications)

Trong giải pháp chuẩn **SAP S/4HANA Sourcing and Procurement (MM)**:
- **Cấu hình Material Master Data:**
  - Tab `MRP 1 View`:
    - `MRP Type`: Cấu hình giá trị `VB` (Manual Reorder Point Planning) hoặc `VM` (Automatic Reorder Point Planning).
    - `Lot Size`: Chọn quy tắc `FX` (Fixed Order Quantity) với giá trị cố định $Q^* = 573$, hoặc `HB` (Replenish to Maximum Stock Level).
    - `Reorder Point`: Nhập trực tiếp giá trị $\text{ROP} = 180$.
  - Tab `MRP 2 View`:
    - `Planned Delivery Time`: Nhập thời gian Lead Time là 8 ngày (làm tròn từ 7,5 ngày).
    - `Safety Stock`: Nhập mức tồn kho dự phòng (nếu có biến động).
- **Quy trình chạy tự động MRP:**
  - Giao dịch `MD01N` (MRP Live): Động cơ tính toán quét qua toàn bộ các mã vật tư loại `VB`. Bất cứ khi nào tổng `Tồn kho vật lý + Lượng hàng đang về - Đơn hàng đã cam kết xuất` $\le \text{ROP}$, hệ thống tự động sinh bản ghi `Purchase Requisition (PR)` trong bảng `EBAN` mà không cần con người can thiệp.

---

## 9. Góc nhìn Chuyên viên Phân tích Nghiệp vụ (Business Analyst Perspective)

### 9.1 Yêu cầu Chức năng (Functional Requirements - FR)
- `FR-INV-01`: Hệ thống PHẢI có khả năng tự động tính toán giá trị EOQ tối ưu cho từng mã SKU dựa trên lịch sử tiêu thụ 12 tháng gần nhất và bảng tham số chi phí $K, h$.
- `FR-INV-02`: Hệ thống PHẢI hỗ trợ tính năng làm tròn quy mô đơn hàng (Rounding Value) theo quy cách đóng thùng (Carton Size) hoặc kiện pallet của nhà cung cấp.

### 9.2 Quy tắc Nghiệp vụ (Business Rules - BR)
- `BR-ROP-01`: Nếu một mặt hàng có Lead Time lớn hơn 30 ngày, hệ thống bắt buộc người dùng cấu hình giá trị Safety Stock lớn hơn 0 trước khi cho phép kích hoạt quy tắc đặt hàng ROP.
- `BR-PO-01`: Kích cỡ đặt hàng gợi ý không bao giờ được nhỏ hơn `Minimum Order Quantity (MOQ)` do nhà cung ứng quy định trong Hợp đồng khung (Purchase Info Record - PIR).

### 9.3 Tiêu chí Nghiệm thu (UAT Acceptance Criteria)
- **Kịch bản:** Kiểm thử kích hoạt đề xuất mua hàng tự động theo ROP cho mã lốp ACT-573.
  - *Given* Mặt hàng ACT-573 có ROP = 180, Lot size = 573, và tồn kho hiện tại là 185 chiếc.
  - *When* Xuất kho 10 chiếc cho đơn bán hàng (Tồn kho giảm xuống còn 175 $\le 180$).
  - *Then* Hệ thống tự động tạo 01 Purchase Requisition với số lượng đặt hàng đúng bằng 573 chiếc trong kỳ chạy MRP tiếp theo.

---

## 10. Phân tích Phản biện & Đánh đổi Chiến lược (Critical Analysis)

- **Độ nhạy của công thức EOQ (Robustness of EOQ):** Một đặc tính ưu việt của công thức căn bậc hai Wilson là **tính trơ / tính bền vững trước sai số tham số (Flat Bottom of the Cost Curve)**. Nếu ước tính sai tham số $K$ hoặc $h$ lên tới 20%, tổng chi phí TVC chỉ chênh lệch dưới 2% so với mức tối ưu tuyệt đối. Điều này giúp doanh nghiệp tự tin triển khai EOQ ngay cả khi không thể đo lường chính xác tuyệt đối chi phí đặt hàng.
- **Rủi ro khi áp dụng mù quáng:** Trong bối cảnh sản xuất tinh gọn (Lean / JIT), mục tiêu chiến lược không phải là "chấp nhận chi phí setup $K$ cao để đặt lô lớn $Q$", mà là **đầu tư cải tiến kỹ thuật để giảm thiểu thời gian setup $K \to 0$ (kỹ thuật SMED - Single Minute Exchange of Die)**. Khi $K \to 0$, quy mô lô tối ưu $Q^* \to 0$, đưa doanh nghiệp tiệm cận dòng chảy một sản phẩm (One-piece Flow).

---

## 11. Tóm tắt Chương học (Chapter Summary)
1. Tồn kho khoa học giải quyết mâu thuẫn đánh đổi giữa chi phí đặt hàng (AOC) và chi phí lưu kho (AHC).
2. Công thức Wilson EOQ $Q^* = \sqrt{2KD/h}$ xác định điểm cân bằng chi phí, tại đó tổng chi phí khả biến là nhỏ nhất.
3. Tình huống Atlantic Coast Tire chứng minh việc áp dụng toán học giúp cắt giảm 13,71% chi phí vận hành hàng năm.
4. Điểm đặt hàng lại $\text{ROP} = d \times L$ là cơ chế kích hoạt nền tảng trong các phân hệ quản lý vật tư của mọi hệ thống ERP hiện đại.

---

## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Trong mô hình EOQ cơ bản không có chiết khấu, khi quy mô lô hàng đặt mua ($Q$) tăng lên gấp đôi, chi phí lưu kho hàng năm (AHC) và chi phí đặt hàng hàng năm (AOC) sẽ biến động như thế nào?
   - A. AHC tăng gấp đôi, AOC giảm đi một nửa.
   - B. Cả AHC và AOC đều tăng gấp đôi.
   - C. AHC giảm một nửa, AOC tăng gấp đôi.
   - D. Cả hai chi phí đều không thay đổi.
   - *Đáp án đúng:* **A**. Vì $\text{AHC} = h(Q/2)$ tỷ lệ thuận với $Q$, còn $\text{AOC} = K(D/Q)$ tỷ lệ nghịch với $Q$.

2. **Câu hỏi:** Trong tình huống Atlantic Coast Tire (ACT), nếu tốc độ tiêu thụ là 24 lốp/ngày và thời gian giao hàng là 7,5 ngày làm việc, điểm đặt hàng lại (ROP) là bao nhiêu khi không xét tồn kho an toàn?
   - A. 573 lốp
   - B. 1.000 lốp
   - C. 180 lốp
   - D. 240 lốp
   - *Đáp án đúng:* **C** ($24 \times 7,5 = 180\text{ lốp}$).
"""

with open("outputs/content/chapters/CHAP_04.md", "w", encoding="utf-8") as f:
    f.write(chap4_content)

print("Saved outputs/content/chapters/CHAP_04.md")
