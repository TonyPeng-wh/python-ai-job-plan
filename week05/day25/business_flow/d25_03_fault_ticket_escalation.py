import json
import requests

def send_fault_ticket(
    ticket_id,
    fault_type,
    severity
):
    request_data = {
        "ticket_id": ticket_id,
        "fault_type": fault_type,
        "severity": severity
    }

    query_params = {
        "source": "fault_center"
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
        "week05/day25/business_flow/fault_ticket_data.json",
        "r",
        encoding="utf-8"
    )as ticket_file:
        ticket_list = json.load(ticket_file)

except json.JSONDecodeError:
    print("故障工单文件不是有效JSON")

else:
    for current_ticket in ticket_list:
        if current_ticket["reported"] == False and current_ticket["severity"] == "HIGH":
            ticket_id = current_ticket["ticket_id"]
            fault_type = current_ticket["fault_type"]
            severity = current_ticket["severity"]

            response_data = send_fault_ticket(
                ticket_id,
                fault_type,
                severity
            )

            if response_data is not None:
                print("API请求成功")
                json_data = response_data.get(
                    "json",
                    {}
                )
                returned_ticket_id = json_data.get(
                    "ticket_id",
                    "未知id"
                )
                returned_fault_type = json_data.get(
                    "fault_type",
                    "未知错误类型"
                )
                returned_severity = json_data.get(
                    "severity",
                    "未知严重程度"
                )
                print(f"工单id：{returned_ticket_id}")
                print(f"错误类型：{returned_fault_type}")
                print(f"严重程度：{returned_severity}")

            else:
                print("API请求失败")