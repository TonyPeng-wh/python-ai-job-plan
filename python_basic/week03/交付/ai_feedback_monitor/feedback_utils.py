# 负责从反馈数据中统计信息。

# 返回反馈总数。
def count_total_feedbacks(feedbacks):
    feedback_count = len(feedbacks)
    return feedback_count

# 返回 category == "回答错误" 的数量。
def count_answer_errors(feedbacks):
    answer_errors_count = 0
    for current_feedback in feedbacks:
        if current_feedback["category"] == "回答错误":
            answer_errors_count = answer_errors_count + 1
    return answer_errors_count

# 返回 processed == False 的数量。
def count_unprocessed_feedbacks(feedbacks):
    unprocessed_feedbacks_count = 0
    for current_feedback in feedbacks:
        if current_feedback["processed"] == False:
            unprocessed_feedbacks_count = unprocessed_feedbacks_count + 1
    return unprocessed_feedbacks_count

# 返回 priority == "HIGH" 的数量。
def count_high_priority_feedbacks(feedbacks):
    high_priority_feedbacks_count = 0
    for current_feedback in feedbacks:
        if current_feedback["priority"] == "HIGH":
            high_priority_feedbacks_count = high_priority_feedbacks_count + 1
    return high_priority_feedbacks_count

# 使用你刚学完的 set，返回不重复的反馈类型。
def get_feedback_categories(feedbacks):
    feedback_categories = set() # 先创建一个空集合。

    for current_feedback in feedbacks:
        feedback_categories.add(current_feedback["category"])

    return feedback_categories