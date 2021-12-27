# 딕셔너리
# 키와 값의 한 쌍을 요소로 갖는 자료형
# 딕셔너리 = {키1:값1, 키2:값2...}

#특징
# 순서가 없다. 따라서, 인덱스로 접근 불가
# 중괄호 {} 사용
# key를 통해서만 접근
# key는 숫자, 문자 다 가능
# key:value 한 쌍을 item이라고 한다.
# 쉼표(,)로 item 구분

# 딕셔너리 생성 : {} or dict()
students = {1:'최선', 2:'홍길동', 3:'강감찬'}

print(students)
print(type(students))
prof = {} # dictionary 만듬
prof[1] = '이순신'  #[]<- key  에 value를 지정
prof[2] = '홍길동'
print(prof)
print(type(prof))
print(students[1]) # 키1에 저장되어있는 value 최선을 출력함


member = {'name':'홍길동', 'phone':'010-1234-1234'}
print(member)
print(member['name'])
print(member['phone'])

member1 = {'name' : '홍길동', 'phone':'010-1234-1234','name':'이순신'}
# member1['name' = 이순신]
print(member1)

naver = {'name':'naver',
         'url':'www.naver.com',
         'id':'djjeon'}
google = {'name':'google',
          'url':'www.google.com',
          'id':'djjeon'}

daum = {'name':'daum',
        'url':'www.daum.net',
        'id':'djjeon'}

print(naver['name'])
naver['id']='idValue'
print(naver['id'])

# keys(), values(), items()
print(naver.keys())
print(naver.values())
print(naver.items())

for key in naver.keys():
    print(key)

print(type(naver.keys()))
to_list = list(naver.keys())
print(to_list)

for value in naver.values():
    print(value)

for item in naver.items():
    print(item)


# key로 value 찾기
print(naver['name'])
print(naver.get('name'))

# print(naver['passwd'])
print(naver.get('passwd', '없음')) # get함수를 활용해 찾는 키가 없다면 없음으로 출력할 수 있다.
key = 'passwd'
if naver.get(key) is None:
    print(key + '에 대한 값이 없습니다.')

# print(key in naver)
# print(key not in naver)

if key not in naver:
    print(key + '에 대한 값이 없습니다.')

