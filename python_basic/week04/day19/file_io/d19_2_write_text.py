# 新语法："w" + .write()
"""
这在以后保存模型回答、日志、分析报告、故障诊断结果时都会用到。
TXT 文件写入,解决的是：Python → 文件
"""
report_file = open(
    "feedback_report.txt",
    "w",
    encoding="utf-8"
)
report_file.write("反馈分析完成")
report_file.close()

"""
"w" → write，写入；文件不存在就创建，存在就覆盖
"""