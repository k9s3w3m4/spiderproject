from urllib import request,error
import socket
# 捕获异常
try:
    response = request.urlopen('http://cuiqincai.com/index.html')
except error.URLError as e :
    print(e.reason)


# 异常类型
# URLerror，HTTPerror
try:
    response = request.urlopen('http://cuiqincai.com/index.html')
except error.HTTPError as  e:      #HTTP异常 可以查到原因 返回代码，headers
    print(e.reason,e.code,e.headers,sep='/n')
except error.URLError as e :      #URL异常 只能看到原因
    print(e.reason)
else:
    print('Requset successful')

# 验证异常原因
try:
     response = request.urlopen('http://www.baidu.com',timeout=0.000001)
except error.URLError as e:
     print(type(e.reason))
     if isinstance(e.reason,socket.timeout):
            print('Time out')