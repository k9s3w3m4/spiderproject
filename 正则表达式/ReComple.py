import re
content = 'Extra string Hello 1234567 World_This is a Regex Demo Extra stings'
parameter = re.compile('Ex.*?ings',re.S)
result = re.match(parameter,content)
print(result)
