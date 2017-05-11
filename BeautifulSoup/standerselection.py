import requests
from bs4 import BeautifulSoup
# 标准选择器
response = requests.get('http://www.ttmeiju.com/latest.html').text
# print(response)
soup =BeautifulSoup(response,'lxml')
# print(soup)
# 根据name查找（标签查找）
# #找出所有tr标签
# print(soup.find_all('tr'))
# # 找出第一组tr标签的类型
# print(type(soup.find_all('tr')[0]))
# for tr in soup.find_all('tr'):
#     print(tr.find_all('td'))

# attrs查找
# print(soup.find_all(attrs={'class':'Scontent','class':'Scontent1'}))
# print(soup.find_all(attrs={'class':'Scontent1'}))
# ps  id class可以快速查询 但class属于关键字只能通过class_进行查找
# print(soup.find_all(class_='Scontent'))
# print(soup.find_all(id ='gtop'))

# text查找
print(soup.find_all(text='熟肉'))

# find 即为找寻单个标签
