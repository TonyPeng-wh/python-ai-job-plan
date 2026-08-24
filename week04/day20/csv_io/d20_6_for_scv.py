import csv

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

field_names = [
    "feedback_id",
    "category",
    "processed",
    "priority"
]

with open(
    "week04/day20/csv_io/cleaned_feedback_data.csv",
    "w",
    encoding="utf-8",
    newline=""
) as output_file:
    feedback_writer = csv.DictWriter(
        output_file,
        fieldnames=field_names # fieldnames是 csv.DictWriter() 这个函数规定好的参数名。
    )

    feedback_writer.writeheader()

    for current_feedback in feedback_list:
        feedback_writer.writerow(current_feedback)# 把当前这个 dict 写成 CSV 的一行