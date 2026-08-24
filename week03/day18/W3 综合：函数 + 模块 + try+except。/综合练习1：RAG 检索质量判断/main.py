import retrieval_utils
try:
    retrieval_score = float(input("请输入检索分数："))
except ValueError:
    print("检索分数格式错误")
else:
    if retrieval_score >= 0 and retrieval_score <= 1:
        result = retrieval_utils.check_retrieval_quality(retrieval_score)
        print(f"检索状态为：{result}")
    else:
        print("检索分数必须在0到1之间")