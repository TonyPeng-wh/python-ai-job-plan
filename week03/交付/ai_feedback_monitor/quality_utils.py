# 后面负责根据统计结果判断质量状态。
def get_quality_status(answer_errors_count, warning_threshold):
    # 在这里判断
    if answer_errors_count >= warning_threshold:
    # return 对应的状态
        return  "需要检查"
    else:
        return  "正常"
