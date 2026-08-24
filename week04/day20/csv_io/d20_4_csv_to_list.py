import csv

feedback_list = []

with open(
    "week04/day20/csv_io/feedback_data.csv",
    "r",
    encoding="utf-8"
) as feedback_file:
    feedback_reader = csv.DictReader(feedback_file)

    for current_feedback in feedback_reader:
        current_feedback["processed"] = (
            current_feedback["processed"] == "True"
        )

        feedback_list.append(current_feedback)

print(feedback_list)

feedback_count = len(feedback_list)

print(f"反馈总数：{feedback_count}")