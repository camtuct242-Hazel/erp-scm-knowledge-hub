with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of app.js:", len(text))
pos_i18n = text.find('const I18N = {')
pos_state = text.find('const state = {')
pos_init = text.find('initApp: function() {')
pos_fc = text.find('renderFlashcard: function() {')
pos_cases = text.find('renderCaseStudy: function() {')
pos_ai = text.find('renderConsultantView: function() {')

print("pos_i18n:", pos_i18n)
print("pos_state:", pos_state)
print("pos_init:", pos_init)
print("pos_fc:", pos_fc)
print("pos_cases:", pos_cases)
print("pos_ai:", pos_ai)
