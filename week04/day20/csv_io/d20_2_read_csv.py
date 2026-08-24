# 读取 CSV 为字典,让 CSV 的每一行直接变成一个 dict。
import csv
with open(
    "week04/day20/csv_io/feedback_data.csv",
    "r",
    encoding="utf-8"
)as feedback_file:
    feedback_reader = csv.DictReader(feedback_file)
    """
    csv.DictReader() 是什么意思？
    csv
    → csv 模块
    DictReader
    → Dictionary Reader
    → 按字典方式读取 CSV
    """
    for current_feedback in feedback_reader:
        print(current_feedback)