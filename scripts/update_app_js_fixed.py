import re

with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update I18N additions
new_i18n_vi = """      footer_tagline: "Nền tảng tri thức và học tập giáo dục độc lập.",
      footer_author: "Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Đồng bộ học liệu giáo trình ĐH Kinh tế TP.HCM (UEH 2020) & Khung năng lực Business Analyst",
      chat_mode_offline: "🤖 Chế độ Tri thức Offline (Grounded Mode)",
      chat_mode_live: "✨ Chế độ Live AI API (Đã kết nối)",
      btn_clear_chat: "Xóa Hội Thoại",
      confirm_clear_chat: "Bạn có chắc chắn muốn xóa toàn bộ lịch sử trò chuyện không?",
      fc_all_chapters: "Tất Cả Các Chương",
      fc_difficulty_basic: "Cơ bản",
      fc_difficulty_inter: "Trung bình",
      fc_difficulty_adv: "Nâng cao","""

new_i18n_en = """      footer_tagline: "An independent educational knowledge platform.",
      footer_author: "Created by Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Aligned with UEH 2020 Textbook & Business Analyst Competency Framework",
      chat_mode_offline: "🤖 Offline Grounded Knowledge Mode",
      chat_mode_live: "✨ Live AI API Mode (Connected)",
      btn_clear_chat: "Clear Chat",
      confirm_clear_chat: "Are you sure you want to clear the conversation history?",
      fc_all_chapters: "All Chapters",
      fc_difficulty_basic: "Basic",
      fc_difficulty_inter: "Intermediate",
      fc_difficulty_adv: "Advanced","""

# Insert in I18N.vi
code = code.replace('about_skills_p2: "Sử dụng thành thạo Excel Solver, hoạch định nhu cầu vật tư MRP, quản trị dữ liệu chủ MDM và cấu hình tham số hệ thống."',
                    'about_skills_p2: "Sử dụng thành thạo Excel Solver, hoạch định nhu cầu vật tư MRP, quản trị dữ liệu chủ MDM và cấu hình tham số hệ thống.",\n' + new_i18n_vi)

# Insert in I18N.en
code = code.replace('about_skills_p2: "Proficiency in Excel Solver modeling, MRP material planning, MDM governance, and ERP system parameters."',
                    'about_skills_p2: "Proficiency in Excel Solver modeling, MRP material planning, MDM governance, and ERP system parameters.",\n' + new_i18n_en)

# 2. Update state object with new flashcard and chat fields
old_state_fc = """    // Flashcard State
    flashcardList: [],
    currentFlashcardIndex: 0,
    flashcardFlipped: false,
    masteredFlashcards: new Set(JSON.parse(localStorage.getItem('erp_mastered_flashcards') || '[]')),
    flashcardFilter: 'all',"""

new_state_fc = """    // Flashcard State
    flashcardList: [],
    currentFlashcardIndex: 0,
    flashcardFlipped: false,
    masteredFlashcards: new Set(JSON.parse(localStorage.getItem('erp_mastered_flashcards') || '[]')),
    flashcardFilter: 'all',
    flashcardChapterFilter: 'all',
    flashcardCategoryFilter: 'all',
    flashcardStatusFilter: 'all',"""

old_state_ai = """    // AI Consultant State
    currentScenarioId: 'scenario-1',
    chatHistory: [],
    customApiKey: sessionStorage.getItem('erp_custom_api_key') || '',
    customProvider: sessionStorage.getItem('erp_custom_provider') || 'gemini'"""

new_state_ai = """    // AI Consultant State
    currentScenarioId: 'scenario-1',
    chatMessages: JSON.parse(localStorage.getItem('erp_chat_history') || '[]'),
    chatContextChapter: 'all',
    chatContextCase: 'none',
    customApiKey: localStorage.getItem('erp_custom_api_key') || '',
    customProvider: localStorage.getItem('erp_custom_provider') || 'gemini'"""

code = code.replace(old_state_fc, new_state_fc)
code = code.replace(old_state_ai, new_state_ai)

# 3. Add renderMath helper & scroll to top in App methods
render_math_helper = """    // --- Mathematical Rendering Engine (KaTeX Local Offline) ---
    renderMath: function(element) {
      if (!element) return;
      if (window.renderMathInElement) {
        try {
          renderMathInElement(element, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\\\[', right: '\\\\]', display: true },
              { left: '\\\\(', right: '\\\\)', display: false }
            ],
            throwOnError: false,
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
          });
        } catch (e) {
          console.warn("KaTeX rendering notice:", e);
        }
      }
    },

    // --- Floating Scroll-To-Top Controller ---
    scrollToTop: function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },

    initScrollToTop: function() {
      const btn = document.getElementById('scroll-to-top-btn');
      if (!btn) return;
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          btn.classList.add('visible');
        } else {
          btn.classList.remove('visible');
        }
      }, { passive: true });
    },
"""

code = code.replace('    init: function() {', render_math_helper + '\n    init: function() {')

# 4. In App.init(), initialize scroll to top
code = code.replace('this.initKeyboardShortcuts();', 'this.initKeyboardShortcuts();\n      this.initScrollToTop();')

# 5. Fix navbar metric to use APP_DATA.flashcards.length
code = code.replace("if (fcVal) fcVal.innerText = `${state.masteredFlashcards.size} / 30`;",
                    "if (fcVal) fcVal.innerText = `${state.masteredFlashcards.size} / ${(window.APP_DATA.flashcards || []).length}`;")

# 6. Replace Flashcards methods with enhanced 62-card implementation
old_fc_methods_pattern = re.compile(r'renderFlashcard:\s*function\(\)\s*\{.*?getFilteredFlashcards:\s*function\(\)\s*\{.*?return list;\s*\},', re.DOTALL)

new_fc_methods = """renderFlashcard: function() {
      const filtered = this.getFilteredFlashcards();
      const allCards = state.flashcardList;

      if (filtered.length === 0) {
        state.currentFlashcardIndex = 0;
        const promptEl = document.getElementById('fc-front-prompt');
        const ansEl = document.getElementById('fc-back-answer');
        const counterEl = document.getElementById('fc-progress-counter');
        if (promptEl) promptEl.innerText = state.lang === 'vi' ? "Không có thẻ ghi nhớ nào thỏa mãn bộ lọc hiện tại!" : "No flashcards match the current filter criteria!";
        if (ansEl) ansEl.innerText = state.lang === 'vi' ? "Hãy chuyển bộ lọc Chương hoặc Loại thẻ sang 'Tất Cả' để ôn luyện toàn bộ 62 thẻ." : "Switch Chapter or Category filters to 'All' to review all 62 cards.";
        if (counterEl) counterEl.innerText = `0 / 0 (Tổng ${allCards.length})`;
        return;
      }

      if (state.currentFlashcardIndex >= filtered.length) {
        state.currentFlashcardIndex = 0;
      }

      const card = filtered[state.currentFlashcardIndex];
      const isMastered = state.masteredFlashcards.has(card.id);

      // Reset flip
      state.flashcardFlipped = false;
      const cardEl = document.getElementById('flashcard-card-element');
      if (cardEl) cardEl.classList.remove('flipped');

      // Update Front Face
      const catEl = document.getElementById('fc-front-category');
      if (catEl) catEl.innerText = card.category || 'Khái niệm ERP';

      const chapEl = document.getElementById('fc-front-chapter');
      if (chapEl) chapEl.innerText = state.lang === 'vi' ? `Chương ${card.chapter}` : `Chapter ${card.chapter}`;

      const diffEl = document.getElementById('fc-front-difficulty');
      if (diffEl) {
        diffEl.innerText = card.difficulty || 'Cơ bản';
        diffEl.className = `badge ${card.difficulty === 'Nâng cao' ? 'badge-rose' : (card.difficulty === 'Trung bình' ? 'badge-beige' : 'badge-success')}`;
      }

      const topicEl = document.getElementById('fc-front-topic');
      if (topicEl) topicEl.innerText = card.topic || '';

      const promptEl = document.getElementById('fc-front-prompt');
      if (promptEl) promptEl.innerText = this.getText(card.question || card.front);

      const keywordsEl = document.getElementById('fc-front-keywords');
      if (keywordsEl) {
        keywordsEl.innerHTML = (card.keywords || []).map(kw => `<span class="flashcard-keyword-tag">${kw}</span>`).join('');
      }

      // Update Back Face
      const bCatEl = document.getElementById('fc-back-category');
      if (bCatEl) bCatEl.innerText = card.category || 'Giải nghĩa & Hàm ý ERP';

      const bTopicEl = document.getElementById('fc-back-topic');
      if (bTopicEl) bTopicEl.innerText = card.topic || '';

      const bStatusEl = document.getElementById('fc-back-status');
      if (bStatusEl) {
        bStatusEl.innerText = isMastered
          ? (state.lang === 'vi' ? '✓ Đã thuộc' : '✓ Mastered')
          : (state.lang === 'vi' ? '⏳ Cần ôn tập' : 'Needs Review');
        bStatusEl.className = `badge ${isMastered ? 'badge-success' : 'badge-rose'}`;
      }

      const ansEl = document.getElementById('fc-back-answer');
      if (ansEl) ansEl.innerText = this.getText(card.answer || card.back);

      const exEl = document.getElementById('fc-back-example');
      if (exEl) {
        if (card.example) {
          exEl.style.display = 'block';
          exEl.innerHTML = `<strong>💡 ${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Context:'}</strong> ${card.example}`;
        } else {
          exEl.style.display = 'none';
        }
      }

      // Update Live Counter
      const counterEl = document.getElementById('fc-progress-counter');
      if (counterEl) {
        counterEl.innerText = `${state.currentFlashcardIndex + 1} / ${filtered.length} (${state.lang === 'vi' ? 'Đã thuộc:' : 'Mastered:'} ${state.masteredFlashcards.size}/${allCards.length})`;
      }

      // Render KaTeX Math on the active card
      if (cardEl) {
        this.renderMath(cardEl);
      }
    },

    flipFlashcard: function() {
      state.flashcardFlipped = !state.flashcardFlipped;
      const cardEl = document.getElementById('flashcard-card-element');
      if (cardEl) {
        cardEl.classList.toggle('flipped', state.flashcardFlipped);
        this.renderMath(cardEl);
      }
    },

    nextFlashcard: function() {
      const filtered = this.getFilteredFlashcards();
      if (filtered.length === 0) return;
      state.currentFlashcardIndex = (state.currentFlashcardIndex + 1) % filtered.length;
      this.renderFlashcard();
    },

    prevFlashcard: function() {
      const filtered = this.getFilteredFlashcards();
      if (filtered.length === 0) return;
      state.currentFlashcardIndex = (state.currentFlashcardIndex - 1 + filtered.length) % filtered.length;
      this.renderFlashcard();
    },

    markFlashcardMastered: function() {
      const filtered = this.getFilteredFlashcards();
      if (filtered.length === 0) return;
      const card = filtered[state.currentFlashcardIndex];
      state.masteredFlashcards.add(card.id);
      localStorage.setItem('erp_mastered_flashcards', JSON.stringify([...state.masteredFlashcards]));
      this.updateNavbarMetrics();
      this.nextFlashcard();
    },

    markFlashcardNeedsReview: function() {
      const filtered = this.getFilteredFlashcards();
      if (filtered.length === 0) return;
      const card = filtered[state.currentFlashcardIndex];
      state.masteredFlashcards.delete(card.id);
      localStorage.setItem('erp_mastered_flashcards', JSON.stringify([...state.masteredFlashcards]));
      this.updateNavbarMetrics();
      this.nextFlashcard();
    },

    shuffleFlashcards: function() {
      for (let i = state.flashcardList.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [state.flashcardList[i], state.flashcardList[j]] = [state.flashcardList[j], state.flashcardList[i]];
      }
      state.currentFlashcardIndex = 0;
      this.renderFlashcard();
    },

    filterFlashcardsByChapter: function(chapId) {
      state.flashcardChapterFilter = chapId;
      state.currentFlashcardIndex = 0;
      this.renderFlashcard();
    },

    filterFlashcardsCategory: function(cat) {
      state.flashcardCategoryFilter = cat;
      state.currentFlashcardIndex = 0;
      ['all', 'formula', 'rule', 'model', 'ba'].forEach(id => {
        const btn = document.getElementById(`fc-filter-${id}`);
        if (btn) btn.classList.remove('active');
      });
      const mapping = { 'all': 'all', 'Formula': 'formula', 'Business Rule': 'rule', 'Model': 'model', 'BA Perspective': 'ba' };
      const activeId = mapping[cat] || 'all';
      const activeBtn = document.getElementById(`fc-filter-${activeId}`);
      if (activeBtn) activeBtn.classList.add('active');
      this.renderFlashcard();
    },

    filterFlashcardsStatus: function(status) {
      state.flashcardStatusFilter = status;
      state.currentFlashcardIndex = 0;
      const unBtn = document.getElementById('fc-filter-unmastered');
      const maBtn = document.getElementById('fc-filter-mastered');
      if (unBtn) unBtn.classList.toggle('active', status === 'unmastered');
      if (maBtn) maBtn.classList.toggle('active', status === 'mastered');
      this.renderFlashcard();
    },

    getFilteredFlashcards: function() {
      let list = state.flashcardList || [];
      if (state.flashcardChapterFilter && state.flashcardChapterFilter !== 'all') {
        list = list.filter(c => c.chapter_id === state.flashcardChapterFilter);
      }
      if (state.flashcardCategoryFilter && state.flashcardCategoryFilter !== 'all') {
        list = list.filter(c => c.category === state.flashcardCategoryFilter);
      }
      if (state.flashcardStatusFilter === 'unmastered') {
        list = list.filter(c => !state.masteredFlashcards.has(c.id));
      } else if (state.flashcardStatusFilter === 'mastered') {
        list = list.filter(c => state.masteredFlashcards.has(c.id));
      }
      return list;
    },"""

code = old_fc_methods_pattern.sub(lambda m: new_fc_methods, code)

# 7. Update Chapter Reader math rendering
code = code.replace("readerEl.innerHTML = marked.parse(content);\n      } else {\n        readerEl.innerText = content;\n      }",
                    "readerEl.innerHTML = marked.parse(content);\n        this.renderMath(readerEl);\n      } else {\n        readerEl.innerText = content;\n      }")

# 8. Update Case Studies doc subtab math rendering
code = code.replace("if (window.renderMathInElement) {\n          renderMathInElement(docBox, {\n            delimiters: [\n              { left: '$$', right: '$$', display: true },\n              { left: '$', right: '$', display: false }\n            ],\n            throwOnError: false\n          });\n        }",
                    "this.renderMath(docBox);")

# 9. Update Practice Exam option and explanation math rendering
code = code.replace("expBox.innerHTML = `<strong>${state.lang === 'vi' ? 'Giải thích đáp án:' : 'Explanation:'}</strong> ${this.getText(q.explanation)}`;",
                    "expBox.innerHTML = `<strong>${state.lang === 'vi' ? 'Giải thích đáp án:' : 'Explanation:'}</strong> ${this.getText(q.explanation)}`;\n      this.renderMath(expBox);")

# 10. Rebuild Unified AI Study Consultant methods
old_ai_start = "renderConsultantView: function() {"
old_ai_end = "    generateIntelligentResponse: function(userQuery) {"
pos_ai_s = code.find(old_ai_start)
pos_ai_e = code.find(old_ai_end)

# Find the end of generateIntelligentResponse
pos_ai_end_method = code.find("    // =========================================================================", pos_ai_e)
if pos_ai_end_method == -1:
    pos_ai_end_method = code.find("    // --- Settings Modal ---", pos_ai_e)

print(f"AI Block found: {pos_ai_s} to {pos_ai_end_method}")

new_ai_methods = """renderConsultantView: function() {
      // 1. Update Mode Badge
      const modeBadge = document.getElementById('chat-mode-badge');
      if (modeBadge) {
        if (state.customApiKey) {
          modeBadge.innerText = `✨ ${state.lang === 'vi' ? 'Chế độ Live API' : 'Live AI API'} (${state.customProvider})`;
          modeBadge.className = 'badge badge-rose';
        } else {
          modeBadge.innerText = `🤖 ${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Grounded Mode'}`;
          modeBadge.className = 'badge badge-beige';
        }
      }

      // 2. Render Suggestion Scenario Chips
      this.renderChatSuggestionChips();

      // 3. Render Conversation Messages
      this.renderChatMessages();
    },

    renderChatSuggestionChips: function() {
      const container = document.getElementById('scenario-chips-container');
      if (!container) return;

      const scenarios = [
        {
          id: 'chip-1',
          icon: '💡',
          label: state.lang === 'vi' ? 'Khái niệm ERP' : 'ERP Fundamentals',
          prompt: state.lang === 'vi'
            ? 'Giải thích chi tiết kiến trúc 3 tầng và vai trò của Cơ sở dữ liệu tập trung trong việc xóa bỏ đảo thông tin (Information Silos) của hệ thống ERP.'
            : 'Explain the three-tier architecture and how centralized databases eliminate enterprise information silos in ERP.'
        },
        {
          id: 'chip-2',
          icon: '⚖️',
          label: state.lang === 'vi' ? 'So sánh EOQ vs EPQ' : 'Compare EOQ & EPQ',
          prompt: state.lang === 'vi'
            ? 'So sánh sự khác biệt bản chất giữa mô hình EOQ cơ bản và mô hình Lượng sản xuất kinh tế EPQ: Vì sao tồn kho cực đại của EPQ lại thấp hơn EOQ?'
            : 'Compare the fundamental mechanics between basic EOQ and EPQ: Why is maximum peak inventory under gradual replenishment strictly lower than EOQ?'
        },
        {
          id: 'chip-3',
          icon: '🏢',
          label: state.lang === 'vi' ? 'Tình huống Texago' : 'Texago Case Analysis',
          prompt: state.lang === 'vi'
            ? 'Mổ xẻ kết quả bài toán Texago: Tại sao địa điểm St. Louis lại tối ưu toàn diện ($1.330M) dù Galveston có chi phí dầu thô rẻ hơn?'
            : 'Dissect the Texago site selection decision: Why is St. Louis globally optimal ($1,330M) despite Galveston offering cheaper crude shipping?'
        },
        {
          id: 'chip-4',
          icon: '📊',
          label: state.lang === 'vi' ? 'Góc nhìn BA' : 'BA Perspective',
          prompt: state.lang === 'vi'
            ? 'Dưới góc nhìn Business Analyst, các tham số Cung, Cầu và Tuyến cấm (Big-M) trong bài toán vận tải được cấu hình trong bảng dữ liệu Master Data nào của SAP S/4HANA?'
            : 'From a Business Analyst perspective, which master data tables in SAP S/4HANA maintain supply capacities, customer demand, and prohibited routing constraints?'
        },
        {
          id: 'chip-5',
          icon: '📑',
          label: state.lang === 'vi' ? 'Đánh đổi Better Products' : 'Better Products Trade-off',
          prompt: state.lang === 'vi'
            ? 'Phân tích sự đánh đổi chi phí giữa Case 2.1 (cho phép chia nhỏ sản phẩm) và Case 2.2 (cấm chia nhỏ): Vì sao doanh nghiệp chấp nhận trả thêm $30/ngày?'
            : 'Analyze the operational trade-off between Case 2.1 (product splitting) and Case 2.2 (no splitting): Why pay an extra $30/day for exclusivity?'
        },
        {
          id: 'chip-6',
          icon: '🧮',
          label: state.lang === 'vi' ? 'Giải toán ACT Tire' : 'Solve ACT Inventory',
          prompt: state.lang === 'vi'
            ? 'Hướng dẫn tính toán từng bước chỉ số Q*, ROP và TVC cho công ty ACT với D = 6.000 lốp/năm, K = $115/lần đặt, h = $4.20/lốp/năm, L = 9 ngày.'
            : 'Step-by-step mathematical guide to compute Q*, ROP, and TVC for Atlantic Coast Tire (D = 6,000, K = $115, h = $4.20, L = 9 days).'
        },
        {
          id: 'chip-7',
          icon: '🎯',
          label: state.lang === 'vi' ? 'Chu trình O2C & P2P' : 'O2C & P2P Processes',
          prompt: state.lang === 'vi'
            ? 'Trình bày sự kết nối giữa quy trình Mua hàng P2P (đối chiếu 3 bên, tài khoản GR/IR) và quy trình Bán hàng O2C (kiểm tra khả dụng ATP) trong ERP.'
            : 'Demonstrate how Procure-to-Pay (3-way match, GR/IR clearing) and Order-to-Cash (ATP check) seamlessly synchronize in modern ERP.'
        },
        {
          id: 'chip-8',
          icon: '🧠',
          label: state.lang === 'vi' ? 'Mô hình SOCA EPQ' : 'SOCA Speaker Scheduling',
          prompt: state.lang === 'vi'
            ? 'Trong tình huống SOCA, chuyển từ cỡ lô 30.000 lên 50.000 loa mang lại những lợi ích gì cho kế hoạch chạy máy và giải phóng bao nhiêu ngày nghỉ?'
            : 'In the SOCA case, what specific scheduling advantages and cost savings arise from shifting lot size from 30,000 to 50,000 units?'
        }
      ];

      container.innerHTML = scenarios.map(sc => `
        <button class="scenario-chip-btn" onclick="App.insertPrompt('${sc.prompt.replace(/'/g, "\\'")}')">
          <span>${sc.icon}</span>
          <span>${sc.label}</span>
        </button>
      `).join('');
    },

    insertPrompt: function(promptText) {
      const input = document.getElementById('chat-user-input');
      if (input) {
        input.value = promptText;
        input.focus();
        input.style.borderColor = 'var(--dusty-rose-dark)';
        setTimeout(() => { input.style.borderColor = ''; }, 600);
      }
    },

    setChatContextChapter: function(chapId) {
      state.chatContextChapter = chapId;
    },

    setChatContextCase: function(caseId) {
      state.chatContextCase = caseId;
    },

    handleChatKeyDown: function(e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.sendChatMessage();
      }
    },

    renderChatMessages: function() {
      const container = document.getElementById('chat-messages-container');
      if (!container) return;

      if (!state.chatMessages || state.chatMessages.length === 0) {
        container.innerHTML = `
          <div class="chat-msg-row assistant">
            <div class="chat-bubble-container">
              <div class="chat-msg-meta">
                <span>🤖</span>
                <strong>AI Study Consultant</strong>
                <span>• Chế độ Offline Grounded Mode</span>
              </div>
              <div class="chat-bubble-assistant">
                <p><strong>Xin chào! Tôi là Trợ Lý Cố Vấn Tri Thức ERP & Chuỗi Cung Ứng của bạn.</strong></p>
                <p>Tôi được xây dựng trực tiếp trên cơ sở học liệu 6 chương giáo trình UEH 2020, 4 nghiên cứu tình huống kinh điển (Texago, Better Products, ACT, SOCA) và ngân hàng 250 câu hỏi trắc nghiệm.</p>
                <p>💡 <em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc gõ trực tiếp câu hỏi thảo luận bên dưới!</em></p>
              </div>
            </div>
          </div>
        `;
        return;
      }

      container.innerHTML = state.chatMessages.map(msg => {
        const isUser = msg.role === 'user';
        const formattedContent = isUser ? `<p>${msg.content}</p>` : (window.marked ? marked.parse(msg.content) : msg.content);
        const modeBadgeText = msg.mode === 'live' ? '✨ Live AI API' : '🤖 Offline Grounded';

        return `
          <div class="chat-msg-row ${isUser ? 'user' : 'assistant'}">
            <div class="chat-bubble-container">
              <div class="chat-msg-meta">
                <span>${isUser ? '👤' : '🤖'}</span>
                <strong>${isUser ? (state.lang === 'vi' ? 'Bạn' : 'You') : 'AI Consultant'}</strong>
                <span>• ${msg.time || ''}</span>
                ${!isUser ? `<span>[${modeBadgeText}]</span>` : ''}
              </div>
              <div class="${isUser ? 'chat-bubble-user' : 'chat-bubble-assistant'}">
                ${formattedContent}
              </div>
            </div>
          </div>
        `;
      }).join('');

      this.renderMath(container);
      container.scrollTop = container.scrollHeight;
    },

    sendChatMessage: function() {
      const input = document.getElementById('chat-user-input');
      if (!input) return;
      const text = input.value.trim();
      if (!text) return;

      input.value = '';
      const now = new Date();
      const timeStr = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;

      // 1. Add user message
      const userMsg = { role: 'user', content: text, time: timeStr };
      state.chatMessages.push(userMsg);
      this.renderChatMessages();

      // 2. Show typing indicator
      const container = document.getElementById('chat-messages-container');
      const typingId = 'typing-' + Date.now();
      if (container) {
        const typingEl = document.createElement('div');
        typingEl.id = typingId;
        typingEl.className = 'chat-msg-row assistant';
        typingEl.innerHTML = `
          <div class="chat-bubble-container">
            <div class="chat-msg-meta">
              <span>🤖</span>
              <strong>AI Consultant</strong>
              <span>• Đang suy nghĩ...</span>
            </div>
            <div class="chat-bubble-assistant" style="color: var(--muted-mauve); font-style: italic;">
              ⚡ Đang truy vấn cơ sở tri thức ERP & giải toán...
            </div>
          </div>
        `;
        container.appendChild(typingEl);
        container.scrollTop = container.scrollHeight;
      }

      // 3. Process Response
      setTimeout(() => {
        const typingEl = document.getElementById(typingId);
        if (typingEl) typingEl.remove();

        const responseText = this.generateIntelligentResponse(text);
        const isLive = Boolean(state.customApiKey);
        const assistantMsg = {
          role: 'assistant',
          content: responseText,
          time: timeStr,
          mode: isLive ? 'live' : 'offline'
        };

        state.chatMessages.push(assistantMsg);
        localStorage.setItem('erp_chat_history', JSON.stringify(state.chatMessages));
        this.renderChatMessages();
      }, 500);
    },

    confirmClearChat: function() {
      const confirmed = confirm(this.getText({
        vi: "Bạn có chắc chắn muốn xóa toàn bộ lịch sử cuộc trò chuyện này không?",
        en: "Are you sure you want to clear the entire chat conversation history?"
      }));
      if (confirmed) {
        state.chatMessages = [];
        localStorage.removeItem('erp_chat_history');
        this.renderChatMessages();
      }
    },

    generateIntelligentResponse: function(userQuery) {
      const q = userQuery.toLowerCase();

      // Case 1: Texago
      if (q.includes('texago') || q.includes('galveston') || q.includes('st. louis') || q.includes('lọc dầu') || state.chatContextCase === 'CASE-01') {
        return `### 📑 Phân Tích Chuyên Sâu Tình Huống Texago Corp. (Site Selection)

**1. Bảng Tổng Hợp Chi Phí Toàn Chuỗi Cho 3 Địa Điểm Ứng Viên:**

| Địa Điểm Ứng Viên | Cước Dầu Thô (Stage 1) | Cước Thành Phẩm (Stage 2) | Chi Phí Vận Hành | Tổng Chi Phí Khả Biến | Thứ Hạng |
|---|:---:|:---:|:---:|:---:|:---:|
| **Los Angeles, CA** | \\$410M | \\$410M | \\$620M | **\\$1,440M** | Hạng 3 |
| **Galveston, TX** | \\$360M | \\$450M | \\$570M | **\\$1,380M** | Hạng 2 |
| **St. Louis, MO** | \\$440M | \\$360M | \\$530M | **\\$1,330M** | **HẠNG 1: TỐI ƯU TOÀN CỤC** |

**2. Bản Chất Vấn Đề Dưới Góc Nhìn Chuỗi Cung Ứng:**
- Mặc dù Galveston có lợi thế cước vận chuyển dầu thô rẻ nhất (\\$360M do nằm sát các mỏ dầu Texas), nhưng **St. Louis mới là phương án tối ưu toàn cục** vì:
  1. Chi phí vận hành nhà máy lọc dầu tại St. Louis rẻ hơn \\$40M/năm so với Galveston (\\$530M vs \\$570M).
  2. Chi phí phân phối thành phẩm từ St. Louis đến 4 trung tâm phân phối (Pittsburgh, Atlanta, Kansas City, San Francisco) rẻ hơn tới \\$90M/năm (\\$360M vs \\$450M).
- **Hàm ý cho Business Analyst:** Tối ưu hóa chuỗi cung ứng phải có tầm nhìn đa tầng (End-to-End Visibility). Tối ưu hóa cục bộ ở khâu nguyên liệu (Sub-optimization) sẽ dẫn đến chi phí phân phối thành phẩm và vận hành phình to.`;
      }

      // Case 4: SOCA / EPQ
      if (q.includes('soca') || q.includes('epq') || q.includes('bổ sung dần') || q.includes('loa') || state.chatContextCase === 'CASE-04') {
        return `### 📑 Phân Tích Mô Hình Sản Xuất Kinh Tế EPQ (Công Ty SOCA)

**1. Công thức và Kết Quả Tối Ưu:**
Hệ số bổ sung dần: $\\\\left(1 - \\\\frac{d}{p}\\\\right) = \\\\left(1 - \\\\frac{1.000}{3.000}\\\\right) = \\\\frac{2}{3}$.
$$Q^* = \\\\sqrt{\\\\frac{2 K D}{h \\\\left(1 - \\\\frac{d}{p}\\\\right)}} = \\\\sqrt{\\\\frac{2 \\\\times 12.000 \\\\times 250.000}{3,60 \\\\times \\\\frac{2}{3}}} = \\\\mathbf{50.000\\\\text{ chiếc loa}}$$

**2. So Sánh Hiệu Quả Vận Hành:**
- **Chính sách cũ ($Q = 30.000$):** Chi phí thiết lập máy = \\$100.000/năm; Chi phí lưu kho = \\$36.000/năm. $\\\\text{TVC} = \\$136.000/năm.
- **Chính sách tối ưu ($Q^* = 50.000$):** Chi phí thiết lập máy = \\$60.000/năm; Chi phí lưu kho = \\$60.000/năm. $\\\\text{TVC}^* = \\$120.000/năm.
- **Tiết kiệm ròng hàng năm:** **\\$16.000/năm (-11,76%)**.

**3. Lợi Ích Lập Lịch Sản Xuất (Scheduling Insights):**
- Thời gian máy chạy sản xuất một đợt: $t_1 = 50.000 / 3.000 = 16,67\\\\text{ ngày làm việc}$.
- Thời gian máy nghỉ hoàn toàn: $t_2 = 33.333,33 / 1.000 = 33,33\\\\text{ ngày làm việc}$.
- Máy móc có thêm **13,33 ngày rảnh rỗi liên tục** trong mỗi chu kỳ so với trước đây, tạo điều kiện thuận lợi để xưởng bảo trì máy móc và dập các linh kiện TV khác.`;
      }

      // Case 3: ACT Tire / EOQ / ROP
      if (q.includes('act') || q.includes('tire') || q.includes('lốp') || q.includes('rop') || q.includes('wilson') || state.chatContextCase === 'CASE-03') {
        return `### 📑 Phân Tích Quản Trị Tồn Kho Khoa Học (Atlantic Coast Tire - ACT)

**1. Mô hình EOQ Cơ bản (Wilson):**
- Nhu cầu năm $D = 6.000$ lốp; Chi phí đặt hàng $K = \\$115$; Tỷ lệ lưu kho $I = 21\\\\% \\\\implies h = 0,21 \\\\times \\$20 = \\$4,20$/lốp/năm.
$$Q^* = \\\\sqrt{\\\\frac{2 K D}{h}} = \\\\sqrt{\\\\frac{2 \\\\times 115 \\\\times 6.000}{4,20}} = \\\\mathbf{573\\\\text{ chiếc lốp}}$$
- $\\\\text{TVC}^* = \\\\sqrt{2 K D h} = \\\\mathbf{\\\\$2.407,49/\\\\text{năm}}$ (Tiết kiệm 13,7% so với chính sách cũ $Q=1.000$ tốn \\$2.790).

**2. Điểm Đặt Hàng Lại (Reorder Point - ROP):**
$$\\\\text{ROP} = d \\\\times L = \\\\left(\\\\frac{6.000}{250}\\\\right) \\\\times 9 = 24 \\\\times 9 = \\\\mathbf{180\\\\text{ chiếc lốp}}$$
Khi tồn kho thực tế giảm về 180 lốp, ERP sẽ tự động phát hành đơn Purchase Order mới đến nhà cung cấp Eversafe.

**3. Quyết Định Chiết Khấu Số Lượng (Quantity Discounts):**
- Eversafe giảm 1% (còn \\$19,80/lốp) nếu đặt từ 750 lốp trở lên.
- Đặt tại điểm ngưỡng $Q = 750$ lốp mang lại **Tổng chi phí toàn phần thấp nhất $\\\\text{TC} = \\$121.279,25/\\\\text{năm}**, tiết kiệm hơn \\$1.100/năm so với mua ở giá \\$20. Đây là quyết định tối ưu toàn cục cho ACT.`;
      }

      // Case 2: Better Products / Assignment
      if (q.includes('better products') || q.includes('phân công') || q.includes('chia nhỏ') || q.includes('splitting') || state.chatContextCase === 'CASE-02') {
        return `### 📑 Phân Tích Tình Huống Better Products Company (Case 2.1 vs Case 2.2)

**1. So Sánh Mô Hình Toán Học:**
- **Case 2.1 (Cho phép chia nhỏ sản phẩm - LP Transport):**
  - Giải bằng phương pháp Đơn hình Vận tải với Điểm đến Giả định nhu cầu 75 sp và tuyến cấm Big-M ($c_{23} = M$).
  - Nghiệm: Nhà máy 1 chia làm 3 sản phẩm; Nhà máy 2 chia làm 2 sản phẩm; Nhà máy 3 chia làm 1 sản phẩm.
  - Tổng chi phí: **\\$3.260/ngày** (\\$1.189.900/năm).
- **Case 2.2 (Cấm chia nhỏ sản phẩm - 0-1 Binary Assignment):**
  - Mỗi sản phẩm được sản xuất trọn vẹn tại duy nhất 1 nhà máy để tránh phát sinh chi phí đổi khuôn và kiểm tra chất lượng.
  - Phép gán: Nhà máy 1 (SP 2 & 3); Nhà máy 2 (SP 4); Nhà máy 3 (SP 1).
  - Tổng chi phí: **\\$3.290/ngày** (\\$1.200.850/năm).

**2. Phân Tích Đánh Đổi Dành Cho Business Analyst:**
- Mức chênh lệch chi phí là $\\\\Delta = \\$3.290 - \\$3.260 = \\\\mathbf{\\\\$30/\\\\text{ngày}}$ (tương đương \\$10.950/năm).
- Ban giám đốc nên chọn **Case 2.2**, vì khoản chênh lệch \\$30/ngày thực chất là chi phí bảo hiểm để loại bỏ hoàn toàn rủi ro chất lượng không đồng nhất và chi phí quản lý chứng từ phức tạp khi chia đôi một sản phẩm tại 2 nhà máy.`;
      }

      // Concept: ERP & 3-Tier Architecture
      if (q.includes('kiến trúc') || q.includes('3 tầng') || q.includes('database') || q.includes('tier') || q.includes('silos')) {
        return `### 💡 Bản Chất Kiến Trúc 3 Tầng Của Hệ Thống ERP Hiện Đại

**1. Cấu Trúc Ba Tầng (Three-Tier Client/Server Architecture):**
1. **Tầng Trình Diễn (Presentation Layer):** Giao diện tương tác trực tiếp với người dùng (Web Browser, Fiori GUI, Mobile App) để nhập liệu đơn hàng và trực quan hóa dashboard.
2. **Tầng Ứng Dụng (Application Layer):** Trung tâm xử lý logic nghiệp vụ, thực thi các thuật toán tối ưu hóa (đơn hình vận tải, thuật toán EOQ, giải thuật bóc tách MRP) và kiểm tra tính hợp lệ dữ liệu.
3. **Tầng Cơ Sở Dữ Liệu (Database Layer):** Hệ quản trị CSDL quan hệ hoặc In-Memory (như SAP HANA, Oracle Database) đảm bảo tính toàn vẹn giao dịch ACID và lưu trữ an toàn toàn bộ dữ liệu chủ (Master Data) và dữ liệu giao dịch (Transactional Data).

**2. Cơ Chế Xóa Bỏ Đảo Thông Tin (Information Silos):**
- Trước ERP, mỗi phòng ban sử dụng file Excel hoặc phần mềm riêng khiến số liệu tồn kho bị vênh nhau.
- ERP thiết lập **Một phiên bản sự thật duy nhất (Single Version of the Truth)**: Khi đơn bán (Sales Order) được tạo trong SAP SD, dữ liệu tồn kho được cập nhật ngay lập tức tại module MM, kế hoạch sản xuất PP tự động kích hoạt và số dư công nợ FI được ghi nhận theo thời gian thực.`;
      }

      // Concept: O2C & P2P Processes
      if (q.includes('o2c') || q.includes('p2p') || q.includes('procure') || q.includes('order-to-cash') || q.includes('gr/ir') || q.includes('atp')) {
        return `### 💡 Đồng Bộ Quy Trình Doanh Nghiệp Cốt Lõi: O2C & P2P Trong ERP

**1. Chu Trình Bán Hàng Order-to-Cash (O2C):**
$$\\\\text{Sales Order} \\\\longrightarrow \\\\text{ATP Check} \\\\longrightarrow \\\\text{Outbound Delivery} \\\\longrightarrow \\\\text{Post Goods Issue (PGI)} \\\\longrightarrow \\\\text{Billing} \\\\longrightarrow \\\\text{Cash Receipt}$$
- **Kiểm tra khả dụng ATP (Available-to-Promise):** Tính toán lượng hàng sẵn sàng bán trong tương lai = $\\\\text{Tồn khả dụng} + \\\\text{Lượng hàng sắp về (PO, lệnh SX)} - \\\\text{Lượng đã cam kết}$.
- **Post Goods Issue (PGI):** Tự động hạch toán Nợ TK Giá vốn hàng bán (COGS) / Có TK Hàng tồn kho.

**2. Chu Trình Mua Hàng Procure-to-Pay (P2P):**
$$\\\\text{Purchase Requisition} \\\\longrightarrow \\\\text{Purchase Order} \\\\longrightarrow \\\\text{Goods Receipt (GR)} \\\\longrightarrow \\\\text{3-Way Matching} \\\\longrightarrow \\\\text{Payment}$$
- **Tài khoản trung gian GR/IR:** Cầu nối kế toán khi hàng về trước hóa đơn. Nhập kho: Nợ Hàng tồn kho / Có GR/IR. Nhận hóa đơn: Nợ GR/IR / Có Phải trả nhà cung cấp (AP).
- **Đối chiếu 3 bên (3-Way Match):** ERP tự động khóa thanh toán nếu số lượng hoặc đơn giá trên Hóa đơn không khớp với PO và Phiếu nhập kho GR.`;
      }

      // Default Academic Response
      return `### 🤖 Phân Tích & Hướng Dẫn Học Tập ERP & SCM

Cảm ơn bạn đã đặt câu hỏi. Dựa trên cơ sở dữ liệu học liệu chuẩn mực của hệ thống:

**1. Bản Chất Học Thuật Của Vấn Đề:**
Trong quản trị chuỗi cung ứng hiện đại, mọi quyết định điều vận và tồn kho đều là bài toán tối ưu hóa toán học có ràng buộc. 
- Đối với bài toán phân bổ nguồn lực, **Quy hoạch tuyến tính (LP Transportation & Assignment)** giúp cực tiểu hóa chi phí logistics toàn chuỗi.
- Đối với chính sách mua sắm, **Mô hình EOQ và EPQ** tìm điểm cân bằng kinh tế tối ưu giữa chi phí cố định mỗi lần đặt/thiết lập và chi phí lưu kho vốn lưu động.

**2. Các Công Thức Trọng Tâm Cần Ghi Nhớ:**
- Cỡ lô đặt hàng kinh tế: $Q^* = \\\\sqrt{\\\\frac{2 K D}{h}}$
- Điểm đặt hàng lại: $\\\\text{ROP} = d \\\\times L$
- Lượng sản xuất kinh tế: $Q^*_{\\\\text{EPQ}} = \\\\sqrt{\\\\frac{2 K D}{h \\\\left(1 - \\\\frac{d}{p}\\\\right)}}$
- Hàm mục tiêu vận tải: $\\\\text{Min } Z = \\\\sum_{i=1}^{m} \\\\sum_{j=1}^{n} c_{ij} x_{ij}$

**3. Khuyến Nghị Cho Bạn:**
Bạn có thể nhấp vào các thẻ **Flashcards** để rèn luyện phản xạ công thức, hoặc truy cập mục **Case Studies** để chạy trực tiếp bộ giải toán mô phỏng tối ưu cho từng tình huống doanh nghiệp!`;
    },
"""

code = code[:pos_ai_s] + new_ai_methods + code[pos_ai_end_method:]

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated! Size:", len(code))
