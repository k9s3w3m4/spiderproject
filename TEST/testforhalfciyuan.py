import re
import requests
response = requests.get('http://bcy.net/coser/detail/88331/1191342')
print(type(response))
content = str(response.text)
# print(content)
result = re.findall('<img.*?src="(.*?)".*?>',content,re.S)
print(type(result))
# for i in  result:
# print(i)
# 通过替换方法将alt标签和／洗掉
subcontent = re.sub('alt=".*?"','',content)
subcontent2 = re.sub('class=\'.*?\'','',subcontent)
print(subcontent2)
result = re.findall('<img  src=\'(.*?)\' />',subcontent2,re.S)
for i in result:
    print(i)

