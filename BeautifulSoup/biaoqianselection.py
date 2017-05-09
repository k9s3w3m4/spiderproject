import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.ttmeiju.com').text
# # 选择元素
soup = BeautifulSoup(response,'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# # P标签或其它有大量的标签比如img li 这种，soup只会返回第一个标签内容
# print(soup.p)
#
# # 获取最外层标签名称
# print(soup.title.name)

#获取属性
# print(soup.p.attrs['href'])
# print(soup.p['target'])

#获取内容
# print(soup.p.string)

# 嵌套选择，soup支持层层嵌套迭代，可以从大标签下一层一层往下选择 QAQ好用爆
# print(soup.p.a.attrs['href'])

# 子节点和子孙节点
#获取子节点
print(soup.div.contents)
# 获取可迭代子节点列表
print(soup.div.children)
#enum将可叠代的东西加上索引，参数为i 通过for循环将children带索引迭代
for i,child in enumerate(soup.head.children):
    print(i,child)
# 获取全部子孙节点
print(soup.div.descendants)
for i,childs in enumerate(soup.div.descendants):
    print(i,childs)

