with open('outputs/content/chapters/CHAP_02.md', 'r', encoding='utf-8') as f:
    c2 = f.read()

# Replace tab characters in LaTeX commands
c2 = c2.replace('\text', r'\text')
c2 = c2.replace('\times', r'\times')
c2 = c2.replace('\to', r'\to')
c2 = c2.replace('\t', ' ')

# Replace Section 4.2 table with clean HTML table
table_start = c2.find('| Nhà máy | Phân bổ Sản phẩm')
table_end = c2.find('#### Đánh giá giải pháp:', table_start)

sec42_new_table = """<div class="table-responsive">
<table class="content-table">
  <thead>
    <tr>
      <th>Nhà máy (Factory)</th>
      <th>Phân bổ Sản phẩm ($x_{ij}^*$)</th>
      <th>Chi phí đơn vị ($c_{ij}$)</th>
      <th>Thành tiền (Total Cost)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nhà máy 1</strong></td>
      <td>Sản phẩm 2: 30 đơn vị<br/>Sản phẩm 4: 40 đơn vị<br/>Dummy (dư thừa): 5 đơn vị</td>
      <td>$27<br/>$24<br/>$0</td>
      <td>30 &times; $27 = $810<br/>40 &times; $24 = $960<br/>5 &times; $0 = $0</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 2</strong></td>
      <td>Sản phẩm 1: 20 đơn vị<br/>Dummy (dư thừa): 55 đơn vị</td>
      <td>$40<br/>$0</td>
      <td>20 &times; $40 = $800<br/>55 &times; $0 = $0</td>
    </tr>
    <tr>
      <td><strong>Nhà máy 3</strong></td>
      <td>Sản phẩm 3: 30 đơn vị<br/>Dummy (dư thừa): 15 đơn vị</td>
      <td>$27<br/>$0</td>
      <td>30 &times; $27 = $810<br/>15 &times; $0 = $0</td>
    </tr>
    <tr style="background: rgba(184, 115, 126, 0.12); font-weight: bold;">
      <td><strong>Tổng cộng</strong></td>
      <td><strong>Sản xuất đủ 120 đơn vị thực tế (75 đơn vị nhàn rỗi)</strong></td>
      <td>—</td>
      <td><strong>$Z^* = \\$3.260\\text{/ngày}\\quad (\\$3,260\\text{/day})</strong></td>
    </tr>
  </tbody>
</table>
</div>

"""

if table_start != -1 and table_end != -1:
    c2 = c2[:table_start] + sec42_new_table + c2[table_end:]

# Format Section 12 review questions as accordion
q1_idx = c2.find('1. **Câu hỏi:**')
q2_idx = c2.find('2. **Câu hỏi:**', q1_idx)
sec12_heading_idx = c2.find('## 12. Kiểm tra Đánh giá Kiến thức')

sec12_content = """## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Khi tổng năng lực cung ứng của các nhà máy lớn hơn tổng nhu cầu thị trường ($\\sum s_i > \\sum d_j$), kỹ thuật nào sau đây được áp dụng để cân bằng bài toán?
   - A. Thêm một nguồn cung ảo (Dummy Source) với năng lực bằng hiệu số Cung - Cầu.
   - B. Thêm một điểm đến ảo (Dummy Destination) với nhu cầu bằng hiệu số Cung - Cầu và chi phí đơn vị thường bằng 0.
   - C. Cắt giảm ngẫu nhiên công suất của các nhà máy.
   - D. Nhân đôi nhu cầu của tất cả các điểm tiêu thụ.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Khi tổng cung vượt tổng cầu, kỹ thuật cân bằng chuẩn tắc là tạo thêm một Điểm đến Ảo (Dummy Destination) với lượng cầu đúng bằng $s_\\text{Dummy} = \\sum s_i - \\sum d_j$. Chi phí vận chuyển vào điểm ảo được gán bằng 0 (đại diện cho năng lực máy móc nhàn rỗi không tốn chi phí giao hàng).</p>
  </div>
</details>

2. **Câu hỏi:** Trong phương pháp Big-M để xử lý tuyến đường cấm, bản chất của tham số $M$ là gì?
   - A. Là số lượng hàng hóa tối đa được phép vận chuyển trên tuyến.
   - B. Là một hằng số dương cực lớn đóng vai trò là mức phạt kinh tế để ép biến quyết định tương ứng về giá trị 0 trong hàm cực tiểu hóa chi phí.
   - C. Là thời gian giao hàng tối thiểu tính bằng phút.
   - D. Là hệ số chiết khấu giá cước vận tải.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Tham số Big-$M$ là một đại lượng dương cực lớn đóng vai trò là mức phạt kinh tế (penalty cost) trong hàm mục tiêu cực tiểu hóa chi phí. Thuật toán Simplex khi tìm nghiệm tối ưu sẽ triệt tiêu biến quyết định $x_{ij}$ của tuyến cấm đó về đúng bằng 0 ($x_{ij}^* = 0$) để tránh bị cộng khoản phạt khổng lồ này.</p>
  </div>
</details>
"""

if sec12_heading_idx != -1:
    c2 = c2[:sec12_heading_idx] + sec12_content

with open('outputs/content/chapters/CHAP_02.md', 'w', encoding='utf-8') as f:
    f.write(c2)

print("CHAP_02.md patched successfully! Remaining tabs:", c2.count('\t'))
