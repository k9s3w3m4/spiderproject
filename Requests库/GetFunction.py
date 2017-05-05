import requests
# 基本用法
response = requests.get('http://httpbin.org/get')
print(response.text)

#get传参数
data = {
    'age':22 ,
    'name':'germey'
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)

#解析json
response =requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))

# 获取二进制数据
response = requests.get('http://httpbin.org/get')
print(type(response.text),type(response.content))
print(response.content)  #二进制数据
print(response.text) #文本数据

# 通过二进制保存图片
response = requests.get('https://img9.bcyimg.com/coser/88331/post/4bo9/e03a52602fc911e79b063f7dbe7df135.jpg/w650')
with open('2bcos.jpg','wb') as f :
    f.write(response.content)
    f.close()


#添加header
response = requests.get('http://zhihu.com/explore')
print(response.text)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
}
response = requests.get('http://zhihu.com/explore',headers=headers)
print(response.text)


