# JSON 数据读取 → 统计 → 输出报告 JSON。
# 这一步不增加新语法，而是把今天的 JSON 和你之前学过的 for / if / dict / count 串起来。
import json

with open(
    "week05/day21/json_io/feedback_list.json",
    "r",
    encoding="utf-8"
) as feedback_file:
    feedback_list = json.load(feedback_file)

feedback_count = len(feedback_list)
unprocessed_feedback_count = 0

for current_feedback in feedback_list:
    if current_feedback["processed"] == False:
        unprocessed_feedback_count = unprocessed_feedback_count + 1
print(f"反馈总数：{feedback_count}")
print(f"未处理反馈数量：{unprocessed_feedback_count}")


#json.dump() 最适合接收一份完整的 Python 数据结构，而你前面现在有的是几个彼此分开的变量,所以需要变成dict
report_data = {
    "feedback_count": feedback_count,
    "unprocessed_feedback_count": unprocessed_feedback_count
}

with open(
    "week05/day21/json_io/feedback_report.json",
    "w",
    encoding="utf-8"
) as output_file:
    json.dump(
        report_data,
        output_file,
        ensure_ascii=False,
        indent=4
    )