# 读取服务器返回的文本内容 response.text。
# response.status_code 看“请求结果状态”，response.text 看“服务器实际返回的文本内容”。
# requests.get() 返回 Response 对象，而 Response.text 可以取得服务器响应中的文本内容。
import requests
response = requests.get("https://example.com")
print(response.status_code)
print(response.text)
print(type(response.text))