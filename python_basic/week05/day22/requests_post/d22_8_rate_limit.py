# HTTP 429：请求过于频繁 / Rate Limit。
"""
这对以后调用 AI API 很重要，因为很多 API 都会限制一定时间内允许发送的请求数量。
HTTP 429 Too Many Requests 就表示客户端在一定时间内发送了过多请求；
Postman 的官方文档也用 429 表示触发了 API rate limit。

200 → 请求成功

401 → 认证凭证有问题

403 → 有身份，但没有相应权限

429 → 请求太频繁，触发服务器限制

503 → 服务器暂时无法正常提供服务

其中 429 和 401、403、503 有一个共同点：它们都有 HTTP 响应，也就是说 response 已经拿到了。
所以还是使用：if / elif / else判断，而不是进入 ConnectionError。
"""
# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备发送给服务器的业务数据，数据类型是 dict
request_data = {
    # question 字段保存用户的问题
    "question": "车辆无法充电是什么原因？"
}

# 创建 HTTP 请求头，数据类型是 dict
request_headers = {
    # Authorization 字段携带认证信息，这里继续使用假的 token
    "Authorization": "Bearer demo-token"
}

# 使用 try 包住可能发生网络异常的代码
try:
    # 发送 POST 请求，并把服务器返回的响应对象保存到 response
    response = requests.post(
        # 指定 POST 请求发送到的 URL
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
        # 输出请求成功提示
        print("请求成功")

    # 如果不是 200，则判断状态码是否为 401
    elif response.status_code == 401:
        # 输出认证失败提示
        print("认证失败，请检查 API Key")

    # 如果前面都不成立，则判断状态码是否为 403
    elif response.status_code == 403:
        # 输出权限不足提示
        print("没有权限访问该资源")

    # 在这里增加对 429 状态码的判断
    # 要求：状态码为 429 时，输出“请求过于频繁，请稍后重试”
    # 基本写法：
    # elif 条件:
    #     print(...)
    elif response.status_code == 429:
        print("请求过于频繁，请稍后重试")
        
    # 如果前面的状态码条件都不成立，则处理其他状态码
    else:
        # 输出服务器实际返回的状态码
        print(f"请求失败，状态码：{response.status_code}")

# 捕获请求过程中发生的超时异常
except requests.exceptions.Timeout:
    # 输出请求超时提示
    print("请求超时，请稍后重试")

# 捕获请求过程中发生的连接异常
except requests.exceptions.ConnectionError:
    # 输出连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")