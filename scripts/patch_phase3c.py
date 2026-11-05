import re

# 1. Patch outputs/app/index.html
with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Fix buttons in view-exam-active
old_buttons = '''            <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.6rem;">
              <button class="btn btn-primary" style="width: 100%;" onclick="App.openSubmitConfirmationModal()"><span data-i18n="btn_submit_exam">Nộp Bài Thi</span></button>
              <button class="btn btn-outline btn-sm" style="width: 100%;" id="btn-exit-exam-active" style="width: 100%; border-color: var(--danger); color: var(--danger);" onclick="App.openExitConfirmationModal()"><span data-i18n="btn_exit_exam">Thoát bài thi</span></button>
            </div>'''

new_buttons = '''            <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.6rem;">
              <button class="btn btn-primary" id="btn-submit-exam-active" style="width: 100%;" onclick="App.handleSubmitExam(event)"><span data-i18n="btn_submit_exam">Nộp Bài Thi</span></button>
              <button class="btn btn-outline btn-sm" id="btn-exit-exam-active" style="width: 100%; border-color: var(--danger); color: var(--danger);" onclick="App.handleExitExam(event)"><span data-i18n="btn_exit_exam">Thoát bài thi</span></button>
            </div>'''

# Normalize line endings for replacement
html_norm = html_content.replace('\r\n', '\n')
old_buttons_norm = old_buttons.replace('\r\n', '\n')
new_buttons_norm = new_buttons.replace('\r\n', '\n')

assert old_buttons_norm in html_norm, "old_buttons not found in index.html"
html_norm = html_norm.replace(old_buttons_norm, new_buttons_norm, 1)

# Fix Modals nesting in index.html
old_modals = '''    <!-- Modals -->

    <!-- Submit Exam Modal -->
    <div id="modal-submit-exam" class="modal-overlay">
      <div class="modal-card">
        <h3 style="font-size: 1.3rem; margin-bottom: 0.8rem;" data-i18n="modal_submit_title">Xác Nhận Nộp Bài Thi</h3>
        <p style="color: var(--muted-mauve); margin-bottom: 1.5rem;" id="modal-submit-stats-text">
          Bạn đã hoàn thành 23/25 câu hỏi. Vẫn còn 2 câu chưa trả lời. Bạn có chắc chắn muốn nộp bài ngay bây giờ?
        </p>
        <div style="display: flex; justify-content: flex-end; gap: 0.8rem;">
          <button class="btn btn-outline" onclick="App.closeSubmitConfirmationModal()"><span data-i18n="btn_continue_exam">Làm Tiếp</span></button>
          <button class="btn btn-primary" onclick="App.confirmSubmitExam()"><span data-i18n="btn_confirm_submit">Xác Nhận Nộp Bài</span></button>
        </div>
      </div>
    
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
</div>'''

new_modals = '''    <!-- Modals -->

    <!-- Submit Exam Modal -->
    <div id="modal-submit-exam" class="modal-overlay">
      <div class="modal-card">
        <h3 style="font-size: 1.3rem; margin-bottom: 0.8rem;" data-i18n="modal_submit_title">Xác Nhận Nộp Bài Thi</h3>
        <p style="color: var(--muted-mauve); margin-bottom: 1.5rem;" id="modal-submit-stats-text">
          Bạn đã hoàn thành 23/25 câu hỏi. Vẫn còn 2 câu chưa trả lời. Bạn có chắc chắn muốn nộp bài ngay bây giờ?
        </p>
        <div style="display: flex; justify-content: flex-end; gap: 0.8rem;">
          <button class="btn btn-outline" id="btn-cancel-submit-exam" onclick="App.closeSubmitConfirmationModal()"><span data-i18n="btn_continue_exam">Làm Tiếp</span></button>
          <button class="btn btn-primary" id="btn-confirm-submit-exam" onclick="App.confirmSubmitExam()"><span data-i18n="btn_confirm_submit">Xác Nhận Nộp Bài</span></button>
        </div>
      </div>
    </div>

    <!-- Exit Exam Confirmation Modal -->
    <div id="modal-exit-exam" class="modal-overlay">
      <div class="modal-card">
        <h3 style="font-size: 1.3rem; margin-bottom: 0.8rem; color: var(--danger);" id="modal-exit-title" data-i18n="modal_exit_title">Thoát bài thi?</h3>
        <p style="color: var(--text-main); margin-bottom: 1.5rem; line-height: 1.6;" id="modal-exit-body" data-i18n="modal_exit_body">
          Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>
          Bạn có chắc chắn muốn thoát không?
        </p>
        <div style="display: flex; justify-content: flex-end; gap: 0.8rem;">
          <button class="btn btn-outline" id="btn-cancel-exit-exam" onclick="App.closeExitConfirmationModal()"><span data-i18n="btn_continue_exam">Tiếp tục làm bài</span></button>
          <button class="btn btn-primary" id="btn-confirm-exit-exam" style="background-color: var(--danger); border-color: var(--danger);" onclick="App.confirmExitExam()"><span data-i18n="btn_confirm_exit">Thoát và xóa bài thi</span></button>
        </div>
      </div>
    </div>'''

old_modals_norm = old_modals.replace('\r\n', '\n')
new_modals_norm = new_modals.replace('\r\n', '\n')

assert old_modals_norm in html_norm, "old_modals not found in index.html"
html_norm = html_norm.replace(old_modals_norm, new_modals_norm, 1)

# Fix Footer in index.html
old_footer = '''    <!-- Footer -->
    <footer class="app-footer">
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
    </footer>'''

new_footer = '''    <!-- Footer -->
    <footer class="app-footer">
      <div class="footer-container">
        <h4 class="footer-heading">ERP & Supply Chain Management Knowledge Hub</h4>
        <p class="footer-tagline-text" data-i18n="footer_tagline">ERP & SCM Knowledge Hub | Nền tảng học tập tri thức giáo dục độc lập.</p>
        <div class="footer-divider"></div>
        <p class="footer-author-box" data-i18n="footer_author">Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)</p>
        <p class="footer-academic-note" data-i18n="footer_academic_note">Nền tảng song ngữ (Việt / Anh) • Chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực Business Analyst.</p>
      </div>
    </footer>'''

old_footer_norm = old_footer.replace('\r\n', '\n')
new_footer_norm = new_footer.replace('\r\n', '\n')

assert old_footer_norm in html_norm, "old_footer not found in index.html"
html_norm = html_norm.replace(old_footer_norm, new_footer_norm, 1)

with open('outputs/app/index.html', 'w', encoding='utf-8') as f:
    f.write(html_norm)

print("index.html patched successfully.")
