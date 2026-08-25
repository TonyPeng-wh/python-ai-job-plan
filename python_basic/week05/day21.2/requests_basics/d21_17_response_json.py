# 如果服务器返回的是 JSON 数据，response.json() 可以把响应里的 JSON 直接解析成 Python 数据。
"""
Requests 官方文档也特别说明：
如果响应不是合法 JSON，调用 response.json() 会抛出 requests.exceptions.JSONDecodeError；
而且 JSON 能成功解析，并不代表 HTTP 请求本身一定成功，仍然应该结合 status_code 判断。
"""
