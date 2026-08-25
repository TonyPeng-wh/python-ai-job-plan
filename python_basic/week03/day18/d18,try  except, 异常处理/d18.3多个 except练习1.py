try:
    total_count = int(input("请输入总数："))
    failed_count = int(input("请输入失败数量："))
    failure_rate = failed_count / total_count
    print(f"失败率为：{failure_rate:.2f}")

except ValueError:
    print("请输入整数")

except ZeroDivisionError:
    print("总数不能为零")