import re
import requests
response = requests.get('http://bcy.net/coser/detail/88331/1191342')
print(type(response))
content = str(response.text)
# print(content)
result = re.findall('<img.*?src="(.*?)".*?alt=".*?">',content,re.S)
print(result)