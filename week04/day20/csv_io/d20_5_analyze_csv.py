"""
CSV 文件
→ 读取
→ 类型整理
→ feedback_list
→ 统计
"""
import csv 

field_names = [         # 是一个 list，里面保存 CSV 的字段名。也就是将来的表头
    "feedback_id",
    "category",
    "processed",
    "priority"
]

current_feedback = {
    "feedback_id": "F001",
    "category": "回答错误",
    "processed": False,
    "priority": "HIGH"
}

with open(
    "week04/day20/csv_io/cleaned_feedback_data.csv",
    "w",
    encoding="utf-8",
    newline=""          # 写 CSV 时，用来避免出现不需要的额外空行。
) as output_file:       # output_file我要写到哪个文件
    feedback_writer = csv.DictWriter(  # 负责按照这些字段写 CSV 的写入器
    output_file,
    fieldnames=field_names  # field_names CSV 有哪些字段
)
    feedback_writer.writeheader()

    feedback_writer.writerow(current_feedback)
