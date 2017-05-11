from pyquery import PyQuery as pq
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'
}
url = 'http://fgowiki.com/'
response = requests.get(url,headers=headers).content
doc = pq(response)
lis = doc('li').items()
print(type(lis))
for i in lis :
    print(i('a'))

# print(doc)