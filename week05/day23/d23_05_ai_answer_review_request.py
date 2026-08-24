import requests

def send_answer_review(
        review_id,
        question, 
        answer_quality_score,
        passed
):
    request_data = {
        "review_id": review_id,
        "question": question,
        "answer_quality_score": answer_quality_score,
        "passed": passed
    }

    request_headers = {
        "Authorization": "Bearer demo-token"
    }
    try:
        response = requests.post(
            "https://postman-echo.com/post",
            json=request_data,
            headers=request_headers,
            timeout=10
        )
        response.raise_for_status()
        response_data = response.json()
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

review_id = "REV-20260819-001"
user_question = "车辆快充速度突然下降是什么原因？"
answer_quality_score = 0.82
passed = True

response_data = send_answer_review(
    review_id,
    user_question,
    answer_quality_score,
    passed,
)

if response_data is not None:
    json_data = response_data.get(
        "json",
        {}
    )
    returned_review_id = json_data.get(
        "review_id",
        "未知评测"
    )
    returned_user_question = json_data.get(
        "question", 
        "为获取到问题"
    )
    returned_answer_quality_score = json_data.get(
        "answer_quality_score",
        0
    )
    returned_passed = json_data.get(
        "passed",
        False
    )

    print(f"评测编号：{returned_review_id}")
    print(f"用户问题：{returned_user_question}")
    print(f"回答质量分数：{returned_answer_quality_score}")
    print(f"是否通过：{returned_passed}")