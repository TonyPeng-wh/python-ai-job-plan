# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备提交给服务器的数据，数据类型是 dict
request_data = {
    # question 字段保存用户的问题
    "question": "车辆无法充电是什么原因？",

    # fault_type 字段保存故障类型
    "fault_type": "充电故障"
}

# 发送 POST 请求，并把服务器返回的响应对象保存到 response
response = requests.post(
    # 指定 POST 请求要发送到的 URL
    "https://postman-echo.com/post",

    # 把 request_data 字典作为 JSON 请求体发送给服务器
    json=request_data,

    # 设置请求超时时间为 10 秒
    timeout=10
)

# 输出服务器返回的 HTTP 状态码
print(response.status_code)

# 把服务器返回的 JSON 响应解析成 Python 数据，并保存到 response_data
response_data = response.json()

# 输出完整的服务器响应数据，观察服务器返回了什么
print(response_data)