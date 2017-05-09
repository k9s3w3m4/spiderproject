import re
import requests
#获取豆瓣读书首页内容
response = requests.get('https://book.douban.com')
print(response.text)

#设定清洗正则对内容进行清洗
partten  = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results=re.findall(partten,response.text)
print(results)

# 进行遍历，将变量对应付值
for i in results:
    url,title,author,data = i

    # 去除换行符号 strip方法
    print(str.strip(url),str.strip(title),str.strip(author),str.strip(data))
    # 去除换行符号 re.sub方法
    url = re.sub('\n','',url)
    title = re.sub('\n','', title)
    author = re.sub('\n','',author)
    data = re.sub('\n','',data)
    print(url,title,author,data)