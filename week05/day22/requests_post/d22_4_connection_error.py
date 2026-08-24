# 处理连接失败 ConnectionError
"""
except requests.exceptions.Timeout:
它负责的是：
请求发出后，等待连接或服务器返回数据的时间超过限制。
但网络请求还可能出现另一种情况：
根本连接不上服务器。
Requests 官方把这种网络连接问题定义为 ConnectionError；而 Timeout 专门表示请求超时。
"""
import requests
# 创建准备提交给服务器的数据，数据类型是 dict
request_data = {
    "question": "车辆无法充电是什么原因？",
    "fault_type": "充电故障"
}

# 使用 try 包住可能发生网络异常的代码
try:
    # 发送 POST 请求，并把服务器返回的响应对象保存到 response
    response = requests.post(
        # 指定 POST 请求发送到的 URL
        "https://postman-echo.com/post",

        # 把 request_data 字典作为 JSON 请求体发送给服务器
        json=request_data,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 判断服务器返回的 HTTP 状态码是否为 200
    if response.status_code == 200:
        # 把服务器返回的 JSON 响应解析成 Python 数据
        response_data = response.json()

        # 输出请求成功提示
        print("请求成功")

        # 输出服务器收到的 JSON 请求体
        print(response_data["json"])

    # 如果服务器已经返回响应，但是状态码不是 200，则进入这里
    else:
        # 输出实际返回的 HTTP 状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获请求过程中发生的超时异常
except requests.exceptions.Timeout:
    # 输出超时提示
    print("请求超时，请稍后重试")

# 捕获请求过程中发生的网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")