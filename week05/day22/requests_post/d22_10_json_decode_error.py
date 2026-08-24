# 处理 JSONDecodeError
"""
你现在已经会：
response_data = response.json()

request_data
→ Python dict
↓
json=request_data
↓
requests 把这个 dict 转成 JSON 格式
↓
放进 HTTP 请求体
↓
发送给服务器
↓
服务器收到并处理
↓
服务器返回一个 HTTP 响应
↓
response
↓
response.json()
↓
把响应里的 JSON 再解析成 Python 数据
↓
response_data

但这里存在一个问题：
服务器返回了响应，不代表响应正文一定是合法 JSON。
例如服务器可能返回普通文本,或者 HTML,这时候如果程序还执行：response.json(),
Requests 无法把它解析成 Python 数据，就会抛出：
requests.exceptions.JSONDecodeError
Requests 官方文档明确说明，当响应正文不是有效 JSON 时，response.json() 会产生这个异常
ConnectionError
→ 连服务器都没正常连上

Timeout
→ 网络请求等待太久

JSONDecodeError
→ 已经拿到响应，但 response.json() 解析失败

401 / 403 / 429 / 503
→ 已经拿到 response，而且服务器返回了具体 HTTP 状态码
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

# 使用 try 包住可能发生异常的代码
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
        # 尝试把服务器返回的 JSON 解析成 Python 数据
        response_data = response.json()

        # 输出请求成功提示
        print("请求成功")

        # 输出服务器返回数据中的 question 字段
        print(response_data["json"]["question"])

    # 判断认证凭证是否有问题
    elif response.status_code == 401:
        # 输出认证失败提示
        print("认证失败，请检查 API Key")

    # 判断是否没有访问权限
    elif response.status_code == 403:
        # 输出权限不足提示
        print("没有权限访问该资源")

    # 判断是否触发请求频率限制
    elif response.status_code == 429:
        # 输出请求过于频繁提示
        print("请求过于频繁，请稍后重试")

    # 处理其他 HTTP 状态码
    else:
        # 输出服务器实际返回的状态码
        print(f"请求失败，状态码：{response.status_code}")

# 在这里捕获 response.json() 解析失败产生的 JSONDecodeError
# 基本结构：
# except requests.exceptions.某个异常:
#     print("服务器返回的数据不是有效的 JSON")
except requests.exceptions.JSONDecodeError:
    print("服务器返回的数据不是有效的 JSON")

# 捕获请求超时异常
except requests.exceptions.Timeout:
    # 输出超时提示
    print("请求超时，请稍后重试")

# 捕获网络连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")
