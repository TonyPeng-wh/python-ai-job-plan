"""
个人学习信息程序
"""

name = input("请输入姓名：")
major = input("请输入专业：")
target_role = input("请输入目标岗位：")
weekly_hours = int(input("请输入本周计划学习小时数："))
daily_hours = weekly_hours / 7


print()
print("===== 个人学习计划 =====")
print(f"我叫{name}，专业是{major}。")
print(f"我的目标岗位是{target_role}。")
print(f"本周计划学习{weekly_hours}小时。")
print(f"每天计划学习{daily_hours:.1f}小时。")