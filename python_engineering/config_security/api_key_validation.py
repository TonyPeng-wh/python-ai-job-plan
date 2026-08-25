# 导入 Python 自带的 os 模块
import os


# 从环境变量读取 API Key
api_key = os.getenv("OPENAI_API_KEY")


# TODO：
# 如果 api_key 不存在或为空，输出配置缺失提示
if not api_key:
    print("未配置有效的 OPENAI_API_KEY")
else:
    print("已成功读取 OPENAI_API_KEY")