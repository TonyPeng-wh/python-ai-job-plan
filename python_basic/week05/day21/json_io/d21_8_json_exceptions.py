# 这一节不学新的异常处理结构，而是把你已经会的 try/except 用到 JSON 文件中。

"""
1. 文件根本不存在
→ FileNotFoundError

2. 文件存在，但是 JSON 格式写错
→ json.JSONDecodeError
"""
import json

try:
    with open(
        "week05/day21/json_io/feedback_list.json",
        "r",
        encoding="utf-8"
    ) as feedback_file:
        feedback_list = json.load(feedback_file)

    print("JSON数据读取成功")

except FileNotFoundError:
    print("JSON文件不存在")

except json.JSONDecodeError:
    print("JSON文件格式错误")

"""
open() 负责“文件能不能找到”，json.load() 负责“里面是不是合法 JSON”；两个阶段会产生不同异常。
"""