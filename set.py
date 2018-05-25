# set 생성

s = {1, 2, 3}
print(s, type(s))

# 기본연산
print(len(s))
print(2 in s)
print(2 not in s)

# list의 중복되는 항목을 제거할 때 유용
nums = [1, 2, 3, 2, 2, 4, 5, 5, 6]
s = set(nums)
print(s)

nums2 = list(s)
print(nums2)

# 객체함수(메서드)
s.add(7)
print(s)

s.add(2)
print(s)

s.discard(2)
print(s)

s.remove(3)
print(s)

s.update({2, 3, 4})
print(s)

s.clear()
print(s)

# 수학 집합 관련 객체 함수

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)

print(s1.issuperset(s4))
print(s5.issuperset(s1))
print(s2.issubset(s3))