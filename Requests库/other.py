import  requests
from  requests.packages import urllib3
from  requests.exceptions import ReadTimeout,HTTPError,RequestException
from  requests.auth import HTTPBasicAuth
#上传文件
files = {'file':open('2bcos.jpg','rb')}
response =requests.post('http://httpbin.org/post',files=files)
print(response.text)

#获取cookies
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key,valuse in response.cookies.items():
    print(key+'='+valuse)

#会话维持  但是进程独立获取不到信息
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)
# 会话维持  通过一个session发起两次请求
s =requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

# 证书验证
response = requests.get('http://www.12306.cn') #无证书会报ssl错误
print(response.status_code)

response =requests.get('http://www.12306.cn',verify = False)  #跳过证书验证
urllib3.disable_warnings()#消除证书验证警告
print(response.status_code)

# response = requests.get('http://www.12306.cn',cert =())    通过本地证书验证

# 代理设置
proxies = {      #代理池配置
    'http': 'http://127.0.0.1:9743',
    'https' : 'https://127.0.0.1:9843',
    'http' : 'http://user:password@127.0.0.1:9700',  #有用户名密码的代理在user处传入用户名，在password处传入密码
    'http' : 'socks5://127.0.0.1:9800'

}
# response =requests.get('https://www.taobao.com',proxies = proxies)
# print(response.status_code)

#socks 代理   需要先pip3 install requests［socks］ 模块

#超时设置
response = requests.get('http://www.baidu.com',timeout = 1000)
print(response.status_code,response.text)

#超时异常处理
try:
    response = requests.get('http://www.baidu.com',timeout = 0.1)
    print(response.status_code)
except ReadTimeout:
    print('TIMEOUT')

#认证设置
# r = requests.get('http://120.27.34.24:9001',auth =('user','123'))
# print(r.status_code)
# r = requests.get('http://120.27.34.24:9001',auth =HTTPBasicAuth('user','123'))
# print(r.status_code)

# 各种异常处理
try:
    r = requests.get('http://httpbin.org/get',timeout = 0.0001)
    print(r.status_code)
except ReadTimeout:
    print('TIMEOUT')
except HTTPError :
    print('Http-error')
except RequestException:
    print('error')