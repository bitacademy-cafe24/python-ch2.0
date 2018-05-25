# 복소수는 실수부 + 허수부
# 허수부는 j또는 J를 숫자뒤에 붙힌다.

a = 4 + 5j
print(type(a))
print(isinstance(a, complex))

# 복소수는 연산
b = 7 - 2j
print(a + b)
print(b.real, b.imag)

# complex() 함수
p = 2.5
q = 3
print(complex(p, q))

# 켤레 복소수
print(a.conjugate())
