with open('outputs/app/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== INDEX.HTML AUDIT ===")
print("KaTeX CDN references:", "cdn.jsdelivr.net/npm/katex" in html)
print("Marked CDN references:", "cdn.jsdelivr.net/npm/marked" in html)
print("Vendor relative references:", "vendor/katex" in html)
print("Scroll to top button present:", "scroll-to-top" in html)
print("Consultant unified chat present (scenarios-sidebar present):", "scenarios-sidebar" in html)
print("Footer author Hazel present:", "Nguyễn Đăng Cẩm Tú" in html or "Hazel" in html)
print("Flashcards chapter dropdown present:", "fc-chapter-select" in html)

with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

print("\n=== APP.JS AUDIT ===")
print("renderMath helper present:", "renderMath:" in js)
print("scrollToTop function present:", "scrollToTop:" in js)
print("Unified chat handler present:", "chat-history" in js or "erp_chat_history" in js)
print("Flashcards total length in navbar metric:", "stat-flashcards-val" in js)
