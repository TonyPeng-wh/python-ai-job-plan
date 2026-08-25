def check_answer_quality(answer_score):
    if answer_score >= 0.8:
        return "质量良好"
    elif answer_score >= 0.6:
        return "需要优化"
    else:
        return "质量较差"