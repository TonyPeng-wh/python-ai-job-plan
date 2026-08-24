# 读取 JSON → 修改数据 → 再保存 JSON。
import json

with open(
    "week05/day21/json_io/feedback_list.json",
    "r",
    encoding="utf-8"
)as feedback_file:
    feedback_list = json.load(feedback_file)
    for current_feedback in feedback_list:
        if current_feedback["feedback_id"] == "F001":
            current_feedback["processed"] = True
with open(
    "week05/day21/json_io/feedback_list.json",
    "w",
    encoding="utf-8"
) as output_file:
    json.dump(
        feedback_list,
        output_file,
        ensure_ascii=False,
        indent=4
    )