# 响应字段不存在时的 KeyError。
"""
这个知识点非常贴近真实 API：
即使 HTTP 请求成功、JSON 也解析成功，返回的数据结构也可能和我们预期的不一样。
注意：KeyError 不是 Requests 异常，是 Python 字典本身的异常。
而应该直接：except KeyError:
之前requests.exceptions.XXXX，属于 Requests 请求相关异常。
"""

# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 创建准备提交给服务器的业务数据，数据类型是 dict
request_data = {
    # question 字段保存用户问题
    "question": "车辆无法充电是什么原因？"
}

# 创建 HTTP 请求头，数据类型是 dict
request_headers = {
    # Authorization 字段保存认证信息，这里继续使用假的 token
    "Authorization": "Bearer demo-token"
}

# 使用 try 包住后面可能发生异常的代码
try:
    # 发送 POST 请求，并把服务器返回的 Response 对象保存到 response
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

    # 检查 HTTP 状态，如果是 HTTP 错误状态则抛出 HTTPError
    response.raise_for_status()

    # 把服务器返回的 JSON 响应解析成 Python 数据
    response_data = response.json()

    # 输出请求成功提示
    print("请求成功")

    # 从服务器返回的大字典中逐层取出 question 字段
    print(response_data["json"]["question"])

# 捕获字典中不存在指定 key 时产生的异常
# 基本写法：
# except 异常名称:
#     print("响应数据中缺少需要的字段")
except KeyError:
    print("响应数据中缺少需要的字段")

# 捕获 HTTP 错误状态产生的异常
except requests.exceptions.HTTPError:
    # 输出 HTTP 请求失败提示
    print("HTTP请求失败")

# 捕获服务器响应无法解析成 JSON 的异常
except requests.exceptions.JSONDecodeError:
    # 输出 JSON 解析失败提示
    print("服务器返回的数据不是有效的 JSON")

# 捕获请求超时异常
except requests.exceptions.Timeout:
    # 输出请求超时提示
    print("请求超时，请稍后重试")

# 捕获网络连接异常
except requests.exceptions.ConnectionError:
    # 输出网络连接失败提示
    print("无法连接服务器，请检查网络或服务器地址")

# 兜底捕获其他 Requests 请求异常
except requests.exceptions.RequestException:
    # 输出其他请求异常提示
    print("请求发生未知异常")