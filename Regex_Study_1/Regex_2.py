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

# case 3
# 이번에는 뒤에 어떤 숫자가 오든지 관계없이 "na"나 "sa"와 관련된 파일을 찾아보자.
text = "sales.xls sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
regex = re.compile(".a..")
answer = regex.findall(text)
print("case 3 =", answer)
# case 3 = ['sale', 'sale', 'sale', 'sale', ' apa', 'na1.', 'na2.', 'sa1.']
# 마침표가 case 2에서 말한 것과 같이 어떠한 문자, 알파벳, 숫자, 문장 부호로 쓰인 '.' 자체와도 일치하기 때문에 예상하지 못한 값들도 포함되어 있다

# case 4
text = "sales.xls sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls"
regex = re.compile(".a.\.")  # 진짜 마침표 '.'를 찾기 위해 역슬래시를 붙여준다.
answer = regex.findall(text)
print("case 4 =", answer)
# case 4 = ['na1.', 'na2.', 'sa1.']
# 잘 나온다.

# case 5
text = "sales1.xls orders3.xls sales2.xls sales3.xls apac1.xls europe2.xls na1.xls na2.xls sa1.xls sa3.doc na4.txt"
regex = re.compile(".a.\.xls")  # 패턴에 "xls"를 추가하여 다른 확장자가 포함되는 것을 방지할 수 있다.
answer = regex.findall(text)
print("case 5 =", answer)
# case 5 = ['na1.xls', 'na2.xls', 'sa1.xls']

# 정규 표현식에서 역슬래시는 주로 특별한 의미를 지니는 문자의 맨 앞에 표시한다.
