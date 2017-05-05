import requests
# 基础内容获取
response = requests.get('http://jianshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)

# 状态码判断
response =requests.get('http://jianshu.com')
exit() if not response.status_code == requests.codes.ok  else print('Request Successfully')


response =requests.get('http://jianshu.com')
exit() if not response.status_code == 200  else print('Request Successfully')

