# CASE STUDY 02: ASSIGNING PLANTS TO PRODUCTS
## (BETTER PRODUCTS COMPANY — CASE 2.1 & CASE 2.2)
## Comprehensive Bilingual Case Study & Business Analysis

---

## 1. Case Overview

- **Case Identifier**: `CASE-02`
- **Official Title**: Assigning Plants to Products (Better Products Company)
- **Academic Source**: Course *ERP Applied to Logistics & SCM*, UEH School of International Business and Marketing (Week 2 Groupwork Practice).
- **Industry**: Industrial Equipment & Consumer Products Manufacturing.
- **Core Optimization Models**:
  - **Case 2.1**: Unbalanced Linear Programming Transportation Model with Dummy Destination (Unused Capacity) and Prohibited Routing ($M$-Method).
  - **Case 2.2**: Zero-One Binary Integer Linear Programming / Bipartite Assignment Problem (No Product Splitting permitted).
- **Key Decision**:
  - Case 2.1: Determining the optimal daily production schedule across 3 excess-capacity plants and 4 new products when product splitting across facilities is allowed.
  - Case 2.2: Re-evaluating the production assignment under the strict managerial constraint that product splitting is prohibited (each product made in exactly one plant) to avoid duplicated changeovers.

---

## 2. Complete Original English Case (Unabridged)

### Practice for Group Work Week 2
#### Case 2.1 – ASSIGNING PLANTS TO PRODUCTS (BETTER PRODUCTS COMPANY)

The Better Products Company has decided to initiate the production of four new products, using three plants that currently have excess production capacity. The products require a comparable production effort per unit, so the available production capacity of the plants is measured by the number of units of any product that can be produced per day, as given in the rightmost column of Table case 2.1. The bottom row gives the required production rate (number of units produced per day) to meet projected sales. Each plant can produce any of these products, except that Plant 2 cannot produce Product 3. However, the variable costs per unit of each product differ from plant to plant, as shown in the main body of the table.

Management now needs to make a decision about which plants should produce which products. Product splitting, where the same product is produced in more than one plant, is permitted.

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Unit Cost ($/unit)</th>
      <th>Product 1</th>
      <th>Product 2</th>
      <th>Product 3</th>
      <th>Product 4</th>
      <th>Capacity Available (units/day)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Plant 1</strong></td>
      <td>$41</td>
      <td>$27</td>
      <td>$28</td>
      <td>$24</td>
      <td>75</td>
    </tr>
    <tr>
      <td><strong>Plant 2</strong></td>
      <td>$40</td>
      <td>$29</td>
      <td>Prohibited (—)</td>
      <td>$23</td>
      <td>75</td>
    </tr>
    <tr>
      <td><strong>Plant 3</strong></td>
      <td>$37</td>
      <td>$30</td>
      <td>$27</td>
      <td>$21</td>
      <td>45</td>
    </tr>
    <tr style="background: var(--surface-subtle); font-weight: bold;">
      <td><strong>Production Rate Needed (units/day)</strong></td>
      <td>20</td>
      <td>30</td>
      <td>30</td>
      <td>40</td>
      <td>Total = 195 (Capacity) / 120 (Demand)</td>
    </tr>
  </tbody>
</table>
</div>

Management now wants to determine how much of each product should be produced by each plant to minimize total variable costs.

---

#### Case 2.2 – ASSIGNING PLANTS TO PRODUCTS WITHOUT PRODUCT SPLITTING

Management has decided to prohibit product splitting, so each product is to be assigned to only one plant. The cost of assigning each product to each plant is summarized below:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Total Cost per Day ($/day)</th>
      <th>Product 1 (20 units)</th>
      <th>Product 2 (30 units)</th>
      <th>Product 3 (30 units)</th>
      <th>Product 4 (40 units)</th>
      <th>Max Allowed Products</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Plant 1</strong></td>
      <td>$820 ($41 &times; 20)</td>
      <td>$810 ($27 &times; 30)</td>
      <td>$840 ($28 &times; 30)</td>
      <td>$960 ($24 &times; 40)</td>
      <td>2</td>
    </tr>
    <tr>
      <td><strong>Plant 2</strong></td>
      <td>$800 ($40 &times; 20)</td>
      <td>$870 ($29 &times; 30)</td>
      <td>Prohibited (M)</td>
      <td>$920 ($23 &times; 40)</td>
      <td>1</td>
    </tr>
    <tr>
      <td><strong>Plant 3</strong></td>
      <td>$740 ($37 &times; 20)</td>
      <td>$900 ($30 &times; 30)</td>
      <td>$810 ($27 &times; 30)</td>
      <td>$840 ($21 &times; 40)</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>

Plant 1 has capacity to produce up to two products, while Plant 2 and Plant 3 each have capacity for at most one product. Determine which plant should produce which product to minimize total daily variable production costs.

---

## 3. Complete Faithful Vietnamese Translation (Bản Dịch Tiếng Việt Đầy Đủ)

### Bài Tập Thực Hành Nhóm Tuần 2
#### Tình huống 2.1 – PHÂN CÔNG NHÀ MÁY CHO CÁC SẢN PHẨM (CÔNG TY BETTER PRODUCTS)

Công ty Better Products đã quyết định bắt đầu sản xuất bốn sản phẩm mới, sử dụng ba nhà máy hiện đang có công suất sản xuất dư thừa. Các sản phẩm này đòi hỏi nỗ lực sản xuất trên mỗi đơn vị tương đương nhau, do đó công suất sẵn có của các nhà máy được đo lường bằng số lượng đơn vị của bất kỳ sản phẩm nào có thể được sản xuất mỗi ngày, như được thể hiện ở cột ngoài cùng bên phải của Bảng tình huống 2.1. Hàng dưới cùng thể hiện sản lượng yêu cầu (số lượng sản phẩm cần làm ra mỗi ngày) để đáp ứng dự báo bán hàng. Mỗi nhà máy đều có thể sản xuất bất kỳ sản phẩm nào trong số này, ngoại trừ Nhà máy 2 không thể sản xuất Sản phẩm 3. Tuy nhiên, chi phí biến đổi trên mỗi đơn vị của từng sản phẩm có sự khác biệt giữa các nhà máy, như được chỉ ra trong phần thân chính của bảng.

Ban giám đốc hiện cần đưa ra quyết định về việc nhà máy nào nên sản xuất sản phẩm nào. Việc chia nhỏ sản phẩm (Product splitting), trong đó cùng một sản phẩm được sản xuất tại nhiều hơn một nhà máy, được cho phép thực hiện.

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Chi Phí Biến Đổi ($/sản phẩm)</th>
      <th>Sản Phẩm 1</th>
      <th>Sản Phẩm 2</th>
      <th>Sản Phẩm 3</th>
      <th>Sản Phẩm 4</th>
      <th>Công Suất Khả Dụng (sp/ngày)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nhà máy 1</strong></td>
      <td>$41</td>
      <td>$27</td>
      <td>$28</td>
      <td>$24</td>
      <td>75</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 2</strong></td>
      <td>$40</td>
      <td>$29</td>
      <td>Tuyến cấm (—)</td>
      <td>$23</td>
      <td>75</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 3</strong></td>
      <td>$37</td>
      <td>$30</td>
      <td>$27</td>
      <td>$21</td>
      <td>45</td>
    </tr>
    <tr style="background: var(--surface-subtle); font-weight: bold;">
      <td><strong>Sản Lượng Nhu Cầu Cần Đáp Ứng</strong></td>
      <td>20</td>
      <td>30</td>
      <td>30</td>
      <td>40</td>
      <td>Tổng cung = 195 / Tổng cầu = 120</td>
    </tr>
  </tbody>
</table>
</div>

Ban giám đốc hiện muốn xác định lượng sản xuất của từng sản phẩm tại từng nhà máy để tối thiểu hóa tổng chi phí biến đổi hàng ngày.

---

#### Tình huống 2.2 – PHÂN CÔNG NHÀ MÁY KHÔNG CHO PHÉP CHIA NHỎ SẢN PHẨM

Ban giám đốc đã quyết định cấm chia nhỏ sản phẩm (không cho phép một sản phẩm được sản xuất ở 2 xưởng khác nhau), do đó mỗi sản phẩm chỉ được phân công cho duy nhất một nhà máy. Chi phí hàng ngày khi gán trọn gói từng sản phẩm cho từng nhà máy được tổng hợp dưới đây:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Tổng Chi Phí Hàng Ngày ($/ngày)</th>
      <th>Sản Phẩm 1 (20 sp)</th>
      <th>Sản Phẩm 2 (30 sp)</th>
      <th>Sản Phẩm 3 (30 sp)</th>
      <th>Sản Phẩm 4 (40 sp)</th>
      <th>Số Sản Phẩm Tối Đa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nhà máy 1</strong></td>
      <td>$820 ($41 &times; 20)</td>
      <td>$810 ($27 &times; 30)</td>
      <td>$840 ($28 &times; 30)</td>
      <td>$960 ($24 &times; 40)</td>
      <td>2 sản phẩm</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 2</strong></td>
      <td>$800 ($40 &times; 20)</td>
      <td>$870 ($29 &times; 30)</td>
      <td>Tuyến cấm (M)</td>
      <td>$920 ($23 &times; 40)</td>
      <td>1 sản phẩm</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 3</strong></td>
      <td>$740 ($37 &times; 20)</td>
      <td>$900 ($30 &times; 30)</td>
      <td>$810 ($27 &times; 30)</td>
      <td>$840 ($21 &times; 40)</td>
      <td>1 sản phẩm</td>
    </tr>
  </tbody>
</table>
</div>

Nhà máy 1 có công suất tối đa cho 2 sản phẩm, trong khi Nhà máy 2 và Nhà máy 3 mỗi nơi chỉ có công suất tối đa cho 1 sản phẩm. Hãy xác định nhà máy nào nên sản xuất sản phẩm nào để tối thiểu hóa tổng chi phí biến đổi hàng ngày.

---

## 4. Supporting Visual Frameworks & Diagrams

### Sơ đồ Mạng lưới Phân bổ Nhà máy - Sản phẩm (Bipartite Network)

```text
[3 Nhà Máy Nguồn]                                     [4 Dòng Sản Phẩm Mới]
Nhà máy 1 (Công suất: 75) ======= cước $27-$41 ======>> Sản phẩm 1 (Nhu cầu: 20)
Nhà máy 2 (Công suất: 75) ======= cước $23-$40 ======>> Sản phẩm 2 (Nhu cầu: 30)
                           \==== TUYẾN CẤM (M) ======>> Sản phẩm 3 (Nhu cầu: 30)
Nhà máy 3 (Công suất: 45) ======= cước $21-$37 ======>> Sản phẩm 4 (Nhu cầu: 40)
                                                     >> Đích Hư Cấu (Dư thừa: 75)
```

---

## 5. Mathematical Modeling & Solution Walkthrough

### 5.1 Lời giải Case 2.1: Cho phép chia nhỏ sản phẩm (LP Simplex)
- Bổ sung Điểm đến Giả định (Dummy) nhu cầu 75 đơn vị với chi phí $0 để cân bằng tổng cung (195) = tổng cầu (195).
- Gán $c_{23} = M$ cho tuyến cấm Nhà máy 2 $	o$ Sản phẩm 3.
- **Phương án phân bổ tối ưu**:
  - Nhà máy 1: Sản xuất 30 sp Sản phẩm 2 ($810), 10 sp Sản phẩm 3 ($280), 35 sp Sản phẩm 4 ($840). Dư 0.
  - Nhà máy 2: Sản xuất 20 sp Sản phẩm 1 ($800), 5 sp Sản phẩm 4 ($115). Dư 50 sp vào Dummy.
  - Nhà máy 3: Sản xuất 20 sp Sản phẩm 3 ($540), dư 25 sp vào Dummy.
- **Tổng chi phí tối thiểu**: **$3,260/ngày** ($1,189,900/năm).

### 5.2 Lời giải Case 2.2: Cấm chia nhỏ sản phẩm (Binary Integer Programming)
- Tách Nhà máy 1 thành hai phân xưởng con: Nhà máy 1A (chọn 1 sp) và Nhà máy 1B (chọn 1 sp).
- **Phép gán nhị phân tối ưu**:
  - Nhà máy 1: Sản xuất trọn vẹn **Sản phẩm 2** ($810) và **Sản phẩm 3** ($840).
  - Nhà máy 2: Sản xuất trọn vẹn **Sản phẩm 4** ($920).
  - Nhà máy 3: Sản xuất trọn vẹn **Sản phẩm 1** ($740).
- **Tổng chi phí tối thiểu**: **$3,290/ngày** ($1,200,850/năm).

### 5.3 So sánh & Phân tích Đánh đổi Chi phí (Trade-off Analysis)

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Mô Hình Hoạch Định</th>
      <th>Chi Phí Hàng Ngày</th>
      <th>Chi Phí Hàng Năm</th>
      <th>Mức Độ Phức Tạp Vận Hành</th>
      <th>Đánh Giá của Business Analyst</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Case 2.1 (Cho phép chia nhỏ)</strong></td>
      <td>$3,260/ngày</td>
      <td>$1,189,900</td>
      <td>Rất cao (Sản phẩm 3 & 4 bị chia đôi xưởng)</td>
      <td>Rủi ro trùng lặp chi phí thiết lập máy, khó đồng bộ chất lượng.</td>
    </tr>
    <tr style="background: rgba(184, 115, 126, 0.12); font-weight: bold;">
      <td><strong>Case 2.2 (Cấm chia nhỏ)</strong></td>
      <td>$3,290/ngày</td>
      <td>$1,200,850</td>
      <td>Thấp (Chuyên môn hóa 1-1 tinh gọn)</td>
      <td>Chi phí cao hơn $30/ngày ($10,950/năm) nhưng tiết kiệm vượt trội chi phí quản lý.</td>
    </tr>
  </tbody>
</table>
</div>

---

## 6. Business Analyst (BA) Practical Implementation Guide

### 6.1 Cấu hình Phân công trong Module SAP S/4HANA PP/DS
1. **Work Center Master Data**: Thiết lập 3 Work Centers đại diện cho 3 nhà máy, định nghĩa công suất khả dụng (Available Capacity = 75, 75, 45).
2. **Routing / Production Version**:
   - Gán `Production Version` liên kết giữa từng Material Master (Product 1-4) với Work Center.
   - Với Nhà máy 2 và Sản phẩm 3: Không tạo Production Version hoặc gán trạng thái `Locked for Scheduling`.
3. **Quy tắc Nghiệp vụ Không chia nhỏ (Lot Integrity Rule)**:
   - Cấu hình trường `Split Allowed` trong đơn hàng sản xuất (Production Order Type) = **False**.
   - Thiết lập thuật toán phân bổ trong PP/DS để tối ưu hóa thời gian đổi khuôn máy (Setup Matrix Optimization).
