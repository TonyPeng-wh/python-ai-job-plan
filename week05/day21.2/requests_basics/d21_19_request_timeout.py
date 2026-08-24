# 给 requests.get() 加超时限制，并用 try/except 处理请求超时。
import requests
try:
    response = requests.get(
        "https://httpbin.org/get",
        timeout=10
    )

    print(response.status_code)
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")

"""
ValueError
→ 值/类型转换问题

FileNotFoundError
→ 文件找不到

requests.exceptions.Timeout
→ 网络请求超时
"""