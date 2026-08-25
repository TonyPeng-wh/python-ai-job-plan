# 导入 requests 第三方库，用于发送 HTTP 请求
import requests


# 定义发送故障分类请求的函数
def send_fault_classification_request(
    ticket_id,
    vehicle_model,
    fault_description,
    mileage,
    urgent
):
    # 创建准备放入 HTTP Request Body 的业务数据
    request_data = {
        "ticket_id": ticket_id,
        "vehicle_model": vehicle_model,
        "fault_description": fault_description,
        "mileage": mileage,
        "urgent": urgent
    }

    # 创建 URL Query Parameters
    query_params = {
        "source": "after_sales"
    }

    # 创建 HTTP 请求头
    request_headers = {
        "Authorization": "Bearer demo-token"
    }

    try:
        # 发送 POST 请求
        response = requests.post(
            "https://postman-echo.com/post",
            params=query_params,
            json=request_data,
            headers=request_headers,
            timeout=10
        )

        # 检查 HTTP 4xx / 5xx 错误
        response.raise_for_status()

        # 把 Response 对象中的 JSON 响应解析成 Python 数据
        response_data = response.json()

        # 把解析后的响应数据返回给函数调用处
        return response_data

    # 捕获 HTTP 状态错误
    except requests.exceptions.HTTPError:
        print("HTTP请求失败")
        return None

    # 捕获 JSON 解析错误
    except requests.exceptions.JSONDecodeError:
        print("响应数据不是有效的 JSON")
        return None

    # 捕获请求超时
    except requests.exceptions.Timeout:
        print("请求超时")
        return None

    # 捕获服务器连接异常
    except requests.exceptions.ConnectionError:
        print("无法连接服务器")
        return None

    # 捕获其他 Requests 异常
    except requests.exceptions.RequestException:
        print("请求发生未知异常")
        return None


# 创建准备提交的业务数据
ticket_id = "TICKET-20260819-008"
vehicle_model = "EV-X9"
fault_description = "车辆行驶过程中动力突然受限，仪表提示动力系统故障"
mileage = 28650
urgent = True


# 调用请求函数，并接收函数返回的数据
response_data = send_fault_classification_request(
    ticket_id,
    vehicle_model,
    fault_description,
    mileage,
    urgent
)


# 只有请求成功并返回数据时，才继续读取业务字段
if response_data is not None:
    # 读取服务器回显的 JSON Request Body
    json_data = response_data.get(
        "json",
        {}
    )

    # 读取服务器回显的 Query Parameters
    args_data = response_data.get(
        "args",
        {}
    )

    # 从 JSON 请求体回显中读取各个业务字段
    returned_ticket_id = json_data.get(
        "ticket_id",
        "未知工单"
    )

    returned_vehicle_model = json_data.get(
        "vehicle_model",
        "未知车型"
    )

    returned_fault_description = json_data.get(
        "fault_description",
        "未获取到故障描述"
    )

    returned_mileage = json_data.get(
        "mileage",
        0
    )

    returned_urgent = json_data.get(
        "urgent",
        False
    )

    # 从 Query Parameters 回显中读取 source
    returned_source = args_data.get(
        "source",
        "unknown"
    )

    # 输出服务器返回的数据
    print(f"工单编号：{returned_ticket_id}")
    print(f"车辆型号：{returned_vehicle_model}")
    print(f"故障描述：{returned_fault_description}")
    print(f"车辆里程：{returned_mileage}")
    print(f"是否紧急：{returned_urgent}")
    print(f"请求来源：{returned_source}")