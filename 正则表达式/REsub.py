import re
content = 'Extra string Hello 1234567 World_This is a Regex Demo Extra stings'
subcontent = re.sub('\d+','',content)
print(subcontent)
subcontent2 = re.sub('\d+','hello2',content)
print(subcontent2)