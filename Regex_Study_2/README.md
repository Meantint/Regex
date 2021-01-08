# Regex(Regular Expression)

## 메타 문자란

> 메타 문자는 정규 표현식에서 문자 그대로의 의미가 아닌 특별한 의미를 갖고 있는 문자다.

## 메타 문자 실습

### 메타 문자 `[`, `]`

- 대괄호는 메타 문자로 그냥 사용하면 문자 그대로의 대괄호를 나타낼 수 없다.

```python
import re

# case 1
text = 'if (myArray[0] == 0)'
# 대괄호는 메타 문자이기 때문에 그냥 '[', ']'를 쓰면 메타문자로 인식해 아무것도 찾지 못한다.
regex = r'myArray[0]'
result = re.dfindall(regex, text)
print('\n'.join(result))
# 결과
'''

'''

# case 2
text = 'if (myArray[0] == 0)'
regex = r'myArray\[0\]'  # 역슬래쉬 '\'를 붙여서 문자 자체를 의미하도록 만든다.
result = re.finall(regex, text)
print('\n'.join(result))
# 결과
'''
myArray[0]
'''
# 역슬래쉬를 붙여 문자 그대로의 대괄호로서 의미를 가지므로 문자를 인식할 수 있게 되었다.
```

### 메타 문자 `\`

-역슬래시 `\`는 메타 문자들을 이스케이프(Escape) 하는 데 사용된다. 문자들을 메타 문자가 아닌 본래 문자의 뜻으로 읽히게 만들어주는 메타 문자이다.

```python
import re

# case 1
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
# `\\`는 문자 그대로의 `\`를 의미한다.
```

### 공백 문자

- 공백 문자도 메타 문자이다.

```python
import re

# case 1
text = '''
"101", "Ben", "Forta"
"102", "Jim", "James"

"103", "Roberta", "Robertson"
"104", "Bob", "Bobson"
'''
regex = r'\n\n'
# 유닉스는 /r/n, 리눅스는 /n을 하면 된다고 한다.
# 필자는 WSL2를 이용한 리눅스 체제의 VSCode를 사용하고 있어서 \n로 해야 되는 것 같다.
result = re.findall(regex, text)
print('\n'.join(result))
# 결과
'''



'''
# 두 칸 공백이 나와야 할 것 같은데 세 칸 공백이 결과 값으로 나오는 이유는
# 우리가 출력하려는 문자 자체가 공백이기 때문에 첫째 줄에서 공백을 읽어서 둘째 줄로 가고
# 둘째 줄에서 두 번째 공백을 읽어 세 번째 줄로 간후 종료되기 떄문에 세번째 줄까지가 결과값으로 나타나는 것이다.
```

### 문자 클래스

- 자주 쓰는 문자 집합들을 특수한 메타 문자로 대신하기도 하는데 이러한 메타 문자들을 문자 클래스라고 한다.

- 메타 문자 `\d`는 숫자 하나(`[0-9]`)와 같다.

- 반대로 메타 문자 `\D`는 숫자를 제외한 문자 하나(`[^0-9]`)와 같다.

```python
import re

# case 1
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
# 숫자로 범위를 지정했을 때와 똑같은 결과 값임을 알 수 있다.
```

- 메타 문자 `\w`는 밑줄과 대소문자를 포함하는 모든 영숫자(`[a-zA-Z0-9_]`)와 같다.

- 역시나 반대로 메타 문자 `\W`는 `\w`가 아닌 모든 문자(`[^a-zA-Z0-9_]`)와 같다.

```python
import re

# case 2
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
# 짝수 번째 문자는 무조건 숫자, 홀수 번째 문자는 대소문자와 밑줄을 포함한 모든 영숫자 중 하나여야 한다.
```

- 이 외에도 `\s`, `\S` 등이 있다.

- 메타 문자 `\s`는 모든 공백 문자(`[\f\n\r\t\v]`)와 같다.

- 반대로 메타 문자 `\S`는 공백 문자가 아닌 모든 문자(`[^\f\n\r\t\v]`)와 같다.

### 문자 집합

- 문자 집합을 사용하면 특정 문자들과 문자 범위를 일치시킬 수 있다.

- 대괄호 `[]`를 통해 문자 집합을 표현해준다.

- 대괄호 안에 있는 문자는 모두 집합의 구성원이 되며, 집합에 속한 가운데 하나가 일치한다.

- 집합에 속한 문자가 모두 일치할 필요는 없다(AND가 아니라 OR의 개념).

```python
import re

# case 1
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls ca1.xls"
regex = re.compile("[ns]a.\.xls")
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 = ['na1.xls', 'na2.xls', 'sa1.xls']
# 'a'의 앞에 'n'과 's'가 들어간 파일만 출력된 것을 볼 수 있다.
# 참고 : 실제 상황에서는 이것도 정답이 아니다. ex) usa1.xls 같은 경우를 제외시킬 수 없음. 나중에 배움
```

## 반복 문자 찾기

### 메타 문자 `+`

- 메타 문자 `\+`는 하나 이상의 문자를 찾아준다.

```python
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
```

- 이메일 형식을 위의 정규표현식으로 완벽하게 나타낼 수는 없다. `case 2`를 보자.

```python
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
```

- 이를 해결하기 위해서는 `\w`가 아닌 `[\w.]`으로 바꿔주어 `.`까지 포함하는 하나의 세트로 찾을 수 있게 만들어준다.

```python
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
```
