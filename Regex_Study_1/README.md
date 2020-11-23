# Regex(Regular Expression)

## Regex란

> Regex는 정규 표현식 Regular Expression의 약자로 텍스트를 찾고 조작하는데 쓰는 문자열이다. 문자열의 검색과 치환에 있어서 간단하고 강력한 모습을 보인다.

## 들어가기 전

- `Regex`를 `Python`으로 공부 할 것이다.

- `Python`은 `re`라는 모듈을 `import`하면 `Regex`를 사용할 수 있다.

## 실습

### 일반 문자열

- 다음은 `my`라는 단어를 `text`에서 찾는 코드이다.

```python
import re

text = "Hello, my name is Ben. Please visit my website at http://www.forta.com/."

# case 1
# "my"와 일치하는 것을 찾는다.
# re.compile 안에 정규식을 작성하면 된다.
regex = re.compile("my")
# findall(text)는 text 안의 글자들 중 regex 정규표현을
# 만족하는 모든 문자열을 찾는 함수이다(리스트 반환).
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 =  ['my', 'my']

# case 2
regex = re.compile("Ben")
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 =  ['Ben']
```

- 위와 같이 일반 문자열도 정규표현식이 될 수 있다.

### 모든 문자 찾기

- 마침표 `.`는 어떠한 문자나 알파벳, 심지어 문장 부호로 쓰인 `.` 자체와도 일치한다.

```python
import re

# case 1
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
# "sales"로 시작하고 "sales" 바로 뒤에 아무 문자가 하나 더 붙는 파일명을 모두 찾는다.
regex = re.compile("sales.")
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 = ['sales1', 'sales2', 'sales3']

# case 2
# '.'는 어떠한 문자나 알파벳, 숫자, 문장 부호로 쓰인 '.' 자체와도 일치한다.
text = "sales.xls sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
regex = re.compile("sales.")
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 = ['sales.', 'sales1', 'sales2', 'sales3']
```

- 위의 `case 1`에서의 정규표현식 `sales.`는 문자 `sales` + (아무 문자 or `.`)이면 모두 만족한다.

- 그러므로 `case 2`에서 추가된 `sales.` 역시 정규표현식을 만족한다.

- 그렇다면 정말 `.`를 찾고 싶을 때는 어떻게 해야할까?

### 특수 문자

- 모든 문자의 의미인 `.`이 아닌 마침표의 의미 `.`를 표현하는 법을 알아보자.

```python
import re

# case 1
# 이번에는 뒤에 어떤 숫자가 오든지 관계없이 "na"나 "sa"와 관련된 파일을 찾아보자.
text = "sales.xls sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
regex = re.compile(".a..")
answer = regex.findall(text)
print("case 1 =", answer)
# case 1 = ['sale', 'sale', 'sale', 'sale', ' apa', 'na1.', 'na2.', 'sa1.']
```

- `case 1`은 `na` 혹은 `sa`로 시작하고 바로 뒤에 숫자, 그리고 마침표가 들어가는 생각을 하며 만든 정규표현식이다.

- 하지만 마침표는 모든 문자, 숫자 그리고 마침표를 표현하는 것이기 때문에 생각과는 다르게 뽑아낸다.

- 이러한 문제를 해결하기 위해 메타 문자 `\`를 붙여 주면 된다.

- 정규표현식에서 역슬래시 `\`는 주로 특별한 의미를 지니는 문자의 맨 앞에 표시한다.

- `\.`는 마침표 문자 자체와 일치한다는 의미이다.

```python
import re

# case 2
text = "sales.xls sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
regex = re.compile(".a.\.")  # 진짜 마침표 '.'를 찾기 위해 역슬래시를 붙여준다.
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 = ['na1.', 'na2.', 'sa1.']

# case 3
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls sa3.doc na4.txt"
regex = re.compile(".a.\.xls")  # 패턴에 "xls"를 추가하여 다른 확장자가 포함되는 것을 방지할 수 있다.
answer = regex.findall(text)
print("case 3 =", answer)
# case 3 = ['na1.xls', 'na2.xls', 'sa1.xls']
```

- 하지만 우리가 배운 특수문자 `.`과 `\.` 만으로는 `na`, `sa`만 찾을 수가 없다. 예를 들어 `text` 안에 `ca`가 포함되어 있는 경우 위의 `case 2`, `case 3`은 `ca`를 정규표현식에서 거르지 못하고 리스트에 담을 것이다.

```python
import re

# case 4
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls ca1.xls"
regex = re.compile(".a.\.xls")
answer = regex.findall(text)
print("case 4 =", answer)
# case 4 = ['na1.xls', 'na2.xls', 'sa1.xls', 'ca1.xls']
# "ca1.xls"가 포함되어 있는 것을 볼 수 있다.
```

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

- 이해를 돕기 위해 하나의 예제를 더 보자.

```python
import re

# case 2
text = "The phrase 'regular expression' is often abbreviated as RegEx or regex."
regex = re.compile("[Rr]eg[Ee]x")
answer = regex.findall(text)
print("case 2 =", answer)
# case 2 = ['RegEx', 'regex']
# "RegEx"와 "regex"는 구별할 수 있으나 "REGEX" 같은 다른 케이스들은 구별하지 못한다.
# 대소문자를 구별하지 않고 모든 문자를 찾아도 된다면 이렇게 할 필요 없음!(당연)
```

- `na`, `sa` 뒤에 숫자를 오게 하고 싶다면 `[ns]a.\.xls`로는 만족할 수 없다(마침표가 문자일수도, 마침표 그 자체일수도 있다).

- 그러므로 문자 집합을 하나 더 만들어준다.

```python
import re

# case 3
# 패턴 "[ns]a.\.xls" 같은 경우는 "sam.xls" 같은 파일도 일치하기 때문에 패턴을 바꿔줘야한다.
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls ca1.xls sam.xls"
regex = re.compile("[ns]a[0123456789]\.xls")
answer = regex.findall(text)
print("case 3 =", answer)
# case 3 = ['na1.xls', 'na2.xls', 'sa1.xls']
# "sam.xls"가 포함되지 않은 것을 볼 수 있다.
```

- 문자 집합의 범위 지정을 위해 `-`를 사용할 수 있다. 단, 조건이 있는데 범위 지정 시 더 큰 값이 앞에 나오면 안된다.

- 그리고 `A-z`는 사용 안하는 것이 좋다. `Z`와 `a`사이의 아스키 코드 값들이 포함되기 때문이다(`[`, `^` 등등).

```python
import re

# case 4
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls ca1.xls sam.xls"
# '-'로 "0123456789"를 다 쓰는게 아닌 범위를 짧게 지정할 수 있다.
regex = re.compile("[ns]a[0-9]\.xls")
answer = regex.findall(text)
print("case 4 =", answer)
# case 4 = ['na1.xls', 'na2.xls', 'sa1.xls']
# case 3의 결과 값과 똑같다.
```

- `[]`과 `-`를 이용해 `css` 파일에서의 색 범위를 지정해보자.

```python
import re

# case 5
text = """
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
"""
regex = re.compile(
    "#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]")
answer = regex.findall(text)
print("case 5 =", answer)
# case 5 = ['#fefbd8', '#0000ff', '#d0f4e6', '#f08970']
# '#'이 일치하고 뒤의 6개 문자가 "0123456789ABCDEFabcdef" 중 하나여야 한다.
```

- 캐럿(`^`)은 제외할 문자 집합을 지정해주는 문자이다.

- 캐럿 문자는 캐럿 문자 바로 뒤에 있는 문자나 범위뿐만 아니라 집합 안에 있는 문자나 범위를 모두 제외한다.

```python
import re

# case 6
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls ca1.xls sam.xls"
regex = re.compile("[ns]a[^0-9]\.xls")
answer = regex.findall(text)
print("case 6 =", answer)
# case 6 = ['sam.xls']
# 'a'의 앞에 'n'이나 's'가 있어야 하고, 'a'의 뒤에는 숫자가 들어오면 안되며
# 그 뒤는 ".xls"가 있어야 하는 조건
```

## 정리

&nbsp;정규표현식의 의미와 특징을 알았으며 모든 문자, 숫자, 마침표 그 자체를 표현하는 `.`, 마침표를 의미하는 `\.`을 공부하였고 문자 집합을 표현해주는 대괄호 `[]`와 범위 지정을 짧게 만들어주는 하이픈 `-`, 그리고 제외시켜주는 문자 캐럿 `^`에 대해 공부하였다.
