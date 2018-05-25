# packing은 tuple로만 가능

t = 10, 20, 30, 'python'
print(t)
print(type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# 오류: 패킹되어 있는 객체가 더 많은 경우
# a, b, c = t
# 오류: 패킹되어 있는 객체가 더 적은 경우
# a, b, c, d, e = t

# unpackinf extended
t = (1, 2, 3, 4, 5)
a, *b = t
print(a)
print(b)

*a, b = t
print(a)
print(b)

a, b, *c = t
print(a)
print(b)
print(c)

a, *b, c = t
print(a)
print(b)
print(c)


