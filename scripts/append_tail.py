tail_code = """
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
"""

with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Check if openApiKeyModal already present
if 'openApiKeyModal:' not in code:
    code = code.rstrip() + tail_code
    with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Appended tail methods and closing IIFE to app.js!")
else:
    print("openApiKeyModal already present.")
