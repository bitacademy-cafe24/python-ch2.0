# 튜플 생성

t = ()          # 공튜플
t = (1,)        # 항목이 하나일 때는 반드시 코마
t = (1, 2, 3)
print(t)
print(type(t))

#
# 시쿼스형 지원 연산
#

# 인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

# 슬라이싱
print(t[1:3])
print(t[:])

# 반복
t2 = t * 2
print(t2)

# 연결
t3 = t + (3, 4, 5)
print(t3)

# 길이
print(len(t3))

# 확인
print(5 in t3)

# 튜플은 변경 불가는(immutable)한 스퀜스형이다.
# t = ('apple', 'banana', 10, 20)
# t[2] = 90
# print(t)

# 튜플을 이용해서 좌우변에 여러개의 값을 치환(대입)할 수있다
x, y, z = 10, 20, 30
print(x, y, z)

# 튜플을 이용해서 값을 바꾸는 작업
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# 튜플은 객체 함수가 많지가 않다: immutable 이기 때문에...
t = (20, 30, 10, 20)
print(t.index(20))
print(t.count(20))

# 변환
t = (1, 2, 3, 3)
print(t)

s = set(t)
print(s, type(s))

l = list(t)
print(l, type(l))

t = tuple(l)
print(t, type(t))


