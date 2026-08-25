import json
feedback_data = {
    "feedback_id": "F001",
    "category": "回答错误",
    "processed": False,
    "retrieval_score": 0.82,
    "error_message": None
}

# 我们的目标是把它保存成：feedback_result.json
with open(
    "week05/day21/json_io/feedback_result.json",
    "w",
    encoding="utf-8"
)as output_file:
        # json.dump()Python 数据→ JSON 文件,和.load()相反
        json.dump(
        feedback_data,
        output_file
    )
# 把 Python 里的 feedback_data 数据，转换成 JSON 格式，并写进 output_file 这个文件。
# json.dump(要写的数据, 要写到的文件)