import requests
#示例
response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(response.text)
print(type(response.text))
print(response.cookies)