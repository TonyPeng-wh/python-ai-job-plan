import csv
import json
import requests

feedback_list = []

pending_feedback_count = 0
urgent_pending_count = 0
success_count = 0
failed_count = 0

# TODO：
# 1. 打开 after_sales_feedback.csv
# 2. 使用 csv.DictReader
# 3. for 逐条读取
# 4. 把 urgent 转成 bool
# 5. 把 submitted 转成 bool
# 6. 把处理后的 current_feedback 加入 feedback_list

with open(
    "week05/day26/w5_integration/after_sales_feedback.csv",
    "r",
    encoding="utf-8"
) as feedback_file:

    feedback_reader = csv.DictReader(feedback_file)

    for current_feedback in feedback_reader:
        current_feedback["urgent"] = current_feedback["urgent"] == "True"
        current_feedback["submitted"] = current_feedback["submitted"] == "True"

        feedback_list.append(current_feedback)

print(feedback_list)

def send_feedback_request(feedback_id, issue):

    # TODO：
    # 创建 request_data
    # 把我们自己的数据映射成 API 要求的数据
    request_data = {
        "title": issue,
        "body": feedback_id,
        "userId": 1
    }

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.post(
            url=url,
            json=request_data,
            timeout=5
        )
        response.raise_for_status()
        response_data = response.json()

        return response_data

    except requests.exceptions.HTTPError:
        print("HTTP请求失败")
        return None

    except json.JSONDecodeError:
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

for current_feedback in feedback_list:

    if current_feedback["submitted"] == False:
        pending_feedback_count = pending_feedback_count + 1

        if current_feedback["urgent"] == True:
            urgent_pending_count = urgent_pending_count + 1

        feedback_id = current_feedback["feedback_id"]
        issue = current_feedback["issue"]

        response_data = send_feedback_request(
            feedback_id,
            issue
        )

        if response_data is not None:
            success_count = success_count + 1
        else:
            failed_count = failed_count + 1

total_feedback_count = len(feedback_list)

report_data = {
    "total_feedback_count": total_feedback_count,
    "pending_feedback_count": pending_feedback_count,
    "urgent_pending_count": urgent_pending_count,
    "success_count": success_count,
    "failed_count": failed_count
}

# 把统计报告保存为 JSON 文件
with open(
    "week05/day26/w5_integration/sync_report.json",
    "w",
    encoding="utf-8"
) as report_file:

    # TODO：
    # 使用 json.dump()
    # 保存 report_data
    # ensure_ascii=False
    # indent=4
    json.dump(
        report_data,
        report_file,
        ensure_ascii=False,
        indent=4
    )


print(f"待提交反馈数量：{pending_feedback_count}")
print(f"紧急待提交反馈数量：{urgent_pending_count}")
print(f"反馈总数量：{total_feedback_count}")
print(f"API 提交成功数量：{success_count}")
print(f"API 提交失败数量：{failed_count}")