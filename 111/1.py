# 导入 csv 标准库，用于读写 CSV 文件
import csv

# 导入 json 标准库，用于读写 JSON 文件
import json

# 导入 requests 第三方库，用于发送 HTTP 请求
import requests


# =========================
# 1. 创建新能源汽车售后反馈数据
# =========================

def create_sample_feedbacks():
    # 整体数据类型是 list
    # list 中的每一个元素都是一个 dict
    feedback_list = [
        {
            "feedback_code": "FB2026001",
            "question": "车辆充电到 60% 后自动停止",
            "fault_type": "充电故障",
            "priority": "HIGH",
            "answer_score": 0.72,
            "processed": False
        },
        {
            "feedback_code": "FB2026002",
            "question": "车辆行驶过程中出现动力受限",
            "fault_type": "电机故障",
            "priority": "HIGH",
            "answer_score": 0.88,
            "processed": False
        },
        {
            "feedback_code": "FB2026003",
            "question": "手机无法连接车辆蓝牙",
            "fault_type": "通信故障",
            "priority": "MEDIUM",
            "answer_score": 0.93,
            "processed": True
        },
        {
            "feedback_code": "FB2026004",
            "question": "动力电池温度过高",
            "fault_type": "电池故障",
            "priority": "HIGH",
            "answer_score": 0.67,
            "processed": False
        }
    ]

    # 返回整个反馈列表
    return feedback_list


# =========================
# 2. 保存 JSON
# =========================

def save_feedbacks_to_json(feedback_list, filename):
    # 以写入模式打开 JSON 文件
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        # Python list/dict → JSON 文件
        json.dump(
            feedback_list,
            file,
            ensure_ascii=False,
            indent=4
        )


# =========================
# 3. 读取 JSON
# =========================

def load_feedbacks_from_json(filename):
    try:
        # 以读取模式打开 JSON 文件
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            # JSON 文件 → Python list/dict
            feedback_list = json.load(file)

            # 返回读取后的数据
            return feedback_list

    # JSON 文件格式错误时捕获异常
    except json.JSONDecodeError:
        print("JSON文件格式错误")
        return []


# =========================
# 4. 保存 CSV
# =========================

def save_feedbacks_to_csv(feedback_list, filename):
    # 定义 CSV 文件的字段顺序
    fieldnames = [
        "feedback_code",
        "question",
        "fault_type",
        "priority",
        "answer_score",
        "processed"
    ]

    # 打开 CSV 文件
    with open(
        filename,
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        # 创建 DictWriter 对象
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        # 写入 CSV 表头
        writer.writeheader()

        # 遍历整个反馈列表
        for current_feedback in feedback_list:
            # 把当前反馈 dict 写入 CSV
            writer.writerow(current_feedback)


# =========================
# 5. 读取 CSV
# =========================

def load_feedbacks_from_csv(filename):
    # 创建空列表，用来保存读取后的数据
    feedback_list = []

    # 打开 CSV 文件
    with open(
        filename,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        # 创建 DictReader 对象
        reader = csv.DictReader(file)

        # 一行一行读取
        for current_feedback in reader:
            try:
                # CSV 中读出来的 answer_score 是 str
                # 转换成 float
                current_feedback["answer_score"] = float(
                    current_feedback["answer_score"]
                )

            # 如果分数字符串不能转换成 float
            except ValueError:
                print("发现无效的回答质量分数，当前数据已跳过")

                # 跳过当前反馈
                continue

            # CSV 中的 True / False 读取后也是字符串
            # 把它转换成真正的 bool
            current_feedback["processed"] = (
                current_feedback["processed"] == "True"
            )

            # 把当前反馈加入大列表
            feedback_list.append(current_feedback)

    # 返回 list[dict]
    return feedback_list


# =========================
# 6. 获取用户输入的质量阈值
# =========================

def get_quality_threshold():
    # 不断要求用户输入，直到得到有效数据
    while True:
        # input() 得到 str
        # strip() 去掉前后空格
        threshold_text = input(
            "请输入AI回答质量合格阈值（0~1）："
        ).strip()

        try:
            # 尝试把字符串转换成 float
            quality_threshold = float(threshold_text)

        # 无法转换时发生 ValueError
        except ValueError:
            print("请输入有效数字")

            # 重新进入下一轮 while
            continue

        else:
            # 数据类型正确后，再判断业务范围
            if (
                quality_threshold >= 0
                and quality_threshold <= 1
            ):
                # 输入正确，返回 float
                return quality_threshold

            else:
                print("阈值必须在 0 到 1 之间")


# =========================
# 7. 分析反馈数据
# =========================

def analyze_feedbacks(feedback_list, quality_threshold):
    # 总反馈数量
    feedback_count = len(feedback_list)

    # 有效反馈数量
    valid_feedback_count = 0

    # HIGH 优先级数量
    high_priority_count = 0

    # 未处理数量
    unprocessed_count = 0

    # 低质量 AI 回答数量
    low_quality_count = 0

    # 需要重点关注的数量
    attention_count = 0

    # 所有有效回答质量分数之和
    total_score = 0

    # 创建空 set
    # 用于保存不重复的故障类型
    fault_types = set()

    # 遍历整个反馈列表
    for current_feedback in feedback_list:
        try:
            # 从当前 dict 中读取字段
            priority = current_feedback["priority"]
            processed = current_feedback["processed"]
            answer_score = current_feedback["answer_score"]
            fault_type = current_feedback["fault_type"]
            feedback_code = current_feedback["feedback_code"]

        # 缺少必要字段时发生 KeyError
        except KeyError:
            print("当前反馈缺少必要字段，已跳过")
            continue

        # 当前反馈有效
        valid_feedback_count = valid_feedback_count + 1

        # 把当前分数加入总分
        total_score = total_score + answer_score

        # 把故障类型加入 set
        # 重复故障类型不会重复保存
        fault_types.add(fault_type)

        # 判断优先级
        if priority == "HIGH":
            high_priority_count = high_priority_count + 1

        # processed 是 bool
        # not False → True
        if not processed:
            unprocessed_count = unprocessed_count + 1

        # 判断 AI 回答质量等级
        if answer_score < quality_threshold:
            low_quality_count = low_quality_count + 1
            quality_level = "需要复查"

        elif answer_score < 0.9:
            quality_level = "基本合格"

        else:
            quality_level = "表现良好"

        # 使用 or：
        # HIGH 或回答质量低，都需要重点关注
        if (
            priority == "HIGH"
            or answer_score < quality_threshold
        ):
            attention_count = attention_count + 1

        # 输出当前反馈的分析结果
        print(
            f"{feedback_code}：{quality_level}"
        )

    # 防止有效数据数量为 0
    if valid_feedback_count > 0:
        average_score = (
            total_score / valid_feedback_count
        )
    else:
        average_score = 0

    # 创建分析结果字典
    analysis_result = {
        "feedback_count": feedback_count,
        "valid_feedback_count": valid_feedback_count,
        "high_priority_count": high_priority_count,
        "unprocessed_count": unprocessed_count,
        "low_quality_count": low_quality_count,
        "attention_count": attention_count,
        "average_score": average_score,
        "fault_types": fault_types
    }

    # 返回统计结果
    return analysis_result


# =========================
# 8. 查找第一条 HIGH 且未处理反馈
# =========================

def find_first_urgent_feedback(feedback_list):
    # 默认没有找到
    urgent_feedback = None

    # 遍历反馈列表
    for current_feedback in feedback_list:
        try:
            # 判断是否同时满足两个条件
            if (
                current_feedback["priority"] == "HIGH"
                and not current_feedback["processed"]
            ):
                # 保存当前反馈
                urgent_feedback = current_feedback

                # 找到第一条以后立即结束循环
                break

        except KeyError:
            # 当前数据字段不完整时跳过
            continue

    # 返回 dict 或 None
    return urgent_feedback


# =========================
# 9. 检查反馈编号
# =========================

def check_feedback_code(feedback_code):
    # 清理字符串前后空格
    feedback_code = feedback_code.strip()

    # 先判断长度
    if len(feedback_code) >= 8:
        # 获取前两个字符
        code_prefix = feedback_code[0:2]

        # 获取年份字符
        code_year = feedback_code[2:6]

        # 判断年份是否全部为数字
        year_is_numeric = code_year.isdigit()

        # 同时判断编号前缀和年份
        if (
            code_prefix == "FB"
            and year_is_numeric
        ):
            print(
                f"反馈编号格式正确，年份：{code_year}"
            )

        else:
            print("反馈编号格式错误")

    else:
        print("反馈编号长度不足")


# =========================
# 10. 选择一条反馈
# =========================

def select_feedback(feedback_list):
    # 不断要求用户输入
    while True:
        selection_text = input(
            "请输入准备提交给API的反馈序号："
        ).strip()

        # 判断输入是否只包含数字
        if not selection_text.isdigit():
            print("请输入数字序号")
            continue

        # str → int
        selection_number = int(selection_text)

        # 判断序号是否在有效范围内
        if (
            selection_number >= 1
            and selection_number <= len(feedback_list)
        ):
            # list 索引从 0 开始
            current_feedback = feedback_list[
                selection_number - 1
            ]

            # 返回用户选择的当前元素
            return current_feedback

        else:
            print("输入的序号超出范围")


# =========================
# 11. 保存 TXT 分析报告
# =========================

def save_analysis_report(analysis_result, filename):
    # 打开 TXT 文件
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        # 写入统计结果
        file.write(
            f"反馈总数："
            f"{analysis_result['feedback_count']}\n"
        )

        file.write(
            f"有效反馈数量："
            f"{analysis_result['valid_feedback_count']}\n"
        )

        file.write(
            f"HIGH优先级数量："
            f"{analysis_result['high_priority_count']}\n"
        )

        file.write(
            f"未处理数量："
            f"{analysis_result['unprocessed_count']}\n"
        )

        file.write(
            f"低质量回答数量："
            f"{analysis_result['low_quality_count']}\n"
        )

        file.write(
            f"重点关注数量："
            f"{analysis_result['attention_count']}\n"
        )

        file.write(
            f"平均回答质量分数："
            f"{analysis_result['average_score']}\n"
        )


# =========================
# 12. 读取 TXT 报告
# =========================

def read_analysis_report(filename):
    # 打开 TXT 文件
    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        # file 是文件对象
        # file.read() 得到真正的 str 文件内容
        report_content = file.read()

    # 返回字符串内容
    return report_content


# =========================
# 13. GET API 请求
# =========================

def send_question_get_request(question):
    # 创建 Query Parameters
    query_params = {
        "question": question
    }

    # 创建请求头
    request_headers = {
        "Authorization": "Bearer demo-token"
    }

    try:
        # 发送 GET 请求
        response = requests.get(
            "https://postman-echo.com/get",
            params=query_params,
            headers=request_headers,
            timeout=10
        )

        # response 是 Response 对象
        print(
            f"GET状态码：{response.status_code}"
        )

        print(
            f"GET最终URL：{response.url}"
        )

        # 检查 HTTP 4xx / 5xx
        response.raise_for_status()

        # Response 对象中的 JSON
        # → Python 数据
        response_data = response.json()

        # 返回解析后的 Python 数据
        return response_data

    except requests.exceptions.HTTPError:
        print("GET请求发生HTTP错误")
        return None

    except requests.exceptions.JSONDecodeError:
        print("GET响应不是有效JSON")
        return None

    except requests.exceptions.Timeout:
        print("GET请求超时")
        return None

    except requests.exceptions.ConnectionError:
        print("GET请求无法连接服务器")
        return None

    except requests.exceptions.RequestException:
        print("GET请求发生其他异常")
        return None


# =========================
# 14. POST API 请求
# =========================

def send_feedback_post_request(current_feedback):
    # 创建准备发送到 Request Body 的业务数据
    request_data = {
        "feedback_code": current_feedback["feedback_code"],
        "question": current_feedback["question"],
        "fault_type": current_feedback["fault_type"],
        "priority": current_feedback["priority"],
        "answer_score": current_feedback["answer_score"],
        "processed": current_feedback["processed"]
    }

    # 创建 Query Parameters
    query_params = {
        "source": "after_sales"
    }

    # 创建请求头
    request_headers = {
        "Authorization": "Bearer demo-token"
    }

    try:
        # 发送 POST 请求
        response = requests.post(
            "https://postman-echo.com/post",

            # params 是 requests 规定的参数名
            # query_params 是自己创建的变量
            params=query_params,

            # json 是 requests 规定的参数名
            # request_data 是自己创建的变量
            json=request_data,

            # headers 是 requests 规定的参数名
            # request_headers 是自己创建的变量
            headers=request_headers,

            # 超时时间
            timeout=10
        )

        # response 是 Response 对象
        print(
            f"POST状态码：{response.status_code}"
        )

        print(
            f"POST最终URL：{response.url}"
        )

        # response.text 是服务器返回的原始字符串
        print(
            f"响应文本前100个字符："
            f"{response.text[:100]}"
        )

        # 检查 HTTP 4xx / 5xx
        response.raise_for_status()

        # JSON 响应 → Python 数据
        response_data = response.json()

        # 返回响应数据
        return response_data

    except requests.exceptions.HTTPError:
        print("POST请求发生HTTP错误")
        return None

    except requests.exceptions.JSONDecodeError:
        print("POST响应不是有效JSON")
        return None

    except requests.exceptions.Timeout:
        print("POST请求超时")
        return None

    except requests.exceptions.ConnectionError:
        print("POST请求无法连接服务器")
        return None

    except requests.exceptions.RequestException:
        print("POST请求发生其他异常")
        return None


# ==================================================
# 从这里开始按照实际业务执行程序
# 没有使用 main()
# ==================================================

print("=== 新能源汽车售后 VOC 综合分析程序 ===")


# 创建最初的 Python 数据
feedback_list = create_sample_feedbacks()


# -------------------------
# JSON 写入和读取
# -------------------------

json_filename = "feedback_data.json"

# Python 数据 → JSON 文件
save_feedbacks_to_json(
    feedback_list,
    json_filename
)

# JSON 文件 → Python 数据
loaded_feedback_list = load_feedbacks_from_json(
    json_filename
)

print(
    f"JSON读取反馈数量："
    f"{len(loaded_feedback_list)}"
)


# -------------------------
# CSV 写入和读取
# -------------------------

csv_filename = "feedback_data.csv"

# Python 数据 → CSV
save_feedbacks_to_csv(
    loaded_feedback_list,
    csv_filename
)

# CSV → Python list[dict]
csv_feedback_list = load_feedbacks_from_csv(
    csv_filename
)

print(
    f"CSV读取反馈数量："
    f"{len(csv_feedback_list)}"
)


# -------------------------
# range + list索引
# -------------------------

print("=== 当前反馈列表 ===")

# range 根据反馈数量生成数字
for index in range(len(csv_feedback_list)):
    # 大容器 → 当前索引 → 当前元素
    current_feedback = csv_feedback_list[index]

    # 输出序号和反馈编号
    print(
        f"{index + 1}. "
        f"{current_feedback['feedback_code']} "
        f"{current_feedback['question']}"
    )


# -------------------------
# 用户输入质量阈值
# -------------------------

quality_threshold = get_quality_threshold()

print(
    f"当前质量合格阈值："
    f"{quality_threshold}"
)


# -------------------------
# 分析数据
# -------------------------

analysis_result = analyze_feedbacks(
    csv_feedback_list,
    quality_threshold
)

print("=== 分析结果 ===")

print(
    f"反馈总数："
    f"{analysis_result['feedback_count']}"
)

print(
    f"HIGH优先级数量："
    f"{analysis_result['high_priority_count']}"
)

print(
    f"未处理数量："
    f"{analysis_result['unprocessed_count']}"
)

print(
    f"低质量回答数量："
    f"{analysis_result['low_quality_count']}"
)

print(
    f"平均质量分数："
    f"{analysis_result['average_score']}"
)

# fault_types 本身就是 set
# 不转换成 list
print(
    f"故障类型集合："
    f"{analysis_result['fault_types']}"
)


# -------------------------
# break
# -------------------------

urgent_feedback = find_first_urgent_feedback(
    csv_feedback_list
)

if urgent_feedback is not None:
    print(
        f"第一个待处理HIGH反馈："
        f"{urgent_feedback['feedback_code']}"
    )

    # 检查字符串编号
    check_feedback_code(
        urgent_feedback["feedback_code"]
    )


# -------------------------
# TXT 文件
# -------------------------

report_filename = "feedback_report.txt"

# 保存 TXT
save_analysis_report(
    analysis_result,
    report_filename
)

# 读取 TXT
report_content = read_analysis_report(
    report_filename
)

print("=== TXT统计报告 ===")

print(report_content)


# -------------------------
# 让用户选择一条反馈
# -------------------------

selected_feedback = select_feedback(
    csv_feedback_list
)

print(
    f"当前选择反馈："
    f"{selected_feedback['feedback_code']}"
)


# -------------------------
# GET 请求
# -------------------------

get_response_data = send_question_get_request(
    selected_feedback["question"]
)

# 请求成功才继续读取
if get_response_data is not None:
    # 大 dict → args 小 dict
    args_data = get_response_data.get(
        "args",
        {}
    )

    # 小 dict → question
    returned_question = args_data.get(
        "question",
        "未获取到问题"
    )

    print(
        f"GET服务器返回问题："
        f"{returned_question}"
    )


# -------------------------
# POST 请求
# -------------------------

post_response_data = send_feedback_post_request(
    selected_feedback
)

# 请求成功才继续处理
if post_response_data is not None:
    # Request Body 回显位于 json
    json_data = post_response_data.get(
        "json",
        {}
    )

    # Query Parameters 回显位于 args
    args_data = post_response_data.get(
        "args",
        {}
    )

    # 从 json_data 中读取具体业务字段
    returned_feedback_code = json_data.get(
        "feedback_code",
        "未知反馈"
    )

    returned_question = json_data.get(
        "question",
        "未获取到问题"
    )

    returned_fault_type = json_data.get(
        "fault_type",
        "未知故障"
    )

    returned_priority = json_data.get(
        "priority",
        "UNKNOWN"
    )

    returned_answer_score = json_data.get(
        "answer_score",
        0
    )

    returned_processed = json_data.get(
        "processed",
        False
    )

    # 从 args_data 中读取 Query Parameter
    returned_source = args_data.get(
        "source",
        "unknown"
    )

    print("=== POST服务器返回数据 ===")

    print(
        f"反馈编号：{returned_feedback_code}"
    )

    print(
        f"问题：{returned_question}"
    )

    print(
        f"故障类型：{returned_fault_type}"
    )

    print(
        f"优先级：{returned_priority}"
    )

    print(
        f"回答质量分数：{returned_answer_score}"
    )

    print(
        f"是否已处理：{returned_processed}"
    )

    print(
        f"请求来源：{returned_source}"
    )