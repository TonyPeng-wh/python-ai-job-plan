import json
import requests

unsubmitted_count = 0
urgent_count = 0

def send_quality_analysis(
        feedback_id,
        product_model,
        feedback,
        urgent
):
    # 这里以后负责发送 API
    request_data = {
        "feedback_id": feedback_id,
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
        "week05/day24/w4_integration/feedback_data.json",
        "r",
        encoding="utf-8"
    )as feedback_file:
        feedback_list = json.load(feedback_file)
except json.JSONDecodeError:
    print("反馈数据文件不是有效JSON")

else:
    for current_feedback in feedback_list:
        
        if current_feedback["submitted"] == False:
            unsubmitted_count = unsubmitted_count + 1
            # 取出当前反馈编号
            feedback_id = current_feedback["feedback_id"]

            # 取出当前产品型号
            product_model = current_feedback["product_model"]

            # 取出当前反馈内容
            feedback = current_feedback["feedback"]

            # 取出当前反馈是否紧急
            urgent = current_feedback["urgent"]

            if urgent == True:
               urgent_count = urgent_count + 1
            
            response_data = send_quality_analysis(
                feedback_id,
                product_model,
                feedback,
                urgent
            )
            if response_data is not None:
                print("API 请求成功")
                # 取出服务器返回结果中的 json 小字典
                returned_json_data = response_data.get(
                    "json",
                    {}
                )
                returned_feedback_id = returned_json_data.get(
                    "feedback_id",
                    "未知反馈id"
                )
                returned_product_model = returned_json_data.get(
                    "product_model",
                    "未知产品型号"
                )
                returned_feedback = returned_json_data.get(
                    "feedback",
                    "未知反馈"
                )
                returned_urgent = returned_json_data.get(
                    "urgent",
                    False
                )
                print(f"提交成功：{returned_feedback_id}")
                print(f"产品型号：{returned_product_model}")
                print(f"反馈内容：{returned_feedback}")
                print(f"是否紧急：{returned_urgent}")
                
            else:
                print("API 请求失败")

    print(f"未提交数量：{unsubmitted_count}")
    print(f"紧急数量：{urgent_count}")

