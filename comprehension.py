# list comprehension
results = []
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = num * num
    results.append(result)

print(results)

results = [num*num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트 만들기
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = [s for s in strings if len(s) <= 2]
print(strings)

# 1~100 사이의 수중에 짝수 리스트 만들기
evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)

# set comprehension
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
strings = {s for s in strings if len(s) <= 2}
print(strings)

# 문자열 리스트에서 문자열 길이를 set으로 저장해 보자
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = {len(s) for s in strings}
print(lens)

# dict comprehension
# 문자열 리스트에서 문자열과 문자열 길이를 함께 dict로 저장 해 보자
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}
print(dicts)

#
# 369 게임
for t in [(n, '짝'*(str(n).count('3')+str(n).count('6')+str(n).count('9')))
          for n in range(1, 1000)
          if('3' in str(n) or '6' in str(n) or '9' in str(n))]:
    print('%s: %s' % t)




