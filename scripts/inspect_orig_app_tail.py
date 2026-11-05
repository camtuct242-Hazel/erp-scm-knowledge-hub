with open('outputs/backup_before_enhancement/app/app.js', 'r', encoding='utf-8') as f:
    orig = f.read()

pos_ai_e = orig.find('generateIntelligentResponse: function(userQuery) {')
# find where generateIntelligentResponse ends
pos_next = orig.find('openApiKeyModal:', pos_ai_e)
print("pos_next found at:", pos_next)
print("--- Code after pos_next ---")
print(orig[pos_next-30:])
