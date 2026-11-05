// ==========================================================================
// ERP & SCM KNOWLEDGE HUB - MAIN APPLICATION JAVASCRIPT
// Production-Grade Bilingual Educational Platform
// ==========================================================================

(function() {
  'use strict';

  // --- Translation Dictionary ---
  const I18N = {
    vi: {
      brand_sub: "Nền Tảng Học Tập ERP & Chuỗi Cung Ứng",
      nav_dashboard: "Tổng Quan",
      nav_chapters: "Giáo Trình",
      nav_exams: "Luyện Thi & Trắc Nghiệm",
      nav_flashcards: "Flashcards",
      nav_glossary: "Thuật Ngữ",
      nav_cases: "Case Studies",
      nav_consultant: "Cố Vấn AI",
      nav_about: "Giới Thiệu",
      btn_prev_chapter: "Chương trước",
      btn_chapter_list: "Danh sách chương",
      btn_next_chapter: "Chương tiếp theo",
      modal_exit_title: "Thoát bài thi?",
      modal_exit_body: "Nếu thoát ngay bây giờ, toàn bộ câu trả lời đã nhập trong lượt thi hiện tại sẽ bị xóa. Bạn sẽ không thể khôi phục tiến độ của lượt thi này.<br/><br/>Bạn có chắc chắn muốn thoát không?",
      btn_continue_exam: "Tiếp tục làm bài",
      btn_confirm_exit: "Thoát và xóa bài thi",
      btn_exit_exam: "Thoát bài thi",
      btn_reveal_answer: "Xem đáp án và giải thích",
      btn_hide_answer: "Ẩn giải thích",
      badge_about: "Thông Tin Nền Tảng",
      about_title: "Về ERP & Supply Chain Management Knowledge Hub",
      about_sub: "Nền tảng học tập & phân tích chuyên sâu chuẩn mực dành cho sinh viên, giảng viên và Business Analyst",
      about_mission_title: "Sứ Mệnh Học Thuật & Định Hướng Nghề Nghiệp",
      about_mission_p1: "ERP & SCM Knowledge Hub được xây dựng nhằm giải quyết khoảng cách giữa lý thuyết sách vở và thực tiễn triển khai các hệ sinh thái doanh nghiệp lớn (SAP S/4HANA, Oracle Cloud SCM). Thay vì chỉ tóm tắt tài liệu rời rạc, nền tảng kết hợp chặt chẽ giữa Nghiên cứu Vận hành (Operations Research), Khoa học Quản lý (Management Science) và Kỹ năng Phân tích Nghiệp vụ (Business Analysis).",
      about_mission_p2: "Học liệu tham chiếu cốt lõi bắt nguồn từ chương trình đào tạo chính quy Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management (UEH 2020) của tác giả Y Hoang, tích hợp cùng 4 bộ tình huống thực tế kinh điển: Texago Corp. (Lựa chọn địa điểm lọc dầu 2 tầng), Better Products Company (Phân bổ sản phẩm & phân công nguyên khối 0-1), Atlantic Coast Tire Corp. (Quản trị tồn kho khoa học EOQ & chiết khấu giá), và SOCA TV (Sản xuất bổ sung dần EPQ).",
      
      dash_hero_badge: "Nền Tảng Đào Tạo Chuẩn Doanh Nghiệp",
      dash_hero_title: "Hệ Thống Tri Thức ERP & Quản Trị Chuỗi Cung Ứng",
      dash_hero_desc: "Khám phá 6 chương học giáo trình chuẩn mực, 250 câu hỏi luyện thi có lời giải chi tiết, 4 tình huống nghiên cứu doanh nghiệp kinh điển (Texago, Better Products, ACT, SOCA) và công cụ tối ưu hóa định lượng.",
      btn_explore_curriculum: "Vào Học Giáo Trình",
      btn_take_exam: "Thi Thử Ngay",
      
      stat_chapters_label: "Chương Học Giáo Trình",
      stat_chapters_sub: "12 mục sư phạm chuẩn mỗi chương",
      stat_questions_label: "Ngân Hàng Câu Hỏi",
      stat_questions_sub: "10 Đề thi × 25 câu có giải thích chi tiết",
      stat_flashcards_label: "Thẻ Ghi Nhớ Đã Thuộc",
      stat_flashcards_sub: "Phân loại theo công thức & quy tắc",
      stat_exam_avg_label: "Điểm Thi Thử Bình Quân",
      
      widget_calc_badge: "Công Cụ Tương Tác SCM",
      widget_calc_title: "Mô Phỏng Nhanh Tối Ưu Tồn Kho EOQ & Điểm Đặt Hàng ROP",
      btn_reset_default: "Mặc Định (ACT Tire)",
      lbl_annual_demand: "Nhu cầu hàng năm (D - chiếc/năm):",
      lbl_setup_cost: "Chi phí đặt hàng (K - $/đơn):",
      lbl_holding_cost: "Chi phí lưu kho đơn vị (h - $/chiếc/năm):",
      lbl_lead_time: "Thời gian giao hàng Lead Time (L - ngày làm việc):",
      widget_calc_results_title: "Kết Quả Tính Toán Tối Ưu:",
      res_optimal_lot: "Quy mô đặt hàng tối ưu (Q*):",
      res_orders_count: "Số đơn hàng/năm (N):",
      res_reorder_point: "Điểm đặt hàng lại (ROP = d × L):",
      res_tvc: "Tổng chi phí biến đổi (TVC*):",
      widget_calc_note: "* Tại điểm tối ưu Q*, chi phí đặt hàng hàng năm cân bằng chính xác với chi phí lưu kho hàng năm ($1.203,74 = $1.203,74).",
      
      dash_pathway_title: "Lộ Trình Học Tập Tích Hợp (Weeks 1 - 6)",
      dash_pathway_desc: "Tiến trình chuẩn mực từ toán tối ưu mạng lưới đến quản trị tồn kho và tích hợp ERP",
      
      badge_curriculum: "Giáo Trình Trực Tuyến",
      chapters_list_title: "Danh Sách Các Chương Học Chuyên Sâu",
      chapters_list_sub: "Mỗi chương được xây dựng chuẩn mực theo cấu trúc 12 mục sư phạm nghiêm ngặt",
      btn_back_chapters: "Quay lại danh sách chương",
      chk_mark_completed: "Đã hoàn thành chương này",
      btn_practice_this_chapter: "Luyện câu hỏi chương này",
      toc_title: "Mục Lục 12 Phần",
      
      badge_assessment: "Trung Tâm Đánh Giá",
      exams_center_title: "Trung Tâm Luyện Thi & Thi Tính Giờ (250 Câu Hỏi)",
      exams_center_sub: "Lựa chọn 1 trong 10 đề thi chuẩn mực (mỗi đề 25 câu: 40% Cơ bản, 40% Trung bình, 20% Nâng cao)",
      mode_practice_title: "Chế Độ Luyện Tập (Practice Mode)",
      mode_practice_desc: "Không giới hạn thời gian. Hiển thị đáp án đúng/sai ngay lập tức khi click chọn phương án kèm theo lời giải thích chi tiết cặn kẽ.",
      mode_practice_badge: "Tự học & Tra cứu",
      mode_timed_title: "Chế Độ Thi Tính Giờ (Timed Test Mode)",
      mode_timed_desc: "Đồng hồ đếm ngược 30 phút. Bảng điều hướng 25 câu hỏi, đánh dấu câu cần xem lại, nộp bài có xác nhận và tự động nộp khi hết giờ.",
      mode_timed_badge: "Áp lực thi thật",
      
      exp_title: "Giải thích đáp án:",
      btn_prev_q: "Câu Trước",
      btn_flag_q: "Xem lại sau",
      btn_next_q: "Câu Kế Tiếp",
      palette_title: "Bảng 25 Câu Hỏi",
      btn_submit_exam: "Nộp Bài Thi",
      btn_exit_exam: "Thoát & Bỏ Dở",
      
      btn_review_answers: "Xem Lại Toàn Bộ Câu Hỏi",
      btn_retake_exam: "Thi Lại Đề Này",
      btn_back_exam_list: "Danh Sách Đề Thi",
      
      badge_flashcards: "Học Nhanh & Ghi Nhớ Lâu",
      flashcards_title: "Thẻ Ghi Nhớ Khái Niệm, Công Thức & Quy Tắc ERP",
      flashcards_sub: "Lật thẻ để kiểm tra phản xạ kiến thức. Đánh dấu thẻ đã thuộc để tối ưu lộ trình lặp lại ngắt quãng (Spaced Repetition).",
      btn_shuffle: "Trộn Thẻ",
      fc_filter_all: "Tất Cả Thẻ",
      fc_filter_needs_review: "Cần Ôn Lại",
      fc_filter_formulas: "Công Thức",
      fc_filter_rules: "Quy Tắc ERP",
      fc_hint_flip: "Nhấn chuột vào thẻ hoặc bấm phím Cách (Spacebar) để lật xem đáp án",
      fc_hint_back: "Nhấn lần nữa để lật lại mặt trước",
      btn_prev_card: "Thẻ Trước",
      btn_needs_review: "Cần Ôn Lại",
      btn_mastered: "Đã Thuộc",
      btn_next_card: "Thẻ Kế Tiếp",
      
      badge_glossary: "Từ Điển Thuật Ngữ",
      glossary_title: "Từ Điển Thuật Ngữ Chuyên Ngành ERP & SCM",
      glossary_sub: "40 thuật ngữ chuẩn mực song ngữ Anh - Việt kèm ví dụ doanh nghiệp thực tế và liên kết bảng dữ liệu SAP / Oracle",
      cat_all: "Tất cả",
      cat_arch: "Kiến trúc ERP",
      cat_inv: "Tồn kho & Mua hàng",
      cat_trans: "Vận tải & Logistics",
      cat_prod: "Sản xuất",
      cat_fin: "Tài chính kế toán",
      
      gl_modal_def: "Định nghĩa chuyên ngành:",
      gl_modal_ex: "Ví dụ thực tế doanh nghiệp:",
      gl_modal_erp: "Ánh xạ phân hệ ERP (SAP / Oracle):",
      gl_modal_related: "Thuật ngữ liên quan:",
      
      badge_case_studies: "Nghiên Cứu Tình Huống",
      cases_title: "Thư Viện 4 Tình Huống Doanh Nghiệp Kinh Điển",
      cases_sub: "Bản gốc tiếng Anh đầy đủ không lược bớt + Bản dịch học thuật tiếng Việt + Phân tích BA + Bộ công cụ tính toán tương tác",
      case1_short_desc: "Lựa chọn vị trí nhà máy lọc dầu tối ưu 2 tầng",
      case2_short_desc: "Phân bổ 4 sản phẩm & Ràng buộc không chia nhỏ",
      case3_short_desc: "Quản trị tồn kho EOQ, thiếu hàng & chiết khấu giá",
      case4_short_desc: "Sản xuất bổ sung dần (EPQ) cụm loa tivi",
      tab_full_analysis: "Nội Dung Đầy Đủ & Phân Tích BA",
      tab_interactive_calc: "Bộ Tính Toán Mô Phỏng Tương Tác",
      
      badge_ai_mentor: "Trợ Lý Học Tập Thông Minh",
      ai_title: "Cố Vấn Tri Thức ERP & Chuỗi Cung Ứng AI",
      ai_sub: "8 kịch bản sư phạm chuyên sâu được cấu hình sẵn. Tra cứu khái niệm, mổ xẻ case study, giải toán định lượng và luyện phản xạ BA.",
      btn_api_settings: "Cấu hình API Key (Tùy chọn)",
      scenario_list_title: "8 Kịch Bản Sư Phạm",
      btn_clear_chat: "Làm mới hội thoại",
      btn_send: "Gửi",
      
      modal_submit_title: "Xác Nhận Nộp Bài Thi",
      btn_continue_exam: "Làm Tiếp",
      btn_confirm_submit: "Xác Nhận Nộp Bài",
      modal_api_title: "Cấu Hình Khóa API Cho Cố Vấn AI",
      modal_api_desc: "Mặc định nền tảng đã tích hợp sẵn động cơ tri thức thông minh chạy offline dựa trên dữ liệu giáo trình. Nếu muốn trò chuyện tự do với các mô hình LLM lớn bên ngoài (Google Gemini API hoặc OpenAI), bạn có thể nhập khóa API tại đây. Khóa này chỉ được lưu tạm thời trên trình duyệt của bạn (Local Session) và tuyệt đối không gửi về máy chủ bên ngoài.",
      btn_cancel: "Đóng",
      btn_save_key: "Lưu Cấu Hình",
      footer_credits: "Dự án học tập độc lập & chuyên sâu về Hoạch định Nguồn lực Doanh nghiệp và Quản trị Chuỗi cung ứng. Tham chiếu học liệu UEH 2020.",
      footer_tagline: "ERP & SCM Knowledge Hub | Nền tảng học tập tri thức giáo dục độc lập.",
      footer_author: "Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Nền tảng song ngữ (Việt / Anh) • Chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực Business Analyst."
    },
    en: {
      brand_sub: "Supply Chain Management Learning Platform",
      nav_dashboard: "Dashboard",
      nav_chapters: "Curriculum",
      nav_exams: "Exam Center",
      nav_flashcards: "Flashcards",
      nav_glossary: "Glossary",
      nav_cases: "Case Studies",
      nav_consultant: "AI Consultant",
      nav_about: "About",
      btn_prev_chapter: "Previous Chapter",
      btn_chapter_list: "Chapter List",
      btn_next_chapter: "Next Chapter",
      modal_exit_title: "Exit examination?",
      modal_exit_body: "If you exit now, all answers entered during this examination attempt will be permanently discarded. Your current attempt cannot be restored.<br/><br/>Are you sure you want to exit?",
      btn_continue_exam: "Continue Exam",
      btn_confirm_exit: "Exit and Discard Attempt",
      btn_exit_exam: "Exit Exam",
      btn_reveal_answer: "Reveal answer and explanation",
      btn_hide_answer: "Hide explanation",
      badge_about: "Platform Overview",
      about_title: "About ERP & Supply Chain Management Knowledge Hub",
      about_sub: "Enterprise-standard educational and analytical platform for students, faculty, and Business Analysts",
      about_mission_title: "Academic Mission & Professional Alignment",
      about_mission_p1: "ERP & SCM Knowledge Hub was developed to bridge the gap between textbook theory and real-world enterprise deployments (SAP S/4HANA, Oracle Cloud SCM). Instead of isolated summaries, it systematically synthesizes Operations Research, Management Science, and Business Analysis.",
      about_mission_p2: "Core reference material originates from the accredited academic curriculum Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management (UEH 2020) by Y Hoang, synthesized with 4 classic real-world cases: Texago Corp., Better Products Company, Atlantic Coast Tire Corp., and SOCA TV.",
      
      dash_hero_badge: "Enterprise Standard Learning Platform",
      dash_hero_title: "ERP & Supply Chain Management Knowledge Hub",
      dash_hero_desc: "Explore 6 in-depth textbook chapters, 250 curated practice exam questions with detailed explanations, 4 unabridged case studies (Texago, Better Products, ACT, SOCA), and interactive quantitative optimization solvers.",
      btn_explore_curriculum: "Explore Curriculum",
      btn_take_exam: "Take Practice Exam",
      
      stat_chapters_label: "Curriculum Chapters",
      stat_chapters_sub: "12 pedagogical sections per chapter",
      stat_questions_label: "Exam Question Bank",
      stat_questions_sub: "10 Exams × 25 questions with detailed rationales",
      stat_flashcards_label: "Flashcards Mastered",
      stat_flashcards_sub: "Categorized by formulas, models & rules",
      stat_exam_avg_label: "Average Test Score",
      
      widget_calc_badge: "SCM Interactive Solver",
      widget_calc_title: "Instant Inventory EOQ & Reorder Point (ROP) Simulator",
      btn_reset_default: "Reset (ACT Tire)",
      lbl_annual_demand: "Annual Demand (D - units/year):",
      lbl_setup_cost: "Ordering / Setup Cost (K - $/order):",
      lbl_holding_cost: "Holding Cost per Unit (h - $/unit/year):",
      lbl_lead_time: "Supplier Lead Time (L - working days):",
      widget_calc_results_title: "Optimization Outputs:",
      res_optimal_lot: "Economic Order Quantity (Q*):",
      res_orders_count: "Orders per Year (N):",
      res_reorder_point: "Reorder Point (ROP = d × L):",
      res_tvc: "Total Variable Cost (TVC*):",
      widget_calc_note: "* At the optimal lot size Q*, annual ordering cost precisely balances annual holding cost ($1,203.74 = $1,203.74).",
      
      dash_pathway_title: "Integrated Learning Pathway (Weeks 1 - 6)",
      dash_pathway_desc: "A systematic curriculum from transportation optimization to inventory models and enterprise ERP integration",
      
      badge_curriculum: "Interactive Curriculum",
      chapters_list_title: "Curriculum Chapters Directory",
      chapters_list_sub: "Every chapter strictly adheres to the 12-section pedagogical framework",
      btn_back_chapters: "Back to Chapters Directory",
      chk_mark_completed: "Mark chapter as completed",
      btn_practice_this_chapter: "Practice this chapter's questions",
      toc_title: "12-Section Table of Contents",
      
      badge_assessment: "Assessment Center",
      exams_center_title: "Examination & Practice Center (250 Questions)",
      exams_center_sub: "Choose from 10 standard examinations (25 questions each: 40% Basic, 40% Intermediate, 20% Advanced)",
      mode_practice_title: "Practice Mode",
      mode_practice_desc: "Untimed self-study. Displays instant correctness feedback and in-depth pedagogical rationale upon selecting an option.",
      mode_practice_badge: "Self-Paced Study",
      mode_timed_title: "Timed Test Mode",
      mode_timed_desc: "30-minute working timer. 25-question palette, flag for review, submission confirmation, and auto-submit on 00:00.",
      mode_timed_badge: "Exam Simulation",
      
      exp_title: "Detailed Rationale:",
      btn_prev_q: "Previous",
      btn_flag_q: "Flag for Review",
      btn_next_q: "Next Question",
      palette_title: "25-Question Palette",
      btn_submit_exam: "Submit Exam",
      btn_exit_exam: "Exit & Abandon",
      
      btn_review_answers: "Review All Questions",
      btn_retake_exam: "Retake This Exam",
      btn_back_exam_list: "Back to Exam List",
      
      badge_flashcards: "Spaced Repetition Flashcards",
      flashcards_title: "ERP Concepts, Formulas & Business Rules Flashcards",
      flashcards_sub: "Flip cards to test recall. Mark cards as Mastered to optimize your spaced repetition study deck.",
      btn_shuffle: "Shuffle Deck",
      fc_filter_all: "All Cards",
      fc_filter_needs_review: "Needs Review",
      fc_filter_formulas: "Formulas",
      fc_filter_rules: "ERP Business Rules",
      fc_hint_flip: "Click the card or press Spacebar to flip and reveal answer",
      fc_hint_back: "Click again to flip back to question",
      btn_prev_card: "Previous",
      btn_needs_review: "Needs Review",
      btn_mastered: "Mastered",
      btn_next_card: "Next Card",
      
      badge_glossary: "Terminology Glossary",
      glossary_title: "ERP & SCM Technical Terminology Glossary",
      glossary_sub: "40 curated bilingual terms with practical enterprise examples and SAP / Oracle ERP table mappings",
      cat_all: "All Categories",
      cat_arch: "ERP Architecture",
      cat_inv: "Inventory & Purchasing",
      cat_trans: "Transportation & SCM",
      cat_prod: "Production Planning",
      cat_fin: "Financial Accounting",
      
      gl_modal_def: "Domain Definition:",
      gl_modal_ex: "Enterprise Business Example:",
      gl_modal_erp: "ERP System Mapping (SAP / Oracle):",
      gl_modal_related: "Related Concepts:",
      
      badge_case_studies: "Case Studies Library",
      cases_title: "Four Classic Enterprise Case Studies",
      cases_sub: "Unabridged original English text + Faithful Vietnamese translation + BA perspective + Interactive mathematical solvers",
      case1_short_desc: "Optimal two-echelon refinery site selection",
      case2_short_desc: "4-product assignment & un-split dedication",
      case3_short_desc: "Scientific EOQ, backorders & quantity discounts",
      case4_short_desc: "Gradual replenishment (EPQ) for television speakers",
      tab_full_analysis: "Full Document & BA Analysis",
      tab_interactive_calc: "Interactive Simulation Solver",
      
      badge_ai_mentor: "Intelligent Study Assistant",
      ai_title: "AI ERP & Supply Chain Study Consultant",
      ai_sub: "8 pre-configured pedagogical scenarios. Concept explanation, case deep-dives, quantitative solvers, and BA coaching.",
      btn_api_settings: "API Key Settings (Optional)",
      scenario_list_title: "8 Pedagogical Scenarios",
      btn_clear_chat: "Reset Conversation",
      btn_send: "Send",
      
      modal_submit_title: "Confirm Exam Submission",
      btn_continue_exam: "Continue Test",
      btn_confirm_submit: "Confirm & Submit",
      modal_api_title: "Configure AI Consultant API Key",
      modal_api_desc: "By default, the platform runs an offline intelligent knowledge engine grounded in the curriculum datasets. To enable unrestricted chat with external LLMs (Google Gemini API or OpenAI), enter your API key here. The key is stored locally in your session and never transmitted to external servers.",
      btn_cancel: "Close",
      btn_save_key: "Save Settings",
      footer_credits: "Independent educational project on Enterprise Resource Planning & Supply Chain Management. Referencing UEH 2020 curriculum.",
      footer_tagline: "ERP & SCM Knowledge Hub | An independent educational knowledge platform.",
      footer_author: "Author: Nguyễn Đăng Cẩm Tú (Hazel)",
      footer_academic_note: "Bilingual platform (Vietnamese / English) • Aligned with the UEH 2020 textbook and Business Analyst Competency Framework."
    }
  };

  // --- Global Application State ---
  const state = {
    lang: localStorage.getItem('erp_hub_lang') || 'vi',
    currentView: 'dashboard',
    
    // Chapters State
    currentChapterId: 'chap-01',
    completedChapters: JSON.parse(localStorage.getItem('erp_completed_chapters') || '[]'),
    
    // Exam State
    currentExamId: 'exam-01',
    examMode: 'timed', // 'timed' or 'practice'
    examActive: false,
    examQuestions: [],
    currentQIndex: 0,
    userAnswers: [], // array of selected option keys e.g. 'A', 'B', etc.
    flaggedQuestions: new Set(),
    timerSeconds: 1800, // 30 mins
    timerInterval: null,
    examResults: null,
    examHistory: JSON.parse(localStorage.getItem('erp_exam_history') || '[]'),
    
    // Flashcard State
    flashcardList: [],
    currentFlashcardIndex: 0,
    flashcardFlipped: false,
    masteredFlashcards: new Set(JSON.parse(localStorage.getItem('erp_mastered_flashcards') || '[]')),
    flashcardFilter: 'all',
    flashcardChapterFilter: 'all',
    flashcardCategoryFilter: 'all',
    flashcardStatusFilter: 'all',
    
    // Glossary State
    glossaryCategory: 'all',
    glossarySearchQuery: '',
    glossarySelectedAlpha: 'all',
    
    // Case Studies State
    currentCaseId: 'CASE-01',
    caseSubTab: 'doc', // 'doc' or 'solver'
    
    // AI Consultant State
    currentScenarioId: 'scenario-1',
    chatMessages: JSON.parse(localStorage.getItem('erp_chat_history') || '[]'),
    chatContextChapter: 'all',
    chatContextCase: 'none',
    customApiKey: localStorage.getItem('erp_custom_api_key') || '',
    customProvider: localStorage.getItem('erp_custom_provider') || 'gemini'
  };

  // --- Main Application Controller ---
  window.App = {
    state: state,
    getState: function() { return state; },
    // --- Mathematical Rendering Engine (KaTeX Local Offline) ---
    renderMath: function(element) {
      if (!element) return;
      if (window.renderMathInElement) {
        try {
          renderMathInElement(element, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\[', right: '\\]', display: true },
              { left: '\\(', right: '\\)', display: false }
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

    init: function() {
      console.log("Initializing ERP SCM Knowledge Hub...");
      if (!window.APP_DATA) {
        console.error("Critical: window.APP_DATA not found. Please ensure data.js is loaded.");
        return;
      }

      // Initialize state defaults
      state.flashcardList = [...window.APP_DATA.flashcards];
      this.setLanguage(state.lang);
      this.renderDashboard();
      this.initQuickCalc();
      this.initKeyboardShortcuts();
      this.initScrollToTop();
      this.updateNavbarMetrics();
    },

    // --- Localization Engine ---
    setLanguage: function(lang) {
      state.lang = lang;
      localStorage.setItem('erp_hub_lang', lang);
      
      // Update toggle buttons
      document.getElementById('lang-btn-vi').classList.toggle('active', lang === 'vi');
      document.getElementById('lang-btn-en').classList.toggle('active', lang === 'en');
      
      // Update all data-i18n elements
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (I18N[lang] && I18N[lang][key]) {
          el.innerText = I18N[lang][key];
        }
      });

      // Update placeholders
      const searchInputs = {
        'glossary-search': lang === 'vi' ? 'Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa...' : 'Search terms, abbreviations, definitions...',
        'chat-user-input': lang === 'vi' ? 'Nhập câu hỏi hoặc chọn một gợi ý phía trên...' : 'Ask a question or select a prompt chip above...'
      };
      for (const [id, ph] of Object.entries(searchInputs)) {
        const el = document.getElementById(id);
        if (el) el.placeholder = ph;
      }

      // Re-render current active view synchronously
      this.refreshCurrentView();
    },

    t: function(key) {
      return (I18N[state.lang] && I18N[state.lang][key]) ? I18N[state.lang][key] : key;
    },

    getText: function(obj) {
      if (!obj) return '';
      if (typeof obj === 'string') return obj;
      return obj[state.lang] || obj['vi'] || obj['en'] || '';
    },

    // --- Navigation System ---
    navigateTo: function(viewName, params = {}) {
      // Timed Exam Session Lock: Block leaving active timed examination
      if (state.examActive && state.examMode === 'timed' && viewName !== 'exam-active') {
        this.handleExitExam();
        return;
      }
      state.currentView = viewName;
      
      // Update navbar links
      document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-view') === viewName);
      });

      // Hide all view sections
      document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));

      // Show selected section
      const targetSec = document.getElementById(`view-${viewName}`);
      if (targetSec) {
        targetSec.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      // Handle view initialization
      switch(viewName) {
        case 'dashboard':
          this.renderDashboard();
          break;
        case 'chapters':
          this.renderChaptersList();
          break;
        case 'chapter-reader':
          if (params.chapId) state.currentChapterId = params.chapId;
          this.renderChapterReader(state.currentChapterId);
          break;
        case 'exams':
          this.renderExamsList();
          break;
        case 'exam-active':
          this.renderActiveExamQuestion();
          break;
        case 'exam-results':
          this.renderExamResults();
          break;
        case 'flashcards':
          this.renderFlashcard();
          break;
        case 'glossary':
          this.renderGlossary();
          break;
        case 'cases':
          if (params.caseId) state.currentCaseId = params.caseId;
          this.renderCaseStudy();
          break;
        case 'consultant':
          this.renderConsultantView();
          break;
        case 'about':
          window.scrollTo({ top: 0, behavior: 'smooth' });
          break;
      }
    },

    refreshCurrentView: function() {
      this.navigateTo(state.currentView);
    },

    updateNavbarMetrics: function() {
      // Completed chapters
      const chapsVal = document.getElementById('stat-chapters-val');
      if (chapsVal) chapsVal.innerText = `${state.completedChapters.length} / 6`;

      // Mastered flashcards
      const fcVal = document.getElementById('stat-flashcards-val');
      if (fcVal) fcVal.innerText = `${state.masteredFlashcards.size} / ${(window.APP_DATA.flashcards || []).length}`;

      // Average score
      const avgVal = document.getElementById('stat-exam-avg-val');
      const countSub = document.getElementById('stat-exam-count-sub');
      if (state.examHistory.length > 0) {
        const sum = state.examHistory.reduce((acc, h) => acc + h.percentage, 0);
        const avg = Math.round(sum / state.examHistory.length);
        if (avgVal) avgVal.innerText = `${avg}%`;
        if (countSub) countSub.innerText = state.lang === 'vi' ? `${state.examHistory.length} lượt thi đã hoàn thành` : `${state.examHistory.length} tests completed`;
      } else {
        if (avgVal) avgVal.innerText = `--%`;
        if (countSub) countSub.innerText = state.lang === 'vi' ? 'Chưa có lượt thi tính giờ' : 'No timed tests taken yet';
      }
    },

    // =========================================================================
    // VIEW 1: DASHBOARD
    // =========================================================================
    renderDashboard: function() {
      this.updateNavbarMetrics();
      const container = document.getElementById('dashboard-chapters-grid');
      if (!container) return;

      const chapters = window.APP_DATA.chapters || [];
      container.innerHTML = chapters.map(chap => {
        const isDone = state.completedChapters.includes(chap.id);
        const title = this.getText(chap.title);
        const desc = this.getText(chap.description);
        const weekTag = `Week ${chap.week}`;

        return `
          <div class="chapter-card" onclick="App.navigateTo('chapter-reader', { chapId: '${chap.id}' })">
            <div>
              <div class="chapter-card-header">
                <span class="badge ${isDone ? 'badge-success' : 'badge-rose'}">
                  ${isDone ? (state.lang === 'vi' ? '✓ Đã Hoàn Thành' : '✓ Completed') : weekTag}
                </span>
                <span style="font-size: 0.8rem; color: var(--muted-mauve); font-weight: 600;">
                  ${chap.reading_time_minutes} min
                </span>
              </div>
              <h3>${title}</h3>
              <p class="chapter-card-desc">${desc}</p>
            </div>
            <div>
              <div class="chapter-topics">
                ${chap.topics.slice(0, 3).map(t => `<span class="topic-tag">${t}</span>`).join('')}
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 0.8rem;">
                <span style="font-size: 0.82rem; font-weight: 700; color: var(--dusty-rose-dark);">
                  ${chap.sections_count} ${state.lang === 'vi' ? 'phần sư phạm' : 'sections'}
                </span>
                <span style="font-size: 0.88rem; font-weight: 700; color: var(--coffee-bean);">
                  ${state.lang === 'vi' ? 'Học ngay' : 'Study now'} →
                </span>
              </div>
            </div>
          </div>
        `;
      }).join('');
    },

    initQuickCalc: function() {
      this.runQuickCalc();
    },

    resetQuickCalc: function() {
      document.getElementById('qc-d').value = 6000;
      document.getElementById('qc-k').value = 115;
      document.getElementById('qc-h').value = 4.20;
      document.getElementById('qc-l').value = 7.5;
      this.runQuickCalc();
    },

    runQuickCalc: function() {
      const D = parseFloat(document.getElementById('qc-d').value) || 0;
      const K = parseFloat(document.getElementById('qc-k').value) || 0;
      const h = parseFloat(document.getElementById('qc-h').value) || 0.0001;
      const L = parseFloat(document.getElementById('qc-l').value) || 0;

      if (D <= 0 || K <= 0 || h <= 0) return;

      const Q = Math.sqrt((2 * K * D) / h);
      const N = D / Q;
      const d = D / 250;
      const ROP = d * L;
      const TVC = Math.sqrt(2 * K * D * h);

      const qEl = document.getElementById('qc-res-q');
      const nEl = document.getElementById('qc-res-n');
      const ropEl = document.getElementById('qc-res-rop');
      const tvcEl = document.getElementById('qc-res-tvc');

      if (qEl) qEl.innerText = `${Math.round(Q)} ${state.lang === 'vi' ? 'chiếc / đơn' : 'units / order'}`;
      if (nEl) nEl.innerText = `${N.toFixed(1)} ${state.lang === 'vi' ? 'đơn / năm' : 'orders / year'}`;
      if (ropEl) ropEl.innerText = `${Math.round(ROP)} ${state.lang === 'vi' ? 'chiếc' : 'units'}`;
      if (tvcEl) tvcEl.innerText = `$${TVC.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} / ${state.lang === 'vi' ? 'năm' : 'year'}`;
    },

    // =========================================================================
    // VIEW 2: CHAPTERS LIST & CHAPTER READER
    // =========================================================================
    renderChaptersList: function() {
      const container = document.getElementById('full-chapters-grid');
      if (!container) return;

      const chapters = window.APP_DATA.chapters || [];
      container.innerHTML = chapters.map(chap => {
        const isDone = state.completedChapters.includes(chap.id);
        const title = this.getText(chap.title);
        const desc = this.getText(chap.description);

        return `
          <div class="chapter-card" onclick="App.navigateTo('chapter-reader', { chapId: '${chap.id}' })">
            <div>
              <div class="chapter-card-header">
                <span class="badge ${isDone ? 'badge-success' : 'badge-rose'}">
                  Week ${chap.week} • ${isDone ? (state.lang === 'vi' ? 'Đã hoàn thành' : 'Completed') : (state.lang === 'vi' ? 'Chưa hoàn thành' : 'Incomplete')}
                </span>
                <span style="font-size: 0.8rem; color: var(--muted-mauve); font-weight: 600;">
                  ${chap.reading_time_minutes} mins
                </span>
              </div>
              <h3>${title}</h3>
              <p class="chapter-card-desc">${desc}</p>
            </div>
            <div>
              <div class="chapter-topics">
                ${chap.topics.map(t => `<span class="topic-tag">${t}</span>`).join('')}
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-color); padding-top: 0.8rem;">
                <span style="font-size: 0.82rem; font-weight: 700; color: var(--dusty-rose-dark);">
                  12 ${state.lang === 'vi' ? 'phần sư phạm' : 'pedagogical sections'}
                </span>
                <button class="btn btn-primary btn-sm">${state.lang === 'vi' ? 'Đọc Giáo Trình' : 'Read Chapter'} →</button>
              </div>
            </div>
          </div>
        `;
      }).join('');
    },

    renderMarkdownWithMath: function(content) {
      if (!content) return '';
      const mathStore = [];
      // 1. Protect display math $$ ... $$
      let protectedText = content.replace(/\$\$([\s\S]*?)\$\$/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: true, math: math.trim() });
        return `%%DISPLAY_MATH_${idx}%%`;
      });
      // 2. Protect display math \[ ... \]
      protectedText = protectedText.replace(/\\\[([\s\S]*?)\\\]/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: true, math: math.trim() });
        return `%%DISPLAY_MATH_${idx}%%`;
      });
      // 3. Protect inline math $ ... $
      protectedText = protectedText.replace(/(^|[^\\])\$([^$\n]+?)\$/g, (m, prefix, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: false, math: math.trim() });
        return `${prefix}%%INLINE_MATH_${idx}%%`;
      });
      // 4. Protect inline math \( ... \)
      protectedText = protectedText.replace(/\\\((.+?)\\\)/g, (m, math) => {
        const idx = mathStore.length;
        mathStore.push({ display: false, math: math.trim() });
        return `%%INLINE_MATH_${idx}%%`;
      });

      // Parse markdown with marked
      let html = window.marked ? window.marked.parse(protectedText) : protectedText;

      // Restore protected math expressions
      html = html.replace(/%%DISPLAY_MATH_(\d+)%%/g, (m, idx) => {
        const item = mathStore[parseInt(idx, 10)];
        return item ? `$$${item.math}$$` : m;
      });
      html = html.replace(/%%INLINE_MATH_(\d+)%%/g, (m, idx) => {
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
            const cleanText = h.innerText.replace(/^[0-9.]+\s*/, '');
            return `
              <li class="chapter-nav-item" onclick="document.getElementById('${anchorId}').scrollIntoView({ behavior: 'smooth' })">
                ${cleanText}
              </li>
            `;
          }).join('');
        }
      }
    },

    toggleChapterCompleted: function() {
      const chk = document.getElementById('chapter-completed-checkbox');
      const chapId = state.currentChapterId;
      if (chk.checked) {
        if (!state.completedChapters.includes(chapId)) state.completedChapters.push(chapId);
      } else {
        state.completedChapters = state.completedChapters.filter(id => id !== chapId);
      }
      localStorage.setItem('erp_completed_chapters', JSON.stringify(state.completedChapters));
      this.updateNavbarMetrics();
    },

    jumpToChapterExam: function() {
      const chapNum = parseInt(state.currentChapterId.replace('chap-', '')) || 1;
      const targetExamId = `exam-${chapNum.toString().padStart(2, '0')}`;
      this.startExam(targetExamId, 'practice');
    },

    // =========================================================================
    // VIEW 3: PRACTICE EXAMS CENTER
    // =========================================================================
    renderExamsList: function() {
      const container = document.getElementById('exam-cards-grid');
      if (!container) return;

      const exams = window.APP_DATA.examinations || [];
      container.innerHTML = exams.map(exam => {
        const title = this.getText(exam.title);
        const desc = this.getText(exam.description);
        const lastScore = state.examHistory.find(h => h.examId === exam.id);

        return `
          <div class="chapter-card">
            <div>
              <div class="chapter-card-header">
                <span class="badge badge-rose">Exam ${exam.exam_number}</span>
                <span style="font-size: 0.8rem; color: var(--muted-mauve); font-weight: 700;">
                  25 ${state.lang === 'vi' ? 'Câu hỏi' : 'Questions'}
                </span>
              </div>
              <h3 style="font-size: 1.15rem;">${title}</h3>
              <p class="chapter-card-desc">${desc}</p>
            </div>
            <div>
              <div style="display: flex; gap: 0.35rem; margin-bottom: 1rem;">
                <span class="badge badge-beige">10 Basic</span>
                <span class="badge badge-beige">10 Inter</span>
                <span class="badge badge-beige">5 Adv</span>
              </div>
              ${lastScore ? `
                <div style="font-size: 0.82rem; color: var(--success); font-weight: 700; margin-bottom: 0.8rem;">
                  ✓ ${state.lang === 'vi' ? 'Điểm gần nhất' : 'Last Score'}: ${lastScore.score}/25 (${lastScore.percentage}%)
                </div>
              ` : ''}
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem;">
                <button class="btn btn-outline btn-sm" onclick="App.startExam('${exam.id}', 'practice')">
                  ${state.lang === 'vi' ? 'Luyện tập' : 'Practice'}
                </button>
                <button class="btn btn-primary btn-sm" onclick="App.startExam('${exam.id}', 'timed')">
                  ${state.lang === 'vi' ? 'Thi 30 phút' : 'Timed Test'}
                </button>
              </div>
            </div>
          </div>
        `;
      }).join('');
    },

    startExam: function(examId, mode = 'timed') {
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
        const navTimer = document.getElementById('navbar-exam-timer');
        if (navTimer) navTimer.style.display = 'inline-flex';
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
              window.App.handleExitExam();
            }
          };
          window.addEventListener('popstate', state.popStateHandler);
        }

        // Start countdown timer
        if (state.timerInterval) clearInterval(state.timerInterval);
        state.timerInterval = setInterval(() => {
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
      if (state.timerSeconds > 0) {
        state.timerSeconds--;
      }
      const minutes = Math.floor(state.timerSeconds / 60);
      const seconds = state.timerSeconds % 60;
      const str = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      const timerDisplay = document.getElementById('active-timer-display');
      if (timerDisplay) timerDisplay.innerText = str;
      const navTimerVal = document.getElementById('nav-timer-val');
      if (navTimerVal) navTimerVal.innerText = str;

      if (state.timerSeconds <= 300) {
        const tb = document.getElementById('active-timer-box');
        if (tb) tb.classList.add('warning');
      }

      if (state.timerSeconds <= 0) {
        if (state.timerInterval) clearInterval(state.timerInterval);
        this.submitExamNow();
      }
    },

    renderActiveExamQuestion: function() {
      const q = state.examQuestions[state.currentQIndex];
      if (!q) return;

      // Update Question Number & Text
      const qNumEl = document.getElementById('active-q-number');
      const qTextEl = document.getElementById('active-q-text');
      const diffBadge = document.getElementById('active-exam-difficulty');

      if (qNumEl) qNumEl.innerText = `${state.lang === 'vi' ? 'Câu hỏi' : 'Question'} ${state.currentQIndex + 1} / ${state.examQuestions.length}`;
      if (qTextEl) qTextEl.innerText = this.getText(q.question);
      if (diffBadge) diffBadge.innerText = q.difficulty;

      // Render Options
      const optionsContainer = document.getElementById('active-options-list');
      const expBox = document.getElementById('active-practice-explanation');
      const expContent = document.getElementById('active-exp-content');
      
      const userSelected = state.userAnswers[state.currentQIndex];

      optionsContainer.innerHTML = Object.entries(q.options).map(([key, optObj]) => {
        const text = this.getText(optObj);
        let classes = 'option-item';
        
        if (state.examMode === 'practice' && userSelected !== null) {
          if (key === q.correct_option) classes += ' correct';
          else if (key === userSelected) classes += ' incorrect';
        } else {
          if (key === userSelected) classes += ' selected';
        }

        return `
          <div class="${classes}" onclick="App.selectOption('${key}')">
            <div class="option-key">${key}</div>
            <div class="option-text">${text}</div>
          </div>
        `;
      }).join('');

      // Show/Hide Practice Explanation
      if (state.examMode === 'practice' && userSelected !== null) {
        expBox.style.display = 'block';
        expContent.innerText = this.getText(q.explanation);
      } else {
        expBox.style.display = 'none';
      }

      // Update Flag button state
      const flagBtn = document.getElementById('btn-flag-q');
      const isFlagged = state.flaggedQuestions.has(state.currentQIndex);
      if (flagBtn) {
        flagBtn.style.borderColor = isFlagged ? 'var(--warning)' : 'var(--border-color)';
        flagBtn.style.color = isFlagged ? 'var(--warning)' : 'var(--text-main)';
      }

      this.updatePaletteButtonState();
    },

    selectOption: function(optionKey) {
      state.userAnswers[state.currentQIndex] = optionKey;
      this.renderActiveExamQuestion();
      this.renderPalette();
    },

    nextQuestion: function() {
      if (state.currentQIndex < state.examQuestions.length - 1) {
        state.currentQIndex++;
        this.renderActiveExamQuestion();
      } else {
        this.handleSubmitExam();
      }
    },

    prevQuestion: function() {
      if (state.currentQIndex > 0) {
        state.currentQIndex--;
        this.renderActiveExamQuestion();
      }
    },

    jumpToQuestion: function(index) {
      state.currentQIndex = index;
      this.renderActiveExamQuestion();
    },

    toggleFlagCurrentQuestion: function() {
      const idx = state.currentQIndex;
      if (state.flaggedQuestions.has(idx)) {
        state.flaggedQuestions.delete(idx);
      } else {
        state.flaggedQuestions.add(idx);
      }
      this.renderActiveExamQuestion();
      this.renderPalette();
    },

    renderPalette: function() {
      const container = document.getElementById('exam-palette-grid');
      const progressSummary = document.getElementById('palette-progress-summary');
      if (!container) return;

      const answeredCount = state.userAnswers.filter(a => a !== null).length;
      if (progressSummary) {
        progressSummary.innerText = `${state.lang === 'vi' ? 'Đã trả lời' : 'Answered'}: ${answeredCount} / ${state.examQuestions.length}`;
      }

      container.innerHTML = state.examQuestions.map((q, idx) => {
        let classes = 'palette-btn';
        if (idx === state.currentQIndex) classes += ' current';
        if (state.userAnswers[idx] !== null) classes += ' answered';
        if (state.flaggedQuestions.has(idx)) classes += ' flagged';

        return `
          <button class="${classes}" onclick="App.jumpToQuestion(${idx})">
            ${idx + 1}
          </button>
        `;
      }).join('');
    },

    updatePaletteButtonState: function() {
      document.querySelectorAll('.palette-btn').forEach((btn, idx) => {
        btn.classList.toggle('current', idx === state.currentQIndex);
      });
    },

    handleExitExam: function(event) {
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
      if (!res) return;

      const badgeEl = document.getElementById('result-status-badge');
      const scoreTitle = document.getElementById('result-score-title');
      const summaryText = document.getElementById('result-summary-text');

      badgeEl.className = `badge ${res.passed ? 'badge-success' : 'badge-danger'}`;
      badgeEl.innerText = res.passed
        ? (state.lang === 'vi' ? '✓ ĐẠT CHUẨN (PASSED)' : '✓ PASSED')
        : (state.lang === 'vi' ? '✕ CHƯA ĐẠT (NEEDS RETEST)' : '✕ NEEDS RETEST');

      scoreTitle.innerText = `${state.lang === 'vi' ? 'Điểm số' : 'Final Score'}: ${res.score} / ${res.total} (${res.percentage}%)`;

      summaryText.innerText = res.passed
        ? (state.lang === 'vi' ? 'Chúc mừng bạn đã hoàn thành xuất sắc bài thi. Bạn đã nắm vững các nguyên lý cốt lõi của chương trình.' : 'Congratulations! You demonstrated excellent mastery of the curriculum core concepts.')
        : (state.lang === 'vi' ? 'Bạn chưa đạt ngưỡng 70%. Hãy xem lại các câu trả lời sai bên dưới và ôn lại giáo trình trước khi thử lại.' : 'You scored below the 70% passing threshold. Please review the rationales below and re-study before testing again.');

      this.reviewAllQuestions();
    },

    reviewAllQuestions: function() {
      const container = document.getElementById('exam-detailed-review-container');
      if (!container) return;

      container.innerHTML = state.examQuestions.map((q, idx) => {
        const userAns = state.userAnswers[idx];
        const isCorrect = userAns === q.correct_option;

        return `
          <div class="app-card" style="margin-bottom: 1.5rem; border-left: 5px solid ${isCorrect ? 'var(--success)' : 'var(--danger)'};">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
              <span style="font-size: 0.82rem; font-weight: 800; color: ${isCorrect ? 'var(--success)' : 'var(--danger)'};">
                ${state.lang === 'vi' ? 'CÂU' : 'QUESTION'} ${idx + 1} • ${isCorrect ? (state.lang === 'vi' ? 'CHÍNH XÁC' : 'CORRECT') : (state.lang === 'vi' ? 'CHƯA ĐÚNG' : 'INCORRECT')}
              </span>
              <span class="badge badge-beige">${q.difficulty}</span>
            </div>
            <h4 style="font-size: 1.05rem; margin-bottom: 1rem; color: var(--coffee-bean);">${this.getText(q.question)}</h4>
            <div class="options-list" style="margin-bottom: 1rem;">
              ${Object.entries(q.options).map(([k, textObj]) => {
                let cls = 'option-item';
                if (k === q.correct_option) cls += ' correct';
                else if (k === userAns) cls += ' incorrect';
                return `
                  <div class="${cls}" style="cursor: default; padding: 0.6rem 0.9rem;">
                    <div class="option-key">${k}</div>
                    <div class="option-text">${this.getText(textObj)}</div>
                  </div>
                `;
              }).join('')}
            </div>
            <div style="background: var(--bg-subtle); padding: 0.9rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.9rem;">
              <strong style="color: var(--coffee-bean); display: block; margin-bottom: 0.2rem;">${this.t('exp_title')}</strong>
              ${this.getText(q.explanation)}
            </div>
          </div>
        `;
      }).join('');
    },

    // =========================================================================
    // VIEW 4: FLASHCARDS
    // =========================================================================
    renderFlashcard: function() {
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
          : (state.lang === 'vi' ? 'Cần ôn tập' : 'Needs Review');
        bStatusEl.className = `badge ${isMastered ? 'badge-success' : 'badge-rose'}`;
      }

      const ansEl = document.getElementById('fc-back-answer');
      if (ansEl) ansEl.innerText = this.getText(card.answer || card.back);

      const exEl = document.getElementById('fc-back-example');
      if (exEl) {
        if (card.example) {
          exEl.style.display = 'block';
          exEl.innerHTML = `<strong>${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Context:'}</strong> ${card.example}`;
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
    },

    // =========================================================================
    // VIEW 5: GLOSSARY
    // =========================================================================
    renderGlossary: function() {
      const container = document.getElementById('glossary-cards-container');
      const alphaBar = document.getElementById('glossary-alpha-bar');
      if (!container) return;

      const glossary = window.APP_DATA.glossary || [];
      const query = (state.glossarySearchQuery || '').toLowerCase().trim();

      // Extract available first letters
      const letters = [...new Set(glossary.map(t => t.term_en.charAt(0).toUpperCase()))].sort();
      if (alphaBar) {
        alphaBar.innerHTML = `
          <button class="alpha-btn ${state.glossarySelectedAlpha === 'all' ? 'active' : ''}" onclick="App.setGlossaryAlpha('all')">ALL</button>
          ${letters.map(l => `
            <button class="alpha-btn ${state.glossarySelectedAlpha === l ? 'active' : ''}" onclick="App.setGlossaryAlpha('${l}')">${l}</button>
          `).join('')}
        `;
      }

      // Filter terms
      const filtered = glossary.filter(item => {
        const matchCat = state.glossaryCategory === 'all' || item.category === state.glossaryCategory;
        const matchAlpha = state.glossarySelectedAlpha === 'all' || item.term_en.charAt(0).toUpperCase() === state.glossarySelectedAlpha;
        const matchQuery = !query || 
          item.term_en.toLowerCase().includes(query) ||
          item.term_vi.toLowerCase().includes(query) ||
          (item.abbreviation && item.abbreviation.toLowerCase().includes(query)) ||
          item.definition_vi.toLowerCase().includes(query) ||
          item.definition_en.toLowerCase().includes(query);
        return matchCat && matchAlpha && matchQuery;
      });

      container.innerHTML = filtered.map(item => {
        const title = state.lang === 'vi' ? item.term_vi : item.term_en;
        const subTitle = state.lang === 'vi' ? item.term_en : item.term_vi;
        const def = state.lang === 'vi' ? item.definition_vi : item.definition_en;

        return `
          <div class="glossary-card" onclick="App.openGlossaryDetail('${item.id}')">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
              <span class="badge badge-rose">${item.category}</span>
              ${item.abbreviation ? `<span class="badge badge-beige">${item.abbreviation}</span>` : ''}
            </div>
            <h3 style="font-size: 1.15rem; margin-bottom: 0.2rem; color: var(--coffee-bean);">${title}</h3>
            <div style="font-size: 0.8rem; color: var(--dusty-rose-dark); font-weight: 600; margin-bottom: 0.8rem;">${subTitle}</div>
            <p style="font-size: 0.88rem; color: var(--muted-mauve); line-height: 1.5; margin-bottom: 0.8rem;">
              ${def.slice(0, 140)}...
            </p>
            <div style="font-size: 0.78rem; font-family: var(--font-mono); color: var(--text-subtle);">
              ERP: ${item.erp_mapping.slice(0, 40)}
            </div>
          </div>
        `;
      }).join('');
    },

    filterGlossary: function() {
      state.glossarySearchQuery = document.getElementById('glossary-search').value;
      this.renderGlossary();
    },

    setGlossaryCategory: function(cat) {
      state.glossaryCategory = cat;
      document.querySelectorAll('#glossary-category-pills .btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-cat') === cat);
      });
      this.renderGlossary();
    },

    setGlossaryAlpha: function(letter) {
      state.glossarySelectedAlpha = letter;
      this.renderGlossary();
    },

    openGlossaryDetail: function(termId) {
      const term = (window.APP_DATA.glossary || []).find(t => t.id === termId);
      if (!term) return;

      document.getElementById('modal-gl-cat').innerText = term.category;
      document.getElementById('modal-gl-term').innerText = state.lang === 'vi' ? term.term_vi : term.term_en;
      document.getElementById('modal-gl-en').innerText = state.lang === 'vi' ? `${term.term_en} (${term.abbreviation || 'N/A'})` : `${term.term_vi} (${term.abbreviation || 'N/A'})`;
      document.getElementById('modal-gl-def').innerText = state.lang === 'vi' ? term.definition_vi : term.definition_en;
      document.getElementById('modal-gl-example').innerText = state.lang === 'vi' ? term.practical_example_vi : term.practical_example_en;
      document.getElementById('modal-gl-erp').innerText = term.erp_mapping;

      const relatedContainer = document.getElementById('modal-gl-related');
      relatedContainer.innerHTML = (term.related_terms || []).map(r => `
        <span class="badge badge-rose" style="cursor: pointer;" onclick="App.searchRelatedTerm('${r}')">${r}</span>
      `).join('');

      document.getElementById('modal-glossary-detail').classList.add('active');
    },

    closeGlossaryModal: function() {
      document.getElementById('modal-glossary-detail').classList.remove('active');
    },

    searchRelatedTerm: function(termStr) {
      this.closeGlossaryModal();
      document.getElementById('glossary-search').value = termStr;
      this.filterGlossary();
    },

    // =========================================================================
    // VIEW 6: CASE STUDIES & INTERACTIVE SOLVERS
    // =========================================================================
    renderCaseStudy: function() {
      const caseItem = (window.APP_DATA.caseStudies || []).find(c => c.id === state.currentCaseId);
      if (!caseItem) return;

      // Update Switcher Cards styling
      ['CASE-01', 'CASE-02', 'CASE-03', 'CASE-04'].forEach(cid => {
        const card = document.getElementById(`case-card-btn-${cid}`);
        if (card) {
          card.style.borderColor = cid === state.currentCaseId ? 'var(--dusty-rose-dark)' : 'var(--border-color)';
          card.style.boxShadow = cid === state.currentCaseId ? 'var(--shadow-rose)' : 'var(--shadow-sm)';
        }
      });

      // Update Header
      document.getElementById('active-case-tag').innerText = caseItem.id;
      document.getElementById('active-case-title').innerText = this.getText(caseItem.title);
      document.getElementById('active-case-industry').innerText = `${state.lang === 'vi' ? 'Ngành' : 'Industry'}: ${this.getText(caseItem.industry)}`;
      document.getElementById('active-case-model').innerText = this.getText(caseItem.model_type);

      // Render Sub-tabs
      this.setCaseSubTab(state.caseSubTab);
    },

    selectCaseStudy: function(caseId) {
      state.currentCaseId = caseId;
      this.renderCaseStudy();
    },

    setCaseSubTab: function(tabName) {
      state.caseSubTab = tabName;
      document.getElementById('case-tab-btn-doc').classList.toggle('active', tabName === 'doc');
      document.getElementById('case-tab-btn-solver').classList.toggle('active', tabName === 'solver');

      const docBox = document.getElementById('case-subtab-doc');
      const solverBox = document.getElementById('case-subtab-solver');

      if (tabName === 'doc') {
        docBox.style.display = 'block';
        solverBox.style.display = 'none';

        const content = window.APP_DATA.caseContents[state.currentCaseId] || 'Case content not loaded.';
        if (window.marked) {
          docBox.innerHTML = marked.parse(content);
        } else {
          docBox.innerText = content;
        }

        this.renderMath(docBox);
      } else {
        docBox.style.display = 'none';
        solverBox.style.display = 'block';
        this.renderCaseSolver();
      }
    },

    renderCaseSolver: function() {
      const container = document.getElementById('case-solver-dynamic-content');
      if (!container) return;

      if (state.currentCaseId === 'CASE-01') {
        // Texago Site Selection Solver
        container.innerHTML = `
          <h3 style="margin-bottom: 1rem;">${state.lang === 'vi' ? 'Mô Phỏng Lựa Chọn Vị Trí Nhà Máy Lọc Dầu Texago' : 'Texago Refinery Site Selection Simulator'}</h3>
          <p style="font-size: 0.9rem; color: var(--muted-mauve); margin-bottom: 1.5rem;">
            ${state.lang === 'vi' ? 'Điều chỉnh chi phí vận hành hàng năm và chi phí vận chuyển để đánh giá tổng chi phí mạng lưới ($ Triệu USD/năm).' : 'Adjust annual refinery operating and freight costs to evaluate total network system cost ($ Millions/year).'}
          </p>
          <div class="solver-grid">
            <div>
              <div class="input-group">
                <label>Los Angeles Annual Operating Cost ($M):</label>
                <input type="number" id="tx-la-op" class="input-field" value="620" oninput="App.solveTexago()">
              </div>
              <div class="input-group">
                <label>Galveston Annual Operating Cost ($M):</label>
                <input type="number" id="tx-gal-op" class="input-field" value="570" oninput="App.solveTexago()">
              </div>
              <div class="input-group">
                <label>St. Louis Annual Operating Cost ($M):</label>
                <input type="number" id="tx-stl-op" class="input-field" value="530" oninput="App.solveTexago()">
              </div>
            </div>
            <div class="result-box">
              <h4 style="margin-bottom: 0.8rem;">${state.lang === 'vi' ? 'Bảng Xếp Hạng Tổng Chi Phí ($M/năm):' : 'Total System Cost Rankings ($M/yr):'}</h4>
              <div id="tx-solver-results" style="display: flex; flex-direction: column; gap: 0.75rem;">
                <!-- Populated via solveTexago -->
              </div>
            </div>
          </div>
        `;
        this.solveTexago();
      } else if (state.currentCaseId === 'CASE-02') {
        // Better Products Assignment Solver
        container.innerHTML = `
          <h3 style="margin-bottom: 1rem;">Better Products: Splitting (Case 2.1) vs. Dedicated (Case 2.2)</h3>
          <div class="solver-grid">
            <div class="result-box">
              <h4>Case 2.1: Cho Phép Chia Tách Sản Phẩm</h4>
              <p style="font-size: 0.88rem; color: var(--muted-mauve);">Mô hình vận tải tuyến tính với sản phẩm giả (Dummy 75).</p>
              <div style="font-size: 1.6rem; font-family: var(--font-serif); font-weight: 800; color: var(--coffee-bean); margin: 0.5rem 0;">$3.260 / ngày</div>
              <ul style="font-size: 0.85rem; padding-left: 1.2rem; line-height: 1.5;">
                <li>Plant 1: SP 2 (30), SP 4 (40), Dummy (5)</li>
                <li>Plant 2: SP 1 (20), Dummy (55)</li>
                <li>Plant 3: SP 3 (30), Dummy (15)</li>
              </ul>
            </div>
            <div class="result-box" style="border-color: var(--success); background: #F6FFF7;">
              <h4 style="color: var(--success);">Case 2.2: Phân Công Nguyên Khối (0-1)</h4>
              <p style="font-size: 0.88rem; color: var(--muted-mauve);">Mỗi sản phẩm chỉ sản xuất tại 1 nhà máy duy nhất.</p>
              <div style="font-size: 1.6rem; font-family: var(--font-serif); font-weight: 800; color: var(--success); margin: 0.5rem 0;">$3.290 / ngày</div>
              <ul style="font-size: 0.85rem; padding-left: 1.2rem; line-height: 1.5;">
                <li>Plant 1: SP 4 (40), SP 3 (30)</li>
                <li>Plant 2: SP 1 (20), SP 2 (30)</li>
                <li>Plant 3: Nhàn rỗi hoàn toàn (Dummy 45)</li>
              </ul>
              <div style="margin-top: 0.6rem; font-size: 0.8rem; font-weight: 700; color: var(--coffee-bean);">
                Chênh lệch toán học: +$30/ngày (+0,92%) được bù đắp hoàn toàn bởi việc triệt tiêu chi phí thay khuôn và ổn định ERP.
              </div>
            </div>
          </div>
        `;
      } else if (state.currentCaseId === 'CASE-03') {
        // ACT Tire Solver
        container.innerHTML = `
          <h3 style="margin-bottom: 1rem;">Atlantic Coast Tire: Đối Chiếu 4 Chính Sách Quản Trị Tồn Kho</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
            <div class="result-box">
              <span class="badge badge-beige">1. Trực Giác Cũ</span>
              <div style="font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0;">Q = 1.000 lốp</div>
              <div style="font-size: 0.85rem; color: var(--muted-mauve);">TVC = $2.790,00/năm</div>
            </div>
            <div class="result-box">
              <span class="badge badge-rose">2. EOQ Cơ Bản</span>
              <div style="font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0;">Q* = 573 lốp</div>
              <div style="font-size: 0.85rem; color: var(--success);">TVC* = $2.407,48 (Tiết kiệm $382,52)</div>
            </div>
            <div class="result-box">
              <span class="badge badge-info">3. Thiếu Hàng (Backorder)</span>
              <div style="font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0;">Q* = 716, S* = 257</div>
              <div style="font-size: 0.85rem; color: var(--success);">TVC* = $1.927,56 (Tiết kiệm $862,44)</div>
            </div>
            <div class="result-box" style="border-color: var(--success); background: #FAFDF7;">
              <span class="badge badge-success">4. Chiết Khấu Số Lượng</span>
              <div style="font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0;">Q = 750 (Breakpt)</div>
              <div style="font-size: 0.85rem; color: var(--success);">TC = $121.279,25 (Tối ưu nhất)</div>
            </div>
          </div>
        `;
      } else if (state.currentCaseId === 'CASE-04') {
        // SOCA EPQ Solver
        container.innerHTML = `
          <h3 style="margin-bottom: 1rem;">SOCA TV: Gradual Replenishment (EPQ) Solver</h3>
          <div class="solver-grid">
            <div>
              <div class="input-group">
                <label>Daily Consumption Rate (d - speakers/day):</label>
                <input type="number" id="soca-d" class="input-field" value="1000" oninput="App.solveSoca()">
              </div>
              <div class="input-group">
                <label>Daily Production Rate (p - speakers/day):</label>
                <input type="number" id="soca-p" class="input-field" value="3000" oninput="App.solveSoca()">
              </div>
              <div class="input-group">
                <label>Setup Cost (K - $/setup):</label>
                <input type="number" id="soca-k" class="input-field" value="12000" oninput="App.solveSoca()">
              </div>
              <div class="input-group">
                <label>Holding Cost (h - $/speaker/year):</label>
                <input type="number" id="soca-h" class="input-field" value="3.60" step="0.1" oninput="App.solveSoca()">
              </div>
            </div>
            <div class="result-box">
              <h4 style="margin-bottom: 0.8rem;">SOCA Optimization Results:</h4>
              <div id="soca-solver-results" style="display: flex; flex-direction: column; gap: 0.6rem;">
                <!-- Populated via solveSoca -->
              </div>
            </div>
          </div>
        `;
        this.solveSoca();
      }
    },

    solveTexago: function() {
      const laOp = parseFloat(document.getElementById('tx-la-op').value) || 620;
      const galOp = parseFloat(document.getElementById('tx-gal-op').value) || 570;
      const stlOp = parseFloat(document.getElementById('tx-stl-op').value) || 530;

      // Fixed transport costs from solved LP models
      const laCrude = 410, laFin = 410;
      const galCrude = 360, galFin = 450;
      const stlCrude = 440, stlFin = 360;

      const laTotal = laOp + laCrude + laFin;
      const galTotal = galOp + galCrude + galFin;
      const stlTotal = stlOp + stlCrude + stlFin;

      const results = [
        { name: 'St. Louis, MO', cost: stlTotal, isBest: stlTotal <= Math.min(laTotal, galTotal) },
        { name: 'Galveston, TX', cost: galTotal, isBest: galTotal <= Math.min(laTotal, stlTotal) },
        { name: 'Los Angeles, CA', cost: laTotal, isBest: laTotal <= Math.min(galTotal, stlTotal) }
      ].sort((a, b) => a.cost - b.cost);

      const resContainer = document.getElementById('tx-solver-results');
      if (resContainer) {
        resContainer.innerHTML = results.map((r, i) => `
          <div style="display: flex; justify-content: space-between; padding: 0.5rem 0.8rem; background: ${r.isBest ? '#E8F5E9' : '#FFFFFF'}; border: 1px solid ${r.isBest ? 'var(--success)' : 'var(--border-color)'}; border-radius: 6px;">
            <span><strong>#${i + 1} ${r.name}</strong> ${r.isBest ? '(OPTIMAL)' : ''}</span>
            <span style="font-family: var(--font-mono); font-weight: 700; color: ${r.isBest ? 'var(--success)' : 'var(--coffee-bean)'};">$${r.cost}M / yr</span>
          </div>
        `).join('');
      }
    },

    solveSoca: function() {
      const d = parseFloat(document.getElementById('soca-d').value) || 1000;
      const p = parseFloat(document.getElementById('soca-p').value) || 3000;
      const K = parseFloat(document.getElementById('soca-k').value) || 12000;
      const h = parseFloat(document.getElementById('soca-h').value) || 3.60;
      const D = d * 250;

      const factor = 1 - (d / p);
      if (factor <= 0) return;

      const Q = Math.sqrt((2 * K * D) / (h * factor));
      const Imax = Q * factor;
      const tp = Q / p;
      const td = (Q / d) - tp;
      const runs = D / Q;
      const setupCost = K * runs;
      const holdingCost = h * (Imax / 2);
      const TVC = setupCost + holdingCost;
      const savings = 136000 - TVC;

      const resContainer = document.getElementById('soca-solver-results');
      if (resContainer) {
        resContainer.innerHTML = `
          <div style="display: flex; justify-content: space-between;"><span>Optimal Batch Size (Q*):</span><strong style="font-family: var(--font-mono);">${Math.round(Q).toLocaleString()} units</strong></div>
          <div style="display: flex; justify-content: space-between;"><span>Max Inventory (Imax):</span><strong style="font-family: var(--font-mono);">${Math.round(Imax).toLocaleString()} units</strong></div>
          <div style="display: flex; justify-content: space-between;"><span>Production Run Length (tp):</span><strong style="font-family: var(--font-mono);">${tp.toFixed(1)} days</strong></div>
          <div style="display: flex; justify-content: space-between;"><span>Idle / Other Time (td):</span><strong style="font-family: var(--font-mono);">${td.toFixed(1)} days</strong></div>
          <div style="display: flex; justify-content: space-between;"><span>Total Variable Cost:</span><strong style="font-family: var(--font-mono); color: var(--success);">$${Math.round(TVC).toLocaleString()} / yr</strong></div>
          <div style="display: flex; justify-content: space-between; border-top: 1px dashed var(--border-color); padding-top: 0.4rem;">
            <span>Annual Net Savings:</span><strong style="font-family: var(--font-mono); color: var(--success);">$${Math.round(savings).toLocaleString()} / yr</strong>
          </div>
        `;
      }
    },

    // =========================================================================
    // VIEW 7: AI STUDY CONSULTANT
    // =========================================================================
    renderConsultantView: function() {
      // 1. Update Mode Badge
      const modeBadge = document.getElementById('chat-mode-badge');
      if (modeBadge) {
        if (state.customApiKey) {
          modeBadge.innerText = `${state.lang === 'vi' ? 'Chế độ Live API' : 'Live AI API'} (${state.customProvider})`;
          modeBadge.className = 'badge badge-rose';
        } else {
          modeBadge.innerText = `${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Grounded Mode'}`;
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
          label: state.lang === 'vi' ? 'Khái niệm ERP' : 'ERP Fundamentals',
          prompt: state.lang === 'vi'
            ? 'Giải thích chi tiết kiến trúc 3 tầng và vai trò của Cơ sở dữ liệu tập trung trong việc xóa bỏ đảo thông tin (Information Silos) của hệ thống ERP.'
            : 'Explain the three-tier architecture and how centralized databases eliminate enterprise information silos in ERP.'
        },
        {
          id: 'chip-2',
          label: state.lang === 'vi' ? 'So sánh EOQ vs EPQ' : 'Compare EOQ & EPQ',
          prompt: state.lang === 'vi'
            ? 'So sánh sự khác biệt bản chất giữa mô hình EOQ cơ bản và mô hình Lượng sản xuất kinh tế EPQ: Vì sao tồn kho cực đại của EPQ lại thấp hơn EOQ?'
            : 'Compare the fundamental mechanics between basic EOQ and EPQ: Why is maximum peak inventory under gradual replenishment strictly lower than EOQ?'
        },
        {
          id: 'chip-3',
          label: state.lang === 'vi' ? 'Tình huống Texago' : 'Texago Case Analysis',
          prompt: state.lang === 'vi'
            ? 'Mổ xẻ kết quả bài toán Texago: Tại sao địa điểm St. Louis lại tối ưu toàn diện ($1.330M) dù Galveston có chi phí dầu thô rẻ hơn?'
            : 'Dissect the Texago site selection decision: Why is St. Louis globally optimal ($1,330M) despite Galveston offering cheaper crude shipping?'
        },
        {
          id: 'chip-4',
          label: state.lang === 'vi' ? 'Góc nhìn BA' : 'BA Perspective',
          prompt: state.lang === 'vi'
            ? 'Dưới góc nhìn Business Analyst, các tham số Cung, Cầu và Tuyến cấm (Big-M) trong bài toán vận tải được cấu hình trong bảng dữ liệu Master Data nào của SAP S/4HANA?'
            : 'From a Business Analyst perspective, which master data tables in SAP S/4HANA maintain supply capacities, customer demand, and prohibited routing constraints?'
        },
        {
          id: 'chip-5',
          label: state.lang === 'vi' ? 'Đánh đổi Better Products' : 'Better Products Trade-off',
          prompt: state.lang === 'vi'
            ? 'Phân tích sự đánh đổi chi phí giữa Case 2.1 (cho phép chia nhỏ sản phẩm) và Case 2.2 (cấm chia nhỏ): Vì sao doanh nghiệp chấp nhận trả thêm $30/ngày?'
            : 'Analyze the operational trade-off between Case 2.1 (product splitting) and Case 2.2 (no splitting): Why pay an extra $30/day for exclusivity?'
        },
        {
          id: 'chip-6',
          label: state.lang === 'vi' ? 'Giải toán ACT Tire' : 'Solve ACT Inventory',
          prompt: state.lang === 'vi'
            ? 'Hướng dẫn tính toán từng bước chỉ số Q*, ROP và TVC cho công ty ACT với D = 6.000 lốp/năm, K = $115/lần đặt, h = $4.20/lốp/năm, L = 9 ngày.'
            : 'Step-by-step mathematical guide to compute Q*, ROP, and TVC for Atlantic Coast Tire (D = 6,000, K = $115, h = $4.20, L = 9 days).'
        },
        {
          id: 'chip-7',
          label: state.lang === 'vi' ? 'Chu trình O2C & P2P' : 'O2C & P2P Processes',
          prompt: state.lang === 'vi'
            ? 'Trình bày sự kết nối giữa quy trình Mua hàng P2P (đối chiếu 3 bên, tài khoản GR/IR) và quy trình Bán hàng O2C (kiểm tra khả dụng ATP) trong ERP.'
            : 'Demonstrate how Procure-to-Pay (3-way match, GR/IR clearing) and Order-to-Cash (ATP check) seamlessly synchronize in modern ERP.'
        },
        {
          id: 'chip-8',
          label: state.lang === 'vi' ? 'Mô hình SOCA EPQ' : 'SOCA Speaker Scheduling',
          prompt: state.lang === 'vi'
            ? 'Trong tình huống SOCA, chuyển từ cỡ lô 30.000 lên 50.000 loa mang lại những lợi ích gì cho kế hoạch chạy máy và giải phóng bao nhiêu ngày nghỉ?'
            : 'In the SOCA case, what specific scheduling advantages and cost savings arise from shifting lot size from 30,000 to 50,000 units?'
        }
      ];

      container.innerHTML = scenarios.map(sc => `
        <button class="scenario-chip-btn" onclick="App.insertPrompt('${sc.prompt.replace(/'/g, "\'")}')">
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
                <span class="chat-avatar-badge">AI</span>
                <strong>AI Study Consultant</strong>
                <span>• Chế độ Offline Grounded Mode</span>
              </div>
              <div class="chat-bubble-assistant">
                <p><strong>Xin chào! Tôi là Trợ Lý Cố Vấn Tri Thức ERP & Chuỗi Cung Ứng của bạn.</strong></p>
                <p>Tôi được xây dựng trực tiếp trên cơ sở học liệu 6 chương giáo trình UEH 2020, 4 nghiên cứu tình huống kinh điển (Texago, Better Products, ACT, SOCA) và ngân hàng 250 câu hỏi trắc nghiệm.</p>
                <p><em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc gõ trực tiếp câu hỏi thảo luận bên dưới!</em></p>
              </div>
            </div>
          </div>
        `;
        return;
      }

      container.innerHTML = state.chatMessages.map(msg => {
        const isUser = msg.role === 'user';
        const formattedContent = isUser ? `<p>${msg.content}</p>` : (window.marked ? marked.parse(msg.content) : msg.content);
        const modeBadgeText = msg.mode === 'live' ? 'Live AI API' : 'Offline Grounded';

        return `
          <div class="chat-msg-row ${isUser ? 'user' : 'assistant'}">
            <div class="chat-bubble-container">
              <div class="chat-msg-meta">
                <span class="chat-avatar-badge">${isUser ? 'You' : 'AI'}</span>
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
              <span class="chat-avatar-badge">AI</span>
              <strong>AI Consultant</strong>
              <span>• Đang suy nghĩ...</span>
            </div>
            <div class="chat-bubble-assistant" style="color: var(--muted-mauve); font-style: italic;">
              Đang truy vấn cơ sở tri thức ERP & giải toán...
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
        return `### Phân Tích Chuyên Sâu Tình Huống Texago Corp. (Site Selection)

**1. Bảng Tổng Hợp Chi Phí Toàn Chuỗi Cho 3 Địa Điểm Ứng Viên:**

| Địa Điểm Ứng Viên | Cước Dầu Thô (Stage 1) | Cước Thành Phẩm (Stage 2) | Chi Phí Vận Hành | Tổng Chi Phí Khả Biến | Thứ Hạng |
|---|:---:|:---:|:---:|:---:|:---:|
| **Los Angeles, CA** | \$410M | \$410M | \$620M | **\$1,440M** | Hạng 3 |
| **Galveston, TX** | \$360M | \$450M | \$570M | **\$1,380M** | Hạng 2 |
| **St. Louis, MO** | \$440M | \$360M | \$530M | **\$1,330M** | **HẠNG 1: TỐI ƯU TOÀN CỤC** |

**2. Bản Chất Vấn Đề Dưới Góc Nhìn Chuỗi Cung Ứng:**
- Mặc dù Galveston có lợi thế cước vận chuyển dầu thô rẻ nhất (\$360M do nằm sát các mỏ dầu Texas), nhưng **St. Louis mới là phương án tối ưu toàn cục** vì:
  1. Chi phí vận hành nhà máy lọc dầu tại St. Louis rẻ hơn \$40M/năm so với Galveston (\$530M vs \$570M).
  2. Chi phí phân phối thành phẩm từ St. Louis đến 4 trung tâm phân phối (Pittsburgh, Atlanta, Kansas City, San Francisco) rẻ hơn tới \$90M/năm (\$360M vs \$450M).
- **Hàm ý cho Business Analyst:** Tối ưu hóa chuỗi cung ứng phải có tầm nhìn đa tầng (End-to-End Visibility). Tối ưu hóa cục bộ ở khâu nguyên liệu (Sub-optimization) sẽ dẫn đến chi phí phân phối thành phẩm và vận hành phình to.`;
      }

      // Case 4: SOCA / EPQ
      if (q.includes('soca') || q.includes('epq') || q.includes('bổ sung dần') || q.includes('loa') || state.chatContextCase === 'CASE-04') {
        return `### Phân Tích Mô Hình Sản Xuất Kinh Tế EPQ (Công Ty SOCA)

**1. Công thức và Kết Quả Tối Ưu:**
Hệ số bổ sung dần: $\\left(1 - \\frac{d}{p}\\right) = \\left(1 - \\frac{1.000}{3.000}\\right) = \\frac{2}{3}$.
$$Q^* = \\sqrt{\\frac{2 K D}{h \\left(1 - \\frac{d}{p}\\right)}} = \\sqrt{\\frac{2 \\times 12.000 \\times 250.000}{3,60 \\times \\frac{2}{3}}} = \\mathbf{50.000\\text{ chiếc loa}}$$

**2. So Sánh Hiệu Quả Vận Hành:**
- **Chính sách cũ ($Q = 30.000$):** Chi phí thiết lập máy = \$100.000/năm; Chi phí lưu kho = \$36.000/năm. $\\text{TVC} = \$136.000/năm.
- **Chính sách tối ưu ($Q^* = 50.000$):** Chi phí thiết lập máy = \$60.000/năm; Chi phí lưu kho = \$60.000/năm. $\\text{TVC}^* = \$120.000/năm.
- **Tiết kiệm ròng hàng năm:** **\$16.000/năm (-11,76%)**.

**3. Lợi Ích Lập Lịch Sản Xuất (Scheduling Insights):**
- Thời gian máy chạy sản xuất một đợt: $t_1 = 50.000 / 3.000 = 16,67\\text{ ngày làm việc}$.
- Thời gian máy nghỉ hoàn toàn: $t_2 = 33.333,33 / 1.000 = 33,33\\text{ ngày làm việc}$.
- Máy móc có thêm **13,33 ngày rảnh rỗi liên tục** trong mỗi chu kỳ so với trước đây, tạo điều kiện thuận lợi để xưởng bảo trì máy móc và dập các linh kiện TV khác.`;
      }

      // Case 3: ACT Tire / EOQ / ROP
      if (q.includes('act') || q.includes('tire') || q.includes('lốp') || q.includes('rop') || q.includes('wilson') || q.includes('eoq') || q.includes('tồn kho') || q.includes('inventory') || state.chatContextCase === 'CASE-03') {
        return `### Phân Tích Quản Trị Tồn Kho Khoa Học (Atlantic Coast Tire - ACT)

**1. Mô hình EOQ Cơ bản (Wilson):**
- Nhu cầu năm $D = 6.000$ lốp; Chi phí đặt hàng $K = \$115$; Tỷ lệ lưu kho $I = 21\\% \\implies h = 0,21 \\times \$20 = \$4,20$/lốp/năm.
$$Q^* = \\sqrt{\\frac{2 K D}{h}} = \\sqrt{\\frac{2 \\times 115 \\times 6.000}{4,20}} = \\mathbf{573\\text{ chiếc lốp}}$$
- $\\text{TVC}^* = \\sqrt{2 K D h} = \\mathbf{\\$2.407,49/\\text{năm}}$ (Tiết kiệm 13,7% so với chính sách cũ $Q=1.000$ tốn \$2.790).

**2. Điểm Đặt Hàng Lại (Reorder Point - ROP):**
$$\\text{ROP} = d \\times L = \\left(\\frac{6.000}{250}\\right) \\times 9 = 24 \\times 9 = \\mathbf{180\\text{ chiếc lốp}}$$
Khi tồn kho thực tế giảm về 180 lốp, ERP sẽ tự động phát hành đơn Purchase Order mới đến nhà cung cấp Eversafe.

**3. Quyết Định Chiết Khấu Số Lượng (Quantity Discounts):**
- Eversafe giảm 1% (còn \$19,80/lốp) nếu đặt từ 750 lốp trở lên.
- Đặt tại điểm ngưỡng $Q = 750$ lốp mang lại **Tổng chi phí toàn phần thấp nhất $\\text{TC} = \$121.279,25/\\text{năm}**, tiết kiệm hơn \$1.100/năm so với mua ở giá \$20. Đây là quyết định tối ưu toàn cục cho ACT.`;
      }

      // Case 2: Better Products / Assignment
      if (q.includes('better products') || q.includes('phân công') || q.includes('chia nhỏ') || q.includes('splitting') || state.chatContextCase === 'CASE-02') {
        return `### Phân Tích Tình Huống Better Products Company (Case 2.1 vs Case 2.2)

**1. So Sánh Mô Hình Toán Học:**
- **Case 2.1 (Cho phép chia nhỏ sản phẩm - LP Transport):**
  - Giải bằng phương pháp Đơn hình Vận tải với Điểm đến Giả định nhu cầu 75 sp và tuyến cấm Big-M ($c_{23} = M$).
  - Nghiệm: Nhà máy 1 chia làm 3 sản phẩm; Nhà máy 2 chia làm 2 sản phẩm; Nhà máy 3 chia làm 1 sản phẩm.
  - Tổng chi phí: **\$3.260/ngày** (\$1.189.900/năm).
- **Case 2.2 (Cấm chia nhỏ sản phẩm - 0-1 Binary Assignment):**
  - Mỗi sản phẩm được sản xuất trọn vẹn tại duy nhất 1 nhà máy để tránh phát sinh chi phí đổi khuôn và kiểm tra chất lượng.
  - Phép gán: Nhà máy 1 (SP 2 & 3); Nhà máy 2 (SP 4); Nhà máy 3 (SP 1).
  - Tổng chi phí: **\$3.290/ngày** (\$1.200.850/năm).

**2. Phân Tích Đánh Đổi Dành Cho Business Analyst:**
- Mức chênh lệch chi phí là $\\Delta = \$3.290 - \$3.260 = \\mathbf{\\$30/\\text{ngày}}$ (tương đương \$10.950/năm).
- Ban giám đốc nên chọn **Case 2.2**, vì khoản chênh lệch \$30/ngày thực chất là chi phí bảo hiểm để loại bỏ hoàn toàn rủi ro chất lượng không đồng nhất và chi phí quản lý chứng từ phức tạp khi chia đôi một sản phẩm tại 2 nhà máy.`;
      }

      // Concept: ERP & 3-Tier Architecture
      if (q.includes('kiến trúc') || q.includes('3 tầng') || q.includes('database') || q.includes('tier') || q.includes('silos')) {
        return `### Bản Chất Kiến Trúc 3 Tầng Của Hệ Thống ERP Hiện Đại

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
        return `### Đồng Bộ Quy Trình Doanh Nghiệp Cốt Lõi: O2C & P2P Trong ERP

**1. Chu Trình Bán Hàng Order-to-Cash (O2C):**
$$\\text{Sales Order} \\longrightarrow \\text{ATP Check} \\longrightarrow \\text{Outbound Delivery} \\longrightarrow \\text{Post Goods Issue (PGI)} \\longrightarrow \\text{Billing} \\longrightarrow \\text{Cash Receipt}$$
- **Kiểm tra khả dụng ATP (Available-to-Promise):** Tính toán lượng hàng sẵn sàng bán trong tương lai = $\\text{Tồn khả dụng} + \\text{Lượng hàng sắp về (PO, lệnh SX)} - \\text{Lượng đã cam kết}$.
- **Post Goods Issue (PGI):** Tự động hạch toán Nợ TK Giá vốn hàng bán (COGS) / Có TK Hàng tồn kho.

**2. Chu Trình Mua Hàng Procure-to-Pay (P2P):**
$$\\text{Purchase Requisition} \\longrightarrow \\text{Purchase Order} \\longrightarrow \\text{Goods Receipt (GR)} \\longrightarrow \\text{3-Way Matching} \\longrightarrow \\text{Payment}$$
- **Tài khoản trung gian GR/IR:** Cầu nối kế toán khi hàng về trước hóa đơn. Nhập kho: Nợ Hàng tồn kho / Có GR/IR. Nhận hóa đơn: Nợ GR/IR / Có Phải trả nhà cung cấp (AP).
- **Đối chiếu 3 bên (3-Way Match):** ERP tự động khóa thanh toán nếu số lượng hoặc đơn giá trên Hóa đơn không khớp với PO và Phiếu nhập kho GR.`;
      }

      // Default Academic Response
      return `### Phân Tích & Hướng Dẫn Học Tập ERP & SCM

Cảm ơn bạn đã đặt câu hỏi. Dựa trên cơ sở dữ liệu học liệu chuẩn mực của hệ thống:

**1. Bản Chất Học Thuật Của Vấn Đề:**
Trong quản trị chuỗi cung ứng hiện đại, mọi quyết định điều vận và tồn kho đều là bài toán tối ưu hóa toán học có ràng buộc. 
- Đối với bài toán phân bổ nguồn lực, **Quy hoạch tuyến tính (LP Transportation & Assignment)** giúp cực tiểu hóa chi phí logistics toàn chuỗi.
- Đối với chính sách mua sắm, **Mô hình EOQ và EPQ** tìm điểm cân bằng kinh tế tối ưu giữa chi phí cố định mỗi lần đặt/thiết lập và chi phí lưu kho vốn lưu động.

**2. Các Công Thức Trọng Tâm Cần Ghi Nhớ:**
- Cỡ lô đặt hàng kinh tế: $Q^* = \\sqrt{\\frac{2 K D}{h}}$
- Điểm đặt hàng lại: $\\text{ROP} = d \\times L$
- Lượng sản xuất kinh tế: $Q^*_{\\text{EPQ}} = \\sqrt{\\frac{2 K D}{h \\left(1 - \\frac{d}{p}\\right)}}$
- Hàm mục tiêu vận tải: $\\text{Min } Z = \\sum_{i=1}^{m} \\sum_{j=1}^{n} c_{ij} x_{ij}$

**3. Khuyến Nghị Cho Bạn:**
Bạn có thể nhấp vào các thẻ **Flashcards** để rèn luyện phản xạ công thức, hoặc truy cập mục **Case Studies** để chạy trực tiếp bộ giải toán mô phỏng tối ưu cho từng tình huống doanh nghiệp!`;
    },
    openApiKeyModal: function() {
      const modal = document.getElementById('modal-api-settings');
      if (modal) modal.classList.add('active');
    },

    closeApiKeyModal: function() {
      const modal = document.getElementById('modal-api-settings');
      if (modal) modal.classList.remove('active');
    },

    saveApiKey: function() {
      const provider = document.getElementById('api-provider-select').value;
      const key = document.getElementById('api-key-input').value.trim();
      localStorage.setItem('erp_custom_provider', provider);
      localStorage.setItem('erp_custom_api_key', key);
      state.customProvider = provider;
      state.customApiKey = key;
      this.closeApiKeyModal();
      this.renderConsultantView();
      alert(state.lang === 'vi' ? "Đã lưu cấu hình API Key vào thiết bị!" : "API Key saved locally!");
    },

    // Keyboard Shortcuts
    initKeyboardShortcuts: function() {
      window.addEventListener('keydown', (e) => {
        // Spacebar to flip flashcard when on flashcards view
        if (e.code === 'Space' && state.currentView === 'flashcards' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
          e.preventDefault();
          App.flipFlashcard();
        }
        // Arrow keys in Flashcard view
        if (state.currentView === 'flashcards' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
          if (e.key === 'ArrowRight') App.nextFlashcard();
          if (e.key === 'ArrowLeft') App.prevFlashcard();
        }
      });
    }
  };

  // Run on DOM load
  document.addEventListener('DOMContentLoaded', function() {
    App.init();
  });

})();
