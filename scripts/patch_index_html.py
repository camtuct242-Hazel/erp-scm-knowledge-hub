with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace view-chapter-reader
reader_start = html.find('<section id="view-chapter-reader"')
reader_end = html.find('<!-- ================= VIEW: EXAM SELECTION ================= -->', reader_start)

new_reader_html = """<!-- ================= VIEW: CHAPTER READER ================= -->
      <section id="view-chapter-reader" class="view-section">
        <!-- Top Navigation & Action Bar -->
        <div class="chapter-reader-top-bar">
          <div class="chapter-nav-cluster">
            <button class="btn btn-outline btn-sm chapter-nav-btn" id="chapter-nav-prev-top" onclick="App.prevChapter()">
              ← <span data-i18n="btn_prev_chapter">Chương trước</span>
            </button>
            <button class="btn btn-outline btn-sm chapter-nav-btn" id="chapter-nav-list-top" onclick="App.navigateTo('chapters')">
              📑 <span data-i18n="btn_chapter_list">Danh sách chương</span>
            </button>
            <button class="btn btn-outline btn-sm chapter-nav-btn" id="chapter-nav-next-top" onclick="App.nextChapter()">
              <span data-i18n="btn_next_chapter">Chương tiếp theo</span> →
            </button>
          </div>
          <div style="display: flex; gap: 0.8rem; align-items: center; flex-wrap: wrap;">
            <label style="display: flex; align-items: center; gap: 0.4rem; cursor: pointer; font-size: 0.88rem; font-weight: 600;">
              <input type="checkbox" id="chapter-completed-checkbox" onchange="App.toggleChapterCompleted()">
              <span data-i18n="chk_mark_completed">Đã hoàn thành chương này</span>
            </label>
            <button class="btn btn-secondary btn-sm" onclick="App.jumpToChapterExam()"><span data-i18n="btn_practice_this_chapter">Luyện câu hỏi chương này</span> →</button>
          </div>
        </div>

        <!-- Chapter Header Banner -->
        <div class="chapter-header-banner">
          <span class="badge badge-rose" id="chapter-reader-badge">Chương 01</span>
          <h1 id="chapter-reader-title" class="chapter-banner-title">Tổng quan Hệ thống ERP</h1>
          <div id="chapter-reader-subtitle" class="chapter-banner-subtitle">Cấu trúc 12 phần sư phạm chuẩn mực</div>
        </div>

        <div class="chapter-reader-layout">
          <!-- Sticky Table of Contents -->
          <aside class="chapter-sidebar">
            <h4 style="font-size: 0.95rem; margin-bottom: 1rem; color: var(--coffee-bean); border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;" data-i18n="toc_title">Mục Lục 12 Phần</h4>
            <ul class="chapter-nav-list" id="chapter-toc-list">
              <!-- Dynamically populated -->
            </ul>
          </aside>

          <!-- Rendered Article Body & Bottom Nav -->
          <div style="flex: 1; min-width: 0;">
            <article class="chapter-article" id="chapter-content-body">
              <!-- Rendered markdown with KaTeX & Mermaid -->
            </article>

            <!-- Bottom Chapter Navigation -->
            <div class="chapter-reader-bottom-nav">
              <button class="btn btn-outline chapter-nav-btn" id="chapter-nav-prev-bottom" onclick="App.prevChapter()">
                ← <span data-i18n="btn_prev_chapter">Chương trước</span>
              </button>
              <button class="btn btn-outline chapter-nav-btn" id="chapter-nav-list-bottom" onclick="App.navigateTo('chapters')">
                📑 <span data-i18n="btn_chapter_list">Danh sách chương</span>
              </button>
              <button class="btn btn-outline chapter-nav-btn" id="chapter-nav-next-bottom" onclick="App.nextChapter()">
                <span data-i18n="btn_next_chapter">Chương tiếp theo</span> →
              </button>
            </div>
          </div>
        </div>
      </section>

      """

if reader_start != -1 and reader_end != -1:
    html = html[:reader_start] + new_reader_html + html[reader_end:]
    print("Replaced view-chapter-reader in index.html")

# 2. Add Exit Exam Modal
exit_modal_html = """
    <!-- Exit Exam Confirmation Modal -->
    <div id="modal-exit-exam" class="modal-overlay">
      <div class="modal-card">
        <h3 style="font-size: 1.3rem; margin-bottom: 0.8rem; color: var(--danger);" id="modal-exit-title" data-i18n="modal_exit_title">Thoát bài thi?</h3>
        <p style="color: var(--text-main); margin-bottom: 1.5rem; line-height: 1.6;" id="modal-exit-body" data-i18n="modal_exit_body">
          Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>
          Bạn có chắc chắn muốn thoát không?
        </p>
        <div style="display: flex; justify-content: flex-end; gap: 0.8rem;">
          <button class="btn btn-outline" onclick="App.closeExitConfirmationModal()"><span data-i18n="btn_continue_exam">Tiếp tục làm bài</span></button>
          <button class="btn btn-primary" style="background-color: var(--danger); border-color: var(--danger);" onclick="App.confirmExitExam()"><span data-i18n="btn_confirm_exit">Thoát và xóa bài thi</span></button>
        </div>
      </div>
    </div>
"""

if 'id="modal-exit-exam"' not in html:
    submit_modal_end = html.find('</div>\n    </div>\n\n    <!-- Glossary Detail Modal -->')
    if submit_modal_end != -1:
        html = html[:submit_modal_end+11] + exit_modal_html + html[submit_modal_end+11:]
        print("Added modal-exit-exam to index.html")
    else:
        # fallback before footer
        footer_idx = html.find('<!-- Footer -->')
        html = html[:footer_idx] + exit_modal_html + html[footer_idx:]
        print("Added modal-exit-exam before footer")

# 3. Update Exit button in active exam view
html = html.replace('onclick="App.exitExam()"><span data-i18n="btn_exit_exam">Thoát & Bỏ Dở</span>',
                    'id="btn-exit-exam-active" style="width: 100%; border-color: var(--danger); color: var(--danger);" onclick="App.openExitConfirmationModal()"><span data-i18n="btn_exit_exam">Thoát bài thi</span>')

with open('outputs/app/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated!")
