# Authorization 请求头——让服务器知道“你有没有权限
# 这个知识点很重要，因为以后调用很多 AI API 时，服务器不会让任何人随便调用，而是要求你提供身份凭证。
# Authorization 是一种常见的 HTTP 请求头，用来携带认证信息。

# 今天我们只用一个假的 token 做练习，不使用真实 API Key。

import requests

request_data = {
    "question":"车辆无法充电是什么原因？"
}

request_headers = {
    "Authorization":"Bearer demo-token"
}

try:
    response = requests.post(
        "https://postman-echo.com/post",# 指定 POST 请求发送到的 URL
        json=request_data,              # 把 request_data 字典作为 JSON 请求体发送
        headers=request_headers,        # 把 request_headers 字典作为 HTTP 请求头发送
        timeout=10
    )

    if response.status_code == 200:
        response_data = response.json()
        print("请求成功")
        print(response_data["headers"]["authorization"])
    else:
        print(f"请求失败，状态码：{response.status_code}")
except requests.exceptions.Timeout:
    print("请求超时，请稍后重试")

except requests.exceptions.ConnectionError:
    print("无法连接服务器，请检查网络或服务器地址")