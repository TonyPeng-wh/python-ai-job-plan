# 函数调用函数②
def count_low_score_retrievals(retrievals):
    count_low_score = 0
    for current_retrieval in retrievals:
        if current_retrieval["score"] <0.75:
            count_low_score = count_low_score + 1
    return count_low_score

morning_retrievals = [
    {"query_id": "Q001", "score": 0.82},
    {"query_id": "Q002", "score": 0.61},
    {"query_id": "Q003", "score": 0.72}
]

afternoon_retrievals = [
    {"query_id": "Q004", "score": 0.91},
    {"query_id": "Q005", "score": 0.88},
    {"query_id": "Q006", "score": 0.70}
]

evening_retrievals = [
    {"query_id": "Q007", "score": 0.55},
    {"query_id": "Q008", "score": 0.68},
    {"query_id": "Q009", "score": 0.71},
    {"query_id": "Q010", "score": 0.90}
]

def check_retrieval_risk(retrievals):
    count_low_score = count_low_score_retrievals(retrievals)
    if count_low_score >= 3:
        return "需要检查检索质量"
    else:
        return "正常"

morning_status = check_retrieval_risk(morning_retrievals)
afternoon_status = check_retrieval_risk(afternoon_retrievals)
evening_status = check_retrieval_risk(evening_retrievals)

print(f"上午检索状态：{morning_status}")
print(f"下午检索状态：{afternoon_status}")
print(f"晚上检索状态：{evening_status}")