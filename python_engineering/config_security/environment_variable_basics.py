# 环境变量是什么，以及 Python 如何用 os.getenv() 读取它。
# 环境变量是什么? :操作系统提供给程序使用的一组“名字 → 值”的配置数据。

import os

# 如果没有专门配置运行模式，就默认使用开发模式。
# 但对于 API Key，通常就不能随便给一个假的默认值。
app_mode = os.getenv("AI_APP_MODE", "development")

print(f"当前应用模式：{app_mode}")
print(f"app_mode 的数据类型：{type(app_mode)}")


"""
对于必须存在的秘密配置，更合理的思路通常是：
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    print("未配置 API Key")
"""