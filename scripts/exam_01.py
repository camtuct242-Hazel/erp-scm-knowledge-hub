# -*- coding: utf-8 -*-
# EXAM 01: ERP Fundamentals & SCM Flows (chap-01)
# 25 Questions: Q001 to Q025 (10 Basic, 10 Intermediate, 5 Advanced)

def get_questions():
    from scripts.exams_part1 import get_exams_1_to_5
    return get_exams_1_to_5()[:25]
