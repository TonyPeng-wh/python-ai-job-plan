"""
当某段代码可能报错时，用 try / except 让程序不要直接崩掉。

"""


try:
    retrieval_score = float(input("请输入检索分数："))
    print(f"检索分数：{retrieval_score}")
except ValueError:
    print("检索分数格式错误")

"""
try
→ 尝试运行这里面的代码

如果没有报 ValueError
→ 正常继续

如果出现 ValueError
→ 跳到 except ValueError
→ 执行异常处理代码
"""
