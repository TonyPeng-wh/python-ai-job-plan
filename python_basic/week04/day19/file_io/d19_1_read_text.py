"""
现在要开始解决一个真实问题：数据不写在 Python 代码里，而是已经存在电脑文件中，Python 怎么把它读进来？
这正是从“语法练习”迈向“数据处理程序”的关键一步。
open()Python 要读取文件，首先需要把文件“打开”
"""
# feedback_file 保存的是文件对象，不是文本内容本身。
# 找到 feedback_notes.txt，按照 UTF-8 编码，以读取模式打开它。
feedback_file = open(
    "feedback_notes.txt",
    "r",
    encoding="utf-8"
)

feedback_text = feedback_file.read()
print(feedback_text)
feedback_file.close()

"""
"r" → read，读取

"feedback_notes.txt"
文件路径字符串
        ↓
      open()
找到并打开文件
        ↓
feedback_file
文件对象
        ↓
     .read()
读取文件内容
        ↓
feedback_text
str 字符串
"""