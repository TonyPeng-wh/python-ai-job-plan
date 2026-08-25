"""
1. HTTP 请求到底是什么
你平时打开网页时，其实就在发生类似过程：
你的电脑 / 浏览器
        ↓
      发送请求
        ↓
      服务器
        ↓
      返回响应
        ↓
你的电脑 / 浏览器
例如你在浏览器访问一个网站：
客户端Client
→ “请把这个网页的数据给我”
服务器Server
→ “好的，这是你要的数据”
这里有两个角色。

客户端 Client
就是主动发起请求的一方。
例如：
浏览器
Python 程序
手机 App
以后你的 AI 应用也经常是客户端。
服务器 Server
就是接收请求、处理请求、返回结果的一方。
例如以后调用模型 API：
你的 Python 程序
        ↓
     HTTP 请求
        ↓
     模型服务器
        ↓
      模型处理
        ↓
     HTTP 响应
        ↓
你的 Python 程序得到模型结果
2. requests 在这里干什么
Python 自己不会凭空知道：
“我要去网上访问这个服务器。”
requests 就是帮助 Python 发送 HTTP 请求 的第三方库。
所以以后你会看到：
import requests
然后类似：
response = requests.get(...)
这里可以先理解成：
Python 使用 requests 向某个服务器发一个请求，并把服务器返回的结果保存到 response。
3. 放到你的 AI 应用场景里
以后你的 RAG 项目可能会发生：
用户问题：
“车辆无法快充是什么原因？”
        ↓
你的 Python 程序
        ↓
整理请求数据
        ↓
HTTP 请求
        ↓
模型 API 服务器
        ↓
模型生成回答
        ↓
HTTP 响应
        ↓
Python 获取结果
        ↓
展示给用户
所以你现在学 requests，实际上是在给以后 模型 API 调用打基础。
"""
