# 让 JSON 输出更适合人阅读。
"""
今天只增加两个参数：
ensure_ascii=False #主要解决的是中文可读性。
indent=4 # 表示 JSON 每一层用 4 个空格缩进。
"""
import json

feedback_data = {
    "feedback_id": "F001",
    "category": "回答错误",
    "processed": False,
    "retrieval_score": 0.82,
    "error_message": None
}

with open(
    "week05/day21/json_io/feedback_result.json",
    "w",
    encoding="utf-8"
) as output_file:
    json.dump(
        feedback_data,
        output_file,
        ensure_ascii=False, # 主要解决的是中文可读性。
        indent=4    # 表示 JSON 每一层用 4 个空格缩进。
    )