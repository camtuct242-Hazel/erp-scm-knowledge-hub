# Patch Chapters 4, 5, 6 review questions

# --- Chapter 4 ---
with open('outputs/content/chapters/CHAP_04.md', 'r', encoding='utf-8') as f:
    c4 = f.read()

sec12_heading_c4 = c4.find('## 12. Kiểm tra Đánh giá Kiến thức')
sec12_content_c4 = """## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Trong mô hình EOQ cơ bản không có chiết khấu, khi quy mô lô hàng đặt mua ($Q$) tăng lên gấp đôi, chi phí lưu kho hàng năm (AHC) và chi phí đặt hàng hàng năm (AOC) sẽ biến động như thế nào?
   - A. AHC tăng gấp đôi, AOC giảm đi một nửa.
   - B. Cả AHC và AOC đều tăng gấp đôi.
   - C. AHC giảm một nửa, AOC tăng gấp đôi.
   - D. Cả hai chi phí đều không thay đổi.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: A</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Chi phí lưu kho hàng năm $\\text{AHC} = h \\times (Q/2)$ tỷ lệ thuận bậc nhất với $Q$, do đó khi $Q$ tăng gấp đôi thì AHC tăng gấp đôi. Ngược lại, chi phí đặt hàng hàng năm $\\text{AOC} = K \\times (D/Q)$ tỷ lệ nghịch với $Q$, do đó khi $Q$ tăng gấp đôi thì số lần đặt hàng giảm một nửa kéo theo AOC giảm đi một nửa.</p>
  </div>
</details>

2. **Câu hỏi:** Trong tình huống Atlantic Coast Tire (ACT), nếu tốc độ tiêu thụ là 24 lốp/ngày và thời gian giao hàng là 7,5 ngày làm việc, điểm đặt hàng lại (ROP) là bao nhiêu khi không xét tồn kho an toàn?
   - A. 573 lốp
   - B. 1.000 lốp
   - C. 180 lốp
   - D. 240 lốp

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: C</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Áp dụng công thức điểm đặt hàng lại chuẩn tắc khi không có tồn kho an toàn: $\\text{ROP} = d \\times L = 24\\text{ lốp/ngày} \\times 7,5\\text{ ngày} = 180\\text{ chiếc lốp}$.</p>
  </div>
</details>
"""

if sec12_heading_c4 != -1:
    c4 = c4[:sec12_heading_c4] + sec12_content_c4
with open('outputs/content/chapters/CHAP_04.md', 'w', encoding='utf-8') as f:
    f.write(c4)
print("CHAP_04.md patched.")

# --- Chapter 5 ---
with open('outputs/content/chapters/CHAP_05.md', 'r', encoding='utf-8') as f:
    c5 = f.read()

sec12_heading_c5 = c5.find('## 12. Kiểm tra Đánh giá Kiến thức')
sec12_content_c5 = """## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Trong mô hình bổ sung dần (EPQ - Gradual Replenishment), tại sao mức tồn kho cực đại ($I_{\\max}$) luôn nhỏ hơn kích cỡ lô sản xuất ($Q$)?
   - A. Do hàng bị hao hụt và hỏng hóc trong quá trình gia công.
   - B. Do trong suốt thời gian dây chuyền đang chạy sản xuất để tạo ra lô $Q$, hàng hóa thành phẩm cũng đồng thời liên tục bị rút ra để tiêu thụ với tốc độ $d$.
   - C. Do nhà xưởng không có đủ chỗ chứa.
   - D. Do công nhân đình công giữa ca.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Khác với mô hình EOQ bổ sung tức thời (nhập toàn bộ $Q$ cùng lúc), mô hình EPQ có tốc độ sản xuất hữu hạn $p$. Trong thời gian chạy máy $t_1 = Q/p$, sản phẩm vừa được tạo ra vừa bị tiêu thụ với tốc độ $d$, do đó tốc độ tích lũy tồn kho ròng trong kho chỉ là $(p - d)$, dẫn đến đỉnh tồn kho $I_{\\max} = Q(1 - d/p) < Q$.</p>
  </div>
</details>

2. **Câu hỏi:** Trong tình huống Atlantic Coast Tire (ACT) áp dụng chính sách chiết khấu số lượng, tại sao phương án đặt $Q = 2.000$ chiếc với đơn giá rẻ nhất ($19,60 USD) lại không được lựa chọn làm điểm tối ưu?
   - A. Vì nhà cung cấp không đủ năng lực giao 2.000 chiếc.
   - B. Vì chi phí lưu kho hàng năm cho lô hàng 2.000 chiếc tăng vọt lên mức $4.116 USD/năm, vượt xa khoản tiền tiết kiệm được từ việc giảm giá mua và giảm số lần đặt hàng, khiến tổng chi phí năm tại $Q = 2.000$ cao hơn mức tối ưu tại $Q = 1.000$.
   - C. Vì chất lượng lô hàng 2.000 lốp bị kém hơn.
   - D. Vì kho hàng của công ty ACT bị ngập nước.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Khi phân tích chiết khấu số lượng theo bậc thang, ta phải so sánh Tổng Chi phí Hàng năm (TAC bao gồm cả tiền mua hàng). Tại $Q = 1.000$ lốp ($c = 19,70$ USD), $\\text{TAC} = 120.970$ USD. Tại $Q = 2.000$ lốp ($c = 19,60$ USD), $\\text{TAC} = 122.061$ USD (đắt hơn gần $1.100$ USD/năm do gánh nặng chi phí lưu giữ lô hàng quá lớn).</p>
  </div>
</details>
"""

if sec12_heading_c5 != -1:
    c5 = c5[:sec12_heading_c5] + sec12_content_c5
with open('outputs/content/chapters/CHAP_05.md', 'w', encoding='utf-8') as f:
    f.write(c5)
print("CHAP_05.md patched.")

# --- Chapter 6 ---
with open('outputs/content/chapters/CHAP_06.md', 'r', encoding='utf-8') as f:
    c6 = f.read()

sec12_heading_c6 = c6.find('## 12. Kiểm tra Đánh giá Kiến thức')
sec12_content_c6 = """## 12. Kiểm tra Đánh giá Kiến thức (Knowledge Check)

1. **Câu hỏi:** Trong chu trình mua hàng Procure-to-Pay (P2P), cơ chế đối chiếu tự động 3 chiều (3-Way Matching) thực hiện so sánh thông tin giữa những chứng từ nào sau đây?
   - A. Báo giá của nhà cung cấp, Hợp đồng kinh tế và Biên bản thanh lý.
   - B. Đơn đặt hàng mua (Purchase Order), Phiếu nhập kho (Goods Receipt Note) và Hóa đơn tài chính của nhà cung cấp (Supplier Invoice).
   - C. Đơn đặt hàng bán (Sales Order), Phiếu xuất kho và Giấy báo nợ của ngân hàng.
   - D. Yêu cầu mua hàng nội bộ (Purchase Requisition), Thẻ kho và Bảng chấm công.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Đối chiếu 3 bên (3-Way Matching) là chốt chặn kiểm soát nội bộ cốt lõi trong phân hệ ERP MM-FI: Hệ thống tự động so khớp Số lượng & Đơn giá trên PO, Số lượng thực nhận trên GR, và Số lượng & Số tiền yêu cầu thanh toán trên Supplier Invoice. Nếu sai lệch vượt ngưỡng dung sai (tolerance limit), hệ thống tự động khóa thanh toán.</p>
  </div>
</details>

2. **Câu hỏi:** Khi một sự kiện xuất kho hàng thành phẩm để giao cho khách hàng (Post Goods Issue - PGI) được ghi nhận trong phân hệ Bán hàng và Phân phối (SD), hệ thống ERP sẽ tự động tạo bút toán kế toán tài chính (FI) nào sau đây?
   - A. Ghi Nợ tài khoản Tiền mặt / Ghi Có tài khoản Doanh thu.
   - B. Ghi Nợ tài khoản Giá vốn hàng bán (Cost of Goods Sold - COGS) / Ghi Có tài khoản Tồn kho thành phẩm (Inventory Finished Goods).
   - C. Ghi Nợ tài khoản Phải thu khách hàng / Ghi Có tài khoản Tạm ứng.
   - D. Ghi Nợ tài khoản Chi phí quản lý doanh nghiệp / Ghi Có tài khoản Tiền gửi ngân hàng.

<details class="review-answer-accordion">
  <summary class="review-answer-toggle">
    <span class="btn-reveal-text">💡 Xem đáp án và giải thích / Reveal answer and explanation</span>
  </summary>
  <div class="review-answer-content">
    <p><strong>✓ Đáp án đúng: B</strong></p>
    <p><strong>Giải thích chi tiết:</strong> Xuất kho giao hàng (PGI) là sự kiện chuyển quyền sở hữu hàng hóa từ kho sang khách hàng. Tại thời điểm này, giá trị hàng hóa giảm (Ghi Có TK Tồn kho) và chuyển hóa thành chi phí trực tiếp của kỳ kinh doanh (Ghi Nợ TK Giá vốn hàng bán - COGS) theo đúng nguyên tắc kế toán dồn tích.</p>
  </div>
</details>
"""

if sec12_heading_c6 != -1:
    c6 = c6[:sec12_heading_c6] + sec12_content_c6
with open('outputs/content/chapters/CHAP_06.md', 'w', encoding='utf-8') as f:
    f.write(c6)
print("CHAP_06.md patched.")
