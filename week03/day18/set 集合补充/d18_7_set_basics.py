# set 最常用的基础用途之一：去重。
ticket_categories = [
    "电池故障",
    "充电故障",
    "电池故障",
    "通信故障",
    "充电故障"
]
# 这是一个 list，里面有重复值。
category_set = set(ticket_categories)
# 重复值会被去掉。
# 注意：set 不保证像 list 一样保持你看到的固定顺序，所以不要依赖它的输出顺序。
print(category_set)


feedback_categories = [
    "回答错误",
    "格式问题",
    "回答错误",
    "检索失败",
    "格式问题"
]

unique_categories = set(feedback_categories)
print(unique_categories)
print(len(unique_categories))