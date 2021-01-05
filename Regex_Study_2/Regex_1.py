import re

# case 1
text = 'if (myArray[0] == 0)'
# 대괄호는 메타 문자이기 때문에 그냥 '[', ']'를 쓰면 메타문자로 인식해 아무것도 찾지 못한다.
regex = r'myArray[0]'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''

'''

# case 2
text = 'if (myArray[0] == 0)'
regex = r'myArray\[0\]'  # 역슬래쉬 '\'를 붙여서 문자 자체를 의미하도록 만든다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
myArray[0]
'''

# case 3
text = '\\home\\ben\\sales\\'
regex = r'\\'  # 역슬래쉬가 두 개 있지만 실제로 찾는 것은 `\`이다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
\
\
\
\
'''

# case 4
text = '''
"101", "Ben", "Forta"
"102", "Jim", "James"

"103", "Roberta", "Robertson"
"104", "Bob", "Bobson"
'''
regex = r'\n\n'
# 유닉스는 /r/n, 리눅스는 /n을 하면 된다고 한다.
# 필자는 WSL2를 이용한 리눅스 체제의 VSCode를 사용하고 있어서 \n로 해야 되는 것 같다.
# 한참을 찾았다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''



'''
# 보이지는 않지만 공백이 3줄 입력됐는데, `\n\n`을 찾아서 두 칸의 공백이 생기고
# print문이 끝나면서 공백을 하나 더 생성하기 때문이다.

# case 5
text = 'if (myArray[0] == 0)'
regex = r'myArray\[\d\]'
# 메타 문자 `\d` : 숫자 하나([0-9])와 같다.
# 메타 문자 `\D` : 숫자를 제외한 문자 하나([^0-9])와 같다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
myArray[0]
'''

# case 6
text = '''
11213
A1C2E3
48075
48237
M1B4F2
90046
H1H2H2
'''
regex = r'\w\d\w\d\w\d'
# 메타 문자 `\w` : 대소문자와 밑줄을 포함하는 모든 영숫자([a-zA-Z0-9_])와 같다.
# 메타 문자 `\W` : 영숫자나 밑줄이 아닌 모든 문자([^a-zA-Z0-9_])와 같다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
A1C2E3
M1B4F2
H1H2H2
'''

# 이 외에도 `\s`, `\S` 등이 있다.
# `\s` : 모든 공백 문자([\f\n\r\t\v])와 같다.
# `\S` : 공백 문자가 아닌 모든 문자([^\f\n\r\t\v])와 같다.
