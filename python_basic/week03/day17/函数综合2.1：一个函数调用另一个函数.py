def count_answer_errors(feedbacks):
    count_category = 0
    for current_feedback in feedbacks:
        if current_feedback["category"] == "回答错误":
            count_category = count_category + 1
    return count_category

morning_feedbacks = [
    {"category":"回答错误"},
    {"category":"格式问题"},
    {"category":"回答错误"}
]
afternoon_feedbacks = [
    {"category": "检索失败"},
    {"category": "回答错误"},
    {"category": "格式问题"}
]
evening_feedbacks = [
    {"category": "回答错误"},
    {"category": "回答错误"},
    {"category": "回答错误"},
    {"category": "检索失败"}
]

def check_feedback_risk(feedbacks):
    count_category = count_answer_errors(feedbacks)
    if count_category >= 3:
        return "高风险"
    else:
        return "正常"

morning_risk = check_feedback_risk(morning_feedbacks)
afternoon_risk = check_feedback_risk(afternoon_feedbacks)
evening_risk = check_feedback_risk(evening_feedbacks)

print(f"上午反馈风险：{morning_risk}")
print(f"下午反馈风险：{afternoon_risk}")
print(f"晚上反馈风险：{evening_risk}")




