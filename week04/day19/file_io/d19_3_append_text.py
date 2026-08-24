"""
"a" 代表 append（追加）。

"w"
→ 文件不存在：创建
→ 文件存在：先清空，再写
"a"
→ 文件不存在：创建
→ 文件存在：保留旧内容，在末尾继续写
"""
report_file = open(
    "feedback_report.txt",
    "a",
    encoding="utf-8"
)

report_file.write("\n回答错误数量：3")

report_file.close()


"""
list.append(元素)
→ 元素可以是 str、int、dict、list 等

文本文件.write(字符串)
→ 通常必须是 str
"""