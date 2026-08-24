import csv

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

        print(current_feedback)
        print(type(current_feedback["processed"]))