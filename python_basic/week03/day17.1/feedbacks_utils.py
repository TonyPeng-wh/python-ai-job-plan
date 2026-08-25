def count_answer_errors(feedbacks):
    answer_error_count = 0
    for current_feedback in feedbacks:
        if current_feedback["category"] == "回答错误":
            answer_error_count = answer_error_count + 1
    return answer_error_count
