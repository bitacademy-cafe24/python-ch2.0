# 한 줄 문자열 정의
s = ''
str1 = 'hello world'
str2 = "hello world"
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 여러줄 문자열 정의
str3 = """ABC
DEF
가나다라마
바사아자차카"""
print(str3)

# 여러줄 주석:
# 여러줄 문자열 사용
"""
여러줄 주석:
여러줄 문자열 사용
"""

# escape
print("Hello\nWorld\nI Say \"Hello World\"")
print('Hello\nWorld\nI Say "Hello World"')

# 문자열 연산
str1 = "First String"
str2 = "Second String"

# 인덱싱
print(str1[0], str1[2], str1[4])

# 슬라이싱
str3 = str2[2:5]
print(str3)
print(str2[2:])

# 연결(+), + 생략 가능
print(str1 + " " + str2)
str3 = "str1" " " "str2"
print(str3)

#  문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = "길동"
age = 40
# print(name + age)

# 반복(*)
print(str1 * 3)

# len() 함수
print(len(str2))

# in, not in 연산
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다(immutable)
# str1[0] = "f"

# 서식(formating) - format() 함수
print("name:" + name + ", age:" + format(age, "d"))
print("name:" + format(name, "s") + ", age:" + format(age, "d"))
# C 스타일
# printf( "name:%s, age:%d", name, age)

# 서식(formating) - 튜플을 이용한 포매팅
f = "name:%s, age:%d"
print(f)
print(f % ("둘리", 13))
print(f % ("또치", 10))

# 서식(formating) - 딕션너리을 이용한 포매팅
f = "name:%(name)s, age:%(age)d"
print(f % {"name": "둘리", "age": 13})
print(f % {"name": "또치", "age": 10})

# 대소문자 관련 객체함수
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색 관련 객체함수
s = "I Like Python, I Like Java Also"
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("JavaScript"))
print(s.rfind("Like"))

# 발견하지 못하면 예외가 발생한다.
# print(s.index("JavaScript"))
print(s.rindex("Like"))
print(s.startswith("I Like"))
print(s.startswith("Like", 2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 26))

# 편집과 치환
s = '    spam and ham    '
print("----" + s.strip() + "-------")
print("----" + s.rstrip() + "-------")
print("----" + s.lstrip() + "-------")

s = '<><abc><><defg><><>'
print(s.strip("<>"))

s = "Hello Java"
print(s.replace("Java", "Python"))

# 정렬
s = "King and Queen"
print("--" + s.center(60) + "--")
print(s.center(60, "-"))
print(s.ljust(60, "-"))
print(s.rjust(60, "-"))

# 분리와 결합
s = "Spam and Ham"
t = s.split()
print(t)

t = s.split(" and ")
print(t)

s2 = ":".join(t)
print(s2)

s3 = "one:two:three:four:five"
print(s3.split(":", 2))
print(s3.rsplit(":", 2))

lines = """1st line
2nd line
3rd line
4th line
"""
print(lines.split("\n"))
print(lines.splitlines())

# 판별
print("1234".isdigit())
print("abcd".isalpha())

print("1234".isalpha())
print("abcd".isdigit())

print("abcd".islower())
print("ABCD".isupper())

print(" ".isspace())
print("".isspace())
print("\r\n".isspace())
print("\t".isspace())

# '0' 채우기
print("20".zfill(5))
print("1234".zfill(5))

# 서식(포매팅) 객체함수
f = "name:{}, age:{}"
print(f.format("둘리", 13))

print("name:{0}, age:{1}".format("둘리", 13))
print("name:{1}, age:{0}".format(13, "둘리"))
print("{:3}의 제곱근은 {:.7}".format(2, 2**0.5))

f = "name:{name}, age:{age}"
print(f.format_map({"age": 13, "name": "둘리"}))
















