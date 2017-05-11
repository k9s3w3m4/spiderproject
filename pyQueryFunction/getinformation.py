from pyquery import PyQuery as pq
url = 'http://fgowiki.com/'
doc = pq(url)
a = doc('.col-md-3.navi li a')
print(type(a))
print(a)
# 提取单个属性
print(a.attr('href'))
print(a.attr.href)

#获取文本
print(a.text())

#获取html
print(a.html())