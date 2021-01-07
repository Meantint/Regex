import re

# case 1
text = '''
ben@naver.com
support@naver.com
spam@naver.com
'''
# `+`는 메타 문자로 하나 이상의 문자를 찾아준다.
regex = r'\w+@\w+\.\w+'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
ben@naver.com
support@naver.com
spam@naver.com
'''

# case 2
text = '''
ben@naver.com
ben.naver@naver.com
support@naver.com
ben@urgent.naver.com
spam@naver.com
'''
# case 1과 똑같은 정규표현식을 썼을 때 제대로 찾지 못하는 경우가 있다.
regex = r'\w+@\w+\.\w+'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
ben@naver.com
naver@naver.com
support@naver.com
ben@urgent.naver
spam@naver.com
'''
# 두 번째 줄의 경우 ben.naver@naver.com가 나와야 하는데 `@`전의 `.` 때문에 앞의 ben.을 찾지 못한다.
# 네 번째 줄의 경우 위와 마찬가지의 상황으로 naver 뒤의 .com을 찾지 못한다.

# case 3
text = '''
ben@naver.com
ben.naver@naver.com
support@naver.com
ben@urgent.naver.com
spam@naver.com
'''
# case 1과 똑같은 정규표현식을 썼을 때 제대로 찾지 못하는 경우가 있다.
regex = r'[\w.]+@[\w.]+\.\w+'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
ben@naver.com.
ben.naver@naver.com.
support@naver.com.
ben@urgent.naver.com.
spam@naver.com.
'''
# 정규식에 두 개의 `\w`를 `[\w.]`으로 바꿔주어 `.`까지 포함하여 하나의 세트로 찾을 수 있게 해준다.
# 맨 뒤의 `\w`에도 앞의 정규식 형태처럼 만들 경우 문장의 마지막을 나타내는 `.`까지 세트로 인식하기 때문에 쓰면 안된다.

# case 4
text = '''
so
site
sss
stu
study
s
'''
# `*`는 메타 문자로 문자가 하나 이상이거나 없는 경우를 나타낼 수 있다.
regex = r's[\w]*'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
so
site
sss
stu
study
s
'''
# 맨 앞의 문자 `s`를 제외한 문자가 하나 이상인 경우와 하나도 없는 경우가 모두 나타난 것을 볼 수 있다.

# case 5
text = '''
http://www.naver.com
http://meantint.tistory.com/
https://www.google.com
https://meantint.tistory.com/
'''
# 메타 문자 `?`는 `?` 앞의 문자가 없거나 그 문자가 하나만 있는 경우 일치한다.
regex = r'https?:\/\/[\w.\/]+'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
http://www.naver.com
http://meantint.tistory.com/
https://www.google.com
https://meantint.tistory.com/
'''
# `http` 뿐만 아니라 `https`까지도 모두 찾아내는 것을 볼 수 있다.

# case 6
text = '''
abc
def

ghi
jkl
'''
regex = r'[\r]?\n[\r]?\n'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''



'''
# `\n`이 두 개가 있는데 세 줄인 이유는 각 행이 끝난 후 공백처리 하기 때문에
# 결과 값이 두개인 case 6의 경우 `\n`, `\n`의 사이에 개행이 한 번 일어난다.
# 이전의 예제에서도 설명한 적이 있다.

# case 7
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
# `{}` : 중괄호 안의 숫자 만큼 개수가 일치하는지 확인한다.
regex = r'#[A-Fa-f0-9]{6}'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
#fefbd8
#0000ff
#d0f4e6
#f08970
'''

# `{a,b}` : 중괄호 안의 숫자 범위 [a, b] 만큼 개수가 일치하는지 확인한다.
# `{0,1}`인 경우 `?`와 같다.
# `{a,} : 최소 a번 일치하는지를 확인한다.

# case 8
text = '''
1001: $496.80
1002: $1290.69
1003: $26.43
1004: $613.42
1005: $7.61
1006: $414.90
1007: $25.00
'''
# 금액이 100달러 이상인 주문을 모두 찾는 정규 표현식
regex = r'\d+: \$\d{3,}\.\d{2}'
result = re.findall(regex, text)
print('\n'.join(result))

# case 9
text = '''
This offer is not available to customers
living in <b>AK</b> and <b>HI</b>.
'''
# `*`와 `+`, 그리고 `{x,}` 같은 수량자는 탐욕적으로 작동하기 때문에
# 최대한 큰 덩어리를 찾으려고 하기 때문에 의도치 않게 더 큰 영역을 찾게 된다.
regex = r'<[Bb]>.*<\/[Bb]>'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
<b>AK</b> and <b>HI</b>
'''
# `<b>AK</b>`와 `<b>HI</b>`로 인식할 수 있었지만 탐욕적으로 탐색하기 때문에
# `<b>AK</b> and <b>HI</b>`로 인식하여 출력하게 된다.

# case 10
text = '''
This offer is not available to customers
living in <b>AK</b> and <b>HI</b>.
'''
# 탐욕적(Greedy) 수량자가 아닌 게으른(Lazy) 수량자로 만들기 위해서는 `?` 메타 문자를 사용하면 된다.
regex = r'<[Bb]>.*?<\/[Bb]>'
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''
<b>AK</b>
<b>HI</b>
'''
# `<b>` 태그가 두개로 나뉘어 출력된 것을 볼 수 있다(`?` 메타 문자를 이용하여).
