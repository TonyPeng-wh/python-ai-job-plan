import csv
feedback_list = []
with open(
    "week04/day20/csv_io/feedback_data.csv",
    "r",
    encoding="utf-8"
)as feedback_file:      # 把刚刚打开的文件对象命名为 feedback_file。
    feedback_reader = csv.DictReader(feedback_file) # csv.DictReader() 会按照字典方式读取 CSV。
    for current_feedback in feedback_reader:    # 开始遍历 CSV。
        current_feedback["processed"] = (       # 修改当前字典里的："processed",因为 CSV 读进来的："False",只是字符串 str。
            current_feedback["processed"] == "True" # 这是一个比较表达式。
        )
    feedback_list.append(current_feedback)

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
    newline=""      # 避免写出的 CSV 出现多余空行。
) as output_file:
    feedback_writer = csv.DictWriter(   # CSV 字典写入器。
        output_file,
        fieldnames=field_names
    )

    feedback_writer.writeheader()

    for current_feedback in feedback_list:
        feedback_writer.writerow(current_feedback)