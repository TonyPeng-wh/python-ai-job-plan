"""
不同代码可能产生不同类型的错误,所以需要多个except处理不同问题。
"""
try:
    answer_count = int(input("请输入回答数量："))
    error_count = int(input("请输入错误数量："))

    error_rate = error_count / answer_count

    print(f"回答错误率：{error_rate}")

except ValueError:
    print("请输入整数")

except ZeroDivisionError:
    print("回答总数不能为0")
# 一个 try 后面可以有多个 except，分别处理不同错误。