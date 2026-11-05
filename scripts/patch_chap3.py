with open('outputs/content/chapters/CHAP_03.md', 'r', encoding='utf-8') as f:
    c3 = f.read()

# 1. Replace the BA commentary with the exact professional BA Insight callout
target_ba = "*(Nhận xét của BA: Mặc dù Case 2.2 có chi phí toán học cao hơn \\$30/ngày, nhưng trong thực tế, chi phí quản lý và chi phí thiết lập máy tiết kiệm được vượt xa con số \\$30 này. Do đó, phương án Case 2.2 luôn được ưu tiên trong thực tế sản xuất).*"

repl_ba = """<div class="ba-insight-callout">
  <div class="ba-insight-header">
    <span class="ba-insight-icon">💡</span>
    <strong>Góc nhìn Business Analyst — Đánh đổi giữa chi phí trực tiếp và chi phí vận hành</strong>
  </div>
  <p>Mặc dù phương án Case 2.2 có chi phí trực tiếp cao hơn Case 2.1 là 30 USD/ngày, phương án này vẫn có thể mang lại hiệu quả kinh tế tốt hơn nếu giúp doanh nghiệp tiết kiệm chi phí đổi khuôn, thời gian thiết lập máy và chi phí quản lý vận hành.</p>
  <p>Tuy nhiên, không thể kết luận Case 2.2 luôn tốt hơn trong mọi trường hợp. Business Analyst cần định lượng tổng chi phí của cả hai phương án, bao gồm chi phí sản xuất trực tiếp, chi phí setup, chi phí quản lý và các chi phí liên quan khác, trước khi đưa ra khuyến nghị.</p>
  
  <div class="ba-insight-divider"></div>
  
  <div class="ba-insight-header-en">
    <strong>Business Analyst Insight — Trade-off Between Direct and Operational Costs</strong>
  </div>
  <p class="ba-insight-text-en">Although Case 2.2 has a direct cost that is USD 30/day higher than Case 2.1, it may still be economically preferable if it reduces machine setup costs, setup time, and operational management expenses.</p>
  <p class="ba-insight-text-en">However, Case 2.2 should not automatically be considered superior in every situation. A Business Analyst should quantify the total cost of both alternatives, including direct production costs, setup costs, management expenses, and other relevant operational costs before making a recommendation.</p>
</div>"""

if target_ba in c3:
    c3 = c3.replace(target_ba, repl_ba, 1)
    print("Found and replaced target_ba in CHAP_03.md")
else:
    # Try finding with regex or substring
    idx = c3.find('Nhận xét của BA')
    if idx != -1:
        line_start = c3.rfind('\n', 0, idx) + 1
        line_end = c3.find('\n', idx)
        print("Found line:", repr(c3[line_start:line_end]))
        c3 = c3[:line_start] + repl_ba + c3[line_end:]
        print("Replaced line in CHAP_03.md")

# 2. Format Section 12 review questions as accordion
sec12_heading_idx = c3.find('## 12. Kiểm tra Đánh giá Kiến thức')
sec12_content = """## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Để chuyển đổi bài toán vận tải cực đại hóa lợi nhuận $\\max \\sum P_{ij} x_{ij}$ thành bài toán cực tiểu hóa chi phí giải được trên các thuật toán thông thường, ta sử dụng phép biến đổi nào?
   - A. $c_{ij} = -P_{ij}$
   - B. $c_{ij} = P_{\\max} - P_{ij}$ (trong đó $P_{\\max}$ là lợi nhuận đơn vị lớn nhất trong ma trận)
   - C. $c_{ij} = 1 / P_{ij}$
   - D. $c_{ij} = P_{ij} \\times 100$

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Để biến đổi bài toán cực đại hóa lợi nhuận sang cực tiểu hóa chi phí mà vẫn giữ mọi hệ số chi phí không âm ($c_{ij} \\ge 0$), ta áp dụng phép tịnh tiến đối ngẫu: $c_{ij} = P_{\\max} - P_{ij}$. Khi đó, tối thiểu hóa tổn thất cơ hội chính là tối đa hóa tổng lợi nhuận thu về.</p>
  </div>
</details>

2. **Câu hỏi:** Tại sao trong Case 2.2 (Better Products), ban lãnh đạo công ty lại chấp nhận mức chi phí $3.290/ngày (cao hơn $30/ngày so với mức $3.260/ngày của Case 2.1)?
   - A. Do tính nhầm số liệu chi phí.
   - B. Vì chính sách không chia nhỏ sản phẩm giúp chuyên môn hóa dây chuyền, loại bỏ chi phí đổi khuôn (setup cost) và giảm gánh nặng giám sát quản trị vận hành vượt xa khoản chênh lệch $30/ngày.
   - C. Vì luật pháp quy định mỗi nhà máy chỉ được sản xuất 1 sản phẩm.
   - D. Vì công đoàn từ chối sản xuất chia nhỏ.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Mặc dù Case 2.2 có chi phí trực tiếp cao hơn 30 USD/ngày ($30/day), nhưng trên thực tế phân xưởng, việc không chia nhỏ sản phẩm giúp mỗi nhà máy tập trung chuyên môn hóa một dòng sản phẩm duy nhất. Nhờ đó công ty tiết kiệm đáng kể thời gian dừng máy thay đổi khuôn mẫu (changeover time) và giảm thiểu rủi ro lẫn lộn chất lượng.</p>
  </div>
</details>
"""

if sec12_heading_idx != -1:
    c3 = c3[:sec12_heading_idx] + sec12_content

with open('outputs/content/chapters/CHAP_03.md', 'w', encoding='utf-8') as f:
    f.write(c3)

print("CHAP_03.md patched successfully!")
