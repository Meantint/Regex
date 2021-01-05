import re

# case 1
text = 'Hello, my name is Ben. Please visit my website at http://www.forta.com/.'
# "my"와 일치하는 것을 찾는다.
regex = r'my'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
my
my
'''

# case 2
text = 'Hello, my name is Ben. Please visit my website at http://www.forta.com/.'
# "Ben"와 일치하는 것을 찾는다.
regex = r'Ben'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
Ben
'''
