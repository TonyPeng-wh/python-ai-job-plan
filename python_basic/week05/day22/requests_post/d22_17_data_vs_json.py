# POST 里的 data= 和 json= 有什么区别。
"""
json=request_data
→ 把 Python 数据编码成 JSON
→ 作为请求体发送

data=request_data
→ 如果传入的是 dict，Requests 通常会把它编码成表单数据
→ 同样放在请求体里
"""

# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备发送给服务器的数据，数据类型是 dict
request_data = {
    # question 字段保存用户的问题
    "question": "车辆无法充电是什么原因？",

    # fault_type 字段保存故障类型
    "fault_type": "充电故障"
}

# 使用 try 包住可能发生异常的代码
try:
    # 发送 POST 请求，并把服务器返回的 Response 对象保存到 response
    response = requests.post(
        # 指定 POST 请求发送到的 URL
        "https://postman-echo.com/post",

        # 这里不要使用 json=，改用 data=
        # 基本写法：data=某个变量
        data=request_data,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 检查 HTTP 状态，如果属于错误状态则抛出 HTTPError
    response.raise_for_status()

    # 把服务器返回的 JSON 响应解析成 Python 数据
    response_data = response.json()

    # 输出服务器看到的 JSON 请求体
    print("JSON数据：")
    print(response_data["json"])

    # 输出服务器看到的表单数据
    print("表单数据：")
    print(response_data["form"])

# 捕获 HTTP 状态错误
except requests.exceptions.HTTPError:
    # 输出 HTTP 请求失败提示
    print("HTTP请求失败")

# 捕获服务器响应 JSON 解析错误
except requests.exceptions.JSONDecodeError:
    # 输出 JSON 格式错误提示
    print("服务器返回的数据不是有效的 JSON")

# 捕获请求超时异常
except requests.exceptions.Timeout:
    # 输出请求超时提示
    print("请求超时，请稍后重试")

# 捕获网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")

# 兜底捕获其他 Requests 请求异常
except requests.exceptions.RequestException:
    # 输出未知请求异常提示
    print("请求发生未知异常")

# 输出服务器看到的请求体数据类型
print(response_data["headers"]["content-type"])