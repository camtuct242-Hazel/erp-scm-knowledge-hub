with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    c = f.read()

t1 = "'glossary-search': lang === 'vi' ? '🔍 Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa...' : '🔍 Search terms, abbreviations, definitions...'"
r1 = "'glossary-search': lang === 'vi' ? 'Tìm kiếm thuật ngữ, từ viết tắt, định nghĩa...' : 'Search terms, abbreviations, definitions...'"

t2 = "exEl.innerHTML = `<strong>💡 ${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Context:'}</strong> ${card.example}`;"
r2 = "exEl.innerHTML = `<strong>${state.lang === 'vi' ? 'Ví dụ thực tiễn & Hàm ý ERP:' : 'Practical ERP Context:'}</strong> ${card.example}`;"

t3 = "modeBadge.innerText = `🤖 ${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Grounded Mode'}`;"
r3 = "modeBadge.innerText = `${state.lang === 'vi' ? 'Chế độ Tri thức Offline (Grounded Mode)' : 'Offline Grounded Mode'}`;"

t4 = "<p>💡 <em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc gõ trực tiếp câu hỏi thảo luận bên dưới!</em></p>"
r4 = "<p><em>Bạn có thể nhấp chọn một trong các gợi ý kịch bản phía trên để đưa prompt vào ô soạn thảo, hoặc gõ trực tiếp câu hỏi thảo luận bên dưới!</em></p>"

assert t1 in c, "t1 not found"
c = c.replace(t1, r1)

assert t2 in c, "t2 not found"
c = c.replace(t2, r2)

assert t3 in c, "t3 not found"
c = c.replace(t3, r3)

assert t4 in c, "t4 not found"
c = c.replace(t4, r4)

with open('outputs/app/app.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("All 4 final emojis in app.js cleaned successfully.")
