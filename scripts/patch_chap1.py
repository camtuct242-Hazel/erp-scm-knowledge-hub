import re

# 1. Fix CHAP_01.md
with open('outputs/content/chapters/CHAP_01.md', 'r', encoding='utf-8') as f:
    c1 = f.read()

# Replace Section 4.3 Heuristic calculation with clean mathematical block
sec43_target = """**Tổng chi phí phân bổ Heuristic:**
$$\\begin{aligned}
Z_{\\text{Heuristic}} &= (20 \\times 513) + (55 \\times 867) + (80 \\times 352) + (45 \\times 416) + (70 \\times 388) + (30 \\times 685) \\\\
&= 10.260 + 47.685 + 28.160 + 18.720 + 27.160 + 20.550 \\\\
&= \\mathbf{\\$152.535} \\quad (\\text{hoặc theo phương án trực giác sai lầm sơ khai: } \\mathbf{\\$179.850})
\\end{aligned}$$"""

sec43_repl = """**Tổng chi phí phân bổ Heuristic:**
$$\\begin{aligned}
Z_{\\text{Heuristic}} &= (20 \\times 513) + (55 \\times 867) + (80 \\times 352) + (45 \\times 416) + (70 \\times 388) + (30 \\times 685) \\\\
&= 10.260 + 47.685 + 28.160 + 18.720 + 27.160 + 20.550 \\\\
&= \\mathbf{152.535\\text{ USD}} \\quad (\\text{hoặc theo phương án sơ khai: } \\mathbf{179.850\\text{ USD}})
\\end{aligned}$$"""

if sec43_target in c1:
    c1 = c1.replace(sec43_target, sec43_repl, 1)

# Format Section 12 review questions as accordion
c1_q1_target = """1. **Câu hỏi:** Trong mô hình bài toán vận tải tuyến tính cân bằng, điều kiện tiên quyết nào sau đây phải được thỏa mãn?
   - A. Số lượng nguồn cung phải bằng số lượng điểm cầu ($m = n$).
   - B. Tổng khả năng cung cấp phải bằng đúng tổng nhu cầu tiêu thụ ($\sum s_i = \sum d_j$).
   - C. Chi phí vận chuyển giữa mọi cặp điểm phải bằng nhau ($c_{ij} = c$).
   - D. Mọi nhà máy đều phải giao hàng cho tất cả các nhà kho.
   - *Đáp án đúng:* **B**. Giải thích: Bài toán vận tải cân bằng đòi hỏi tổng cung bằng tổng cầu. Số lượng nguồn $m$ và đích $n$ hoàn toàn có thể khác nhau."""

c1_q1_repl = """1. **Câu hỏi:** Trong mô hình bài toán vận tải tuyến tính cân bằng, điều kiện tiên quyết nào sau đây phải được thỏa mãn?
   - A. Số lượng nguồn cung phải bằng số lượng điểm cầu ($m = n$).
   - B. Tổng khả năng cung cấp phải bằng đúng tổng nhu cầu tiêu thụ ($\\sum s_i = \\sum d_j$).
   - C. Chi phí vận chuyển giữa mọi cặp điểm phải bằng nhau ($c_{ij} = c$).
   - D. Mọi nhà máy đều phải giao hàng cho tất cả các nhà kho.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Bài toán vận tải cân bằng đòi hỏi tổng cung bằng tổng cầu ($\\sum s_i = \\sum d_j$). Số lượng nguồn $m$ và số lượng đích $n$ hoàn toàn có thể khác nhau.</p>
  </div>
</details>"""

c1_q2_target = """2. **Câu hỏi:** Tại sao phương pháp giải trực quan Heuristic (chọn tuyến rẻ nhất trước) lại thường dẫn đến tổng chi phí cao hơn thuật toán Simplex LP?
   - A. Vì phương pháp Heuristic tính nhầm chi phí đơn vị.
   - B. Vì phương pháp Heuristic mang tính tham lam cục bộ, làm cạn kiệt năng lực của các nguồn giá rẻ và ép buộc các phân bổ cuối cùng phải đi vào các tuyến có cước phí cực đắt.
   - C. Vì thuật toán Simplex LP không áp dụng được cho thực tế.
   - D. Vì phương pháp Heuristic chỉ giải được các bài toán có quy mô dưới 3 nhà máy.
   - *Đáp án đúng:* **B**."""

c1_q2_repl = """2. **Câu hỏi:** Tại sao phương pháp giải trực quan Heuristic (chọn tuyến rẻ nhất trước) lại thường dẫn đến tổng chi phí cao hơn thuật toán Simplex LP?
   - A. Vì phương pháp Heuristic tính nhầm chi phí đơn vị.
   - B. Vì phương pháp Heuristic mang tính tham lam cục bộ, làm cạn kiệt năng lực của các nguồn giá rẻ và ép buộc các phân bổ cuối cùng phải đi vào các tuyến có cước phí cực đắt.
   - C. Vì thuật toán Simplex LP không áp dụng được cho thực tế.
   - D. Vì phương pháp Heuristic chỉ giải được các bài toán có quy mô dưới 3 nhà máy.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Bản chất của phương pháp Heuristic trực giác là tham lam cục bộ (Greedy approach). Việc vội vã lấp đầy các tuyến cước thấp ban đầu khiến năng lực cung ứng giá rẻ cạn kiệt sớm, ép buộc các đợt giao hàng cuối cùng phải rơi vào các tuyến cước cấm hoặc cực đắt, làm tổng chi phí chuỗi tăng vọt.</p>
  </div>
</details>"""

c1 = c1.replace(c1_q1_target, c1_q1_repl)
c1 = c1.replace(c1_q2_target, c1_q2_repl)

with open('outputs/content/chapters/CHAP_01.md', 'w', encoding='utf-8') as f:
    f.write(c1)
print("CHAP_01.md updated.")
