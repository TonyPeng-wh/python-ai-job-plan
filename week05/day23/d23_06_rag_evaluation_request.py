import requests

def send_rag_evaluation(
    evaluation_id,
    query,
    retrieval_score,
    answer_score,
    passed
):
    request_data = {
        "evaluation_id": evaluation_id,
        "query": query,
        "retrieval_score": retrieval_score,
        "answer_score": answer_score,
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
        print("HTTP访问失败")
        return None
    except requests.exceptions.JSONDecodeError:
        print("响应数据不是有效JSON")
        return None
    except requests.exceptions.Timeout:
        print("访问超时")
        return None
    except requests.exceptions.ConnectionError:
        print("无法连接服务器")
        return None
    except requests.exceptions.RequestException:
        print("请求发生未知异常")
        return None

evaluation_id = "RAG-EVAL-001"
query = "动力电池温度过高应该如何处理？"
retrieval_score = 0.91
answer_score = 0.86
passed = True

response_data = send_rag_evaluation(
    evaluation_id,
    query,
    retrieval_score,
    answer_score,
    passed
)

if response_data is not None:
    json_data = response_data.get(
        "json",
        {}
    )
    returned_evaluation_id = json_data.get("evaluation_id","未知评测")
    returned_query = json_data.get("query","未知问题")
    returned_retrieval_score = json_data.get("retrieval_score", 0)
    returned_answer_score = json_data.get("answer_score", 0)
    returned_passed = json_data.get("passed", False)

    print(f"评测编号：{returned_evaluation_id}")
    print(f"问题：{returned_query}")
    print(f"检索分数：{returned_retrieval_score}")
    print(f"回答分数：{returned_answer_score}")
    print(f"是否通过：{returned_passed}")
