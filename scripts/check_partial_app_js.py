with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Let's see what is already replaced
print("Checking previous replacements...")
print("render_math_helper present:", "renderMath: function" in code)
print("scrollToTop present:", "scrollToTop: function" in code)
print("flashcardChapterFilter present:", "flashcardChapterFilter" in code)
print("chatContextChapter present:", "chatContextChapter" in code)
