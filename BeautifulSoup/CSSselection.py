import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.ttmeiju.com/latest.html').text
# print(response)
soup =BeautifulSoup(response,'lxml')
# print(soup)
# # class选择
print(soup.select('.latesttable .Scontent1'))
# # 标签选择
print(soup.select('tr td'))
# # id选择
print(soup.select('#zimulink'))

# 层层迭代的两种方式
# 1 直接写在select选择器中，空格分割开
print(soup.select('.latesttable .Scontent1 a'))
# 2 通过for循环进行
for tr in soup.select('tr'):
    for td in tr.select('td'):
            print(td.select('a'))