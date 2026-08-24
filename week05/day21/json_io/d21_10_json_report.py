# 给 JSON 统计报告增加一个指标。JSON读取 → 遍历统计 → 组织报告字典 → 保存JSON报告 的完整流程
"""
JSON 文件
→ json.load()
→ feedback_list
→ 统计
→ report_data
→ json.dump()
→ JSON 报告
"""
import json

with open(
    "week05/day21/json_io/feedback_list.json",
    "r",
    encoding="utf-8"
) as feedback_file:
    feedback_list = json.load(feedback_file)

feedback_count = len(feedback_list)
unprocessed_feedback_count = 0
high_priority_feedback_count = 0

for current_feedback in feedback_list:
    if current_feedback["processed"] == False:
        unprocessed_feedback_count = unprocessed_feedback_count + 1
    if current_feedback["priority"] == "HIGH":
        high_priority_feedback_count = high_priority_feedback_count + 1
print(f"反馈总数：{feedback_count}")
print(f"未处理反馈数量：{unprocessed_feedback_count}")
print(f"HIGH优先级反馈数量：{high_priority_feedback_count}")

report_data = {
    "feedback_count": feedback_count,
    "unprocessed_feedback_count": unprocessed_feedback_count,
    "high_priority_feedback_count": high_priority_feedback_count
}

with open(
    "week05/day21/json_io/feedback_report.json",
    "w",
    encoding="utf-8",
)as output_file:
    json.dump(
        report_data,
        output_file,
        ensure_ascii=False,
        indent=4
    )