# 服务器已经收到请求，但认证信息有问题时，会发生什么？
"""
401
→ 缺少有效的认证凭证，或者凭证无效

403
→ 服务器理解了请求，但拒绝你访问
→ 常见原因是权限不足
"""
# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备提交给服务器的数据，数据类型是 dict
request_data = {
    # question 字段保存用户的问题
    "question": "车辆无法充电是什么原因？"
}

# 创建请求头，数据类型是 dict
request_headers = {
    # 使用假的 token 模拟 API 认证信息
    "Authorization": "Bearer demo-token"
}

# 使用 try 包住可能发生网络异常的代码
try:
    # 发送 POST 请求，并把服务器返回的响应对象保存到 response
    response = requests.post(
        # 指定 POST 请求发送到的 URL
        "https://postman-echo.com/post",

        # 把 request_data 作为 JSON 请求体发送
        json=request_data,

        # 把 request_headers 作为 HTTP 请求头发送
        headers=request_headers,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 判断状态码是否为 200
    if response.status_code == 200:
        # 输出请求成功提示
        print("请求成功")

    # 判断状态码是否为 401
    elif response.status_code == 401:
        # 输出认证失败提示
        print("认证失败，请检查 API Key")

    # 判断状态码是否为 403
    elif response.status_code == 403:
        # 输出权限不足提示
        print("没有权限访问该资源")

    # 处理其他已经收到响应的状态码
    else:
        # 输出实际返回的状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获请求超时异常
except requests.exceptions.Timeout:
    # 输出超时提示
    print("请求超时，请稍后重试")

# 捕获网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")