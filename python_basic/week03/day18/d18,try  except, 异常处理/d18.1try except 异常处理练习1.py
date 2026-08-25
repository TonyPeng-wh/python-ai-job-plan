try:
    answer_quality_score = float(input("请输入回答质量分数："))
    print(f"回答质量分数为：{answer_quality_score}")
except ValueError:
    print("回答质量分数格式错误")