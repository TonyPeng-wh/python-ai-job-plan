# 导入 requests 第三方库
import requests


# 定义发送故障信息的函数
def send_fault_report(question, fault_type, priority):
    # TODO 1：
    # 创建 request_data 字典
    # 包含三个字段：
    # question
    # fault_type
    # priority
    
    # 创建 request_data 字典
    request_data = {
        "question": question,
        "fault_type": fault_type,
        "priority": priority
    }

    # 创建请求头
    request_headers = {
        "Authorization": "Bearer demo-token"
    }

    # 使用 try 处理请求过程中可能发生的异常
    try:
        
        # TODO 2：
        # 使用 requests.post() 发送 POST 请求
        # URL：
        # https://postman-echo.com/post
        #
        # 要求：
        # json=request_data
        # headers=request_headers
        # timeout=10
        #
        # 用 response 接收返回结果
        
        response = requests.post(
            "https://postman-echo.com/post",
            json=request_data,
            headers=request_headers,
            timeout=10
        )
        
        # TODO 3：
        # 检查 HTTP 错误状态
        # 提示：response.________()
        
        response.raise_for_status()

        
        # TODO 4：
        # 把响应 JSON 解析成 Python 数据
        # 用 response_data 保存
        
        response_data = response.json()


        # TODO 5：
        # 返回 response_data
        return response_data


    # 捕获 HTTP 错误
    except requests.exceptions.HTTPError:
        print("HTTP请求失败")
        return None

    # 捕获 JSON 解析错误
    except requests.exceptions.JSONDecodeError:
        print("服务器返回的数据不是有效的 JSON")
        return None

    # 捕获请求超时
    except requests.exceptions.Timeout:
        print("请求超时，请稍后重试")
        return None

    # 捕获连接异常
    except requests.exceptions.ConnectionError:
        print("无法连接服务器，请检查网络或服务器地址")
        return None

    # 捕获其他 Requests 异常
    except requests.exceptions.RequestException:
        print("请求发生未知异常")
        return None


# 创建准备提交的数据
user_question = "车辆充电到 60% 后自动停止"
fault_type = "充电故障"
priority = "HIGH"

# TODO 6：
# 调用 send_fault_report()
# 传入上面的三个变量
# 用 response_data 接收返回值
response_data = send_fault_report(
    user_question,
    fault_type,
    priority
)

# 判断请求函数是否返回了正常数据
if response_data is not None:
    # TODO 7：
    # 从 response_data 安全读取 "json"
    # 如果不存在，默认得到空字典
    # 用 json_data 保存
    json_data = response_data.get("json",{})

    # TODO 8：
    # 从 json_data 中安全读取 question
    # 默认值："未获取到问题"
    question = json_data.get("question","未获取到问题")

    # TODO 9：
    # 从 json_data 中安全读取 fault_type
    # 默认值："未知故障"
    returned_fault_type = json_data.get("fault_type","未知故障")

    # TODO 10：
    # 从 json_data 中安全读取 priority
    # 默认值："UNKNOWN"
    returned_priority = json_data.get("priority","UNKNOWN")

    # 输出最终结果
    print(f"问题：{question}")
    print(f"故障类型：{returned_fault_type}")
    print(f"优先级：{returned_priority}")