# 函数 + try / except
# 业务场景：AI 检索分数输入检查。
def get_retrieval_score():

    try:
        retrieval_score = float(input("请输入检索分数："))
        return retrieval_score
    except ValueError:
        return -1

retrieval_score = get_retrieval_score()

if retrieval_score == -1:
    print("检索分数格式错误")
else:
    print(f"检索分数：{retrieval_score}")