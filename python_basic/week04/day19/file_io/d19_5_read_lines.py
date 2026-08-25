# 逐行读取 TXT 文件。
# 先用你已经学过的 for：
with open(
    "week04/day19/file_io/feedback_notes.txt",
    "r",
    encoding="utf-8"
) as feedback_file:
    for current_line in feedback_file:
        cleaned_line = current_line.strip()# 和字符串基础一样用.strip()清除两侧空白，这里是清除空行
        print(cleaned_line)

"""
feedback_file
→ 整个文件对象

current_line
→ 当前这一行文本
→ str
"""