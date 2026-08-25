# for 遍历
# set 也可以像 list 一样遍历：
fault_types = {
    "电池故障",
    "充电故障",
    "通信故障"
}

for current_fault_type in fault_types:
    print(current_fault_type)


feedback_categories = {
    "回答错误",
    "格式问题",
    "检索失败"
}
for current_feedback_category in feedback_categories:
    print(f"反馈类型：{current_feedback_category}")

# 空集合要这样写：empty_set = set()
# empty_data = {}这个不是空 set，而是空 dict。

"""
result = 空容器

for current_item in 数据:
    result.add(需要的值)

return result

你以后做“收集不重复的故障类型、工单类型、模型名称”时都会遇到这个结构。
"""