# except 处理“程序异常”，if 处理“业务不合法”
try:
    answer_quality_score = float(input("请输入回答质量分数："))
    if answer_quality_score >= 0 and answer_quality_score <= 1:
        print(f"回答质量分数：{answer_quality_score}")
    else:
        print("回答质量分数必须在0到1之间")

except ValueError:
    print("回答质量分数格式错误")