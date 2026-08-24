# raise_for_status() 和 HTTPError
"""
你目前处理 HTTP 状态码的方法是：
if response.status_code == 200:
    ...
elif response.status_code == 401:
    ...
elif response.status_code == 403:
    ...
elif response.status_code == 429:
    ...
这叫：我们自己读取 status_code，然后用 if / elif 判断。
Requests 还提供了另一种方式：response.raise_for_status()
它会检查 HTTP 响应状态。
如果响应属于 HTTP 错误状态，它会抛出 HTTPError；如果没有 HTTP 错误，则继续往下执行
先看最基本写法:
response = requests.post(...)

response.raise_for_status()“检查一下这次 HTTP 响应有没有错误，如果有，就主动抛出异常。”
Response.raise_for_status() 遇到不成功的 HTTP 状态时会抛出 HTTPError。
"""

# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备发送给服务器的业务数据
request_data = {
    # question 字段保存用户问题
    "question": "车辆无法充电是什么原因？"
}

# 创建 HTTP 请求头
request_headers = {
    # 使用假的认证凭证进行练习
    "Authorization": "Bearer demo-token"
}

# 使用 try 包住可能发生异常的代码
try:
    # 发送 POST 请求，并把服务器返回的 Response 对象保存到 response
    response = requests.post(
        # 指定 POST 请求的 URL
        "https://postman-echo.com/post",

        # 把 request_data 作为 JSON 请求体发送
        json=request_data,

        # 把 request_headers 作为 HTTP 请求头发送
        headers=request_headers,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 让 requests 检查 HTTP 状态码
    # 基本写法：response.某个方法()
    response.raise_for_status()

    # 把服务器返回的 JSON 响应解析成 Python 数据
    response_data = response.json()

    # 输出请求成功提示
    print("请求成功")

    # 输出服务器返回数据中的 question 字段
    print(response_data["json"]["question"])

# 捕获 HTTP 状态错误产生的 HTTPError
# 基本写法：
# except requests.exceptions.某个异常:
#     print("HTTP请求失败")
except requests.exceptions.HTTPError:
    print("HTTP请求失败")

# 捕获服务器响应无法解析为 JSON 的异常
except requests.exceptions.JSONDecodeError:
    # 输出 JSON 解析失败提示
    print("服务器返回的数据不是有效的 JSON")

# 捕获请求超时异常
except requests.exceptions.Timeout:
    # 输出超时提示
    print("请求超时，请稍后重试")

# 捕获网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")

# 兜底捕获其他 Requests 请求异常
except requests.exceptions.RequestException:
    # 输出其他请求异常提示
    print("请求发生未知异常")