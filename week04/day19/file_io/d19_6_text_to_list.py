"""
把 TXT 的每一行保存到 list
前面只是读出来然后打印，但真实数据处理时，我们通常还要继续统计、分类、判断，所以需要先把数据保存下来。
"""
"""
思路：
先准备一个空容器
↓
遍历数据
↓
把处理后的结果一个个放进去
"""
feedback_list = []

with open(
    "week04/day19/file_io/feedback_notes.txt",
    "r",
    encoding="utf-8"
) as feedback_file:
    for current_line in feedback_file:
        cleaned_line =current_line.strip()
        if cleaned_line != "":
            feedback_list.append(cleaned_line)
print(feedback_list)
print(type(feedback_list))

valid_feedback_count = len(feedback_list)
print(f"有效反馈数量：{valid_feedback_count}")
