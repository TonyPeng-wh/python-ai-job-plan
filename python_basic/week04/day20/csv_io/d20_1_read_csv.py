"""
1. 为什么要学 CSV？
CSV 可以保存成类似：(你可以把它先理解成一个简单的表格文件)
feedback_id,category,processed,priority
F001,回答错误,False,HIGH
F002,格式问题,True,LOW
F003,检索失败,False,HIGH

这就很接近你之前一直处理的：

feedback_list = [
    {
        "feedback_id": "F001",
        "category": "回答错误",
        "processed": False,
        "priority": "HIGH"
    }
]

2. CSV 和 TXT 有什么关系？
CSV 本质上仍然是文本文件。只不过它约定：用逗号 , 分隔不同字段。
所以 CSV 的名字就是：Comma-Separated Values逗号分隔的值。
"""
