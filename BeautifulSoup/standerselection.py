import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.ttmeiju.com/latest.html').text
# print(response)
soup =BeautifulSoup(response,'lxml')
print(soup)
