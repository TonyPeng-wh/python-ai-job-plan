"""
try 里到底放哪些代码
"""
try:
    retrieval_score = float(input("请输入检索分数："))

    if retrieval_score >= 0.75:
        print("检索合格")
    else:
        print("检索不合格")

except ValueError:
    print("检索分数格式错误")



