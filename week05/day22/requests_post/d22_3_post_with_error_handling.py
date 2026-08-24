# POST 请求不能只负责“发送”，还要判断有没有成功，并处理超时。
import requests

request_data ={
    "question": "车辆无法充电是什么原因？",
    "fault_type": "充电故障"
}

# 使用 try 包住可能发生网络异常的代码
try:
    # 发送 POST 请求，并把服务器返回的响应对象保存到 response
    response = requests.post(
        "https://postman-echo.com/post",
        # 把 request_data 作为 JSON 请求体发送给服务器
        json=request_data,
        timeout=10
    )

    # 判断服务器返回的 HTTP 状态码是否为 200
    if response.status_code == 200:
        # 把服务器返回的 JSON 响应解析成 Python 数据
        response_data = response.json()
        print("请求成功")
        # 输出服务器解析到的 JSON 请求体
        print(response_data["json"])
    else:
        print(f"请求失败，状态码：{response.status_code}")
        
# 捕获 requests 请求过程中出现的超时异常
except requests.exceptions.Timeout:
    # 输出超时提示
    print("请求超时，请稍后重试")