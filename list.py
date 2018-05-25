# 리스트 생성

l = []
l = [1, 2, 'python']

# indexing
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# slicing
print(l[1:3])
print(l[:])
print(l[2:])
print(l[len(l)-1::-1])

# 반복(*)
l2 = l * 2
print(l2)

# 연결(+)
l3 = l + [3, 4, 5]
print(l3)

# 길이
print(len(l3))

# 확인
print(5 in l3)

# 삭제
del l3[0]
print(l3)

# 변경가능한 시퀀스다(mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이스를 통한 치환
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

a[2:3] = [30]
print(a)

# 슬라이스를 통한 삭제
a = [1, 12, 123, 1234]

a[1:2] = []
print(a)

a[0:] = []
print(a)

# 슬라이스를 통한 삽입
a = [1, 12, 123, 1234]

# 중간 삽입
a[1:1] = ['a']
print(a)

# 마지막 삽입
a[5:] = [12345]
print(a)

# 처음에 삽입
a[:0] = [0]
print(a)

# 여러개 삽입
a[2:2] = [-12, -1, 0]
print(a)

#
# 객체함수(메서드)
#
a = [1, 3, 4]

# 중간삽입
a.insert(1, 2)
print(a)

# 뒤에 삽입
a.append(5)
print(a)

# 앞에 삽입
a.insert(0, 0)
print(a)

# reverse
a.reverse()
print(a)

# 제거(값으로 삭제)
a.remove(3)
print(a)

# 확장
a.extend([-1, -2, -3])
print(a)

# 스택으로 사용하기
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

# 큐로 사용하기
q = [1, 2]

q.append(3)
q.append(4)
q.append(5)

print(q)
print(q.pop(0))
print(q.pop(0))
print(q)

# sort(): 객체함수 : 내장된 소팅 알고리즘에 따라 정렬
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str)
print(l)

l.sort(key=int)
print(l)

# 내장(전역) 함수 : sorted
l = [19, 46, 37, 28, 91, 55, 64]
l2 = sorted(l)
print(l2)

l2 = sorted(l, reverse=True)
print(l2)

l = [19, 46, 37, 28, 91, 55, 64]
def f(i):
    return i % 10

l2 = sorted(l, key=f, reverse=True)
print(l2)


