with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Head: Replace KaTeX and Marked CDN with local vendor paths
old_head_libs = """  <!-- KaTeX for Math -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  
  <!-- Marked.js for Markdown -->
  <script src="https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js"></script>"""

new_head_libs = """  <!-- KaTeX for Math (Local Offline) -->
  <link rel="stylesheet" href="vendor/katex/katex.min.css">
  <script src="vendor/katex/katex.min.js"></script>
  <script src="vendor/katex/auto-render.min.js"></script>
  
  <!-- Marked.js for Markdown (Local Offline) -->
  <script src="vendor/marked.min.js"></script>"""

if old_head_libs in html:
    html = html.replace(old_head_libs, new_head_libs)
    print("Replaced CDN head scripts with local vendor paths.")
else:
    print("Warning: old_head_libs exact match not found.")

# 2. Update Flashcards Section
old_fc_section_start = '<section id="view-flashcards" class="view-section">'
old_fc_section_end = '</section>\n\n      <!-- ================= VIEW: GLOSSARY ================= -->'

new_fc_section = """<section id="view-flashcards" class="view-section">
        <div class="page-header">
          <div>
            <span class="badge badge-rose" data-i18n="badge_flashcards">Học Nhanh & Ghi Nhớ Lâu</span>
            <h1 data-i18n="flashcards_title">Thẻ Ghi Nhớ Khái Niệm, Công Thức & Quy Tắc ERP</h1>
            <p style="color: var(--muted-mauve); font-size: 0.92rem;" data-i18n="flashcards_sub">Lật thẻ để kiểm tra phản xạ kiến thức. Đánh dấu thẻ đã thuộc để tối ưu lộ trình lặp lại ngắt quãng (Spaced Repetition).</p>
          </div>
          <div style="display: flex; gap: 0.6rem; align-items: center; flex-wrap: wrap;">
            <span class="badge badge-beige" id="fc-progress-counter">1 / 62</span>
            <button class="btn btn-outline btn-sm" onclick="App.shuffleFlashcards()">🔀 <span data-i18n="btn_shuffle">Trộn Thẻ</span></button>
          </div>
        </div>

        <!-- Filter controls -->
        <div class="fc-filters-row">
          <select id="fc-chapter-select" class="fc-chapter-select" onchange="App.filterFlashcardsByChapter(this.value)">
            <option value="all">📚 Tất Cả Các Chương (All Chapters)</option>
            <option value="chap-01">Chương 1: Tổng quan ERP & Vận tải Tuyến tính</option>
            <option value="chap-02">Chương 2: Biến thể Vận tải & Tuyến cấm</option>
            <option value="chap-03">Chương 3: Trung chuyển & Phân công Nhị phân</option>
            <option value="chap-04">Chương 4: Quản trị Tồn kho & EOQ Cơ bản</option>
            <option value="chap-05">Chương 5: Biến thể EOQ: Thiếu hàng, Chiết khấu & EPQ</option>
            <option value="chap-06">Chương 6: Tích hợp Quy trình ERP (O2C & P2P)</option>
          </select>

          <div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
            <button class="btn btn-outline btn-sm active" id="fc-filter-all" onclick="App.filterFlashcardsCategory('all')"><span data-i18n="fc_filter_all">Tất Cả Loại</span></button>
            <button class="btn btn-outline btn-sm" id="fc-filter-formula" onclick="App.filterFlashcardsCategory('Formula')"><span data-i18n="fc_filter_formulas">Công Thức</span></button>
            <button class="btn btn-outline btn-sm" id="fc-filter-rule" onclick="App.filterFlashcardsCategory('Business Rule')"><span data-i18n="fc_filter_rules">Quy Tắc ERP</span></button>
            <button class="btn btn-outline btn-sm" id="fc-filter-model" onclick="App.filterFlashcardsCategory('Model')"><span>Mô Hình</span></button>
            <button class="btn btn-outline btn-sm" id="fc-filter-ba" onclick="App.filterFlashcardsCategory('BA Perspective')"><span>Góc Nhìn BA</span></button>
          </div>

          <div style="display: flex; gap: 0.4rem; margin-left: auto;">
            <button class="btn btn-outline btn-sm" id="fc-filter-unmastered" onclick="App.filterFlashcardsStatus('unmastered')"><span data-i18n="fc_filter_needs_review">⏳ Cần Ôn Lại</span></button>
            <button class="btn btn-outline btn-sm" id="fc-filter-mastered" onclick="App.filterFlashcardsStatus('mastered')"><span>✓ Đã Thuộc</span></button>
          </div>
        </div>

        <div class="flashcards-container">
          <div class="flashcard-wrapper" onclick="App.flipFlashcard()">
            <div class="flashcard-inner" id="flashcard-card-element">
              <!-- Front -->
              <div class="flashcard-face flashcard-front">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span class="flashcard-category" id="fc-front-category">ĐỊNH NGHĨA CỐT LÕI</span>
                  <div style="display: flex; gap: 0.4rem; align-items: center;">
                    <span class="badge badge-beige" id="fc-front-chapter">Chương 1</span>
                    <span class="badge badge-rose" id="fc-front-difficulty">Cơ bản</span>
                  </div>
                </div>
                <div class="flashcard-topic-tag" id="fc-front-topic">Tổng quan ERP</div>
                <div class="flashcard-prompt" id="fc-front-prompt">
                  Câu hỏi đang được nạp...
                </div>
                <div class="flashcard-keywords" id="fc-front-keywords">
                  <!-- Keywords tags -->
                </div>
                <div class="flashcard-hint" data-i18n="fc_hint_flip">
                  💡 Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án
                </div>
              </div>
              <!-- Back -->
              <div class="flashcard-face flashcard-back">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <span class="flashcard-category" id="fc-back-category">GIẢI NGHĨA & HÀM Ý ERP</span>
                  <span class="badge badge-rose" id="fc-back-status">Cần ôn tập</span>
                </div>
                <div class="flashcard-topic-tag" id="fc-back-topic">Tổng quan ERP</div>
                <div class="flashcard-answer" id="fc-back-answer">
                  Nội dung chi tiết của thẻ ghi nhớ...
                </div>
                <div class="flashcard-example-box" id="fc-back-example">
                  <!-- Practical example note -->
                </div>
                <div class="flashcard-hint" data-i18n="fc_hint_back">
                  Nhấn lần nữa để lật lại mặt trước
                </div>
              </div>
            </div>
          </div>

          <!-- Controls -->
          <div class="flashcard-controls">
            <button class="btn btn-outline" onclick="App.prevFlashcard()">← <span data-i18n="btn_prev_card">Thẻ Trước</span></button>
            <button class="btn btn-outline" style="border-color: var(--danger); color: var(--danger);" onclick="App.markFlashcardNeedsReview()">❌ <span data-i18n="btn_needs_review">Cần Ôn Lại</span></button>
            <button class="btn btn-primary" style="background-color: var(--success);" onclick="App.markFlashcardMastered()">✓ <span data-i18n="btn_mastered">Đã Thuộc</span></button>
            <button class="btn btn-outline" onclick="App.nextFlashcard()"><span data-i18n="btn_next_card">Thẻ Kế Tiếp</span> →</button>
          </div>
        </div>
      </section>"""

pos_fc_start = html.find(old_fc_section_start)
pos_fc_end = html.find(old_fc_section_end)
if pos_fc_start != -1 and pos_fc_end != -1:
    html = html[:pos_fc_start] + new_fc_section + html[pos_fc_end + len('</section>'):]
    print("Replaced Flashcards section with enhanced 62-card interface.")
else:
    print("Warning: Flashcard section boundaries not found.")

# 3. Update AI Consultant Section (Unified Chat Interface)
old_ai_start = '<section id="view-consultant" class="view-section">'
old_ai_end = '</section>\n\n      <!-- ================= VIEW: ABOUT ================= -->'

new_ai_section = """<section id="view-consultant" class="view-section">
        <div class="page-header">
          <div>
            <span class="badge badge-rose" data-i18n="badge_ai_mentor">Trợ Lý Học Tập Thông Minh</span>
            <h1 data-i18n="ai_title">Cố Vấn Tri Thức ERP & Chuỗi Cung Ứng AI</h1>
            <p style="color: var(--muted-mauve); font-size: 0.92rem;" data-i18n="ai_sub">Một không gian hội thoại hợp nhất kết hợp tri thức 6 chương giáo trình, 4 case studies kinh điển và 250 câu hỏi trắc nghiệm.</p>
          </div>
          <div style="display: flex; gap: 0.6rem; align-items: center; flex-wrap: wrap;">
            <button class="btn btn-outline btn-sm" onclick="App.confirmClearChat()">🧹 <span data-i18n="btn_clear_chat">Xóa Hội Thoại</span></button>
            <button class="btn btn-outline btn-sm" onclick="App.openApiKeyModal()">⚙️ <span data-i18n="btn_api_settings">Cấu hình API Key (Tùy chọn)</span></button>
          </div>
        </div>

        <div class="unified-chat-layout">
          <!-- Chat Header Bar -->
          <div class="unified-chat-header">
            <div style="display: flex; align-items: center; gap: 0.8rem;">
              <div class="brand-icon" style="width: 34px; height: 34px; font-size: 1rem;">AI</div>
              <div>
                <strong style="font-size: 1rem; color: var(--coffee-bean);">Hội Thoại Trợ Lý Tri Thức ERP & SCM</strong>
                <div style="font-size: 0.78rem; color: var(--muted-mauve);">Học liệu tham chiếu giáo trình UEH 2020 & 4 Case Studies</div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.6rem;">
              <span id="chat-mode-badge" class="badge badge-beige">🤖 Chế độ Tri thức Offline (Grounded Mode)</span>
            </div>
          </div>

          <!-- Context Selector Bar -->
          <div class="unified-chat-context-bar">
            <span style="font-weight: 600; color: var(--coffee-bean);">🎯 Ngữ cảnh tham vấn:</span>
            <label style="display: flex; align-items: center; gap: 0.3rem;">
              <span>Chương:</span>
              <select id="chat-context-chapter" class="chat-context-select" onchange="App.setChatContextChapter(this.value)">
                <option value="all">Tất cả 6 chương học</option>
                <option value="chap-01">Chương 1: Tổng quan ERP & Vận tải Tuyến tính</option>
                <option value="chap-02">Chương 2: Biến thể Vận tải & Ràng buộc</option>
                <option value="chap-03">Chương 3: Trung chuyển & Phân công Nhị phân</option>
                <option value="chap-04">Chương 4: Quản trị Tồn kho & EOQ Cơ bản</option>
                <option value="chap-05">Chương 5: Biến thể EOQ: Thiếu hàng, Chiết khấu & EPQ</option>
                <option value="chap-06">Chương 6: Tích hợp Quy trình ERP (O2C & P2P)</option>
              </select>
            </label>
            <label style="display: flex; align-items: center; gap: 0.3rem;">
              <span>Tình huống:</span>
              <select id="chat-context-case" class="chat-context-select" onchange="App.setChatContextCase(this.value)">
                <option value="none">Không chọn tình huống cụ thể</option>
                <option value="CASE-01">Case 1: Texago Corp. (Chọn địa điểm lọc dầu)</option>
                <option value="CASE-02">Case 2: Better Products (Phân công nhà máy)</option>
                <option value="CASE-03">Case 3: Atlantic Coast Tire (Quản trị tồn kho EOQ)</option>
                <option value="CASE-04">Case 4: SOCA (Sản xuất bổ sung dần EPQ)</option>
              </select>
            </label>
          </div>

          <!-- Messages Container -->
          <div class="unified-chat-messages" id="chat-messages-container">
            <!-- Messages rendered dynamically -->
          </div>

          <!-- Predefined Scenario Chips Bar -->
          <div class="unified-chat-suggestions">
            <div style="font-size: 0.76rem; font-weight: 700; color: var(--muted-mauve); margin-bottom: 0.4rem; text-transform: uppercase;">
              💡 Chọn mẫu kịch bản để đưa prompt vào ô soạn thảo:
            </div>
            <div class="suggestions-scroll-row" id="scenario-chips-container">
              <!-- Suggestion prompt chips rendered dynamically -->
            </div>
          </div>

          <!-- Input Area -->
          <div class="unified-chat-input-area">
            <textarea id="chat-user-input" class="chat-textarea" placeholder="Nhập câu hỏi thảo luận hoặc nhấp chọn một gợi ý phía trên (Nhấn Enter để gửi, Shift+Enter để xuống dòng)..." onkeydown="App.handleChatKeyDown(event)"></textarea>
            <button class="btn btn-primary" id="chat-send-btn" onclick="App.sendChatMessage()" style="height: 48px; padding: 0 1.5rem; display: flex; align-items: center; gap: 0.4rem;">
              <span data-i18n="btn_send">Gửi</span> ➔
            </button>
          </div>
        </div>
      </section>"""

pos_ai_start = html.find(old_ai_start)
pos_ai_end = html.find(old_ai_end)
if pos_ai_start != -1 and pos_ai_end != -1:
    html = html[:pos_ai_start] + new_ai_section + html[pos_ai_end + len('</section>'):]
    print("Replaced AI Consultant section with Unified Chat Interface.")
else:
    print("Warning: AI Consultant section boundaries not found.")

# 4. Update Footer with Required Author Attribution
old_footer_start = '<footer class="app-footer">'
old_footer_end = '</footer>\n  </div>'

new_footer = """<footer class="app-footer">
      <div style="max-width: 900px; margin: 0 auto; text-align: center;">
        <div style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; color: var(--coffee-bean); margin-bottom: 0.3rem;">
          ERP & Supply Chain Management Knowledge Hub
        </div>
        <div class="footer-tagline-text" data-i18n="footer_tagline">
          An independent educational knowledge platform.
        </div>
        <div class="footer-author-box" data-i18n="footer_author">
          Created by Nguyễn Đăng Cẩm Tú (Hazel)
        </div>
        <div style="font-size: 0.8rem; color: var(--text-subtle); margin-top: 0.6rem;" data-i18n="footer_academic_note">
          Bilingual Platform (Vietnamese / English) • Aligned with UEH 2020 Textbook & Business Analyst Competency Framework
        </div>
      </div>
    </footer>"""

pos_ft_start = html.find(old_footer_start)
pos_ft_end = html.find(old_footer_end)
if pos_ft_start != -1 and pos_ft_end != -1:
    html = html[:pos_ft_start] + new_footer + html[pos_ft_end + len('</footer>'):]
    print("Updated footer with author attribution.")
else:
    print("Warning: Footer boundaries not found.")

# 5. Add Floating Scroll-to-Top Button
scroll_btn_html = """    <!-- Floating Scroll-To-Top Button -->
    <button id="scroll-to-top-btn" class="scroll-to-top-btn" onclick="App.scrollToTop()" title="Lên đầu trang / Scroll to top" aria-label="Scroll to top">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M18 15l-6-6-6 6"/>
      </svg>
    </button>
  </div>"""

if "scroll-to-top-btn" not in html:
    html = html.replace('  </div>\n\n  <!-- Load Embedded Datasets First -->', scroll_btn_html + '\n\n  <!-- Load Embedded Datasets First -->')
    print("Added Floating Scroll-To-Top button HTML.")

with open('outputs/app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated! Length:", len(html))
