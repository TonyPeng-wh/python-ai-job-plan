# GET 主要是向服务器获取数据；POST 常用于把数据提交给服务器。
# response = requests.post(...)
import requests

request_data = {
    "question": "车辆无法充电是什么原因？",
    "fault_type": "充电故障"
}

response = requests.post(
    "https://postman-echo.com/post",
    json=request_data,# 把 request_data 这个 Python 字典，作为 JSON 请求体发送给服务器。
    timeout=10
)

print(response.status_code)