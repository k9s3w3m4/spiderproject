import urllib.request
import http.cookiejar

# 代理设置
proxy_handler = urllib.request.ProxyHandler({   #代理池设定
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
print(response.read())

# cookie设置  获取cookie
cookie = http.cookiejar.CookieJar()   #声明对象为cookie对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)


# cookie设置 将cookie保存到文件中
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)  #火狐浏览器cookiejar
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://wwww.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

# cookie设置 IWP类型cookiejar
filename = "IEcookie.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_expires=True,ignore_discard=True)

# cookie 设置  从文件中读取cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load('IEcookie.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener =urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))