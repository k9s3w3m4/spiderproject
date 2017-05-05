from urllib.parse import urlencode
# 将字典快速转换成url参数
params = {
    'name' : 'germey',
    'age' : 22
}

base_url = 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)