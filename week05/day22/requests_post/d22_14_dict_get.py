# 用字典 .get() 安全读取 API 返回字段
"""
它的基本写法：字典.get("key")
fault_data = {
    "fault_type": "充电故障"
}

fault_type = fault_data.get("fault_type")
得到：充电故障
但是如果写：priority = fault_data.get("priority")
即使 "priority" 不存在，程序不会产生 KeyError，而是得到：None
"""
"""
为什么 API 场景特别适合 .get()
例如你以为模型服务器一定返回：
{
    "answer": "建议检查充电枪"
}
但某一次实际返回：
{
    "message": "模型暂时不可用"
}
如果直接：response_data["answer"]就会：KeyError
response_data.get("answer")会得到：None
然后我们就可以自己判断：
if answer is None:
    print("响应中没有 answer 字段")
这里的 is None 先把它理解成：判断这个变量的值是不是 None。
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
        # 指定 POST 请求发送到的 URL
        "https://postman-echo.com/post",

        # 把 request_data 字典作为 JSON 请求体发送
        json=request_data,

        # 把 request_headers 字典作为 HTTP 请求头发送
        headers=request_headers,

        # 设置请求超时时间为 10 秒
        timeout=10
    )

    # 检查 HTTP 状态码，如果是 HTTP 错误状态则抛出 HTTPError
    response.raise_for_status()

    # 把服务器返回的 JSON 响应解析成 Python 数据
    response_data = response.json()

    # 从大字典中取出 json 字段对应的小字典
    json_data = response_data["json"]

    # 使用 .get() 从 json_data 中读取 question 字段
    # 基本写法：变量 = 字典.get("key")
    question = json_data.get("question")


    # 判断 question 是否没有取到数据
    if question is None:
        # 输出字段不存在提示
        print("响应数据中没有 question 字段")

    # 如果 question 成功取到数据，则执行这里
    else:
        # 输出 question 字段的内容
        print(question)

# 捕获 HTTP 错误状态产生的异常
except requests.exceptions.HTTPError:
    # 输出 HTTP 请求失败提示
    print("HTTP请求失败")

# 捕获服务器响应无法解析为 JSON 的异常
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