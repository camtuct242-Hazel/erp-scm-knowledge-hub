with open('outputs/content/chapters/CHAP_01.md', 'r', encoding='utf-8') as f:
    c1 = f.read()

q2_old = """2. **Câu hỏi:** Tại sao phương pháp giải trực quan Heuristic (chọn tuyến rẻ nhất trước) lại thường dẫn đến tổng chi phí cao hơn thuật toán Simplex LP?
   - A. Vì phương pháp Heuristic tính nhầm chi phí đơn vị.
   - B. Vì phương pháp Heuristic mang tính tham lam cục bộ, làm cạn kiệt năng lực của các nguồn giá rẻ và ép buộc các phân bổ cuối cùng phải đi vào các tuyến có chi phí cực đắt.
   - C. Vì phương pháp Heuristic không áp dụng được trên máy tính.
   - D. Vì Heuristic không tính đến thuế giá trị gia tăng.
   - *Đáp án đúng:* **B**."""

q2_new = """2. **Câu hỏi:** Tại sao phương pháp giải trực quan Heuristic (chọn tuyến rẻ nhất trước) lại thường dẫn đến tổng chi phí cao hơn thuật toán Simplex LP?
   - A. Vì phương pháp Heuristic tính nhầm chi phí đơn vị.
   - B. Vì phương pháp Heuristic mang tính tham lam cục bộ, làm cạn kiệt năng lực của các nguồn giá rẻ và ép buộc các phân bổ cuối cùng phải đi vào các tuyến có chi phí cực đắt.
   - C. Vì phương pháp Heuristic không áp dụng được trên máy tính.
   - D. Vì Heuristic không tính đến thuế giá trị gia tăng.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Bản chất của phương pháp Heuristic trực giác là tham lam cục bộ (Greedy approach). Việc vội vã lấp đầy các tuyến cước thấp ban đầu khiến năng lực cung ứng giá rẻ cạn kiệt sớm, ép buộc các đợt giao hàng cuối cùng phải rơi vào các tuyến cước cấm hoặc cực đắt, làm tổng chi phí chuỗi tăng vọt.</p>
  </div>
</details>"""

c1 = c1.replace(q2_old, q2_new)

with open('outputs/content/chapters/CHAP_01.md', 'w', encoding='utf-8') as f:
    f.write(c1)

print("CHAP_01.md Question 2 patched successfully!")
