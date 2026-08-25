import feedbacks_utils
feedback_list = [
    {"category": "回答错误"},
    {"category": "格式问题"},
    {"category": "回答错误"},
    {"category": "检索失败"}
]
result = feedbacks_utils.count_answer_errors(feedback_list)
print(f"错误回答数量:{result}")