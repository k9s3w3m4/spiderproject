from urllib.parse import urlunparse
#通过数组拼接url
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))