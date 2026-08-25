# “先判断状态码，再解析成功响应数据”
"""
200
→ 服务器正常返回我们预期的数据

503
→ 服务器可能返回错误页面

401
→ 服务器可能返回认证错误信息
而 response.json() 要求响应正文能够被解析为 JSON。
如果正文不是有效 JSON，它会产生 requests.exceptions.JSONDecodeError。

拿到 response
↓
检查 status_code
↓
200？
├─ 是 → 解析 response.json()
└─ 否 → 根据状态码处理错误
"""
# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备提交给服务器的业务数据，数据类型是 dict
request_data = {
    # question 字段保存需要服务器处理的问题
    "question": "车辆无法充电是什么原因？"
}

# 创建 HTTP 请求头，数据类型是 dict
request_headers = {
    # Authorization 字段携带认证信息，这里继续使用假的 token
    "Authorization": "Bearer demo-token"
}

# 使用 try 包住可能发生网络异常的代码
try:
    response = requests.post(
        "https://postman-echo.com/post",
        json=request_data,
        headers=request_headers,
        timeout=10
    )
    # 判断服务器返回的状态码是否为 200
    if response.status_code == 200:
        #把 response 中的 JSON 响应解析成 Python 数据，并保存到 response_data
        response_data = response.json()
        print("请求成功")
        # 从 response_data 的 "json" 小字典中取出 "question" 字段并输出
        print(response_data["json"]["question"])

    # 判断认证凭证是否有问题
    elif response.status_code ==401:
        print("认证失败，请检查 API Key")

    # 判断当前身份是否没有访问权限
    elif response.status_code == 403:
        # 输出权限不足提示
        print("没有权限访问该资源")

    # 判断是否因为请求过于频繁而受到限制
    elif response.status_code == 429:
        # 输出请求频率过高提示
        print("请求过于频繁，请稍后重试")

    # 处理其他已经收到 HTTP 响应的失败状态
    else:
        # 输出服务器实际返回的状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获请求过程中发生的超时异常
except requests.exceptions.Timeout:
    # 输出请求超时提示
    print("请求超时，请稍后重试")

# 捕获请求过程中发生的网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")