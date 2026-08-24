# Python AI Application Engineer Learning Plan

面向 **AI 应用工程师 / 大模型应用开发 / RAG / Agent / 智能制造 + AI** 方向的个人学习与项目实践仓库。

本仓库记录从 Python 基础开始，逐步进入 HTTP/API、工程化、数据处理、大模型 API、RAG、Agent、评测与部署的完整学习过程。

当前学习重点不是“学完整个 Python”，而是围绕真实 AI 应用工程师岗位需要，建立能够独立编写、理解、调试和维护 AI 应用代码的能力。

---

## 1. Career Goal

目标岗位：

* AI 应用工程师
* AI 应用开发实习生
* 大模型 API 应用开发
* RAG / 企业知识库开发
* Agent / 智能体应用开发
* 智能制造 + AI 应用
* 新能源汽车 AI 应用方向

目标城市：

* 深圳

长期能力方向：

* Python 工程能力
* HTTP / REST API
* 大模型 API
* Structured Output
* Prompt Engineering
* Pydantic
* FastAPI
* SQL
* Pandas
* Embedding
* Vector Database
* RAG
* Hybrid Search
* Rerank
* Tool Calling
* Agent Workflow
* MCP
* LLM Evaluation
* Tracing / Observability
* Docker
* Git / GitHub
* 基础 CI/CD

---

## 2. Current Progress

当前进度：

**Week 05 / Day 26**

当前阶段已经从单纯的 Python 语法学习，逐渐进入：

**Python 基础收尾 + HTTP/API 综合应用 + 工程化过渡阶段**

目前已经能够完成：

* 读取 TXT / CSV / JSON 数据
* 使用 `list[dict]` 处理结构化业务数据
* 使用函数封装独立业务职责
* 使用 `try / except` 处理常见异常
* 使用 Requests 发送 GET / POST 请求
* 处理 Query Parameters / JSON Body / Headers
* 解析 HTTP Response
* 处理嵌套 JSON 数据
* 根据业务条件筛选需要调用 API 的数据
* 使用 `return response_data / None` 管理函数调用结果
* 统计 API 成功 / 失败数量
* 将处理结果重新保存为 JSON 报告
* 初步根据业务需求独立设计程序执行流程

---

## 3. Learned Topics

### Python Basics

已学习：

* Variables
* `int`
* `float`
* `str`
* `bool`
* `None`
* `input()`
* 类型转换
* f-string
* 比较运算
* `and`
* `or`
* `not`

条件判断：

```python
if
elif
else
```

---

### Loops

已学习：

```python
for
range()
while
break
continue
```

主要练习场景：

* 遍历售后反馈
* 遍历故障工单
* 遍历 AI 回答质量评测结果
* 条件统计
* 多条件筛选

---

### String Basics

已学习：

* 字符串索引
* 字符串切片
* `strip()`
* `isdigit()`
* 基础字符串处理

后续会继续补充 AI 数据清洗高频方法：

```text
split
join
replace
lower
upper
startswith
endswith
```

---

### Python Containers

已学习：

```python
list
dict
set
```

重点训练的数据层级：

```text
大容器
→ 当前元素
→ 当前元素中的字段
```

例如：

```python
feedback_list

current_feedback

current_feedback["priority"]
```

目前大量业务数据采用：

```python
list[dict]
```

结构处理。

---

### Functions

已学习：

```python
def
参数
默认参数
return
```

当前重点理解：

```text
主流程
→ 判断哪条数据需要处理

函数
→ 负责一项独立工作
```

例如：

```python
def send_review(evaluation_id, question, answer_score):
    ...
```

函数负责：

* 构造请求数据
* 调用 API
* 处理 HTTP Response
* 返回结果

成功：

```python
return response_data
```

失败：

```python
return None
```

---

### Modules

已学习：

```python
import
from ... import ...
```

已经练习：

```text
main.py
utils.py
```

等基础模块拆分思路。

---

### Exception Handling

已学习：

```python
try
except
else
```

常见异常：

```text
ValueError
ZeroDivisionError
KeyError
FileNotFoundError
JSONDecodeError
Timeout
ConnectionError
HTTPError
RequestException
```

当前重点训练：

> 不只判断“发生了什么异常”，还要判断“异常到底发生在哪一行”。

例如：

```text
requests.post()
→ Timeout / ConnectionError

response.raise_for_status()
→ HTTPError

response.json()
→ JSONDecodeError
```

---

## 4. File and Structured Data

### TXT

已学习：

```python
with open(...)
```

以及基础文件读取与写入。

---

### CSV

已学习：

```python
csv.DictReader
csv.DictWriter
```

重点掌握：

CSV 中：

```text
"True"
"False"
```

进入 Python 后仍然是：

```python
str
```

例如：

```python
current_feedback["urgent"] = (
    current_feedback["urgent"] == "True"
)
```

转换后才变成真正的：

```python
bool
```

---

### JSON

已学习：

```python
json.load()
json.dump()
```

JSON 与 Python 基础类型对应：

```text
JSON Object
→ dict

JSON Array
→ list

true / false
→ True / False

null
→ None
```

当前已经能够完成：

```text
JSON 文件
→ Python 数据
→ 业务处理
→ 新 dict
→ JSON 文件
```

的数据闭环。

---

## 5. Python Environment

已经学习：

* `.venv`
* 虚拟环境激活
* `pip`
* `python -m pip`
* 第三方库安装
* `requirements.txt`

当前主要第三方依赖：

```text
requests
```

环境恢复基本流程：

```bash
python -m venv .venv
```

激活虚拟环境后：

```bash
python -m pip install -r requirements.txt
```

---

## 6. HTTP and Requests

Requests 基础阶段已经基本完成。

已经学习：

### HTTP Basics

* Client
* Server
* API
* URL
* Endpoint
* Request
* Response

---

### HTTP Methods

```text
GET
POST
```

---

### Query Parameters

```python
response = requests.get(
    url=url,
    params=query_params
)
```

---

### JSON Request Body

```python
response = requests.post(
    url=url,
    json=request_data,
    timeout=5
)
```

这里：

```text
json
→ requests.post() 规定的参数名

request_data
→ 自己创建的 Python dict
```

---

### Headers

已接触：

```python
headers=request_headers
```

以及：

```text
Authorization
Bearer Token
```

基础概念。

---

### Response

已经使用：

```python
response.status_code
response.text
response.url
response.json()
response.raise_for_status()
```

需要持续区分：

```text
requests
→ 第三方库

response
→ Response 对象

response_data
→ response.json() 后的 Python 数据
```

---

## 7. API Data Flow

目前重点使用的数据流：

```text
本地业务数据

→ 函数参数

→ request_data

→ requests.post()

→ response

→ response.raise_for_status()

→ response.json()

→ response_data

→ return

→ 主流程继续处理
```

API 请求函数示例：

```python
def send_review(evaluation_id, question, answer_score):

    request_data = {
        "evaluation_id": evaluation_id,
        "question": question,
        "answer_score": answer_score
    }

    try:
        response = requests.post(
            url=url,
            json=request_data,
            timeout=10
        )

        response.raise_for_status()

        response_data = response.json()

        return response_data

    except requests.exceptions.RequestException:
        return None
```

---

## 8. Business Logic Practice

当前已经完成多种接近真实 AI / 智能制造业务的练习。

包括：

### 售后反馈处理

业务场景：

```text
读取售后反馈

检查是否已经提交

统计未提交反馈

统计紧急待提交反馈

调用 API

统计成功 / 失败

生成 JSON 报告
```

---

### AI 回答质量复核

业务规则：

```text
submitted == False

并且

answer_score < 0.75
```

才进入人工复核流程。

重点训练：

* 双条件业务判断
* 嵌套 `if`
* API 调用范围
* 函数参数提取
* 成功 / 失败统计
* JSON 报告生成

---

### 工单分类

已经练习：

```text
已处理
紧急待处理
普通待处理
```

等互斥分类。

重点理解：

```python
if
elif
else
```

适用于：

> 一条数据最终只能进入一个业务分类。

---

## 9. Current Key Weak Points

目前需要继续在新知识中强化：

### 1. Data Flow

持续确认：

```text
数据从哪里来？
当前变量是什么类型？
进入哪个函数？
return 到哪里？
最终保存到哪里？
```

---

### 2. Container Levels

重点继续训练：

```text
quality_task_list

current_quality_task

current_quality_task["answer_score"]
```

也就是：

```text
全部数据
→ 当前一条
→ 当前字段
```

---

### 3. Object vs Data

需要持续区分：

```text
file object
vs
file content

Response object
vs
response JSON

report_file
vs
report_data
```

---

### 4. Function Parameters

需要继续理解：

```python
json=request_data
```

以及：

```python
"url": url
```

等代码中：

> 哪些名字由库/API规定，哪些变量由自己定义。

---

### 5. Business Indentation

目前一个重要训练点：

> 缩进不只是代码格式，而是在表示业务范围。

例如：

```python
if submitted == False:

    if answer_score < 0.75:

        response_data = send_review(...)
```

表示：

只有满足两个条件的数据才调用 API。

---

### 6. Exception Location

持续训练：

```text
异常发生在：

requests.post()？

raise_for_status()？

response.json()？

json.load()？

字典字段读取？

open()？
```

---

## 10. Project Roadmap

学习过程同步推进三个连续业务项目。

### P1 — New Energy Vehicle VOC / AI Quality Analysis

新能源汽车售后 VOC / AI 回答质量分析平台。

目标：

```text
发现问题
分析用户反馈
分析模型回答质量
识别低质量结果
生成分析报告
```

---

### P2 — Engineering Knowledge Base RAG

新能源汽车 / 智能制造工程知识库。

目标：

```text
问题输入
知识检索
答案生成
引用证据
质量评估
```

---

### P3 — Fault Diagnosis and Ticket Agent

故障排查与工单协同 Agent。

目标：

```text
发现故障
检索知识
辅助诊断
调用工具
生成 / 更新工单
协同处理
```

三个项目形成：

```text
发现问题
→ 检索工程知识
→ 辅助故障处理
→ 工单协同
```

---

## 11. Current Repository Structure

当前仓库主要按照：

```text
weekXX/
└── dayXX/
```

组织学习代码。

例如：

```text
week05/
└── day26/
    └── w5_integration/
        ├── d26_01_after_sales_feedback_sync.py
        ├── after_sales_feedback.csv
        ├── sync_report.json
        ├── d26_02_ai_quality_review_sync.py
        ├── ai_quality_tasks.json
        └── quality_sync_report.json
```

文件命名规范：

```text
英文
snake_case
不使用空格
不使用中文文件名
```

---

## 12. Current Stage

目前已经结束：

```text
纯 Python 基础语法为主
```

正在进入：

```text
Python 工程基础
+
AI 应用工程前置阶段
```

下一阶段重点：

```text
Git / GitHub
Linux / CLI
环境变量
API Key 安全
Python 基础补丁
Pandas
真实大模型 API
Structured Output
Pydantic
```

Python 基础不会停止使用，但以后主要会：

> 在 Git、数据处理、LLM API、RAG、Agent 等真实场景中继续强化，而不是重新进行大规模纯语法复习。

---

## 13. Upcoming Python Foundation Patches

为了后续顺利进入 AI 应用开发，将在 W5–W9 中按需补充：

### High Priority

```text
tuple
packing / unpacking

dict.keys()
dict.values()
dict.items()

常用字符串方法

None
is / is not
Truthy / Falsy

关键字参数

可变对象与引用

UTF-8 / encoding

Type Hints

Minimal OOP

json.loads()
json.dumps()
```

### Engineering Additions

```text
__name__ == "__main__"

变量作用域

路径 / Current Working Directory

enumerate()

zip()

列表推导式

sorted(..., key=...)

正则表达式基础

logging

assert
```

这些内容不会单独重新开启一轮 Python 基础课程，而会嵌入后续真实业务任务。

---

## 14. Learning Principles

本仓库遵循以下学习原则：

1. 不以“学完整个 Python”为目标。
2. 以 AI 应用工程师岗位能力为目标。
3. 每个知识点尽量放进真实业务场景。
4. 不为了练函数进行无意义拆分。
5. 代码不仅要求能运行，还需要解释数据流。
6. 遇到错误优先通过 traceback 和执行位置定位。
7. 项目与课程同步推进。
8. 不为了简历堆框架。
9. 项目重点体现解决了什么问题。
10. 持续使用 Git / GitHub 记录学习和项目进化过程。

---

## 15. Current Milestone

当前阶段已经能够独立完成一个基础的：

```text
结构化文件输入

→ Python 数据处理

→ 业务规则筛选

→ HTTP API 调用

→ Response 解析

→ 异常处理

→ 成功 / 失败统计

→ JSON 报告输出
```

下一阶段将重点提升：

> **代码工程化、数据处理能力，以及真实 AI 模型 API 应用开发能力。**
