# HTTP 请求头 headers。
"""
这个知识点很重要，因为以后调用很多 AI API 时，除了 URL 和请求体，
还需要通过请求头告诉服务器一些额外信息，比如“数据格式是什么”“身份凭证是什么”。
Requests 官方支持直接把一个 dict 传给 headers=。
"""
# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备提交给服务器的数据，数据类型是 dict
request_data = {
    # question 字段保存用户的问题
    "question": "车辆无法充电是什么原因？",

    # fault_type 字段保存故障类型
    "fault_type": "充电故障"
}

# ==================================================
# 创建请求头数据，数据类型是 dict
request_headers = {
    # 添加一个自定义请求头，用来标识当前客户端名称
    "X-Client-Name": "fault-diagnosis-demo"
}
# ==================================================

# 使用 try 包住可能发生网络异常的代码
try:
    # 发送 POST 请求，并把服务器返回的响应对象保存到 response
    response = requests.post(
        # 指定 POST 请求发送到的 URL
        "https://postman-echo.com/post",

        # 把 request_data 字典作为 JSON 请求体发送给服务器
        json=request_data,

        # 把 request_headers 字典作为 HTTP 请求头发送给服务器
        headers=request_headers,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 判断服务器返回的 HTTP 状态码是否为 200
    if response.status_code == 200:
        # 把服务器返回的 JSON 数据解析成 Python 数据
        response_data = response.json()

        # 输出请求成功提示
        print("请求成功")

        # 输出服务器实际收到的请求头
        print(response_data["headers"])

    # 如果服务器已经返回响应，但是状态码不是 200，则执行这里
    else:
        # 输出服务器实际返回的 HTTP 状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获请求过程中发生的超时异常
except requests.exceptions.Timeout:
    # 输出请求超时提示
    print("请求超时，请稍后重试")

# 捕获请求过程中发生的连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")