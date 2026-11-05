case4_content = """# CASE STUDY 04: THE SOCA PROBLEM (GRADUAL REPLENISHMENT / EPQ)
## Nghiên Cứu Tình Huống 04: Bài Toán Bổ Sung Hàng Dần Dần (Mô Hình Sản Xuất Kinh Tế - EPQ)

---

## 1. Case Overview

- **Case Identifier**: `CASE-04`
- **Official Title**: The SOCA Problem (Gradual Replenishment / Economic Production Quantity)
- **Academic Source**: Course *ERP Applied to Logistics & SCM*, UEH School of International Business and Marketing (Week 5 Groupwork Practice).
- **Industry**: Consumer Electronics & Television Manufacturing.
- **Core Optimization Model**: Economic Production Quantity (EPQ) with Gradual Replenishment Factor $(1 - d/p)$, Production Uptime/Downtime Scheduling, and Finite Capacity Planning.
- **Key Decision**: Evaluating whether SOCA should alter its internal manufacturing lot size for speaker subassemblies from the legacy batch of 30,000 units to an optimized production batch, balancing fixed machine changeover costs with working capital holding constraints.

---

## 2. Complete Original English Case (Unabridged)

### Practice for Group Work Week 5
#### Case Study: The SOCA Company

SOCA, a television manufacturing company, produces its own speakers for assembly into its television sets. To maintain its production schedule for television sets, the company needs to have 1,000 speakers available for assembly per day. Each time an order is placed to produce more speakers, the rate of production is 3,000 speakers per day until the order is filled, after which the production facilities are used for other purposes until another production run for speakers is needed. Since this production rate is three times the rate at which the speakers are needed, speakers are being produced only one-third of the time.

The current policy for managing SOCA’s inventory of speakers is summarized below:

#### Current Inventory Policy of SOCA
a. Daily demand rate = 1,000 speakers per day.  
b. Daily production rate = 3,000 speakers per day (when producing).  
c. The production facilities get set up to start a production run each time the inventory level is scheduled to drop to 0.  
d. Each production run produces 30,000 speakers over a period of 10 working days, so another 20 working days elapse before the next production run is needed.  

This policy leads to the pattern of inventory levels over time. Thus, the inventory level fluctuates between 0 and a maximum inventory level that is somewhat under 30,000 speakers. The reason for not reaching 30,000 is that speakers also are being withdrawn from inventory for assembly into television sets while a production run is under way. Consequently:

$$\\begin{aligned}
\\text{Maximum inventory level} &= \\text{Production lot size} - \\text{Demand during production run} \\\\
&= 30,000\\text{ speakers} - (10\\text{ days}) \\times (1,000\\text{ speakers/day}) \\\\
&= 30,000\\text{ speakers} - 10,000\\text{ speakers} \\\\
&= \\mathbf{20,000\\text{ speakers}}
\\end{aligned}$$

Therefore:

$$\\begin{aligned}
\\text{Average inventory level} &= \\frac{\\text{Maximum inventory level}}{2} \\\\
&= \\frac{20,000}{2} = \\mathbf{10,000\\text{ speakers}}
\\end{aligned}$$

SOCA’s costs associated with this inventory policy are summarized below:
- $c = \\text{Unit production cost} = \\$12\\text{ per speaker produced}$.
- $K = \\text{Setup cost for a production run} = \\$12,000$.
- $h = \\text{Unit holding cost} = \\$3.60\\text{ per speaker in inventory per year}$.
- Operating schedule: 250 working days per year $\\implies$ Annual demand $D = 250 \\times 1,000 = 250,000\\text{ speakers/year}$.

#### Questions
1. What is the annual total variable inventory cost under the current policy ($Q = 30,000$)?
2. What is the optimal production quantity $Q^*$ that minimizes total variable cost?
3. What is the resulting maximum inventory level, cycle time, and annual cost savings achieved by switching to the optimal EPQ policy?

---

## 3. Complete Faithful Vietnamese Translation (Bản Dịch Tiếng Việt Đầy Đủ)

### Bài Tập Thực Hành Nhóm Tuần 5
#### Tình huống nghiên cứu: Công ty SOCA (Mô hình Bổ sung dần EPQ)

SOCA là một công ty sản xuất tivi, tự sản xuất loa để lắp ráp vào các bộ tivi của mình. Để duy trì lịch trình sản xuất tivi, công ty cần có sẵn 1.000 chiếc loa để lắp ráp mỗi ngày làm việc. Mỗi khi một lệnh sản xuất được phát hành để làm thêm loa, tốc độ sản xuất đạt 3.000 chiếc loa mỗi ngày cho đến khi hoàn thành xong đơn hàng, sau đó các trang thiết bị máy móc sản xuất sẽ được chuyển sang sử dụng cho các mục đích khác cho đến khi cần một đợt chạy sản xuất loa tiếp theo. Vì tốc độ sản xuất này gấp ba lần tốc độ tiêu thụ loa của dây chuyền lắp ráp, nên loa chỉ được sản xuất trong một phần ba thời gian làm việc.

Chính sách hiện tại để quản lý hàng tồn kho loa của SOCA được tóm tắt dưới đây:

#### Chính sách Tồn kho Hiện hành của SOCA
a. Tốc độ nhu cầu hàng ngày = 1.000 chiếc loa mỗi ngày.  
b. Tốc độ sản xuất hàng ngày = 3.000 chiếc loa mỗi ngày (khi máy đang chạy).  
c. Các cơ sở sản xuất được thiết lập (setup máy) để bắt đầu một đợt sản xuất mới mỗi khi mức tồn kho dự kiến giảm về 0.  
d. Mỗi đợt sản xuất làm ra 30.000 chiếc loa trong khoảng thời gian 10 ngày làm việc, do đó sẽ có 20 ngày làm việc tiếp theo trôi qua trước khi cần đợt sản xuất mới.  

Chính sách này dẫn đến mô hình mức tồn kho theo thời gian dao động giữa 0 và mức tồn kho cực đại thấp hơn 30.000 loa. Nguyên nhân mức tồn kho không bao giờ chạm tới 30.000 là do loa liên tục được rút ra khỏi kho để lắp ráp vào tivi trong khi đợt sản xuất vẫn đang diễn ra. Do đó:

$$\\begin{aligned}
\\text{Mức tồn kho cực đại } (I_{\\text{max}}) &= \\text{Quy mô lô sản xuất} - \\text{Lượng tiêu thụ trong thời gian sản xuất} \\\\
&= 30.000\\text{ loa} - (10\\text{ ngày}) \\times (1.000\\text{ loa/ngày}) \\\\
&= 30.000 - 10.000 = \\mathbf{20.000\\text{ chiếc loa}}
\\end{aligned}$$

Vì vậy:

$$\\begin{aligned}
\\text{Mức tồn kho bình quân } (I_{\\text{avg}}) &= \\frac{\\text{Mức tồn kho cực đại}}{2} \\\\
&= \\frac{20.000}{2} = \\mathbf{10.000\\text{ chiếc loa}}
\\end{aligned}$$

Các chi phí của SOCA gắn liền với chính sách tồn kho này được tổng kết dưới đây:
- $c = \\text{Chi phí sản xuất đơn vị} = \\$12\\text{ cho mỗi chiếc loa sản xuất ra}$.
- $K = \\text{Chi phí thiết lập máy móc cho mỗi đợt chạy} = \\$12.000$.
- $h = \\text{Chi phí lưu kho một chiếc loa trong một năm} = \\$3.60\\text{/loa/năm}$.
- Lịch làm việc: 250 ngày làm việc mỗi năm $\\implies$ Tổng nhu cầu năm $D = 250 \\times 1.000 = 250.000\\text{ chiếc loa/năm}$.

#### Câu hỏi yêu cầu
1. Tổng chi phí biến đổi tồn kho hàng năm (TVC) theo chính sách hiện tại ($Q = 30.000$) là bao nhiêu?
2. Quy mô lô sản xuất kinh tế tối ưu $Q^*$ giúp cực tiểu hóa tổng chi phí biến đổi là bao nhiêu?
3. Mức tồn kho cực đại, độ dài chu kỳ sản xuất, và số tiền tiết kiệm hàng năm đạt được khi chuyển sang chính sách EPQ tối ưu là bao nhiêu?

---

## 4. Supporting Visual EPQ Framework

### Đồ thị Bổ sung Dần (EPQ Sawtooth Curve) với Tốc độ Sản xuất Hữu hạn

```text
Mức tồn kho (loa)
  ^
33,333|           /| [Tối ưu Q* = 50.000]
      |          / |  Tích lũy ròng: (p - d) = 2.000 loa/ngày
20,000|  /|     /  |  [Chính sách cũ Q = 30.000]
      | / |    /   |  Tiêu hao khi máy nghỉ: -d = -1.000 loa/ngày
      |/  |   /    |
     0+---+--+-----+---------------------------> Thời gian (ngày)
      <-t1-><--t2-->
      16.67d 33.33d
      <-- Chu kỳ T = 50 ngày -->
```

---

## 5. Quantitative Mathematical Modeling & Comparative Analysis

### 5.1 Công thức EPQ và Kết quả Tối ưu
Áp dụng công thức Lượng Sản xuất Kinh tế với hệ số bổ sung dần:
$$Q^* = \\sqrt{\\frac{2 K D}{h \\left(1 - \\frac{d}{p}\\right)}} = \\sqrt{\\frac{2 \\times 12.000 \\times 250.000}{3,60 \\times \\left(1 - \\frac{1.000}{3.000}\\right)}} = \\sqrt{\\frac{6.000.000.000}{2,40}} = \\mathbf{50.000\\text{ chiếc loa}}$$

- **Thời gian sản xuất một lô ($t_1$)**: $t_1 = \\frac{Q^*}{p} = \\frac{50.000}{3.000} = \\mathbf{16,67\\text{ ngày làm việc}}$.
- **Thời gian tiêu thụ khi máy nghỉ ($t_2$)**: $t_2 = \\frac{I_{\\text{max}}}{d} = \\frac{33.333,33}{1.000} = \\mathbf{33,33\\text{ ngày làm việc}}$.
- **Tổng chu kỳ ($T = t_1 + t_2$)**: $16,67 + 33,33 = \\mathbf{50\\text{ ngày làm việc}}$ (đúng 5 đợt chạy mỗi năm).
- **Mức tồn kho cực đại**: $I_{\\text{max}} = 50.000 \\times \\left(1 - \\frac{1}{3}\\right) = \\mathbf{33.333,33\\text{ chiếc loa}}$.
- **Mức tồn kho bình quân**: $I_{\\text{avg}} = \\frac{33.333,33}{2} = \\mathbf{16.666,67\\text{ chiếc loa}}$.

### 5.2 Bảng Đối Chiếu So Sánh Toàn Diện

<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Chỉ Số Vận Hành</th>
      <th>Chính Sách Hiện Tại ($Q = 30.000$)</th>
      <th>Chính Sách Tối Ưu EPQ ($Q^* = 50.000$)</th>
      <th>Mức Độ Cải Thiện / Chênh Lệch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Cỡ lô sản xuất ($Q$)</strong></td>
      <td>30.000 loa</td>
      <td>50.000 loa</td>
      <td>Tăng +66,67%</td>
    </tr>
    <tr>
      <td><strong>Số đợt chạy máy ($N$)</strong></td>
      <td>8,33 lần/năm</td>
      <td>5,00 lần/năm</td>
      <td>Giảm -3,33 lần/năm (Ít gián đoạn)</td>
    </tr>
    <tr>
      <td><strong>Thời gian sản xuất ($t_1$)</strong></td>
      <td>10,0 ngày</td>
      <td>16,67 ngày</td>
      <td>Tăng +6,67 ngày/đợt</td>
    </tr>
    <tr>
      <td><strong>Thời gian máy nghỉ ($t_2$)</strong></td>
      <td>20,0 ngày</td>
      <td>33,33 ngày</td>
      <td>Dư thêm 13,33 ngày trống cho sản phẩm khác</td>
    </tr>
    <tr>
      <td><strong>Tồn kho cực đại ($I_{\\text{max}}$)</strong></td>
      <td>20.000 chiếc</td>
      <td>33.333 chiếc</td>
      <td>Tăng +13.333 chiếc (+66,67%)</td>
    </tr>
    <tr>
      <td><strong>Chi phí thiết lập máy hàng năm</strong></td>
      <td>$100.000/năm</td>
      <td>$60.000/năm</td>
      <td><strong>Tiết kiệm $40.000/năm</strong> (Giảm 40%)</td>
    </tr>
    <tr>
      <td><strong>Chi phí lưu kho hàng năm</strong></td>
      <td>$36.000/năm</td>
      <td>$60.000/năm</td>
      <td>Tăng +$24.000/năm (Tại điểm tối ưu $60k = $60k)</td>
    </tr>
    <tr style="background: rgba(184, 115, 126, 0.12); font-weight: bold;">
      <td><strong>Tổng Chi Phí Biến Đổi (TVC)</strong></td>
      <td><strong>$136.000/năm</strong></td>
      <td><strong>$120.000/năm</strong></td>
      <td><strong>TIẾT KIỆM RÒNG $16.000/NĂM (-11,76%)</strong></td>
    </tr>
  </tbody>
</table>
</div>

---

## 6. Business Analyst (BA) Practical Implementation Guide

### 6.1 Cấu hình Quy trình Sản xuất trong SAP S/4HANA (Module PP)
1. **Material Master (MM02) - View MRP 1**:
   - `Procurement Type`: Thiết lập là **E** (In-house production / Sản xuất nội bộ).
   - `Lot Sizing Procedure`: Cấu hình là **FX** (Fixed order quantity) với `Fixed Lot Size` = **50.000 EA**.
2. **Work Center Routing (CA02)**:
   - Khai báo công suất máy dập và lắp ráp loa với định mức $3.000\\text{ chiếc/ngày}$ ($0,00033\\text{ ngày/chiếc}$).
   - Thiết lập thời gian chuyển đổi khuôn (Setup Time) chuẩn tương ứng với chi phí $12.000 phát sinh.
3. **Quản lý Năng lực Kho Đệm (SAP EWM Storage Capacity Check)**:
   - Vì tồn kho đỉnh tăng từ 20.000 lên 33.334 loa, BA cần khảo sát dung lượng lưu trữ thực tế tại xưởng (Storage Bin Capacity) để đảm bảo không bị quá tải diện tích đệm.
"""

with open('outputs/content/case-studies/CASE_04_SOCA.md', 'w', encoding='utf-8') as f:
    f.write(case4_content)

print("Updated CASE_04_SOCA.md successfully! Length:", len(case4_content))
