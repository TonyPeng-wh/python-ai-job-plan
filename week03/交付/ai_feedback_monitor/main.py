# 保存测试数据、调用其他模块、负责最终输出。
from feedback_utils import (
    count_total_feedbacks,
    count_answer_errors,
    count_unprocessed_feedbacks,
    count_high_priority_feedbacks,
    get_feedback_categories
)

from quality_utils import get_quality_status

feedback_list = [
    {
        "feedback_id": "F001",
        "category": "回答错误",
        "processed": False,
        "priority": "HIGH"
    },
    {
        "feedback_id": "F002",
        "category": "格式问题",
        "processed": True,
        "priority": "LOW"
    },
    {
        "feedback_id": "F003",
        "category": "检索失败",
        "processed": False,
        "priority": "HIGH"
    },
    {
        "feedback_id": "F004",
        "category": "回答错误",
        "processed": False,
        "priority": "MEDIUM"
    },
    {
        "feedback_id": "F005",
        "category": "回答错误",
        "processed": True,
        "priority": "HIGH"
    },
    {
        "feedback_id": "F006",
        "category": "格式问题",
        "processed": True,
        "priority": "LOW"
    }
]

# 反馈总数：6
feedback_count = count_total_feedbacks(feedback_list)
print(f"反馈总数：{feedback_count}")

# 回答错误数量：3
answer_errors_count = count_answer_errors(feedback_list)
print(f"回答错误数量：{answer_errors_count}")

# 未处理反馈数量：3
unprocessed_feedbacks_count = count_unprocessed_feedbacks(feedback_list)
print(f"未处理反馈数量：{unprocessed_feedbacks_count}")

# HIGH优先级反馈数量：3
high_priority_feedbacks_count = count_high_priority_feedbacks(feedback_list)
print(f"HIGH优先级反馈数量：{high_priority_feedbacks_count}")

# 反馈类型：{'回答错误', '格式问题', '检索失败'}
feedback_categories = get_feedback_categories(feedback_list)
print(f"反馈类型：{feedback_categories}")

try:
    warning_threshold = int(input("请输入回答错误警戒阈值："))
except ValueError:
    print("警戒阈值必须是整数")
else:
    if warning_threshold > 0:
        quality_status = get_quality_status(
            answer_errors_count,
            warning_threshold
        )
        print(f"质量状态：{quality_status}")
    else:
        print("警戒阈值必须大于0")