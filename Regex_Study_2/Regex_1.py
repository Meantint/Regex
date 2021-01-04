import re

# case 1
text = "if (myArray[0] == 0)"
# 대괄호는 메타 문자이기 때문에 그냥 '[', ']'를 쓰면
# 메타문자로 인식해 아무것도 찾지 못한다.
regex = re.compile("myArray[0]")
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 = []

# case 2
text = "if (myArray[0] == 0)"
regex = re.compile("myArray\[0\]")
# 역슬래쉬 '\'를 붙여서 문자 자체를 의미하도록 만든다.
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 = ['myArray[0]']

# *** 보류! 책과 다름
# case 3
text = "\\home\\ben\\sales\\"
regex = re.compile(r"\\")
answer = regex.findall(text)
print("case 3 =", answer)

# *** 보류! 책과 다름
# case 4
text = '''
"101", "Ben", "Forta"
"102", "Jim", "James"

"103", "Roberta", "Robertson"
"104", "Bob", "Bobson"
'''
regex = re.compile("\n")
answer = regex.findall(text)
print("case 4 =", answer)
