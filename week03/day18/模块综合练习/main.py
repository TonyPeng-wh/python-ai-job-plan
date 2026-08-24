import feedbacks_utils

feedback_list = [
    {"category": "回答错误", "processed": False},
    {"category": "格式问题", "processed": True},
    {"category": "回答错误", "processed": False},
    {"category": "检索失败", "processed": True}
]

answer_error_count = feedbacks_utils.count_answer_errors(feedback_list)
unprocessed_feedbacks_count = feedbacks_utils.count_unprocessed_feedbacks(feedback_list)

print(f"回答错误数量：{answer_error_count}")
print(f"未处理反馈数量：{unprocessed_feedbacks_count}")
