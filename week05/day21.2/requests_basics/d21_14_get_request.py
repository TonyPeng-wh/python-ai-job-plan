# GET 请求。GET 可以先理解成：向服务器“获取数据”。

# response = requests.get("某个网址")
# “请把这个网址对应的数据返回给我。”

# 注意，模型调用后面很多时候会用到 POST，因为要把问题、参数等数据一起发送给服务器。但现在先不学 POST，先把最简单的 GET 搞清楚。

import requests

response = requests.get("https://example.com")
# <Response [200]>    200叫 HTTP 状态码。它表示服务器有没有正常处理你的请求。
print(response)
"""
200
→ 请求成功

requests.get(...)
↓
response 响应对象
↓
response 里面包含
    状态码
    返回文本
    JSON 数据
    ...
"""
