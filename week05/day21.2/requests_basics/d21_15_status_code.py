# response.status_code：查看服务器返回的 HTTP 状态码
import requests

response = requests.get("https://example.com")

print(response.status_code) # response.status_code从 response 这个响应对象里，取出“状态码”。
"""
你的 Python 程序
↓
requests.get()
↓
向服务器发送 GET 请求
↓
服务器返回响应
↓
response 保存响应对象

为什么状态码有用？
因为程序不能只知道：
“服务器给我回东西了。”
还要知道：
“这次请求到底成功没有？”
"""
print(type(response.status_code))

# 404
# → 请求的资源找不到

# 500
# → 服务器内部出现错误

import requests

response = requests.get("https://example.com")

print(response.status_code)
print(type(response.status_code))

if response.status_code == 200:
    print("请求成功")
else:
    print("请求失败")