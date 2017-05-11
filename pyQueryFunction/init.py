import requests
from pyquery import PyQuery as pq
url = 'http://fgowiki.com'
response = requests.get(url).text
# 字符串初始化
doc = pq(response)
print(doc)
# url初始化
doc = pq(url)
print(doc('header'))
# 文件初始化
# doc ＝ pq(filename = '文件路径') 同一目录下直接填写文件名
