# 状态码判断 + 成功后再解析 JSON。先判断请求是否成功，再决定要不要处理服务器返回的数据。
"""
发送请求
↓
是否超时？
├─ 是 → except
└─ 否
   ↓
   status_code 是否 == 200？
   ├─ 是 → 解析 response.json()
   └─ 否 → 输出失败状态码
"""
import requests
try:
    response = requests.get(
        "https://httpbin.org/get",
        timeout=10
    )
    if response.status_code == 200:
        response_data = response.json()
        print("请求成功")
        print(response_data["url"]) # 从 response_data 里取出具体字段。从服务器返回的数据中，取出 url 这个字段对应的值。
    else:
        print(f"请求失败，状态码：{response.status_code}")
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")