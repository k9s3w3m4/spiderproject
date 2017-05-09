import requests
import re
from  bs4 import BeautifulSoup
response = requests.get('https://book.douban.com').text
soup = BeautifulSoup(response,'lxml')
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

# 父节点和祖父节点
print(soup.a.parent)
print(list(enumerate(soup.a.parents)))

#获取兄弟节点
print(soup.li)
print(list(enumerate(soup.p.next_silblings)))
print(list(enumerate(soup.li.previous_silblings)))