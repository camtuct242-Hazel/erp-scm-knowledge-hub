with open('outputs/app/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add enhancements to style.css
enhancements = """
/* ==========================================================================
   MATHEMATICAL RENDERING (KATEX) & HORIZONTAL CONTAINMENT
   ========================================================================== */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  max-width: 100%;
  padding: 0.6rem 0.2rem;
  margin: 1rem 0;
  -webkit-overflow-scrolling: touch;
}
.katex {
  font-size: 1.05em;
  color: var(--coffee-bean);
}

/* ==========================================================================
   FLOATING SCROLL-TO-TOP BUTTON
   ========================================================================== */
.scroll-to-top-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: var(--surface-card);
  color: var(--coffee-bean);
  border: 1.5px solid var(--border-color);
  box-shadow: 0 4px 16px rgba(27, 17, 16, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 990;
  opacity: 0;
  visibility: hidden;
  transform: translateY(12px);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}
.scroll-to-top-btn.visible {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.scroll-to-top-btn:hover {
  background: var(--dusty-rose-dark);
  color: #ffffff;
  border-color: var(--dusty-rose-dark);
  box-shadow: 0 6px 20px rgba(184, 115, 126, 0.35);
  transform: translateY(-2px);
}
.scroll-to-top-btn:active {
  transform: translateY(0);
}
@media (max-width: 768px) {
  .scroll-to-top-btn {
    bottom: 1.2rem;
    right: 1.2rem;
    width: 40px;
    height: 40px;
  }
}

/* ==========================================================================
   CASE STUDIES & CHAPTER CONTENT TABLES (RESPONSIVE)
   ========================================================================== */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  margin: 1.2rem 0;
  -webkit-overflow-scrolling: touch;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-color);
  background: var(--surface-card);
}
.content-table {
  width: 100%;
  border-collapse: collapse;
  min-width: 580px;
  font-size: 0.9rem;
  text-align: left;
}
.content-table th {
  background: var(--surface-subtle);
  color: var(--coffee-bean);
  font-family: var(--font-serif);
  font-weight: 700;
  padding: 0.75rem 1rem;
  border-bottom: 2px solid var(--border-color);
}
.content-table td {
  padding: 0.65rem 1rem;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-main);
}
.content-table tr:last-child td {
  border-bottom: none;
}
.content-table tr:hover {
  background: rgba(255, 209, 220, 0.15);
}

/* ==========================================================================
   ENHANCED FLASHCARDS MODULE
   ========================================================================== */
.fc-filters-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  align-items: center;
  margin-bottom: 1.5rem;
}
.fc-chapter-select {
  padding: 0.45rem 0.9rem;
  border-radius: var(--radius-sm);
  border: 1.5px solid var(--border-color);
  background: var(--surface-card);
  color: var(--coffee-bean);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  outline: none;
}
.fc-chapter-select:focus {
  border-color: var(--dusty-rose-dark);
}
.flashcard-topic-tag {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--dusty-rose-dark);
  margin-top: 0.4rem;
}
.flashcard-keywords {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 0.8rem;
}
.flashcard-keyword-tag {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  background: var(--surface-subtle);
  color: var(--muted-mauve);
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  border: 1px solid var(--border-color);
}
.flashcard-example-box {
  margin-top: 0.9rem;
  padding: 0.6rem 0.8rem;
  background: var(--surface-subtle);
  border-left: 3px solid var(--dusty-rose-dark);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 0.83rem;
  color: var(--text-main);
  line-height: 1.5;
}

/* ==========================================================================
   AI STUDY CONSULTANT — UNIFIED CHAT INTERFACE
   ========================================================================== */
.unified-chat-layout {
  display: flex;
  flex-direction: column;
  background: var(--surface-card);
  border-radius: var(--radius-lg);
  border: 1.5px solid var(--border-color);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  margin-bottom: 2rem;
}
.unified-chat-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  background: var(--surface-subtle);
  border-bottom: 1.5px solid var(--border-color);
  flex-wrap: wrap;
  gap: 0.8rem;
}
.unified-chat-context-bar {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.6rem 1.5rem;
  background: rgba(255, 248, 245, 0.6);
  border-bottom: 1px solid var(--border-color);
  font-size: 0.82rem;
  flex-wrap: wrap;
}
.chat-context-select {
  padding: 0.3rem 0.6rem;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: #ffffff;
  color: var(--coffee-bean);
  font-size: 0.8rem;
  outline: none;
}
.unified-chat-messages {
  height: 480px;
  max-height: 60vh;
  overflow-y: auto;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  background: #ffffff;
  -webkit-overflow-scrolling: touch;
}
.chat-msg-row {
  display: flex;
  width: 100%;
}
.chat-msg-row.user {
  justify-content: flex-end;
}
.chat-msg-row.assistant {
  justify-content: flex-start;
}
.chat-bubble-container {
  max-width: 82%;
  display: flex;
  flex-direction: column;
}
.chat-msg-meta {
  font-size: 0.72rem;
  color: var(--text-subtle);
  margin-bottom: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.chat-msg-row.user .chat-msg-meta {
  justify-content: flex-end;
}
.chat-bubble-user {
  background: linear-gradient(135deg, var(--dusty-rose-dark), #9d5d6a);
  color: #ffffff;
  padding: 0.85rem 1.15rem;
  border-radius: 16px 16px 2px 16px;
  box-shadow: 0 2px 8px rgba(184, 115, 126, 0.25);
  font-size: 0.92rem;
  line-height: 1.6;
  word-break: break-word;
}
.chat-bubble-assistant {
  background: var(--surface-card);
  color: var(--text-main);
  padding: 1.1rem 1.3rem;
  border-radius: 16px 16px 16px 2px;
  border: 1.5px solid var(--border-color);
  box-shadow: var(--shadow-sm);
  font-size: 0.92rem;
  line-height: 1.65;
  word-break: break-word;
}
.chat-bubble-assistant h1, .chat-bubble-assistant h2, .chat-bubble-assistant h3, .chat-bubble-assistant h4 {
  font-family: var(--font-serif);
  color: var(--coffee-bean);
  margin-top: 0.6rem;
  margin-bottom: 0.4rem;
}
.chat-bubble-assistant ul, .chat-bubble-assistant ol {
  padding-left: 1.3rem;
  margin: 0.5rem 0;
}
.unified-chat-suggestions {
  padding: 0.8rem 1.5rem;
  background: var(--surface-subtle);
  border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);
}
.suggestions-scroll-row {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.2rem;
  -webkit-overflow-scrolling: touch;
}
.scenario-chip-btn {
  white-space: nowrap;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.35rem 0.75rem;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  background: #ffffff;
  color: var(--coffee-bean);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.scenario-chip-btn:hover {
  background: var(--soft-pink);
  border-color: var(--dusty-rose-dark);
  color: var(--dusty-rose-dark);
  transform: translateY(-1px);
}
.unified-chat-input-area {
  padding: 1rem 1.5rem;
  background: var(--surface-card);
  display: flex;
  gap: 0.8rem;
  align-items: flex-end;
}
.chat-textarea {
  flex: 1;
  min-height: 48px;
  max-height: 140px;
  padding: 0.75rem 1rem;
  border-radius: var(--radius-sm);
  border: 1.5px solid var(--border-color);
  background: #ffffff;
  color: var(--coffee-bean);
  font-family: var(--font-sans);
  font-size: 0.92rem;
  line-height: 1.5;
  resize: vertical;
  outline: none;
  transition: border-color 0.2s ease;
}
.chat-textarea:focus {
  border-color: var(--dusty-rose-dark);
  box-shadow: 0 0 0 3px rgba(223, 166, 181, 0.25);
}

/* ==========================================================================
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
}
"""

if "MATHEMATICAL RENDERING (KATEX)" not in css:
    with open('outputs/app/style.css', 'w', encoding='utf-8') as f:
        f.write(css + "\n" + enhancements)
    print("style.css successfully updated!")
else:
    print("style.css already contains enhancements.")
