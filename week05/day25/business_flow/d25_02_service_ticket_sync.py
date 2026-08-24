import requests
import json

unprocessed_tickets_count = 0
HIGH_priority_count = 0

def send_unprocessed_ticket(
        ticket_id,
        fault_type,
        priority,
):
    request_data ={
        "ticket_id": ticket_id,
        "fault_type": fault_type,
        "priority": priority
    }
    query_params = {
        "source": "service_center"
    }

    try:
        response = requests.post(
            "https://httpbin.org/post",
            json=request_data,
            params=query_params,
            timeout=5
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data

    except requests.exceptions.HTTPError:
        print("HTTP请求失败")
        return None

    except requests.exceptions.JSONDecodeError:
        print("响应数据不是有效JSON")
        return None

    except requests.exceptions.Timeout:
        print("响应超时")
        return None

    except requests.exceptions.ConnectionError:
        print("无法连接服务器")
        return None

    except requests.exceptions.RequestException:
        print("请求发送未知异常")
        return None

try:
    with open(
        "week05/day25/business_flow/service_ticket_data.json",
        "r",
        encoding="utf-8"
    )as tickets_file:
        tickets_list = json.load(tickets_file)
except json.JSONDecodeError:
    print("反馈数据文件不是有效JSON")
else:
    for current_ticket in tickets_list:
        if current_ticket["processed"] == False:
            unprocessed_tickets_count = unprocessed_tickets_count + 1

            ticket_id = current_ticket["ticket_id"]
            fault_type = current_ticket["fault_type"]
            priority = current_ticket ["priority"]

            if priority == "HIGH":
                HIGH_priority_count = HIGH_priority_count + 1

            response_data = send_unprocessed_ticket(
                ticket_id,
                fault_type,
                priority
            )

            if response_data is not None:
                print("API请求成功")
                json_data = response_data.get(
                    "json",
                    {}
                )
                returned_ticket_id = json_data.get(
                    "ticket_id",
                    "未知工单id"
                )
                returned_fault_type = json_data.get(
                    "fault_type",
                    "未知错误类型"
                )
                returned_priority = json_data.get(
                    "priority",
                    "Low"
                )
                print(f"工单id:{returned_ticket_id}")
                print(f"错误类型：{returned_fault_type}")
                print(f"优先级：{returned_priority}")

            else:
                print("API请求失败")
    print(f"未处理工单数量：{unprocessed_tickets_count}")
    print(f"高优先级数量：{HIGH_priority_count}")