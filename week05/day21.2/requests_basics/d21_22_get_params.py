# 向服务器发 GET 请求时，除了网址，还可以附带查询条件。
import requests

query_params = {
    "fault_type": "充电故障",
    "priority": "HIGH"
}
try:
    response = requests.get(
        "https://postman-echo.com/get",
        params=query_params,
        timeout=10
    )

    if response.status_code == 200:
        response_data = response.json()

        print("请求成功")
        print(response_data["args"])
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(f"实际请求地址：{response.url}")
        print(response.text)
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")

"""
① import requests
   ↓
准备 HTTP 请求工具

② query_params
   ↓
准备要发送的查询条件

③ requests.get(...)
   ↓
发送 GET 请求

④ params=query_params
   ↓
把字典作为查询参数发给服务器

⑤ timeout=10
   ↓
防止请求无限等待

⑥ response
   ↓
拿到服务器响应对象

⑦ response.status_code
   ↓
判断 HTTP 请求结果

      ├─ 200
      │   ↓
      │ response.json()
      │   ↓
      │ 得到 Python 数据
      │   ↓
      │ response_data["args"]
      │   ↓
      │ 读取具体字段
      │
      └─ 非 200
          ↓
          输出状态码、URL、响应正文

如果请求过程中发生 Timeout
↓
except
↓
输出“请求超时”
"""