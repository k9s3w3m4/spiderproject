from  urllib.parse import urlparse
# url解析模块  解析url
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

# 没有协议类型指定协议类型
result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)

# 有协议类型，指定协议类型无效
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)

# 是否允许fragement  如果不允许，fragement会自动向前拼接
result =urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments=False)
print(result)

result = urlparse('http://www.baidu.com/index.html#comment',allow_fragments=False)
print(result)