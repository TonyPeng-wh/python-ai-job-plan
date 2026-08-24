# 导入 requests 第三方库，用于发送 HTTP 请求
import requests

# 从 json 模块导入 JSONDecodeError，用于处理 JSON 解析失败
from json import JSONDecodeError


# 定义发送故障请求的函数
def send_fault_request(question, fault_type):
    # API 请求地址
    url = "https://httpbin.org/post"

    # 把函数收到的问题和故障类型整理成请求数据
    request_data = {
        "question": question,
        "fault_type": fault_type
    }

    try:
        # 向 API 发送 POST 请求
        response = requests.post(
            url,
            json=request_data,
            timeout=5
        )

        # 检查 HTTP 状态码
        # 如果服务器返回 4xx 或 5xx，会抛出 HTTPError
        response.raise_for_status()

        # 把响应中的 JSON 数据解析成 Python 数据
        response_data = response.json()

        # 返回解析后的响应数据
        return response_data

    # 请求等待时间超过 timeout 时执行
    except requests.exceptions.Timeout:
        print("请求超时，请稍后重试")
        return {}

    # 网络连接失败时执行
    except requests.exceptions.ConnectionError:
        print("网络连接失败，请检查网络")
        return {}

    # HTTP 状态码为 4xx 或 5xx 时执行
    except requests.exceptions.HTTPError:
        print("HTTP 请求失败")
        return {}

    # response.json() 无法正确解析 JSON 时执行
    except JSONDecodeError:
        print("服务器返回的数据不是有效的 JSON")
        return {}

    # 处理其他 requests 请求异常
    except requests.exceptions.RequestException:
        print("API 请求发生异常")
        return {}


# 用户输入故障问题，并去掉前后空格
user_question = input("请输入故障问题：").strip()

# 用户输入故障类型，并去掉前后空格
fault_type = input("请输入故障类型：").strip()


# 调用函数，把用户输入的数据传进去
response_data = send_fault_request(
    user_question,
    fault_type
)


# 从服务器返回的大字典中取得 "json" 对应的小字典
# 如果没有 "json"，默认得到空字典 {}
returned_json_data = response_data.get("json", {})

# 从小字典中取得 question
returned_question = returned_json_data.get(
    "question",
    "未获取到故障问题"
)

# 从小字典中取得 fault_type
returned_fault_type = returned_json_data.get(
    "fault_type",
    "未获取到故障类型"
)

# 输出最终结果
print(f"返回故障问题：{returned_question}")
print(f"返回故障类型：{returned_fault_type}")