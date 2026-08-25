import requests
import json


def send_quality_analysis(
        feedback_id,
        product_model,
        feedback,
        urgent
):
    # 把当前一条反馈整理成 HTTP Request Body
    request_data = {
        "feedback_id": feedback_id,
        "product_model": product_model,
        "feedback": feedback,
        "urgent": urgent
    }

    # 设置 URL Query Parameters
    query_params = {
        "source": "after_sales"
    }

    try:
        # 向后端 API 发送 POST 请求
        response = requests.post(
            "https://httpbin.org/post",
            json=request_data,
            params=query_params,
            timeout=10
        )

        # 如果服务器返回 4xx / 5xx，则触发 HTTPError
        response.raise_for_status()

        # 把服务器返回的 JSON 转换成 Python 数据
        response_data = response.json()

        # 把响应数据返回到函数外
        return response_data

    except requests.exceptions.HTTPError:
        print("HTTP 请求失败")
        return None

    except requests.exceptions.JSONDecodeError:
        print("服务器响应数据不是有效 JSON")
        return None

    except requests.exceptions.Timeout:
        print("请求响应超时")
        return None

    except requests.exceptions.ConnectionError:
        print("无法连接服务器")
        return None

    except requests.exceptions.RequestException:
        print("请求发送发生未知异常")
        return None


try:
    # 打开本地反馈 JSON 文件
    with open(
        "week05/day24/w4_integration/feedback_data.json",
        "r",
        encoding="utf-8"
    ) as feedback_file:

        # JSON 文件内容 → Python list
        feedback_list = json.load(feedback_file)

except json.JSONDecodeError:
    # 本地 JSON 文件格式错误
    print("反馈数据文件不是有效的 JSON")

else:
    # 遍历全部反馈
    for current_feedback in feedback_list:

        # 判断当前这一条反馈是否还没有提交
        if current_feedback["submitted"] == False:
            print(f"正在处理反馈：{current_feedback['feedback_id']}")

            # 从当前反馈 dict 中取出业务字段
            feedback_id = current_feedback["feedback_id"]
            product_model = current_feedback["product_model"]
            feedback = current_feedback["feedback"]
            urgent = current_feedback["urgent"]

            # 把当前这一条反馈发送给 API
            response_data = send_quality_analysis(
                feedback_id,
                product_model,
                feedback,
                urgent
            )

            # 请求成功后才继续读取服务器返回数据
            if response_data is not None:

                # 取出 httpbin 返回结果中的 json 小字典
                returned_json_data = response_data.get(
                    "json",
                    {}
                )

                # 读取服务器返回的业务字段
                returned_feedback_id = returned_json_data.get(
                    "feedback_id",
                    "未知反馈编号"
                )

                returned_product_model = returned_json_data.get(
                    "product_model",
                    "未知型号"
                )

                returned_feedback = returned_json_data.get(
                    "feedback",
                    "未知反馈"
                )

                returned_urgent = returned_json_data.get(
                    "urgent",
                    False
                )

                # 输出服务器实际返回的数据
                print(f"提交成功：{returned_feedback_id}")
                print(f"产品型号：{returned_product_model}")
                print(f"反馈内容：{returned_feedback}")
                print(f"是否紧急：{returned_urgent}")
                print()

            else:
                # API 请求失败时输出当前反馈编号
                print(f"{feedback_id} 提交失败")
                print()

        else:
            # submitted 为 True 时，不再发送 API 请求
            print(
                f"跳过已提交反馈："
                f"{current_feedback['feedback_id']}"
            )
            print()