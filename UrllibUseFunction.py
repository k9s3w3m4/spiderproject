# URLLIB库
import urllib.request
import urllib.parse
import socket
import urllib.error
# urlopen
# get方法获取网页
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
# post方法获取网页
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read)
# 超时判断
response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(response.read())
# 超时判断并输出错误结果
try:
    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance( e.reason,socket.timeout):
        print('TIMEOUT')