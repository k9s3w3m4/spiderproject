from pyquery import PyQuery as pq
url = 'http://fgowiki.com'
doc = pq(url)
# 注意：＃代表id  　.表示class  什么都不加表示标签
# print(doc('#page .container a'))
# 查找元素
# 子元素 find方法
items = doc('.col-md-3')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
print('________________________________________________________')
# 子元素 children 查找直接子元素
lis = items.children()
print(lis)
print('________________________________________________________')
lis = items.children('ul')
print(lis)
print('________________________________________________________')
#父元素 直系夫节点
items = doc('.col-md-3')
container = items.parent()
print(type(container))
print(container)
print('________________________________________________________')
# 全部父节点
items = doc('.col-md-3')
container = items.parents()
print(type(container))
print(container)
print('________________________________________________________')
# 兄弟元素
li = doc('.col-md-3 li')
print(li.siblings())
print('________________________________________________________')
# 没有空格直接连接的两个元素表示并列
items = doc('.col-md-3.navi')
print(items)