import requests
# 基本形式
data = {
    'age': 22,
    'name':'germey'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
}
response = requests.post('http://httpbin.org/post',data=data)
print(response.text)

response = requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.json())


