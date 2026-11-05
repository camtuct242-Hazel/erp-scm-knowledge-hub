with open("outputs/app/app.js", "r", encoding="utf-8") as f:
    text = f.read()

# Add to vi
vi_target = 'nav_consultant: "Cố Vấn AI",'
vi_replacement = '''nav_consultant: "Cố Vấn AI",
      nav_about: "Giới Thiệu",
      badge_about: "Thông Tin Nền Tảng",
      about_title: "Về ERP & Supply Chain Management Knowledge Hub",
      about_sub: "Nền tảng học tập & phân tích chuyên sâu chuẩn mực dành cho sinh viên, giảng viên và Business Analyst",
      about_mission_title: "Sứ Mệnh Học Thuật & Định Hướng Nghề Nghiệp",
      about_mission_p1: "ERP & SCM Knowledge Hub được xây dựng nhằm giải quyết khoảng cách giữa lý thuyết sách vở và thực tiễn triển khai các hệ sinh thái doanh nghiệp lớn (SAP S/4HANA, Oracle Cloud SCM). Thay vì chỉ tóm tắt tài liệu rời rạc, nền tảng kết hợp chặt chẽ giữa Nghiên cứu Vận hành (Operations Research), Khoa học Quản lý (Management Science) và Kỹ năng Phân tích Nghiệp vụ (Business Analysis).",
      about_mission_p2: "Học liệu tham chiếu cốt lõi bắt nguồn từ chương trình đào tạo chính quy Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management (UEH 2020) của tác giả Y Hoang, tích hợp cùng 4 bộ tình huống thực tế kinh điển: Texago Corp. (Lựa chọn địa điểm lọc dầu 2 tầng), Better Products Company (Phân bổ sản phẩm & phân công nguyên khối 0-1), Atlantic Coast Tire Corp. (Quản trị tồn kho khoa học EOQ & chiết khấu giá), và SOCA TV (Sản xuất bổ sung dần EPQ).",'''

# Add to en
en_target = 'nav_consultant: "AI Consultant",'
en_replacement = '''nav_consultant: "AI Consultant",
      nav_about: "About",
      badge_about: "Platform Overview",
      about_title: "About ERP & Supply Chain Management Knowledge Hub",
      about_sub: "Enterprise-standard educational and analytical platform for students, faculty, and Business Analysts",
      about_mission_title: "Academic Mission & Professional Alignment",
      about_mission_p1: "ERP & SCM Knowledge Hub was developed to bridge the gap between textbook theory and real-world enterprise deployments (SAP S/4HANA, Oracle Cloud SCM). Instead of isolated summaries, it systematically synthesizes Operations Research, Management Science, and Business Analysis.",
      about_mission_p2: "Core reference material originates from the accredited academic curriculum Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management (UEH 2020) by Y Hoang, synthesized with 4 classic real-world cases: Texago Corp., Better Products Company, Atlantic Coast Tire Corp., and SOCA TV.",'''

# Add to navigateTo
nav_target = '''case 'consultant':
          this.renderConsultantView();
          break;'''
nav_replacement = '''case 'consultant':
          this.renderConsultantView();
          break;
        case 'about':
          window.scrollTo({ top: 0, behavior: 'smooth' });
          break;'''

assert vi_target in text, "vi_target not found"
assert en_target in text, "en_target not found"
assert nav_target in text, "nav_target not found"

text = text.replace(vi_target, vi_replacement)
text = text.replace(en_target, en_replacement)
text = text.replace(nav_target, nav_replacement)

with open("outputs/app/app.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated app.js with about navigation and translations!")
