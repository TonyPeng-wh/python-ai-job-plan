def count_unprocessed_ticket(tickets):
    count_unprocessed = 0
    for current_ticket in tickets:
        if current_ticket["processed"] == False:
            count_unprocessed = count_unprocessed + 1
    return count_unprocessed

ticket_list = [
    {"ticket_id": "T001", "processed": False},
    {"ticket_id": "T002", "processed": True},
    {"ticket_id": "T003", "processed": False},
    {"ticket_id": "T004", "processed": False},
    {"ticket_id": "T005", "processed": True}
]

def check_ticket_workload(tickets):
    count_unprocessed = count_unprocessed_ticket(tickets)
    if count_unprocessed >= 3:
        return "任务较多"
    else:
        return "任务正常"

workload_status = check_ticket_workload(ticket_list)

print(f"工单处理状态：{workload_status}")