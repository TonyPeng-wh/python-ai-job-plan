# 把一次 API 调用封装成函数
"""
“发送一次 API 请求”本身就是一个完整、可重复执行的任务。
"""

# 导入 requests 第三方库，用来发送 HTTP 请求
import requests


# 定义发送故障问题 API 请求的函数，question 接收外部传入的问题
def send_fault_request(question):
    # 创建准备提交给服务器的业务数据，数据类型是 dict
    request_data = {
        # question 字段使用函数参数 question 的值
        "question": question
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

        # 1：把解析后的 response_data 返回给调用这个函数的位置
        # 基本写法：return 某个变量
        return response_data


    # 捕获 HTTP 错误状态产生的异常
    except requests.exceptions.HTTPError:
        # 输出 HTTP 请求失败提示
        print("HTTP请求失败")

        # 请求失败时返回 None
        return None

    # 捕获服务器响应无法解析成 JSON 的异常
    except requests.exceptions.JSONDecodeError:
        # 输出 JSON 解析失败提示
        print("服务器返回的数据不是有效的 JSON")

        # 解析失败时返回 None
        return None

    # 捕获请求超时异常
    except requests.exceptions.Timeout:
        # 输出请求超时提示
        print("请求超时，请稍后重试")

        # 请求失败时返回 None
        return None

    # 捕获网络连接异常
    except requests.exceptions.ConnectionError:
        # 输出连接失败提示
        print("无法连接服务器，请检查网络或服务器地址")

        # 请求失败时返回 None
        return None

    # 兜底捕获其他 Requests 请求异常
    except requests.exceptions.RequestException:
        # 输出其他请求异常提示
        print("请求发生未知异常")

        # 请求失败时返回 None
        return None


# 创建用户问题变量，数据类型是 str
user_question = "车辆无法充电是什么原因？"

# 2：调用 send_fault_request()，把 user_question 传进去
# 并把函数返回的数据保存到 response_data
# 基本写法：变量 = 函数名(参数)
response_data = send_fault_request(user_question)

# 判断函数是否成功返回了响应数据
if response_data is not None:
    # 从 response_data 大字典中取出 json 对应的小字典
    json_data = response_data.get("json", {})

    # 从 json_data 中安全读取 question，没有时使用默认提示
    question = json_data.get("question", "未获取到问题")

    # 输出服务器返回的问题内容
    print(question)


"""
return None:
“这次 API 调用没有得到可供主程序继续使用的正常响应数据，因此函数返回 None 作为‘失败标记’。”
"""