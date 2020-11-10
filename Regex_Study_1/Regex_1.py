import re

# case 1
text = "Hello, my name is Ben. Please visit my website at http://www.forta.com/."
# "my"와 일치하는 것을 찾는다.
regex = re.compile("my")
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 =  ['my', 'my']

# case 2
text = "Hello, my name is Ben. Please visit my website at http://www.forta.com/."
# "Ben"와 일치하는 것을 찾는다.
regex = re.compile("Ben")
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 =  ['Ben']
