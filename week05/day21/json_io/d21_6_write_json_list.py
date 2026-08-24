# 把整个 list[dict] 写成 JSON 文件。
import json

feedback_list = [
    {
        "feedback_id": "F001",
        "category": "回答错误",
        "processed": False,
        "priority": "HIGH"
    },
    {
        "feedback_id": "F002",
        "category": "格式问题",
        "processed": True,
        "priority": "LOW"
    },
    {
        "feedback_id": "F003",
        "category": "检索失败",
        "processed": False,
        "priority": "HIGH"
    }
]

with open(
    "week05/day21/json_io/feedback_list.json",
    "w",
    encoding="utf-8"
)as output_file:
    json.dump(
        feedback_list,
        output_file,
        ensure_ascii=False,
        indent=4
    )


"""
CSV
→ 一行一条记录
→ 常配合 for + writerow()

JSON
→ 可以保存完整嵌套结构
→ json.dump() 可以一次写整个 list[dict]
"""