print("#사전 생생 ------------------------")
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

print("#인덱싱 대신 키로 접근해야 한다. --")
print(d['basketball'])

# 연결(+) 지원하지 않는다.
# print(d + {"valleyball": 6})

print("#변경가능 하기 때문에 수정 가능 --")
d['valleyball'] = 6
print(d)

# 반복(*) 지원하지 않는다.
# print(d * 2)

print("#len() --------")
print(len(d))

print("in, not in은 키값으로만 가능 --------")
print('soccer' in d)
print('valleyball' in d)

print("다양한 dict 생성 방법 --------")
# literal를 사용하는 방법
d = {}
print(d)

# dict() 함수를 사용하는 방법
d = dict()
print(d)

# dict() 함수를 사용하는 방법
# keyword argument를 사용하는 방법
d = dict(one=1, two=2)
print(d)

# dict() 함수를 사용하는 방법
# tuple list를 사용하는 방법
d = dict([('one', 1), ('two', 2)])
print(d)

# dict() 함수를 사용하는 방법
# zip 객체를 사용하는 방법
keys = ('one', 'two', 'three')
value = (1, 2, 3)
d = dict(zip(keys, value))
print(d)

print("다양한 dict의 key 타입 --------")
d = {}
print(d)

d[True] = 'true'
d[10] = '10'
d['twenty'] = '20'
d[(1, 2, 3)] = '6'

# 오류: list는 mutable 이기 때문에 key값으로 사용할 수 없다.
# d[[1, 2, 3]] = '6'
# keynums = [1, 2, 3]
# d[keynums] = '6'
# keynums[0] = 10

print(d)

print("keys() 객체함수--------")
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))


print("values() 객체함수--------")
values = d.values();
print(values)
print(type(values))

print("items() 객체함수--------")
items = d.items()
print(items)

print("copy() 객체함수--------")
phone = {'둘리': '0000-0000-0000',
         '도우넛': '1111-1111-1111',
         '또치': '2222-2222-2222'}
p = phone
print(phone)
print(p)
phone['마이콜'] = '3333-3333-3333'
print(phone)
print(p)

phone = {'둘리': '0000-0000-0000',
         '도우넛': '1111-1111-1111',
         '또치': '2222-2222-2222'}
p = phone.copy()
print(phone)
print(p)
phone['마이콜'] = '3333-3333-3333'
print(phone)
print(p)

print("get(), setdefault(), pop(), popitem() 객체함수--------")
# print(phone['둘리'])
print(phone.get('둘리'))

# 오류:
# get을 쓰는 이유는 해당 키값이 없는 경우 None을 받기 위해서
# name = phone['길동']
# print(name)
print(phone.get('길동', '0000-0000-0000'))

# cf : 차이점은 실제로 사전에 저장된다.
print(phone)
print(phone.setdefault('길동', '0000-0000-0000'))
print(phone)

# 삭제와 동시에 값 가져오기
name = phone.pop('둘리')
print(name)
print(phone)

# 튜플로 가져오기
item = phone.popitem()
print(item)
print(phone)

print("update(), clear() 객체함수--------")
phone.update({"도우넛": "010-1111-1111",
              "또치": "010-2222-2222"})
print(phone)

phone.clear()
print(phone)

print("dict 조회--------")
d = {'c': 3, 'a': 1, 'b': 2}

for key in d:
    print(key, end=' ')
else:
    print('')

for key in d:
    print(key + ":" + str(d[key]), end=' ')
else:
    print('')

for key in d.keys():
    print(key + ":" + str(d[key]), end=' ')
else:
    print('')

for key, value in d.items():
    print('{0}:{1}'.format(key, value), end=' ')
else:
    print('')




