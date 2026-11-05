# CASE STUDY 01: THE TEXAGO CORP. SITE SELECTION PROBLEM
## Comprehensive Bilingual Case Study & Business Analysis

---

## 1. Case Overview

- **Case Identifier**: `CASE-01`
- **Official Title**: The Texago Corp. Site Selection Problem
- **Academic Source**: Course *ERP Applied to Logistics & SCM*, UEH School of International Business and Marketing (Week 1 Groupwork Practice).
- **Industry**: Fully Integrated Petroleum Refining & Energy Supply Chain Management.
- **Core Optimization Model**: Two-echelon Linear Programming Transportation Model & Facility Location Selection.
- **Key Decision**: Selecting the optimal site for constructing a new high-capacity petroleum refinery (processing 120 million barrels of crude annually) from three candidate locations: **Los Angeles, California**, **Galveston, Texas**, or **St. Louis, Missouri**.

---

## 2. Complete Original English Case (Unabridged)

### Practice for Group Work Week 1
#### Case 1 – A CASE STUDY: THE TEXAGO CORP. SITE SELECTION PROBLEM

The Texago Corporation is a large, fully integrated petroleum company based in the United States. The company produces most of its oil in its own oil fields and then imports the rest of what it needs from the Middle East. An extensive distribution network is used to transport the oil to the company’s refineries and then to transport the petroleum products from the refineries to Texago’s distribution centers. The locations of these various facilities are given in table below:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Type of Facility</th>
      <th>Locations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Oil Fields</strong></td>
      <td>1. Several in Texas<br>2. Several in California<br>3. Several in Alaska</td>
    </tr>
    <tr>
      <td><strong>Refineries</strong></td>
      <td>1. Near New Orleans, Louisiana<br>2. Near Charleston, South Carolina<br>3. Near Seattle, Washington</td>
    </tr>
    <tr>
      <td><strong>Distribution Centers</strong></td>
      <td>1. Pittsburgh, Pennsylvania<br>2. Atlanta, Georgia<br>3. Kansas City, Missouri<br>4. San Francisco, California</td>
    </tr>
  </tbody>
</table>
</div>

Texago is continuing to increase its sales, so it will soon construct a new refinery with a capacity of 120 million barrels of crude oil per year. The company will also increase its imports of crude oil from the Middle East to provide this new refinery with the necessary crude oil. The following table gives the capacity of all facilities:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Oil Fields</th>
      <th>Annual Crude Capacity (Million Barrels)</th>
      <th>Refineries</th>
      <th>Annual Processing Capacity (Million Barrels)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Texas</td>
      <td>80</td>
      <td>New Orleans</td>
      <td>100</td>
    </tr>
    <tr>
      <td>California</td>
      <td>60</td>
      <td>Charleston</td>
      <td>60</td>
    </tr>
    <tr>
      <td>Alaska</td>
      <td>100</td>
      <td>Seattle</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Middle East</td>
      <td>120 (additional)</td>
      <td>New Refinery</td>
      <td>120</td>
    </tr>
    <tr>
      <td><strong>Total Crude</strong></td>
      <td><strong>360</strong></td>
      <td><strong>Total Capacity</strong></td>
      <td><strong>360</strong></td>
    </tr>
  </tbody>
</table>
</div>

Three potential sites are being considered for the new refinery: near Los Angeles, California; near Galveston, Texas; and near St. Louis, Missouri. The operational cost of a refinery depends on its location. The following table shows the annual operating costs for the candidate locations:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Potential Site</th>
      <th>Annual Operating Cost ($ Millions)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Near Los Angeles, California</td>
      <td>$620</td>
    </tr>
    <tr>
      <td>Near Galveston, Texas</td>
      <td>$570</td>
    </tr>
    <tr>
      <td>Near St. Louis, Missouri</td>
      <td>$530</td>
    </tr>
  </tbody>
</table>
</div>

The freight cost per unit of crude oil shipped to each refinery is given in the table below:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Crude Oil Source</th>
      <th>New Orleans</th>
      <th>Charleston</th>
      <th>Seattle</th>
      <th>Los Angeles (Cand.)</th>
      <th>Galveston (Cand.)</th>
      <th>St. Louis (Cand.)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Texas</td>
      <td>$2</td>
      <td>$4</td>
      <td>$5</td>
      <td>$3</td>
      <td>$1</td>
      <td>$1</td>
    </tr>
    <tr>
      <td>California</td>
      <td>$5</td>
      <td>$5</td>
      <td>$3</td>
      <td>$1</td>
      <td>$3</td>
      <td>$4</td>
    </tr>
    <tr>
      <td>Alaska</td>
      <td>$5</td>
      <td>$7</td>
      <td>$3</td>
      <td>$4</td>
      <td>$5</td>
      <td>$7</td>
    </tr>
    <tr>
      <td>Middle East</td>
      <td>$2</td>
      <td>$3</td>
      <td>$5</td>
      <td>$4</td>
      <td>$3</td>
      <td>$4</td>
    </tr>
  </tbody>
</table>
</div>

The freight cost per unit of finished product shipped from each refinery to each distribution center, along with the annual finished product units required by each distribution center, are given below:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Refinery</th>
      <th>Pittsburgh</th>
      <th>Atlanta</th>
      <th>Kansas City</th>
      <th>San Francisco</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>New Orleans</td>
      <td>$6.5</td>
      <td>$5.5</td>
      <td>$6.0</td>
      <td>$8.0</td>
    </tr>
    <tr>
      <td>Charleston</td>
      <td>$7.0</td>
      <td>$5.0</td>
      <td>$4.0</td>
      <td>$7.0</td>
    </tr>
    <tr>
      <td>Seattle</td>
      <td>$7.0</td>
      <td>$8.0</td>
      <td>$4.0</td>
      <td>$3.0</td>
    </tr>
    <tr>
      <td>Los Angeles (Candidate)</td>
      <td>$8.0</td>
      <td>$6.0</td>
      <td>$3.0</td>
      <td>$2.0</td>
    </tr>
    <tr>
      <td>Galveston (Candidate)</td>
      <td>$5.0</td>
      <td>$4.0</td>
      <td>$3.0</td>
      <td>$6.0</td>
    </tr>
    <tr>
      <td>St. Louis (Candidate)</td>
      <td>$4.0</td>
      <td>$3.0</td>
      <td>$1.0</td>
      <td>$5.0</td>
    </tr>
    <tr style="background: var(--surface-subtle); font-weight: bold;">
      <td>Annual Demand Needed</td>
      <td>100</td>
      <td>80</td>
      <td>80</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>

#### Questions: Calculate
1. Total shipping cost for crude oil with each potential choice of a site for the new refinery.
2. Total shipping cost for finished product with each potential choice of a site for the new refinery.
3. Calculate total variable cost from the choice of each site for the new Texago refinery.

---

## 3. Complete Faithful Vietnamese Translation (Bản Dịch Tiếng Việt Đầy Đủ)

### Bài Tập Thực Hành Nhóm Tuần 1
#### Tình huống 1 – CASE STUDY: BÀI TOÁN LỰA CHỌN ĐỊA ĐIỂM CỦA TẬP ĐOÀN TEXAGO

Tập đoàn Texago (The Texago Corporation) là một công ty dầu khí tích hợp toàn diện quy mô lớn có trụ sở chính tại Hoa Kỳ. Công ty tự khai thác phần lớn lượng dầu thô từ các mỏ dầu của chính mình và sau đó nhập khẩu phần còn thiếu từ Trung Đông. Một mạng lưới phân phối rộng lớn được vận hành để vận chuyển dầu thô đến các nhà máy lọc dầu của công ty và sau đó vận chuyển các sản phẩm dầu khí tinh chế từ các nhà máy lọc dầu đến các trung tâm phân phối của Texago. Vị trí của các cơ sở khác nhau này được cho trong bảng dưới đây:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Loại Cơ Sở</th>
      <th>Vị Trí Địa Lý Cụ Thể</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Mỏ dầu thô</strong></td>
      <td>1. Một số mỏ tại bang Texas<br>2. Một số mỏ tại bang California<br>3. Một số mỏ tại bang Alaska</td>
    </tr>
    <tr>
      <td><strong>Nhà máy lọc dầu</strong></td>
      <td>1. Gần New Orleans, bang Louisiana<br>2. Gần Charleston, bang South Carolina<br>3. Gần Seattle, bang Washington</td>
    </tr>
    <tr>
      <td><strong>Trung tâm phân phối</strong></td>
      <td>1. Pittsburgh, bang Pennsylvania<br>2. Atlanta, bang Georgia<br>3. Kansas City, bang Missouri<br>4. San Francisco, bang California</td>
    </tr>
  </tbody>
</table>
</div>

Texago đang tiếp tục gia tăng doanh số bán hàng, vì vậy công ty sẽ sớm xây dựng một nhà máy lọc dầu mới với công suất 120 triệu thùng dầu thô mỗi năm. Công ty cũng sẽ tăng lượng dầu thô nhập khẩu từ Trung Đông để cung cấp lượng dầu thô cần thiết cho nhà máy lọc dầu mới này. Bảng dưới đây cung cấp công suất của tất cả các cơ sở:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Mỏ Dầu Thô</th>
      <th>Sản Lượng Hàng Năm (Triệu thùng)</th>
      <th>Nhà Máy Lọc Dầu</th>
      <th>Công Suất Chế Biến (Triệu thùng)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Texas</td>
      <td>80</td>
      <td>New Orleans</td>
      <td>100</td>
    </tr>
    <tr>
      <td>California</td>
      <td>60</td>
      <td>Charleston</td>
      <td>60</td>
    </tr>
    <tr>
      <td>Alaska</td>
      <td>100</td>
      <td>Seattle</td>
      <td>80</td>
    </tr>
    <tr>
      <td>Trung Đông (Nhập khẩu)</td>
      <td>120 (bổ sung)</td>
      <td>Nhà máy lọc dầu mới</td>
      <td>120</td>
    </tr>
    <tr>
      <td><strong>Tổng lượng dầu thô</strong></td>
      <td><strong>360</strong></td>
      <td><strong>Tổng công suất lọc dầu</strong></td>
      <td><strong>360</strong></td>
    </tr>
  </tbody>
</table>
</div>

Ba địa điểm tiềm năng đang được xem xét cho nhà máy lọc dầu mới: gần Los Angeles, bang California; gần Galveston, bang Texas; và gần St. Louis, bang Missouri. Chi phí vận hành của một nhà máy lọc dầu phụ thuộc vào vị trí của nó. Bảng sau đây cho thấy chi phí vận hành hàng năm cho các địa điểm ứng viên:

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Địa Điểm Tiềm Năng (Ứng viên)</th>
      <th>Chi Phí Vận Hành Hàng Năm ($ Triệu USD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gần Los Angeles, California</td>
      <td>$620</td>
    </tr>
    <tr>
      <td>Gần Galveston, Texas</td>
      <td>$570</td>
    </tr>
    <tr>
      <td>Gần St. Louis, Missouri</td>
      <td>$530</td>
    </tr>
  </tbody>
</table>
</div>

Cước phí vận chuyển trên mỗi đơn vị dầu thô chuyển đến từng nhà máy lọc dầu được cho trong bảng dưới đây ($ Triệu USD / Triệu thùng):

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Nguồn Dầu Thô</th>
      <th>New Orleans</th>
      <th>Charleston</th>
      <th>Seattle</th>
      <th>Los Angeles (UV)</th>
      <th>Galveston (UV)</th>
      <th>St. Louis (UV)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Texas</td>
      <td>$2</td>
      <td>$4</td>
      <td>$5</td>
      <td>$3</td>
      <td>$1</td>
      <td>$1</td>
    </tr>
    <tr>
      <td>California</td>
      <td>$5</td>
      <td>$5</td>
      <td>$3</td>
      <td>$1</td>
      <td>$3</td>
      <td>$4</td>
    </tr>
    <tr>
      <td>Alaska</td>
      <td>$5</td>
      <td>$7</td>
      <td>$3</td>
      <td>$4</td>
      <td>$5</td>
      <td>$7</td>
    </tr>
    <tr>
      <td>Trung Đông</td>
      <td>$2</td>
      <td>$3</td>
      <td>$5</td>
      <td>$4</td>
      <td>$3</td>
      <td>$4</td>
    </tr>
  </tbody>
</table>
</div>

Cước phí vận chuyển trên mỗi đơn vị thành phẩm tinh chế từ mỗi nhà máy lọc dầu đến mỗi trung tâm phân phối, cùng với nhu cầu thành phẩm hàng năm của từng trung tâm phân phối, được thể hiện dưới đây ($ Triệu USD / Triệu thùng):

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Nhà Máy Lọc Dầu</th>
      <th>Pittsburgh</th>
      <th>Atlanta</th>
      <th>Kansas City</th>
      <th>San Francisco</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>New Orleans</td>
      <td>$6.5</td>
      <td>$5.5</td>
      <td>$6.0</td>
      <td>$8.0</td>
    </tr>
    <tr>
      <td>Charleston</td>
      <td>$7.0</td>
      <td>$5.0</td>
      <td>$4.0</td>
      <td>$7.0</td>
    </tr>
    <tr>
      <td>Seattle</td>
      <td>$7.0</td>
      <td>$8.0</td>
      <td>$4.0</td>
      <td>$3.0</td>
    </tr>
    <tr>
      <td>Los Angeles (Ứng viên)</td>
      <td>$8.0</td>
      <td>$6.0</td>
      <td>$3.0</td>
      <td>$2.0</td>
    </tr>
    <tr>
      <td>Galveston (Ứng viên)</td>
      <td>$5.0</td>
      <td>$4.0</td>
      <td>$3.0</td>
      <td>$6.0</td>
    </tr>
    <tr>
      <td>St. Louis (Ứng viên)</td>
      <td>$4.0</td>
      <td>$3.0</td>
      <td>$1.0</td>
      <td>$5.0</td>
    </tr>
    <tr style="background: var(--surface-subtle); font-weight: bold;">
      <td>Nhu Cầu Hàng Năm Cần Tiếp Nhận</td>
      <td>100</td>
      <td>80</td>
      <td>80</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>

#### Câu hỏi yêu cầu: Hãy tính toán
1. Tổng chi phí vận chuyển dầu thô với từng lựa chọn địa điểm tiềm năng cho nhà máy lọc dầu mới.
2. Tổng chi phí vận chuyển thành phẩm tinh chế với từng lựa chọn địa điểm tiềm năng cho nhà máy lọc dầu mới.
3. Tính tổng chi phí biến đổi phát sinh từ việc lựa chọn từng địa điểm cho nhà máy lọc dầu Texago mới.

---

## 4. Supporting Materials & Visual Network Diagram

### Tài liệu bổ sung chính thức: Bổ sung dữ liệu cho case study 1 - TEXAGO
Trong đề bài gốc PDF, Bảng 2.8.2 bị khuyết hàng số liệu nhu cầu tại 4 trung tâm phân phối. Hình ảnh dưới đây trích xuất từ tài liệu bổ sung chính thức xác lập rõ nhu cầu 360 triệu thùng:

<div class="case-image-container" style="text-align: center; margin: 1.5rem 0;">
  <img src="assets/texago_supplementary_data.jpg" alt="Bảng bổ sung dữ liệu nhu cầu Texago" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: var(--shadow-sm); border: 1px solid var(--border-color);">
  <p style="font-size: 0.85rem; color: var(--muted-mauve); margin-top: 0.5rem; font-style: italic;">
    Hình 1.1: Bảng số liệu bổ sung chính thức - Nhu cầu tiếp nhận thành phẩm: Pittsburgh (100), Atlanta (80), Kansas City (80), San Francisco (100) — Tổng cộng 360 triệu thùng.
  </p>
</div>

### Sơ đồ Chuỗi Cung ứng 2 Cấp của Texago (Two-Echelon Network)

```text
[4 Nguồn Dầu Thô]                 [4 Nhà Máy Lọc Dầu]              [4 Trung Tâm Phân Phối]
Texas (80M)        \             / New Orleans (100M) \            / Pittsburgh (100M)
California (60M)    -- Vận chuyển -- Charleston (60M)   -- Vận chuyển -- Atlanta (80M)
Alaska (100M)       --  Dầu Thô   -- Seattle (80M)      -- Thành Phẩm -- Kansas City (80M)
Trung Đông (120M)  /             \ [Ứng viên mới] (120M)/          \ San Francisco (100M)
                                   (LA / Galveston / St. Louis)
```

---

## 5. Quantitative Solution & Comparative Analysis

Để giải quyết bài toán, ta xây dựng mô hình quy hoạch tuyến tính cho 3 kịch bản ứng viên:

### So sánh Tổng Chi phí Toàn chuỗi ($ Triệu USD / năm)

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Địa Điểm Ứng Viên</th>
      <th>Cước Dầu Thô (Stage 1)</th>
      <th>Cước Thành Phẩm (Stage 2)</th>
      <th>Chi Phí Vận Hành Nhà Máy</th>
      <th>Tổng Chi Phí Biến Đổi</th>
      <th>Đánh Giá & Thứ Hạng</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Los Angeles, CA</strong></td>
      <td>$410M</td>
      <td>$410M</td>
      <td>$620M</td>
      <td><strong>$1,440M</strong></td>
      <td>Hạng 3 (Kém nhất)</td>
    </tr>
    <tr>
      <td><strong>Galveston, TX</strong></td>
      <td>$360M</td>
      <td>$450M</td>
      <td>$570M</td>
      <td><strong>$1,380M</strong></td>
      <td>Hạng 2 (Cao hơn $50M)</td>
    </tr>
    <tr style="background: rgba(184, 115, 126, 0.12); font-weight: bold;">
      <td><strong>St. Louis, MO</strong></td>
      <td>$440M</td>
      <td>$360M</td>
      <td>$530M</td>
      <td><strong>$1,330M</strong></td>
      <td><strong>HẠNG 1: TỐI ƯU TOÀN CỤC</strong></td>
    </tr>
  </tbody>
</table>
</div>

### Kết luận phân tích định lượng
- **Địa điểm tối ưu**: **St. Louis, Missouri** với tổng chi phí **$1,330 triệu USD/năm**.
- **Lợi thế mấu chốt**: Mặc dù cước vận chuyển dầu thô đến St. Louis cao hơn Galveston $80M ($440M vs $360M), nhưng St. Louis lại tiết kiệm được $40M chi phí vận hành nhà máy và tiết kiệm tới $90M cước vận chuyển thành phẩm đến các trung tâm tiêu thụ vùng Trung Tây và Bờ Đông (Pittsburgh, Atlanta, Kansas City).
- **Nguyên lý Chuỗi cung ứng**: Tối ưu hóa tổng thể (Global Optimum) phải đánh giá toàn diện chuỗi cung ứng hai đầu (End-to-End), tránh tối ưu hóa cục bộ (Sub-optimization) tại khâu cung cấp nguyên liệu.

---

## 6. Business Analyst (BA) Practical Implementation Guide

### 6.1 Ánh xạ Thực thể vào Hệ thống ERP (SAP S/4HANA & TM)
1. **Master Data Thiết lập Nguồn & Đích**:
   - Mỏ dầu & Trung Đông: Tạo mã `Vendor Master` (BP Role: Vendor) kết hợp `Plant` loại cung ứng thô.
   - Nhà máy lọc dầu: Thiết lập các `Plants` trong cấu trúc doanh nghiệp SAP MM/PP.
   - Trung tâm phân phối: Thiết lập `Storage Locations` hoặc `Customer Master` (Ship-to Parties trong SAP SD).
2. **Transportation Lane Master Data (SAP TM)**:
   - Cấu hình từng làn vận chuyển giữa Nguồn $	o$ Nhà máy và Nhà máy $	o$ Kho.
   - Gán biểu cước trong bảng điều kiện giá `Condition Records`.
3. **Chạy Mô hình Tối ưu hóa Tuyến (Optimization Run)**:
   - SAP TM Freight Order Execution sử dụng bộ giải đơn hình mạng lưới tích hợp để lập kế hoạch điều vận hàng tuần.
