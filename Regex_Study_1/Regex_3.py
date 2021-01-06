import re

# case 1
# 만약 "ca1.xls" 같은 파일도 있다면 Regex_2.py에서 했던 방식으로는 "na" 파일과 "sa" 파일만 골라낼 수 없게 된다.
text = '''
sales1.xls
orders3.xls
sales2.xls
sales3.xls
apac1.xls
europe2.xls
na1.xls
na2.xls
sa1.xls
ca1.xls
'''
regex = r'.a.\.xls'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
na1.xls
na2.xls
sa1.xls
ca1.xls
'''
# "ca1.xls"가 포함되어 있는 것을 볼 수 있다.

# case 2
# 대괄호 "[]"를 통해 문자 집합을 표현해주면 된다.
# 대괄호 안에 있는 문자는 모두 집합의 구성원이 되며, 집합에 속한 문자 가운데 하나가 일치한다.
# 집합에 속한 문자가 모두 일치할 필요는 없다.
text = '''
sales1.xls
orders3.xls
sales2.xls
sales3.xls
apac1.xls
europe2.xls
na1.xls
na2.xls
sa1.xls
ca1.xls	
'''
regex = r'[ns]a.\.xls'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
na1.xls
na2.xls
sa1.xls
'''
# 'a'의 앞에 'n'과 's'가 들어간 파일만 출력된 것을 볼 수 있다.
# 참고 : 실제 상황에서는 이것도 정답이 아니다. ex) usa1.xls 같은 경우를 제외시킬 수 없음. 나중에 배움

# case 3
text = 'The phrase "regular expression" is often abbreviated as RegEx or regex.'
regex = r'[Rr]eg[Ee]x'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
RegEx
regex
'''
# "RegEx"와 "regex"는 구별할 수 있으나 "REGEX" 같은 다른 케이스들은 구별하지 못한다.
# 대소문자를 구별하지 않고 모든 문자를 찾아도 된다면 이렇게 할 필요 없음!(당연)

# case 4
# 패턴 "[ns]a.\.xls" 같은 경우는 "sam.xls" 같은 파일도 일치하기 때문에 패턴을 바꿔줘야한다.
text = '''
sales1.xls
orders3.xls
sales2.xls
sales3.xls
apac1.xls
europe2.xls
na1.xls
na2.xls
sa1.xls
ca1.xls
sam.xls
'''
regex = r'[ns]a[0123456789]\.xls'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
na1.xls
na2.xls
sa1.xls
'''
# "sam.xls"가 포함되지 않은 것을 볼 수 있다.

# case 5
# 범위 지정을 위해 '-'를 사용할 수 있다.
# 조건이 있는데, 범위 지정 시 더 큰 값이 앞에 나오면 안된다.
# A-z는 사용 안하는 것이 좋다(범위의 기준이 ASCII라서 'Z'와 'a' 사이에 있는 것 까지 포함되기 때문이다. '[', '^' 같은 것들)
text = '''
sales1.xls
orders3.xls
sales2.xls
sales3.xls
apac1.xls
europe2.xls
na1.xls
na2.xls
sa1.xls
ca1.xls
sam.xls
'''
# '-'로 "0123456789"를 다 쓰는게 아닌 범위를 짧게 지정할 수 있다.
regex = r'[ns]a[0-9]\.xls'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
na1.xls
na2.xls
sa1.xls
'''
# case 4의 결과 값과 똑같다.

# case 6
text = '''
body {
	background-color: #fefbd8;
}
h1 {
	background-color: #0000ff;
}
div {
	background-color: #d0f4e6;
}
span {
	background-color: #f08970;
}
'''
regex = r'#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
#fefbd8
#0000ff
#d0f4e6
#f08970
'''
# '#'이 일치하고 뒤의 6개 문자가 "0123456789ABCDEFabcdef" 중 하나여야 한다.

# case 7
# 제외하기 위해서는 캐럿('^')을 사용한다.
# 캐럿 문자는 이 문자 바로 뒤에 있는 문자나 범위뿐만 아니라 집합 안에 있는 문자나 범위를 모두 제외한다.
text = '''
sales1.xls
orders3.xls
sales2.xls
sales3.xls
apac1.xls
europe2.xls
na1.xls
na2.xls
sa1.xls
ca1.xls
sam.xls
'''
regex = r'[ns]a[^0-9]\.xls'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
sam.xls
'''
# 'a'의 앞에 'n'이나 's'가 있어야 하고, 'a'의 뒤에는 숫자가 들어오면 안되는 조건

# 대괄호 "[]"와 하이픈 '-', 그리고 캐럿 '^'에 대해 공부하였다.
