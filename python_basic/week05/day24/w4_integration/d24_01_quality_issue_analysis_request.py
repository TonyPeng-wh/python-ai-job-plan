import requests

def send_quality_analysis(
        product_model,
        feedback,
        urgent
        ):

    request_data = {
        "product_model": product_model,
        "feedback": feedback,
        "urgent": urgent
    }

    query_params = {
        "source": "after_sales"
    }

    try:
        response = requests.post(
            "https://httpbin.org/post",
            params=query_params,
            json=request_data,
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

product_model = input("请输入产品型号：").strip()
feedback = input("请输入用户反馈：").strip()
urgent = False

response_data = send_quality_analysis(
    product_model,
    feedback,
    urgent
)

if response_data is not None:
    json_data = response_data.get(
        "json",
        {}
    )

    args_data = response_data.get(
        "args",
        {}
    )

    returned_product_model = json_data.get(
        "product_model",
        "未知型号"
    )

    returned_feedback = json_data.get(
        "feedback",
        "未知反馈"
    )

    returned_urgent = json_data.get(
        "urgent",
        False
    )

    returned_source = args_data.get(
        "source",
        "unknown"
    )

    print(f"产品型号:{returned_product_model}")
    print(f"用户反馈:{returned_feedback}")
    print(f"是否紧急:{returned_urgent}")
    print(f"请求来源:{returned_source}")



