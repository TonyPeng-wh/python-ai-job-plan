import ticket_utils
try:
    fault_level = int(input("请输入错误等级："))

except ValueError:
    print("错误等级格式错误")

else:
    if fault_level >= 1 and fault_level<= 5:
        check_ticket_priority = ticket_utils.check_ticket_priority(fault_level)
        print(f"检查优先级为：{check_ticket_priority}")
    else:
        print("错误等级必须在1~5之间")