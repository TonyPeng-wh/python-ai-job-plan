"""
先定义负责 API 通信的函数，然后读取并处理本地 JSON/CSV 数据；
当本地业务判断确定某条数据需要发送时，再调用 API 函数与服务器通信；最后继续在本地统计结果并写入 JSON。
"""
import requests
import json

unsubmitted_task_count = 0
low_score_task_count = 0 
success_count = 0
failed_count = 0

def send_review(    
    evaluation_id,    
    question,    
    answer_score,    
):    

    request_data = {    
        "evaluation_id": evaluation_id,    
        "question": question,
        "answer_score":answer_score
    }

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.post(
            url=url,
            json=request_data,
            timeout=10
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data

    except requests.exceptions.HTTPError:    
        print("HTTP请求失败")
        return None

    except requests.exceptions.JSONDecodeError:
        print("服务器返回的数据不是有效 JSON")
        return None

    except requests.exceptions.Timeout:
        print("API 请求超时")
        return None

    except requests.exceptions.ConnectionError:
        print("API 连接失败")
        return None

    except requests.exceptions.RequestException:
        print("API 请求发生其他异常")
        return None

        
with open(
    "week05/day26/w5_integration/ai_quality_tasks.json",
    "r",
    encoding="utf-8"
)as quality_task_file:
    quality_task_list = json.load(quality_task_file)

for current_quality_task in quality_task_list:
    if current_quality_task["submitted"] == False:
        unsubmitted_task_count = unsubmitted_task_count + 1
        if current_quality_task["answer_score"] < 0.75:
            low_score_task_count = low_score_task_count + 1

            evaluation_id = current_quality_task["evaluation_id"]
            question = current_quality_task["question"]
            answer_score = current_quality_task["answer_score"]

            response_data = send_review(
                evaluation_id,
                question,
                answer_score
            )

            if response_data is not None:
                success_count = success_count + 1
            else:
                failed_count = failed_count + 1

total_task_count = len(quality_task_list)

report_data = {
    "total_task_count": total_task_count,
    "unsubmitted_task_count": unsubmitted_task_count,
    "low_score_task_count": low_score_task_count,
    "success_count": success_count,
    "failed_count": failed_count
}

with open(
    "week05/day26/w5_integration/quality_sync_report.json",
    "w",
    encoding="utf-8"
)as report_file:
    
    json.dump(
        report_data,
        report_file,
        ensure_ascii=False,
        indent=4
    )

print("JSON 报告写入完成")