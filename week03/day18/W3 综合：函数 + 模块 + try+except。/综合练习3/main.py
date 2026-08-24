import answer_utils
try:
    answer_score = float(input("请输入回答质量分数："))
except ValueError:
    print("回答质量分数格式错误")
else:
    if answer_score >= 0 and answer_score <= 1:
        answer_quality = answer_utils.check_answer_quality(answer_score)
        print(f"回答质量状态：{answer_quality}")
    else:
        print("回答质量分数必须在0到1之间")