with open('outputs/app/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_styles = """
/* ==========================================================================
   Phase 3B: Chapter Navigation, BA Insight & Exam Lock
   ========================================================================== */

/* Chapter Reader Layout & Nav */
.chapter-reader-top-bar {
  margin-bottom: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.chapter-nav-cluster {
  display: flex;
  gap: 0.4rem;
  align-items: center;
  flex-wrap: wrap;
}

.chapter-nav-btn {
  font-weight: 600;
  transition: all 0.2s ease;
}

.chapter-nav-btn:disabled,
.chapter-nav-btn.disabled {
  opacity: 0.45 !important;
  cursor: not-allowed !important;
  pointer-events: none !important;
  background: var(--bg-subtle) !important;
  border-color: var(--border-color) !important;
  color: var(--text-subtle) !important;
}

.chapter-header-banner {
  margin-bottom: 1.75rem;
  padding: 1.4rem 1.75rem;
  background: var(--bg-subtle);
  border-radius: var(--radius-md);
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
}

.chapter-banner-title {
  font-family: var(--font-serif);
  font-size: 1.45rem;
  margin-top: 0.35rem;
  margin-bottom: 0.25rem;
  color: var(--coffee-bean);
  line-height: 1.35;
}

.chapter-banner-subtitle {
  font-size: 0.88rem;
  color: var(--muted-mauve);
}

.chapter-reader-bottom-nav {
  margin-top: 2.5rem;
  padding: 1.5rem 0;
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

/* BA Insight Callout */
.ba-insight-callout {
  background: var(--bg-subtle);
  border-left: 4px solid var(--dusty-rose-dark);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 1.25rem 1.5rem;
  margin: 1.75rem 0;
  box-shadow: var(--shadow-sm);
}

.ba-insight-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-serif);
  font-size: 1.05rem;
  color: var(--coffee-bean);
  margin-bottom: 0.6rem;
}

.ba-insight-divider {
  margin: 0.9rem 0;
  border-top: 1px dashed var(--border-color);
}

.ba-insight-header-en {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  color: var(--muted-mauve);
  margin-bottom: 0.4rem;
}

.ba-insight-text-en {
  font-size: 0.88rem;
  color: var(--muted-mauve);
  line-height: 1.6;
}

/* Review Answer Accordion */
.review-answer-accordion {
  margin-top: 0.8rem;
  margin-bottom: 1.2rem;
  border-radius: var(--radius-sm);
  background: var(--bg-subtle);
  border: 1px solid var(--border-color);
  overflow: hidden;
  transition: all 0.2s ease;
}

.review-answer-accordion summary {
  padding: 0.65rem 1rem;
  font-weight: 600;
  font-size: 0.88rem;
  color: var(--dusty-rose-dark);
  cursor: pointer;
  user-select: none;
  background: var(--surface-subtle);
  transition: background 0.2s ease;
}

.review-answer-accordion summary:hover {
  background: var(--warm-beige);
  color: var(--coffee-bean);
}

.review-answer-content {
  padding: 1rem 1.25rem;
  border-top: 1px solid var(--border-color);
  background: #FFFFFF;
  line-height: 1.65;
  font-size: 0.92rem;
}

/* Timed Exam Navigation Lock */
body.exam-locked .app-nav {
  display: none !important;
}

body.exam-locked .brand {
  pointer-events: none !important;
  cursor: default !important;
}

body.exam-locked .header-actions {
  display: none !important;
}

body.exam-locked .scroll-to-top-btn {
  display: none !important;
}
"""

if "Phase 3B: Chapter Navigation" not in css:
    css += new_styles
    with open('outputs/app/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated with Phase 3B styles!")
else:
    print("style.css already contains Phase 3B styles.")
