import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.ttmeiju.com/latest.html').text
# print(response)
soup =BeautifulSoup(response,'lxml')
# print(soup)
# 获取属性
for tr in soup.select('tr'):
    print(tr['class'])
    print(tr.attrs['class'])
# 获取内容
for a in soup.select('a'):
    # print(a)
    print(str.strip(a.get_text()))
