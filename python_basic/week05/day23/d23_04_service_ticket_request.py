# 导入 requests 第三方库
import requests


# 定义提交售后工单的函数
def send_service_ticket(
    ticket_code,
    vehicle_model,
    fault_description,
    priority
):
    # TODO 1：
    # 创建 request_data 字典
    # 注意：这里必须使用上面的函数参数
    # 不要把具体业务数据重新写死
    request_data = {
        "ticket_code": ticket_code,
        "vehicle_model": vehicle_model,
        "fault_description": fault_description,
        "priority": priority
    }

    # TODO 2：
    # 创建 request_headers 字典
    # Authorization:
    # Bearer demo-token
    request_headers = {
        "Authorization": "Bearer demo-token"
    }

    try:
        # TODO 3：
        # 使用 requests.post() 发送请求
        #
        # URL：
        # https://postman-echo.com/post
        #
        # 需要传入：
        # json=request_data
        # headers=request_headers
        # timeout=10
        #
        # 用 response 接收 Response 对象
        url = "https://postman-echo.com/post"
        response = requests.post(
            url,
            json=request_data,
            headers=request_headers,
            timeout=10
        )
        # TODO 4：
        # 检查 HTTP 错误状态
        response.raise_for_status()

        # TODO 5：
        # 把服务器 JSON 响应解析成 Python 数据
        # 保存到 response_data
        response_data = response.json()

        # TODO 6：
        # 返回 response_data
        return response_data

    except requests.exceptions.HTTPError:
        print("HTTP请求失败")
        return None

    except requests.exceptions.JSONDecodeError:
        print("响应数据不是有效的 JSON")
        return None

    except requests.exceptions.Timeout:
        print("请求超时")
        return None

    except requests.exceptions.ConnectionError:
        print("无法连接服务器")
        return None

    except requests.exceptions.RequestException:
        print("请求发生未知异常")
        return None


# 创建待提交的工单数据
ticket_code = "WO-20260819-001"
vehicle_model = "EV-S7"
fault_description = "车辆快充时频繁中断"
priority = "HIGH"


# TODO 7：
# 调用 send_service_ticket()
# 把上面四个变量传进去
# 使用 response_data 接收返回值
response_data = send_service_ticket(
    ticket_code,
    vehicle_model,
    fault_description,
    priority
)

# TODO 8：
# 判断 response_data 是否不是 None
if response_data is not None:

    # TODO 9：
    # 从 response_data 中安全读取 "json"
    # 缺失时使用空字典 {}
    # 保存到 json_data
    json_data = response_data.get("json",{})

    # TODO 10：
    # 分别从 json_data 中安全读取：
    # ticket_code
    # vehicle_model
    # fault_description
    # priority
    #
    # 默认值分别使用：
    # "未知工单"
    # "未知车型"
    # "未获取到故障描述"
    # "UNKNOWN"
    returned_ticket_code = json_data.get("ticket_code", "未知工单")
    returned_vehicle_model = json_data.get("vehicle_model", "未知车型")
    returned_fault_description = json_data.get("fault_description", "未获取到故障描述")
    returned_priority = json_data.get("priority", "UNKNOWN")

    # 已学内容，输出部分可以直接完成
    print(f"工单编号：{returned_ticket_code}")
    print(f"车辆型号：{returned_vehicle_model}")
    print(f"故障描述：{returned_fault_description}")
    print(f"优先级：{returned_priority}")