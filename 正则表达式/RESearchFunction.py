import  re
content = 'Extra string Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hell.*?(\d+).*?Demo',content)
result2 = re.search('Hell.*?(\d+).*?Demo',content)
print(result)
print(result2)
print(result2.group(1))