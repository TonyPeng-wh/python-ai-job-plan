#  JSON 和 Python 的 dict / list 到底是什么关系？
# 你会先看到这种 JSON 数据：
[
    {
        "feedback_id": "F001",
        "category": "回答错误",
        "processed": false,
        "priority": "HIGH"
    },
    {
        "feedback_id": "F002",
        "category": "格式问题",
        "processed": true,
        "priority": "LOW"
    }
]
# 你应该会发现它非常像 Python：
feedback_list = [
    {
        "feedback_id": "F001",
        "category": "回答错误",
        "processed": False,
        "priority": "HIGH"
    }
]
# 但它们不是同一种东西。下一节会重点搞清楚这几个对应关系：
# JSON object   ↔ Python dict
# JSON array    ↔ Python list
# JSON string   ↔ Python str
# JSON number   ↔ Python int / float
# JSON true     ↔ Python True
# JSON false    ↔ Python False
# JSON null     ↔ Python None