
import json

processed_ticket_count = 0
urgent_pending_ticket_count = 0
normal_pending_ticket_count = 0

try:
    with open(
        "week05/day25/business_flow/ticket_triage_data.json",
        "r",
        encoding="utf-8"
    )as ticket_file:
        ticket_list = json.load(ticket_file)
except json.JSONDecodeError:
    print("工单数据文件不是有效JSON")
else:
    for current_ticket in ticket_list:
        if current_ticket["processed"] == True:
            processed_ticket_count = processed_ticket_count + 1

        elif current_ticket["priority"] == "HIGH":
            urgent_pending_ticket_count = urgent_pending_ticket_count + 1

        else:
            normal_pending_ticket_count = normal_pending_ticket_count + 1

    print(f"已处理工单数量：{processed_ticket_count}")
    print(f"紧急待处理工单数量：{urgent_pending_ticket_count}")
    print(f"普通待处理工单数量：{normal_pending_ticket_count}")

# 把统计结果整理成一个报告字典
report_data = {
    "processed_ticket_count": processed_ticket_count,
    "urgent_pending_ticket_count": urgent_pending_ticket_count,
    "normal_pending_ticket_count": normal_pending_ticket_count
}

# 打开准备保存统计报告的 JSON 文件
with open(
    "week05/day25/business_flow/ticket_triage_report.json",
    "w",
    encoding="utf-8"
) as report_file:

    # 把 Python dict 保存成 JSON 文件
    json.dump(
        report_data,
        report_file,
        ensure_ascii=False,
        indent=4
    )

        