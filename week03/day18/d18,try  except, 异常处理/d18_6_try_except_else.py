# 函数 + 模块 + 异常处理综合。
# try / except / else 主要在以后代码变长时有价值：可以让 try 里只放“可能报错的代码”，正常业务逻辑放到 else，职责更明确。
try:
    retrieval_score = float(input("请输入检索分数："))

except ValueError:
    print("检索分数格式错误")

else: # =====
    if retrieval_score >= 0.75:
        print("检索合格")
    else:
        print("检索不合格")