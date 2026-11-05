with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
methods = ['startExam', 'submitExamNow', 'exitExam', 'renderActiveExamQuestion', 'openSubmitConfirmationModal']
for m in methods:
    idx = code.find(f'{m}:')
    if idx != -1:
        print(f"=== {m} ===")
        print(code[idx:idx+500])
