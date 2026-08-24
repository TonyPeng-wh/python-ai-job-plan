# 导入 requests 第三方库，用来发送 HTTP 请求
import requests

# 定义发送故障问题 API 请求的函数
def send_fault_request(question):
    # 创建准备提交给服务器的业务数据，数据类型是 dict
    request_data = {
        # question 字段保存函数接收到的问题
        "question": question
    }

    # 创建 HTTP 请求头，数据类型是 dict
    request_headers = {
        # Authorization 字段保存认证信息，这里使用练习用的假 token
        "Authorization": "Bearer demo-token"
    }

    # 使用 try 包住可能发生异常的 API 调用代码
    try:
        # 发送 POST 请求，并用 response 接收服务器返回的 Response 对象
        response = requests.post(
            # 指定请求发送到的 URL
            "https://postman-echo.com/post",

            # 把 request_data 字典作为 JSON 请求体发送
            json=request_data,

            # 把 request_headers 字典作为 HTTP 请求头发送
            headers=request_headers,

            # 设置请求超时时间
            timeout=10
        )

        # 检查 HTTP 状态码，4xx / 5xx 会抛出 HTTPError
        response.raise_for_status()

        #  1：
        # 把 response 中的 JSON 响应解析成 Python 数据
        # 并保存到 response_data
        response_data = response.json()

        #  2：
        # 把 response_data 返回给函数调用处
        return response_data

    # 捕获 HTTP 4xx / 5xx 错误
    except requests.exceptions.HTTPError:
        # 输出 HTTP 请求失败提示
        print("HTTP请求失败")

        # 函数没有得到正常业务数据
        return None

    # 捕获服务器响应无法解析为 JSON 的异常
    except requests.exceptions.JSONDecodeError:
        # 输出 JSON 解析失败提示
        print("服务器返回的数据不是有效的 JSON")

        # 函数没有得到正常业务数据
        return None

    # 捕获请求超时异常
    except requests.exceptions.Timeout:
        # 输出请求超时提示
        print("请求超时，请稍后重试")

        # 函数没有得到正常业务数据
        return None

    # 捕获网络连接异常
    except requests.exceptions.ConnectionError:
        # 输出连接失败提示
        print("无法连接服务器，请检查网络或服务器地址")

        # 函数没有得到正常业务数据
        return None

    # 兜底捕获其他 Requests 异常
    except requests.exceptions.RequestException:
        # 输出其他请求异常提示
        print("请求发生未知异常")

        # 函数没有得到正常业务数据
        return None


# 创建准备发送给函数的用户问题
user_question = "车辆无法充电是什么原因？"

#  3：
# 调用 send_fault_request()
# 把 user_question 传入
# 用 response_data 接收函数返回值
response_data = send_fault_request(user_question)

# 判断函数是否成功返回了数据
if response_data is not None:
    # 从大字典 response_data 中读取 json 字段
    # 如果 json 不存在，就得到一个空字典
    json_data = response_data.get("json", {})

    #  4：
    # 从 json_data 中读取 question
    # 如果 question 不存在，默认使用“未获取到问题”
    question = json_data.get(
        "question",
        "未获取到问题"
    )

    # 输出最终取得的问题内容
    print(question)