import re
content = 'Hello 123 4567 WORLD_THIS is a Regex DEMO'
# 常规匹配，内容与正则一一匹配
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*DEMO$',content)
print(result)

# 泛匹配，正则规定匹配内容开始内容和结束内容
result = re.match('^Hello.*DEMO$',content)
print(result)

# 匹配目标  小括号决定匹配目标，然后输入左右端点即可
result = re.match('^Hello\s(\d+)\s.*DEMO$',content)
print(result)
print(result.group(1))
print(result.span())

# 贪婪匹配  在遇到最后一个匹配目标前会一直匹配，只显示最后一个匹配目标
result =re.match('^He.*(\d+).*DEMO$',content)
print(result)
print(result.group(1))

# 非贪婪匹配 从遇到的第一个匹配目标开始匹配
result =re.match('^He.*?(\d+).*DEMO$',content)
print(result)
print(result.group(1))

# 匹配模式
content2 = 'Hello 123 4567 \n WORLD_THIS is a Regex DEMO'

result =re.match('He.*?(\d+).*?DEMO',content2,re.S)  #使用re.S使.＊匹配任意字符
print(result)
print(result.group(1))

#转义
content3 = 'price is $5.00'
result = re.match('price is \$5\.00',content3)
print(result)

