import re
import requests
import os
response = requests.get('http://bcy.net/coser/toppost100?type=week&date=20170507').text
# print(response)
# 设定正则
parten =re.compile('thumbnail">.*?href="(.*?)".*?title="(.*?)".*?src="(.*?)".*?lh24">.*?<a.*?>(.*?)</a>.*?</li>',re.S)
results = re.findall(parten,response)
print(results)
count = 0
# 遍历results结果
for i in results:
    halfurl,cosname,img,cosername = i
    print(halfurl,cosname,img,cosername)
    count = count+1
    # 洗掉cosname中的／防止保存图片发生错喔
    cosname2 = re.sub('\/','',cosname)
    print(count)
    print(cosname2)
    imgresponse = requests.get(img).content
    # if not os.path.exists('picture/'+cosname2+'.jpg'):
    #     os.mkdir('picture/'+cosname2+'.jpg')
    # 保存图片
    with open('picture/'+cosname2+'.jpg', 'wb') as f:
         f.write(imgresponse)
         f.close()
