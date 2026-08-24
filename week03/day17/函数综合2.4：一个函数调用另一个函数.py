# 这次增加一点实际项目里很常见的情况：判断标准不是固定的，而是从参数传进去。
def count_answer_errors(feedbacks):
    count_categories = 0
    for current_feedback in feedbacks:
        if current_feedback["category"] == "回答错误":
            count_categories = count_categories + 1
    return count_categories

feedback_list = [
    {"category": "回答错误"},
    {"category": "回答错误"},
    {"category": "格式问题"},
    {"category": "检索失败"},
    {"category": "回答错误"}
]

def check_answer_quality(feedbacks,error_limit):
    count_categories = count_answer_errors(feedbacks)
    if count_categories >= error_limit:
        return "需要优化"
    else:
        return "质量正常"

quality_status = check_answer_quality(feedback_list,3)

print(f"回答质量状态：{quality_status}")

status_1 = check_answer_quality(feedback_list, 2)
status_2 = check_answer_quality(feedback_list, 3)
status_3 = check_answer_quality(feedback_list, 4)

print(f"阈值为2{status_1}")
print(f"阈值为3{status_2}")
print(f"阈值为4{status_3}")


"""
def 定义函数
参数接收数据
return 返回结果
外部变量保存返回值
一个参数 / 多个参数
默认参数、位置参数、关键字参数
list / dict 作为参数
函数处理数据并统计
一个函数调用另一个函数
用参数控制判断标准
"""