# 把 .json 文件里的数据，读取成 Python 的 list / dict。
# 导入 json 模块
import json

# 打开 JSON 文件
with open(
    "week05/day21/json_io/feedback_data.json",
    "r",
    encoding="utf-8"
)as feedback_file:
    # 从 feedback_file 里读取 JSON，并自动转换成 Python 数据类型。
    feedback_list = json.load(feedback_file)
print(feedback_list)
print(type(feedback_list))
print(type(feedback_list[0]))
print(type(feedback_list[0]["processed"]))

"""
CSV 的 False
→ DictReader 后是 "False"
→ str
→ 需要自己转换

JSON 的 false
→ json.load() 后是 False
→ bool
→ 自动转换
"""