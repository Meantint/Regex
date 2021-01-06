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
