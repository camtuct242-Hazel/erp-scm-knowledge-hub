with open('outputs/app/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_lock = """/* Timed Exam Navigation Lock */
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
}"""

new_lock = """/* Timed Exam Navigation Lock */
body.exam-locked .nav-links {
  display: none !important;
}

body.exam-locked .brand-wrapper {
  pointer-events: none !important;
  cursor: default !important;
}

body.exam-locked .nav-actions {
  display: none !important;
}

body.exam-locked .scroll-to-top-btn {
  display: none !important;
}"""

if old_lock in css:
    css = css.replace(old_lock, new_lock)
    with open('outputs/app/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css navigation lock updated successfully!")
else:
    print("old_lock pattern not found in style.css")
