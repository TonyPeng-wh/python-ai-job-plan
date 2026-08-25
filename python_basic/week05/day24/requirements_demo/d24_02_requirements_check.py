# 导入当前虚拟环境中的 requests 第三方库
import requests

# 输出当前实际使用的 requests 版本
print(f"当前 requests 版本：{requests.__version__}")

"""
python -m pip show requests 查看某一个包的信息。
python -m pip freeze 列出当前 Python 环境中安装的包，以及它们的版本。
"""


"""
② 新电脑恢复环境的完整顺序

完整顺序应该是：
进入项目目录
↓
创建虚拟环境 .venv
↓
激活 .venv
↓
python -m pip install -r requirements.txt
↓
依赖安装进 .venv
↓
运行项目

最重要的是：
requirements.txt 只是依赖清单，真正安装依赖的是 pip；
而依赖安装到哪里，取决于当前使用的是哪个 Python 环境。
"""