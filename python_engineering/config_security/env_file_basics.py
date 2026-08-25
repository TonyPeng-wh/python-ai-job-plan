# 导入 Python 自带的 os 模块
import os

# 从 python-dotenv 中导入 load_dotenv
from dotenv import load_dotenv


# TODO 1：
# 加载 .env 文件
load_dotenv()

# TODO 2：
# 从环境变量中读取 OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")


# 检查配置是否存在，但不打印 Key 本身
if not api_key:
    print("未配置有效的 OPENAI_API_KEY")
else:
    print("已成功从 .env 读取 OPENAI_API_KEY")