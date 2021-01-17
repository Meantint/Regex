import re

# case 1
text = 're, regex, regular expression'
# `re`가 하나의 완전한 단어가 아닌 어떤 단어에 포함된 문자여도 다 읽는다.
regex = r're'
result = re.finditer(regex, text)
for res in result:
    print(res.group(), res.span())
# 결과
'''
re (0, 2)
re (4, 6)
re (11, 13)
re (22, 24)
'''

# case 2
text = 're, regex, regular expression'
# `re`라는 완전한 단어를 찾고 싶다면 경계를 지정해줘야한다.
# `\b`는 단어의 경계 위치(b -> boundary)를 나타내는 메타 문자이다.
# `\b`는 `\w`와 `\W`의 사이에 있는 위치와 일치한다.
regex = r'\bre\b'
result = re.finditer(regex, text)
for res in result:
    print(res.group(), res.span())
# 결과
'''
re (0, 2)
'''
# 앞 뒤로 경계를 지정해준 결과 완전한 `re` 문자 하나만 읽은 것을 볼 수 있다.

# case 3
text = 're, regex, regular expression'
# `re`의 앞부분에만 경계를 지정해줬을 때의 결과값을 보자.
regex = r'\bre'
result = re.finditer(regex, text)
for res in result:
    print(res.group(), res.span())
# 결과
'''
re (0, 2)
re (4, 6)
re (11, 13)
'''
# `expression` 안에 있는 `re`를 제외한 나머지 `re`들이 탐색되었다.
# `expression`의 경우 `re`의 앞에 `exp`가 붙어있기 때문에 탐색되지 않았다.

# case 4
text = 're, regex, regular expression'
# `re`의 뒷부분에만 경계를 지정해줬을 때의 결과값을 보자.
regex = r're\b'
result = re.finditer(regex, text)
for res in result:
    print(res.group(), res.span())
# 결과
'''
re (0, 2)
'''
# 맨 앞의 `re`를 제외한 나머지 `re`들이 탐색되지 않았다.
# 맨 앞의 `re`의 바로 뒤에 `,`가 있는데도 탐색된 이유는
# `\b`는 `\w`와 `\W`사이에 있는 위치인데 `,`는 `\W` 안에 포함되는 문자이기 떄문이다.

# case 5
text = '''
<?xml version="1.0" encoding="UTF-8" ?>
<wsdl:definitions targetNamespace="http://tips.cf"
'''
# 문자열 경계는 전체 문자열의 시작이나 마지막 부분과 패턴을 일치시키고자 할 때 사용한다.
regex = r'<\?xml.*\?>'
result = re.finditer(regex, text)
for res in result:
    print("{0}, {1}".format(res.group(), res.span()))
# 결과
'''
<?xml version="1.0" encoding="UTF-8" ?>, (1, 40)
'''

# case 6
text = '''
html, css, javascript
<?xml version="1.0" encoding="UTF-8" ?>
<wsdl:definitions targetNamespace="http://tips.cf"
'''
# case 5의 정규표현식은 앞에 다른 문자열이 있을 때 제대로 동작하지 않는다.
regex = r'<\?xml.*\?>'
result = re.finditer(regex, text)
for res in result:
    print("{0}, {1}".format(res.group(), res.span()))
# 결과
'''
<?xml version="1.0" encoding="UTF-8" ?>, (23, 62)
'''
# 결과값은 잘 나오지만 유효한 정규표현식이 아니다.

# case 7
text = '''
<?xml version="1.0" encoding="UTF-8" ?>
<wsdl:definitions targetNamespace="http://tips.cf"
'''
# `^`를 앞에 붙이면 실제 텍스트에서 첫 번째 줄에 위치하는지의 사실 여부를 확인할 수 있다.
# `^\s*`는 문자열 시작이면서 바로 뒤에 공백 문자가 없거나 하나 이상 있는 경우와 일치한다.
# 즉, XML 문서가 시작하기 전에 나올 수 있는 빈칸, 탭, 줄바꿈들을 처리한다.
regex = r'^\s*<\?xml.*\?>'
result = re.finditer(regex, text)
for res in result:
    print("{0}, {1}".format(res.group(), res.span()))
# 결과
'''
<?xml version="1.0" encoding="UTF-8" ?>, (0, 40)
'''
# case 6의 text를 넣고 동작했을 때는 탐색된 것이 하나도 없는것을 볼 수 있다.

# case 8
text = '</html>'
# 문자 집합은 대소문자를 어떻게 조합해도 일치하도록 하였고 `\s*$`는 공백 문자와 그 뒤에 오는 문자열 마지막을 찾는다.
regex = r'</[Hh][Tt][Mm][Ll]>\s*$'
result = re.finditer(regex, text)
for res in result:
    print("{0}, {1}".format(res.group(), res.span()))
# 결과
'''
</html>, (0, 7)
'''

# case 9
text = '''
<script>
function doSpellCheck(form, field) {
	// Make sure not empty
	if (field.value == '') {
		return false;
	}
	// Init
	var windowName='spellWindow';
	var spellCheckURL='spell.cfm?formname=comment&fieldname='+field.name;

	// Done
	return false;
}
</script>
'''
# `(?m)`은 다중행(multiline)을 지원한다.
# 다중행 모드로 변경하면 정규 표현식 엔진이 줄바꿈 문자를 문자열 구분자로 강제로 인식한다.
# `(?m)`은 항산 패턴 제일 앞에 두어야 한다.
# 코드 블록 내의 모든 자바스크립트 주석을 찾는 예제
regex = r'(?m)^\s*\/\/.*$'
result = re.finditer(regex, text)
for res in result:
    print("{0}, {1}".format(res.group(), res.span()))
# 결과
'''
        // Make sure not empty, (47, 70)
        // Init, (116, 124)

        // Done, (227, 236)
'''

# case 10
text = 're, regex, regular expression'
# `\B`는 `\b`와 반대의 의미를 가지는 메타 문자로
# `\Bre\B`인 경우 `r`의 왼쪽과 `e`의 오른쪽이 `\w`로 둘러쌓인 경우만 탐색하여 출력해주는 정규표현식이 된다.
regex = r'\Bre\B'
result = re.finditer(regex, text)
for res in result:
    print(res.group(), res.span())
# 결과
'''
re (22, 24)
'''
# `re`의 양쪽 모두에 문자가 붙어있는 마지막 `re`만 탐색된 것을 볼 수 있다.
