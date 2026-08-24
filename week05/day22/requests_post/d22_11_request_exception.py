# 用 RequestException 兜底处理其他 Requests 异常
# 但 Requests 还可能出现其他请求相关异常。官方文档说明，Requests 
# 明确抛出的异常都继承自 requests.exceptions.RequestException，所以它可以作为一个最后的"兜底"异常。

"""
为什么还需要它？
可以先理解成：
已知异常
→ 单独处理
没提前想到的其他 Requests 异常
→ RequestException 最后兜底
关键还有一点：具体异常写前面，范围更大的 RequestException 写最后。
因为 Timeout、ConnectionError 等都属于 RequestException 的子类。
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

# 使用 try 包住可能发生异常的请求代码
try:
    # 发送 POST 请求，并把服务器返回的 Response 对象保存到 response
    response = requests.post(
        # 指定请求发送到的 URL
        "https://postman-echo.com/post",

        # 把 request_data 字典作为 JSON 请求体发送
        json=request_data,

        # 把 request_headers 字典作为 HTTP 请求头发送
        headers=request_headers,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 判断服务器返回的状态码是否为 200
    if response.status_code == 200:
        # 把服务器返回的 JSON 响应解析成 Python 数据
        response_data = response.json()

        # 输出请求成功提示
        print("请求成功")

        # 输出服务器返回数据里的 question 字段
        print(response_data["json"]["question"])

    # 判断认证凭证是否无效
    elif response.status_code == 401:
        # 输出认证失败提示
        print("认证失败，请检查 API Key")

    # 判断当前身份是否没有权限
    elif response.status_code == 403:
        # 输出权限不足提示
        print("没有权限访问该资源")

    # 判断是否触发请求频率限制
    elif response.status_code == 429:
        # 输出请求频率过高提示
        print("请求过于频繁，请稍后重试")

    # 处理其他已经收到 HTTP 响应的状态码
    else:
        # 输出服务器实际返回的状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获服务器响应无法解析为 JSON 的异常
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

# 在这里增加 RequestException，兜底处理其他 Requests 请求异常
# 基本写法：except requests.exceptions.异常名称:
except requests.exceptions.RequestException:
# 输出“请求发生未知异常”
    print("请求发生未知异常")