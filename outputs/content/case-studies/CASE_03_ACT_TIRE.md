# CASE STUDY 03: THE ATLANTIC COAST TIRE CORP. (ACT) PROBLEM
## Comprehensive Bilingual Case Study & Business Analysis

---

## 1. Case Overview

- **Case Identifier**: `CASE-03`
- **Official Title**: The Atlantic Coast Tire Corp. (ACT) Problem
- **Academic Source**: Course *ERP Applied to Logistics & SCM*, UEH School of International Business and Marketing (Week 3 Groupwork Practice).
- **Industry**: Automotive Wholesale Tire Distribution & Aftermarket Supply Chain.
- **Core Optimization Models**:
  - Scientific Inventory Management & Trade-off Analysis.
  - Basic Economic Order Quantity (EOQ) with Reorder Point (ROP).
  - EOQ Model with Planned Shortages (Backorders).
  - EOQ Model with Quantity Discounts (Price Break Optimization).
- **Key Decision**: Resolving a classic interdepartmental conflict between the Sales Manager (who advocates large buffer stocks to ensure high fulfillment) and the Finance Director (who demands aggressive stock cuts to release working capital), establishing mathematically optimal ordering policies for high-volume tire model **185/70 R13**.

---

## 2. Complete Original English Case (Unabridged)

### Practice for Group Work Week 3
#### Case 3 – The Atlantic Coast Tire Corp. (ACT) Problem

The Atlantic Coast Tire Corporation (ACT) is a wholesale distributor of a line of automobile tires. It maintains a warehouse that stocks a dozen different sizes of tires. It makes shipments continually to retail dealers. The shipments to the warehouse to replenish the stock of tires are made as needed from the manufacturing plant of the tire manufacturer (Eversafe). When an order is placed by ACT with Eversafe, the tires are delivered in an average of nine working days.

ACT has had a continuing dispute between its sales manager and its finance manager. The sales manager argues that a large inventory of tires should be kept on hand in the warehouse to minimize the risk of having a tire size out of stock when an order is received from a retail dealer. On the other hand, the finance manager argues that the inventory level should be kept as low as possible to reduce the capital tied up in inventory.

Management has decided to resolve this dispute by undertaking a scientific study to determine how much inventory should be kept on hand. The study will focus initially on one of the popular tire sizes, the 185/70 R13 size tire. Because the pattern of sales for this tire is quite regular throughout the year, the study will assume that the demand rate is constant at 500 tires per month, which works out to 6,000 tires per year.

The current policy is to order 1,000 tires of this size from Eversafe once every two months. The question is whether 1,000 is the right amount for the order quantity. Cutting this number down somewhat would reduce the average inventory level by a proportional amount, but at the cost of increasing the frequency of placing orders. What the order quantity should be will depend on the various cost factors. Therefore, ACT now turn their attention to estimating the values of these various costs.

One major cost associated with maintaining the inventory of 185/70 R13 size tires is ACT’s cost for purchasing the tires. Eversafe charges ACT $20 per tire.

In addition to this purchase price, ACT incurs some additional administrative costs each time it places an order with Eversafe. A purchase order must be initiated and processed. The shipment must be received, placed into storage, and recorded in the computerized information processing system that monitors the status of the inventory. Then the payment to Eversafe must be processed.

All these steps triggered by placing an order require a significant amount of time from various employees of ACT. The labor charges (including both wages and benefits) average $15 per hour, and that approximately six hours of labor are associated with placing an order, resulting in a labor cost of $90. In addition to these direct labor charges, there also are associated overhead costs (supervision, office space, etc.), which are estimated to be $25. The sum of these two figures is $115.

When ACT receives a shipment of tires from Eversafe, there are a number of additional costs associated with holding these tires in inventory until they are sold. The most important of these costs are the cost of capital tied up in inventory. For example, suppose that there currently are 1,000 of the 185/70 R13 tires in inventory. The purchase of these 1,000 tires required an expenditure of 1,000 ($20) = $20,000 (plus a bit more in administrative costs), and this money will not be regained until the tires are sold. If this capital of $20,000 were not tied up in these tires, ACT would have other opportunities to use the money that would earn an attractive return. The finance manager estimates that the capital could earn approximately a 15% return per year.

There also are other holding costs associated with storing the tires in the warehouse, including the cost of warehouse space, property insurance, property taxes, and the risk of theft and degradation. The finance manager estimates that the holding costs per tire per year, other than the cost of capital, are approximately 6% of the purchase price. Thus, the total holding cost rate per tire per year is estimated to be 15% + 6% = 21% of the purchase price, or $4.20 per tire per year.

Another consideration is that occasionally orders from retail dealers cannot be filled immediately because the warehouse has run out of tires of that size. The sales manager points out that this causes customer dissatisfaction and may result in lost future sales. If customers are willing to wait, ACT must expedite the order from Eversafe, incurring additional communication, handling, and goodwill compensation costs. ACT estimates that the cost of being out of stock (shortage cost) is approximately $7.50 per tire short per year.

Finally, Eversafe has recently announced a quantity discount pricing schedule to encourage larger orders:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Discount Category</th>
      <th>Order Quantity</th>
      <th>Discount Rate</th>
      <th>Unit Price ($/tire)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 (Standard)</td>
      <td>0 to 749</td>
      <td>0%</td>
      <td>$20.00</td>
    </tr>
    <tr>
      <td>2</td>
      <td>750 to 1,999</td>
      <td>1%</td>
      <td>$19.80</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2,000 or more</td>
      <td>2%</td>
      <td>$19.60</td>
    </tr>
  </tbody>
</table>
</div>

#### Questions
1. When a wholesaler (like ACT) places an order for goods, what can cause the cost to exceed the purchase price?
2. What are the cost components of ACT inventory model?
3. Calculate the optimal order quantity $Q^*$ and Total Variable Cost (TVC) under the basic EOQ model.
4. Calculate the Reorder Point (ROP).
5. If planned shortages are allowed, calculate the optimal order quantity $Q^*$, maximum shortage $S^*$, and resulting TVC.
6. What order quantity should ACT adopt under Eversafe's quantity discount pricing schedule?

---

## 3. Complete Faithful Vietnamese Translation (Bản Dịch Tiếng Việt Đầy Đủ)

### Bài Tập Thực Hành Nhóm Tuần 3
#### Tình huống 3 – BÀI TOÁN CÔNG TY LỐP XE BỜ ĐÔNG (ACT)

Tập đoàn Lốp xe Bờ Đông (The Atlantic Coast Tire Corporation - ACT) là một nhà phân phối bán buôn một dòng lốp xe ô tô. Công ty duy trì một nhà kho lưu trữ hàng tá kích cỡ lốp xe khác nhau và thực hiện các chuyến hàng xuất kho liên tục đến các đại lý bán lẻ. Các lô hàng nhập kho để bổ sung lượng lốp tồn trữ được thực hiện khi có nhu cầu từ nhà máy sản xuất của hãng sản xuất lốp Eversafe. Khi một đơn đặt hàng được ACT phát hành đến Eversafe, lốp xe sẽ được giao tới kho trong thời gian trung bình chín ngày làm việc.

ACT từ lâu đã xuất hiện một cuộc tranh cãi dai dẳng giữa giám đốc bán hàng (Sales Manager) và giám đốc tài chính (Finance Manager). Giám đốc bán hàng lập luận rằng công ty nên duy trì một lượng tồn kho lốp xe lớn trong kho để giảm thiểu rủi ro hết một kích cỡ lốp nào đó khi nhận được đơn đặt hàng từ một đại lý bán lẻ. Ngược lại, giám đốc tài chính lại lập luận rằng mức tồn kho nên được duy trì ở mức thấp nhất có thể để giảm lượng vốn bị ứ đọng trong hàng tồn kho.

Ban giám đốc đã quyết định giải quyết tranh chấp này bằng cách thực hiện một nghiên cứu khoa học để xác định lượng hàng tồn kho nên duy trì trong kho là bao nhiêu. Nghiên cứu ban đầu sẽ tập trung vào một trong những kích cỡ lốp phổ biến nhất: lốp cỡ 185/70 R13. Do mô hình tiêu thụ của kích cỡ lốp này diễn ra rất đều đặn trong suốt cả năm, nghiên cứu sẽ giả định rằng tốc độ nhu cầu là không đổi ở mức 500 chiếc lốp mỗi tháng, tương đương 6.000 chiếc lốp mỗi năm.

Chính sách hiện tại của công ty là đặt 1.000 chiếc lốp kích cỡ này từ Eversafe định kỳ hai tháng một lần. Câu hỏi đặt ra là liệu 1.000 chiếc có phải là quy mô đặt hàng phù hợp hay không. Giảm bớt con số này sẽ giúp giảm mức tồn kho bình quân theo tỷ lệ thuận tương ứng, nhưng đổi lại phải trả giá bằng việc gia tăng tần suất đặt hàng. Quy mô đơn hàng nên là bao nhiêu sẽ phụ thuộc vào các yếu tố chi phí khác nhau. Do đó, ACT hiện chuyển hướng chú ý sang việc ước tính giá trị của các khoản chi phí này.

Một khoản chi phí lớn liên quan đến việc duy trì tồn kho lốp cỡ 185/70 R13 là chi phí mua lốp của ACT. Hãng Eversafe tính giá bán cho ACT là $20 cho mỗi chiếc lốp.

Ngoài giá mua hàng này, ACT phát sinh thêm một số chi phí hành chính mỗi khi đặt một đơn hàng với Eversafe. Một đơn đặt hàng mua (PO) phải được khởi tạo và xử lý. Lô hàng khi chuyển đến phải được tiếp nhận, bốc dỡ vào kho, và ghi nhận vào hệ thống thông tin máy tính quản lý trạng thái tồn kho. Sau đó, thủ tục thanh toán tiền hàng cho Eversafe phải được xử lý.

Tất cả các bước phát sinh từ việc đặt một đơn hàng đều đòi hỏi một lượng thời gian đáng kể từ nhiều nhân viên của ACT. Chi phí nhân công (bao gồm cả tiền lương và phúc lợi) bình quân là $15 mỗi giờ, và có khoảng sáu giờ lao động gắn liền với việc xử lý một đơn đặt hàng, dẫn đến chi phí nhân công là $90. Ngoài các chi phí lao động trực tiếp này, còn có các chi phí quản lý gián tiếp liên quan (giám sát, không gian văn phòng, v.v.), ước tính là $25. Tổng của hai con số này là $115 cho mỗi lần đặt hàng.

Khi ACT tiếp nhận một lô hàng lốp xe từ Eversafe, có một số chi phí bổ sung liên quan đến việc lưu trữ những chiếc lốp này trong kho cho đến khi chúng được bán đi. Quan trọng nhất trong số các chi phí này là chi phí cơ hội của vốn bị ứ đọng trong tồn kho. Ví dụ, giả sử hiện có 1.000 chiếc lốp cỡ 185/70 R13 trong kho. Việc mua 1.000 chiếc lốp này đòi hỏi khoản chi tiêu là 1.000 &times; $20 = $20.000 (cộng thêm một ít chi phí hành chính), và số tiền này sẽ không thể thu hồi cho đến khi lốp được bán hết. Nếu số vốn $20.000 này không bị chôn chặt trong lốp xe, ACT sẽ có các cơ hội khác để sử dụng tiền nhằm kiếm được mức sinh lời hấp dẫn. Giám đốc tài chính ước tính rằng số vốn này có thể kiếm được lợi nhuận xấp xỉ 15% mỗi năm.

Ngoài ra còn có các chi phí lưu kho khác liên quan đến việc chứa lốp trong kho, bao gồm chi phí thuê mặt bằng kho, bảo hiểm tài sản, thuế tài sản, và nguy cơ mất cắp hoặc suy giảm phẩm chất lốp. Giám đốc tài chính ước tính rằng các chi phí lưu kho này (ngoài chi phí vốn) xấp xỉ 6% giá mua lốp. Do đó, tổng tỷ lệ chi phí lưu kho hàng năm ước tính là 15% + 6% = 21% giá mua, tương đương $4.20 cho mỗi chiếc lốp mỗi năm.

Một cân nhắc khác là đôi khi các đơn hàng từ đại lý bán lẻ không thể được đáp ứng ngay lập tức vì nhà kho đã hết sạch lốp cỡ đó. Giám đốc bán hàng chỉ ra rằng điều này gây ra sự không hài lòng cho khách hàng và có thể dẫn đến mất doanh số trong tương lai. Nếu khách hàng chấp nhận chờ, ACT phải xử lý đơn hàng hỏa tốc từ Eversafe, phát sinh thêm chi phí liên lạc, chiết khấu giữ chân khách hàng. ACT ước tính tổn thất do thiếu hàng (chi phí thiếu hụt) xấp xỉ $7.50 cho mỗi chiếc lốp nợ mỗi năm.

Cuối cùng, Eversafe gần đây đã công bố biểu giá chiết khấu theo số lượng để khuyến khích đặt các đơn hàng quy mô lớn hơn:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Phân Loại Chiết Khấu</th>
      <th>Quy Mô Đơn Hàng (Chiếc lốp)</th>
      <th>Tỷ Lệ Chiết Khấu</th>
      <th>Đơn Giá Mua ($/chiếc lốp)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hạng 1 (Tiêu chuẩn)</td>
      <td>0 đến 749</td>
      <td>0%</td>
      <td>$20.00</td>
    </tr>
    <tr>
      <td>Hạng 2</td>
      <td>750 đến 1.999</td>
      <td>1%</td>
      <td>$19.80</td>
    </tr>
    <tr>
      <td>Hạng 3</td>
      <td>2.000 trở lên</td>
      <td>2%</td>
      <td>$19.60</td>
    </tr>
  </tbody>
</table>
</div>

#### Câu hỏi yêu cầu
1. Khi một nhà bán buôn (như ACT) đặt hàng, điều gì có thể khiến chi phí vượt quá giá mua hàng đơn thuần?
2. Những thành phần chi phí nào cấu thành mô hình quản trị tồn kho của ACT?
3. Tính lượng đặt hàng kinh tế tối ưu $Q^*$ và Tổng Chi phí Biến đổi (TVC) theo mô hình EOQ cơ bản.
4. Tính Điểm Đặt Hàng Lại (ROP).
5. Nếu cho phép thiếu hàng có kế hoạch (Planned Shortages), hãy tính cỡ lô tối ưu $Q^*$, lượng thiếu hụt cực đại $S^*$, và TVC tương ứng.
6. ACT nên áp dụng quy mô đặt hàng nào theo biểu giá chiết khấu số lượng của Eversafe?

---

## 4. Supporting Visual Inventory Frameworks

### Đồ thị Răng cưa Tồn kho So sánh Chính sách Cũ ($Q=1000$) vs EOQ Tối ưu ($Q^*=573$)

```text
Mức tồn kho
  ^
  |  [Chính sách cũ Q=1000]
1000|   /|          /|          /|
    |  / |         / |         / |      Tồn kho bình quân cũ = 500 lốp
 573| /  | [EOQ Q* = 573]      / |
    |/   | /|  /|  /|  /|  /| /  |      Tồn kho bình quân EOQ = 286.5 lốp (Giảm 42.7%)
 180|----+--+--+--+--+--+--+--+--+---> [Điểm đặt hàng lại ROP = 180 lốp]
   0+----+-----+-----+-----+-----+-----> Thời gian (ngày)
    <--- Lead Time = 9 ngày --->
```

---

## 5. Comprehensive Quantitative Solutions across All Variations

### 5.1 So sánh 4 Chính sách Quản trị Tồn kho của ACT

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Chính Sách Hoạch Định</th>
      <th>Cỡ Lô Đặt ($Q$)</th>
      <th>Số Lần Đặt ($N$)</th>
      <th>Tồn Kho Cực Đại</th>
      <th>Tồn Kho Bình Quân</th>
      <th>Chi Phí Biến Đổi (TVC)</th>
      <th>Tổng Chi Phí Toàn Phần (TC)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Chính sách cũ (Heuristic)</strong></td>
      <td>1.000 lốp</td>
      <td>6,0 lần/năm</td>
      <td>1.000 lốp</td>
      <td>500,0 lốp</td>
      <td>$2.790,00</td>
      <td>$122.790,00</td>
    </tr>
    <tr>
      <td><strong>2. EOQ Cơ bản (Wilson)</strong></td>
      <td>573 lốp</td>
      <td>10,47 lần/năm</td>
      <td>573 lốp</td>
      <td>286,5 lốp</td>
      <td>$2.407,49</td>
      <td>$122.407,49</td>
    </tr>
    <tr>
      <td><strong>3. Cho phép Thiếu hàng ($p=\$7.5$)</strong></td>
      <td>716 lốp</td>
      <td>8,38 lần/năm</td>
      <td>459 lốp ($S=257$)</td>
      <td>147,1 lốp</td>
      <td>$1.927,56</td>
      <td>$121.927,56</td>
    </tr>
    <tr style="background: rgba(184, 115, 126, 0.12); font-weight: bold;">
      <td><strong>4. Chiết khấu Số lượng (Tại breakpoint)</strong></td>
      <td>750 lốp</td>
      <td>8,0 lần/năm</td>
      <td>750 lốp</td>
      <td>375,0 lốp</td>
      <td>$2.479,25</td>
      <td><strong>$121.279,25 (TỐI ƯU TOÀN DIỆN)</strong></td>
    </tr>
  </tbody>
</table>
</div>

### 5.2 Phân tích Điểm Đặt Hàng Lại (ROP)
$$\text{ROP} = d \times L = \left(\frac{6.000\text{ lốp}}{250\text{ ngày}}\right) \times 9\text{ ngày} = 24\text{ lốp/ngày} \times 9\text{ ngày} = \mathbf{180\text{ chiếc lốp}}$$
Khi lượng tồn kho khả dụng chạm mốc 180 lốp, hệ thống ERP sẽ tự động kích hoạt tạo đơn mua hàng mới.

---

## 6. Business Analyst (BA) Practical Implementation Guide

### 6.1 Cấu hình Thông số Tồn kho trong SAP S/4HANA (Module MM)
1. **Material Master (MM02) - Views MRP 1 & MRP 2**:
   - `MRP Type`: Thiết lập là **VB** (Manual Reorder Point Planning) hoặc **VM** (Automatic ROP).
   - `Reorder Point`: Nhập giá trị **180 EA**.
   - `Lot Sizing Procedure`: Chọn **FX** (Fixed Order Quantity) với `Fixed Lot Size` = **750 EA**.
   - `Planned Delivery Time`: Cấu hình **9 Days** (Lead Time).
2. **Purchasing Info Record (ME11) - Biểu giá Chiết khấu**:
   - Cấu hình điều kiện giá `PB00` trong Scales:
     - Từ 1 đến 749 lốp: Đơn giá $20.00.
     - Từ 750 đến 1.999 lốp: Đơn giá $19.80.
     - Từ 2.000 lốp trở lên: Đơn giá $19.60.
3. **Cơ chế Kiểm soát Hóa đơn 3-Way Match (MIRO)**:
   - Hệ thống tự động so sánh đơn giá trên Purchase Order, số lượng trên Goods Receipt và số tiền trên Hóa đơn vendor để bảo vệ dòng tiền.
