from pyquery import PyQuery as pq
url = 'http://fgowiki.com/'
doc = pq(url)
# 伪类选择注意层级关系
items = doc('.col-md-3.navi .nav.nav-pills.nav-stacked.submenu ')
print(items)
print('_____________________________________________________')
print('获取第一个子标签')
li = items('li:first-child')
print(li)
print('_____________________________________________________')
print('获取最后一个子标签')
li = items('li:last-child')
print(li)
print('_____________________________________________________')
print('获取第二个子标签')
li = items('li:nth-child(2)')
print(li)
print('_____________________________________________________')
# 获取比二大的子标签
li = items('li:gt(2)')
print(li)
print('_____________________________________________________')
# 获取n倍数的标签
li = items('li:nth-child(2n)')
print(li)
print('_____________________________________________________')
# 获取包涵内容文本的标签
li = items('li:contains(second)')
print(li)