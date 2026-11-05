import sys

# Patch outputs/app/app.js
with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# 1. Update i18n VI
old_vi = '''      footer_credits: "Dự án học tập độc lập & chuyên sâu về Hoạch định Nguồn lực Doanh nghiệp và Quản trị Chuỗi cung ứng. Tham chiếu học liệu UEH 2020.",
      footer_tagline: "ERP & SCM Knowledge Hub | Nền tảng học tập tri thức giáo dục độc lập.",
      footer_author: "Created by Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Nền tảng song ngữ (Việt / Anh) • Chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực Business Analyst."'''

new_vi = '''      footer_credits: "Dự án học tập độc lập & chuyên sâu về Hoạch định Nguồn lực Doanh nghiệp và Quản trị Chuỗi cung ứng. Tham chiếu học liệu UEH 2020.",
      footer_tagline: "ERP & SCM Knowledge Hub | Nền tảng học tập tri thức giáo dục độc lập.",
      footer_author: "Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Nền tảng song ngữ (Việt / Anh) • Chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực Business Analyst."'''

# 2. Update i18n EN
old_en = '''      footer_credits: "Independent educational project on Enterprise Resource Planning & Supply Chain Management. Referencing UEH 2020 curriculum.",
      footer_tagline: "ERP & SCM Knowledge Hub | An independent educational knowledge platform.",
      footer_author: "Created by Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Bilingual Platform (Vietnamese / English) • Aligned with UEH 2020 Textbook & Business Analyst Competency Framework."'''

new_en = '''      footer_credits: "Independent educational project on Enterprise Resource Planning & Supply Chain Management. Referencing UEH 2020 curriculum.",
      footer_tagline: "ERP & SCM Knowledge Hub | An independent educational knowledge platform.",
      footer_author: "Author: Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Bilingual platform (Vietnamese / English) • Aligned with the UEH 2020 textbook and Business Analyst Competency Framework."'''

# Normalize line endings
app_norm = app_js.replace('\r\n', '\n')
old_vi_norm = old_vi.replace('\r\n', '\n')
new_vi_norm = new_vi.replace('\r\n', '\n')
old_en_norm = old_en.replace('\r\n', '\n')
new_en_norm = new_en.replace('\r\n', '\n')

assert old_vi_norm in app_norm, "old_vi not found"
app_norm = app_norm.replace(old_vi_norm, new_vi_norm, 1)

assert old_en_norm in app_norm, "old_en not found"
app_norm = app_norm.replace(old_en_norm, new_en_norm, 1)

# 3. Update navigateTo exam lock call
old_nav_lock = '''      // Timed Exam Session Lock: Block leaving active timed examination
      if (state.examActive && state.examMode === 'timed' && viewName !== 'exam-active') {
        this.openExitConfirmationModal();
        return;
      }'''

new_nav_lock = '''      // Timed Exam Session Lock: Block leaving active timed examination
      if (state.examActive && state.examMode === 'timed' && viewName !== 'exam-active') {
        this.handleExitExam();
        return;
      }'''

old_nav_lock_norm = old_nav_lock.replace('\r\n', '\n')
new_nav_lock_norm = new_nav_lock.replace('\r\n', '\n')
assert old_nav_lock_norm in app_norm, "old_nav_lock not found"
app_norm = app_norm.replace(old_nav_lock_norm, new_nav_lock_norm, 1)

# 4. Update popStateHandler in initExam
old_pop = '''          state.popStateHandler = function(e) {
            if (state.examActive && state.examMode === 'timed') {
              history.pushState({ inExam: true }, document.title);
              window.App.openExitConfirmationModal();
            }
          };'''

new_pop = '''          state.popStateHandler = function(e) {
            if (state.examActive && state.examMode === 'timed') {
              history.pushState({ inExam: true }, document.title);
              window.App.handleExitExam();
            }
          };'''

old_pop_norm = old_pop.replace('\r\n', '\n')
new_pop_norm = new_pop.replace('\r\n', '\n')
assert old_pop_norm in app_norm, "old_pop not found"
app_norm = app_norm.replace(old_pop_norm, new_pop_norm, 1)

# 5. Update nextQuestion on last question
old_next_q = '''      if (state.currentQIndex < state.examQuestions.length - 1) {
        state.currentQIndex++;
        this.renderActiveExamQuestion();
      } else {
        this.openSubmitConfirmationModal();
      }'''

new_next_q = '''      if (state.currentQIndex < state.examQuestions.length - 1) {
        state.currentQIndex++;
        this.renderActiveExamQuestion();
      } else {
        this.handleSubmitExam();
      }'''

old_next_q_norm = old_next_q.replace('\r\n', '\n')
new_next_q_norm = new_next_q.replace('\r\n', '\n')
assert old_next_q_norm in app_norm, "old_next_q not found"
app_norm = app_norm.replace(old_next_q_norm, new_next_q_norm, 1)

# 6. Update modal handlers and submitExamNow / confirmExitExam
old_modal_methods = '''    openSubmitConfirmationModal: function() {
      const answeredCount = state.userAnswers.filter(a => a !== null).length;
      const total = state.examQuestions.length;
      const remaining = total - answeredCount;

      const statsText = document.getElementById('modal-submit-stats-text');
      if (statsText) {
        statsText.innerText = state.lang === 'vi'
          ? `Bạn đã hoàn thành ${answeredCount}/${total} câu hỏi. Vẫn còn ${remaining} câu chưa trả lời. Bạn có chắc chắn muốn nộp bài ngay bây giờ?`
          : `You have answered ${answeredCount}/${total} questions. There are ${remaining} unanswered questions remaining. Are you sure you want to submit now?`;
      }

      document.getElementById('modal-submit-exam').classList.add('active');
    },

    closeSubmitConfirmationModal: function() {
      document.getElementById('modal-submit-exam').classList.remove('active');
    },

    confirmSubmitExam: function() {
      this.closeSubmitConfirmationModal();
      this.submitExamNow();
    },

    submitExamNow: function() {
      if (state.timerInterval) clearInterval(state.timerInterval);
      state.examActive = false;
      this.cleanupExamProtection();
      document.getElementById('navbar-exam-timer').style.display = 'none';

      // Grade Exam
      let correctCount = 0;
      state.examQuestions.forEach((q, idx) => {
        if (state.userAnswers[idx] === q.correct_option) {
          correctCount++;
        }
      });

      const percentage = Math.round((correctCount / state.examQuestions.length) * 100);
      const passed = percentage >= 70;

      // Save Exam Result to history
      const resultObj = {
        examId: state.currentExamId,
        date: new Date().toISOString(),
        score: percentage,
        correctCount: correctCount,
        totalQuestions: state.examQuestions.length,
        passed: passed,
        mode: state.examMode
      };
      state.examHistory.push(resultObj);
      localStorage.setItem('erp_exam_history', JSON.stringify(state.examHistory));

      this.closeSubmitConfirmationModal();
      this.closeExitConfirmationModal();
      this.updateNavbarMetrics();
      this.renderExamResults(resultObj);
      this.navigateTo('exam-results');
    },

    openExitConfirmationModal: function() {
      const modal = document.getElementById('modal-exit-exam');
      if (!modal) return;
      const titleEl = document.getElementById('modal-exit-title');
      const bodyEl = document.getElementById('modal-exit-body');
      if (titleEl) titleEl.innerText = state.lang === 'vi' ? 'Thoát bài thi?' : 'Exit examination?';
      if (bodyEl) {
        bodyEl.innerHTML = state.lang === 'vi'
          ? 'Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>Bạn có chắc chắn muốn thoát không?'
          : 'If you exit now, all answers entered during this examination attempt will be permanently discarded. Your current attempt cannot be restored.<br/><br/>Are you sure you want to exit?';
      }
      modal.classList.add('active');
    },

    closeExitConfirmationModal: function() {
      const modal = document.getElementById('modal-exit-exam');
      if (modal) modal.classList.remove('active');
    },

    cleanupExamProtection: function() {
      document.body.classList.remove('exam-locked');
      if (state.beforeUnloadHandler) {
        window.removeEventListener('beforeunload', state.beforeUnloadHandler);
        state.beforeUnloadHandler = null;
      }
      if (state.popStateHandler) {
        window.removeEventListener('popstate', state.popStateHandler);
        state.popStateHandler = null;
      }
    },

    confirmExitExam: function() {
      if (state.timerInterval) clearInterval(state.timerInterval);
      document.getElementById('navbar-exam-timer').style.display = 'none';
      state.examActive = false;
      state.userAnswers = [];
      this.cleanupExamProtection();
      this.closeExitConfirmationModal();
      this.navigateTo('exams');
    },

    exitExam: function() {
      this.openExitConfirmationModal();
    },

    retakeExam: function() {
      this.startExam(state.currentExamId, state.examMode);
    },

    renderExamResults: function() {
      const res = state.examResults;
      if (!res) return;'''

new_modal_methods = '''    handleExitExam: function(event) {
      if (event) {
        event.preventDefault();
        event.stopPropagation();
      }
      this.closeSubmitConfirmationModal();
      this.openExitConfirmationModal();
    },

    handleSubmitExam: function(event) {
      if (event) {
        event.preventDefault();
        event.stopPropagation();
      }
      this.closeExitConfirmationModal();
      this.openSubmitConfirmationModal();
    },

    openSubmitConfirmationModal: function() {
      this.closeExitConfirmationModal();
      const answeredCount = state.userAnswers.filter(a => a !== null).length;
      const total = state.examQuestions.length;
      const remaining = total - answeredCount;

      const statsText = document.getElementById('modal-submit-stats-text');
      if (statsText) {
        statsText.innerText = state.lang === 'vi'
          ? `Bạn đã hoàn thành ${answeredCount}/${total} câu hỏi. Vẫn còn ${remaining} câu chưa trả lời. Bạn có chắc chắn muốn nộp bài ngay bây giờ?`
          : `You have answered ${answeredCount}/${total} questions. There are ${remaining} unanswered questions remaining. Are you sure you want to submit now?`;
      }

      const modal = document.getElementById('modal-submit-exam');
      if (modal) modal.classList.add('active');
    },

    closeSubmitConfirmationModal: function() {
      const modal = document.getElementById('modal-submit-exam');
      if (modal) modal.classList.remove('active');
    },

    confirmSubmitExam: function() {
      this.closeSubmitConfirmationModal();
      this.submitExamNow();
    },

    submitExamNow: function() {
      if (state.timerInterval) clearInterval(state.timerInterval);
      state.examActive = false;
      this.cleanupExamProtection();
      const timerBadge = document.getElementById('navbar-exam-timer');
      if (timerBadge) timerBadge.style.display = 'none';

      // Grade Exam
      let correctCount = 0;
      state.examQuestions.forEach((q, idx) => {
        if (state.userAnswers[idx] === q.correct_option) {
          correctCount++;
        }
      });

      const percentage = Math.round((correctCount / state.examQuestions.length) * 100);
      const passed = percentage >= 70;

      // Save Exam Result to history
      const resultObj = {
        examId: state.currentExamId,
        date: new Date().toISOString(),
        score: correctCount,
        total: state.examQuestions.length,
        percentage: percentage,
        correctCount: correctCount,
        totalQuestions: state.examQuestions.length,
        passed: passed,
        mode: state.examMode
      };
      state.examResults = resultObj;
      state.examHistory.push(resultObj);
      localStorage.setItem('erp_exam_history', JSON.stringify(state.examHistory));

      this.closeSubmitConfirmationModal();
      this.closeExitConfirmationModal();
      this.updateNavbarMetrics();
      this.renderExamResults(resultObj);
      this.navigateTo('exam-results');
    },

    openExitConfirmationModal: function() {
      this.closeSubmitConfirmationModal();
      const modal = document.getElementById('modal-exit-exam');
      if (!modal) return;
      const titleEl = document.getElementById('modal-exit-title');
      const bodyEl = document.getElementById('modal-exit-body');
      if (titleEl) titleEl.innerText = state.lang === 'vi' ? 'Thoát bài thi?' : 'Exit examination?';
      if (bodyEl) {
        bodyEl.innerHTML = state.lang === 'vi'
          ? 'Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>Bạn có chắc chắn muốn thoát không?'
          : 'If you exit now, all answers entered during this examination attempt will be permanently discarded. Your current attempt cannot be restored.<br/><br/>Are you sure you want to exit?';
      }
      modal.classList.add('active');
    },

    closeExitConfirmationModal: function() {
      const modal = document.getElementById('modal-exit-exam');
      if (modal) modal.classList.remove('active');
    },

    cleanupExamProtection: function() {
      document.body.classList.remove('exam-locked');
      if (state.beforeUnloadHandler) {
        window.removeEventListener('beforeunload', state.beforeUnloadHandler);
        state.beforeUnloadHandler = null;
      }
      if (state.popStateHandler) {
        window.removeEventListener('popstate', state.popStateHandler);
        state.popStateHandler = null;
      }
    },

    confirmExitExam: function() {
      if (state.timerInterval) clearInterval(state.timerInterval);
      const timerBadge = document.getElementById('navbar-exam-timer');
      if (timerBadge) timerBadge.style.display = 'none';
      state.examActive = false;
      state.userAnswers = [];
      this.cleanupExamProtection();
      this.closeExitConfirmationModal();
      this.navigateTo('exams');
    },

    exitExam: function(event) {
      this.handleExitExam(event);
    },

    retakeExam: function() {
      this.startExam(state.currentExamId, state.examMode);
    },

    renderExamResults: function(resultObj) {
      const res = resultObj || state.examResults;
      if (!res) return;'''

old_modal_methods_norm = old_modal_methods.replace('\r\n', '\n')
new_modal_methods_norm = new_modal_methods.replace('\r\n', '\n')
assert old_modal_methods_norm in app_norm, "old_modal_methods not found"
app_norm = app_norm.replace(old_modal_methods_norm, new_modal_methods_norm, 1)

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(app_norm)

print("app.js patched successfully.")

# Patch outputs/app/style.css
with open('outputs/app/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

old_css_footer = '''/* ==========================================================================
   FOOTER AUTHOR ATTRIBUTION
   ========================================================================== */
.footer-author-box {
  border-top: 1px solid var(--border-color);
  margin-top: 0.8rem;
  padding-top: 0.8rem;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--coffee-bean);
}
.footer-tagline-text {
  font-size: 0.82rem;
  color: var(--muted-mauve);
  margin-top: 0.25rem;
}'''

new_css_footer = '''/* ==========================================================================
   FOOTER AUTHOR ATTRIBUTION & ACADEMIC HIERARCHY (PHASE 3C)
   ========================================================================== */
.footer-container {
  max-width: 850px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.35rem;
  text-align: center;
}
.footer-heading {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--coffee-bean);
  letter-spacing: -0.01em;
  margin: 0;
}
.footer-tagline-text {
  font-size: 0.85rem;
  color: var(--muted-mauve);
  margin: 0;
  line-height: 1.5;
}
.footer-divider {
  width: 48px;
  height: 1px;
  background: var(--border-accent);
  margin: 0.5rem auto;
}
.footer-author-box {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--coffee-bean);
  margin: 0;
}
.footer-academic-note {
  font-size: 0.8rem;
  color: var(--text-subtle);
  margin: 0;
  line-height: 1.5;
}
@media (max-width: 600px) {
  .footer-heading {
    font-size: 1.05rem;
  }
  .footer-tagline-text, .footer-academic-note {
    font-size: 0.78rem;
  }
}'''

css_norm = css_content.replace('\r\n', '\n')
old_css_footer_norm = old_css_footer.replace('\r\n', '\n')
new_css_footer_norm = new_css_footer.replace('\r\n', '\n')

assert old_css_footer_norm in css_norm, "old_css_footer not found"
css_norm = css_norm.replace(old_css_footer_norm, new_css_footer_norm, 1)

with open('outputs/app/style.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("style.css patched successfully.")
