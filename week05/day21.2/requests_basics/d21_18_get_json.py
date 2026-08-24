import requests
response = requests.get(
    "https://httpbin.org/get"
)
print(response.status_code)
response_data = response.json()
print(response_data)
print(type(response_data))