from  urllib.parse import urljoin
# 根据后面的参数，对前面进行合并。存在内容进行合并，不存在内容进行填充
# scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment'
print(urljoin('http:www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','http:www.taobao.com'))
print(urljoin('http://www.baidu.com/about.html','http://www.taobao.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://www.taobao.com/FAQ.html?question=2'))
print(urljoin('http://www.taobao.com/FAQ.html?question=2','https://www.baidu.com'))
print(urljoin('http://www.baidu.com','?category=2#comment'))
print(urljoin('http://www.baidu.com#comment','?category=2'))
