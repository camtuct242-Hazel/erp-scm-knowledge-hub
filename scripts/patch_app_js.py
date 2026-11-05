with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update i18n dictionary for VI
vi_marker = 'nav_about: "Giới Thiệu",'
vi_additions = """nav_about: "Giới Thiệu",
      btn_prev_chapter: "Chương trước",
      btn_chapter_list: "Danh sách chương",
      btn_next_chapter: "Chương tiếp theo",
      modal_exit_title: "Thoát bài thi?",
      modal_exit_body: "Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>Bạn có chắc chắn muốn thoát không?",
      btn_continue_exam: "Tiếp tục làm bài",
      btn_confirm_exit: "Thoát và xóa bài thi",
      btn_exit_exam: "Thoát bài thi",
      btn_reveal_answer: "💡 Xem đáp án và giải thích",
      btn_hide_answer: "Ẩn giải thích","""

code = code.replace(vi_marker, vi_additions, 1)

# 2. Update i18n dictionary for EN
en_marker = 'nav_about: "About",'
en_additions = """nav_about: "About",
      btn_prev_chapter: "Previous Chapter",
      btn_chapter_list: "Chapter List",
      btn_next_chapter: "Next Chapter",
      modal_exit_title: "Exit examination?",
      modal_exit_body: "If you exit now, all answers entered during this examination attempt will be permanently discarded. Your current attempt cannot be restored.<br/><br/>Are you sure you want to exit?",
      btn_continue_exam: "Continue Exam",
      btn_confirm_exit: "Exit and Discard Attempt",
      btn_exit_exam: "Exit Exam",
      btn_reveal_answer: "💡 Reveal answer and explanation",
      btn_hide_answer: "Hide explanation","""

code = code.replace(en_marker, en_additions, 1)

# 3. Update navigateTo to block when in timed exam mode
old_nav = """    navigateTo: function(viewName, params = {}) {
      state.currentView = viewName;"""

new_nav = """    navigateTo: function(viewName, params = {}) {
      // Timed Exam Session Lock: Block leaving active timed examination
      if (state.examActive && state.examMode === 'timed' && viewName !== 'exam-active') {
        this.openExitConfirmationModal();
        return;
      }
      state.currentView = viewName;"""

code = code.replace(old_nav, new_nav, 1)

# 4. Add renderMarkdownWithMath and replace renderChapterReader
old_reader = code[code.find('renderChapterReader:'):code.find('toggleChapterCompleted:')]

new_reader_block = """renderMarkdownWithMath: function(content) {
      if (!content) return '';
      const mathStore = [];
      // 1. Protect display math $$ ... $$
      let protectedText = content.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: true, math: math.trim() });
        return `%%DISPLAY_MATH_${idx}%%`;
      });
      // 2. Protect display math \\[ ... \\]
      protectedText = protectedText.replace(/\\\\\\[([\\s\\S]*?)\\\\\\]/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: true, math: math.trim() });
        return `%%DISPLAY_MATH_${idx}%%`;
      });
      // 3. Protect inline math $ ... $
      protectedText = protectedText.replace(/(^|[^\\\\])\\$([^$\\n]+?)\\$/g, (m, prefix, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: false, math: math.trim() });
        return `${prefix}%%INLINE_MATH_${idx}%%`;
      });
      // 4. Protect inline math \\( ... \\)
      protectedText = protectedText.replace(/\\\\\\((.+?)\\\\\\)/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: false, math: math.trim() });
        return `%%INLINE_MATH_${idx}%%`;
      });

      // Parse markdown with marked
      let html = window.marked ? window.marked.parse(protectedText) : protectedText;

      // Restore protected math expressions
      html = html.replace(/%%DISPLAY_MATH_(\\d+)%%/g, (m, idx) => {
        const item = mathStore[parseInt(idx, 10)];
        return item ? `$$${item.math}$$` : m;
      });
      html = html.replace(/%%INLINE_MATH_(\\d+)%%/g, (m, idx) => {
        const item = mathStore[parseInt(idx, 10)];
        return item ? `$${item.math}$` : m;
      });

      return html;
    },

    prevChapter: function() {
      const order = ['chap-01', 'chap-02', 'chap-03', 'chap-04', 'chap-05', 'chap-06'];
      const curIdx = order.indexOf(state.currentChapterId);
      if (curIdx > 0) {
        this.renderChapterReader(order[curIdx - 1]);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },

    nextChapter: function() {
      const order = ['chap-01', 'chap-02', 'chap-03', 'chap-04', 'chap-05', 'chap-06'];
      const curIdx = order.indexOf(state.currentChapterId);
      if (curIdx < order.length - 1) {
        this.renderChapterReader(order[curIdx + 1]);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    },

    renderChapterReader: function(chapId) {
      state.currentChapterId = chapId;
      const content = (window.APP_DATA.chapterContents && window.APP_DATA.chapterContents[chapId])
        ? window.APP_DATA.chapterContents[chapId]
        : `# Chapter not found: ${chapId}`;

      const articleEl = document.getElementById('chapter-content-body');
      const tocEl = document.getElementById('chapter-toc-list');
      const chkEl = document.getElementById('chapter-completed-checkbox');

      // Update completion checkbox
      if (chkEl) {
        chkEl.checked = state.completedChapters.includes(chapId);
      }

      // Update Chapter Header Banner
      const chapInfo = (window.APP_DATA.chapters || []).find(c => c.id === chapId);
      const chapNum = chapInfo ? chapInfo.chapter_number : parseInt(chapId.replace('chap-0', ''), 10);
      const badgeEl = document.getElementById('chapter-reader-badge');
      const titleEl = document.getElementById('chapter-reader-title');
      const subEl = document.getElementById('chapter-reader-subtitle');

      if (badgeEl) badgeEl.innerText = state.lang === 'vi' ? `Chương 0${chapNum}` : `Chapter 0${chapNum}`;
      if (titleEl) titleEl.innerText = chapInfo ? this.getText(chapInfo.title) : `Chương ${chapNum}`;
      if (subEl) subEl.innerText = state.lang === 'vi' ? 'Cấu trúc 12 phần sư phạm chuẩn mực' : 'Standard 12-Section Pedagogical Structure';

      // Update Navigation Buttons (Top & Bottom)
      const order = ['chap-01', 'chap-02', 'chap-03', 'chap-04', 'chap-05', 'chap-06'];
      const curIdx = order.indexOf(chapId);
      const isFirst = curIdx === 0;
      const isLast = curIdx === order.length - 1;

      ['top', 'bottom'].forEach(pos => {
        const prevBtn = document.getElementById(`chapter-nav-prev-${pos}`);
        const nextBtn = document.getElementById(`chapter-nav-next-${pos}`);
        if (prevBtn) {
          prevBtn.disabled = isFirst;
          prevBtn.classList.toggle('disabled', isFirst);
          prevBtn.title = isFirst ? (state.lang === 'vi' ? 'Đây là chương đầu tiên' : 'First chapter') : '';
        }
        if (nextBtn) {
          nextBtn.disabled = isLast;
          nextBtn.classList.toggle('disabled', isLast);
          nextBtn.title = isLast ? (state.lang === 'vi' ? 'Đây là chương cuối cùng' : 'Last chapter') : '';
        }
      });

      // Render Markdown with protected math
      if (articleEl) {
        articleEl.innerHTML = this.renderMarkdownWithMath(content);
        // Render Math with KaTeX
        this.renderMath(articleEl);

        // Render Mermaid Diagrams if present
        if (window.mermaid) {
          try {
            mermaid.init(undefined, articleEl.querySelectorAll('.language-mermaid'));
          } catch (e) {
            console.warn("Mermaid rendering deferred:", e);
          }
        }

        // Build Table of Contents from h2 elements
        const headers = articleEl.querySelectorAll('h2');
        if (tocEl) {
          tocEl.innerHTML = Array.from(headers).map((h, idx) => {
            const anchorId = `toc-heading-${idx}`;
            h.id = anchorId;
            const cleanText = h.innerText.replace(/^[0-9.]+\\s*/, '');
            return `
              <li class="chapter-nav-item" onclick="document.getElementById('${anchorId}').scrollIntoView({ behavior: 'smooth' })">
                ${cleanText}
              </li>
            `;
          }).join('');
        }
      }
    },

    """

code = code.replace(old_reader, new_reader_block, 1)

# 5. Update startExam with Navigation Lock and Protection
old_start = code[code.find('startExam:'):code.find('renderActiveExamQuestion:')]

new_start_block = """startExam: function(examId, mode = 'timed') {
      const exam = (window.APP_DATA.examinations || []).find(e => e.id === examId);
      if (!exam) return;

      state.currentExamId = examId;
      state.examMode = mode;
      state.examQuestions = exam.questions || [];
      state.currentQIndex = 0;
      state.userAnswers = new Array(state.examQuestions.length).fill(null);
      state.flaggedQuestions = new Set();
      state.examActive = true;
      state.timerSeconds = 1800; // 30 minutes

      const timerBox = document.getElementById('active-timer-box');
      const modeBadge = document.getElementById('active-exam-mode-badge');
      const badge = document.getElementById('active-exam-badge');
      const expCard = document.getElementById('active-practice-explanation');

      if (badge) badge.innerText = examId;
      if (modeBadge) {
        modeBadge.innerText = mode === 'timed' ? (state.lang === 'vi' ? 'Thi tính giờ' : 'Timed Mode') : (state.lang === 'vi' ? 'Luyện tập' : 'Practice Mode');
      }

      if (mode === 'timed') {
        if (timerBox) timerBox.style.display = 'flex';
        if (expCard) expCard.style.display = 'none';

        // Lock Navigation
        document.body.classList.add('exam-locked');

        // Browser beforeunload protection
        if (!state.beforeUnloadHandler) {
          state.beforeUnloadHandler = function(e) {
            e.preventDefault();
            e.returnValue = '';
            return '';
          };
          window.addEventListener('beforeunload', state.beforeUnloadHandler);
        }

        // Browser history popstate protection
        history.pushState({ inExam: true }, document.title);
        if (!state.popStateHandler) {
          state.popStateHandler = function(e) {
            if (state.examActive && state.examMode === 'timed') {
              history.pushState({ inExam: true }, document.title);
              window.App.openExitConfirmationModal();
            }
          };
          window.addEventListener('popstate', state.popStateHandler);
        }

        // Start countdown timer
        if (state.timerInterval) clearInterval(state.timerInterval);
        state.timerInterval = setInterval(() => {
          state.timerSeconds--;
          this.tickTimer();
        }, 1000);
      } else {
        // Practice Mode: Free navigation
        if (timerBox) timerBox.style.display = 'none';
        if (state.timerInterval) clearInterval(state.timerInterval);
        this.cleanupExamProtection();
      }

      this.renderActiveExamQuestion();
      this.renderPalette();
      this.navigateTo('exam-active');
    },

    tickTimer: function() {
      const minutes = Math.floor(state.timerSeconds / 60);
      const seconds = state.timerSeconds % 60;
      const str = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      const timerDisplay = document.getElementById('active-timer-display');
      if (timerDisplay) timerDisplay.innerText = str;

      if (state.timerSeconds <= 300) {
        const tb = document.getElementById('active-timer-box');
        if (tb) tb.classList.add('warning');
      }

      if (state.timerSeconds <= 0) {
        clearInterval(state.timerInterval);
        this.submitExamNow();
      }
    },

    """

code = code.replace(old_start, new_start_block, 1)

# 6. Update submitExamNow & exit methods with Modal and cleanup
old_submit_block = code[code.find('submitExamNow:'):code.find('renderExamResults:')]

new_submit_block = """submitExamNow: function() {
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

    """

code = code.replace(old_submit_block, new_submit_block, 1)

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js updated with Chapter Navigation & Timed Exam Lock!")
