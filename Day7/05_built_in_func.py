# 내장함수(built-in functions)
# 파이선에 이미 만들어져 내장되어 있는 함수를
# 별도의 모듈을 import하지 않고 사용가능

# 함수의 형식과 목적에 따라 호출해서 사용
# print(), input(), id(), type(), sum(), int(), str(), list(), len()
# 특정 객체를 통해 사용가능한 함수(method)
# 리스트.index(), append(), insert(), count(), remove(),...
# 문자열, index(), find(), sort(), reverse(),...




# 참고사이트 : https://docs.python.org/ko/3/library/functions.html

# abs() : 절대값 계산
print('abs()---')
print(abs(-10.5))

# all() : 모든 요소가 참이면 True
# False : 0, True : 0이 아닌 값
# iterable (반복 가능한 자료형) : 리스트, 튜플, 딕셔너리, 집합
# for 반복문을 이용해서
print('all()------------')
print(all([1,2,3]))
print(all([0,2,3]))
print(all([0,0,0]))


# any() : 하나라도 참이면 True
print('any()------------')
print(any([1,2,3]))
print(any([0,2,3]))
print(any([0,0,0]))
print(any([0, "", 0])) # 빈 문자열 "" : False
print(any([0, "", []])) # 빈 리스트 [] : False


# bool() : 부울 값으로 변환 True, False
print('bool()---------')
print(bool(''))
print(bool([]))
print(bool(1))
print(bool(10))
print(bool(-1))
print(bool({}))
print(bool(None))
print(bool(0))

# chr() : 아스키코드(ASCII) 값에 해당하는 문자 반환
print('chr()------')
print(chr(95))
print(chr(97))
print(chr(65))
print(chr(55))
print(chr(48))

# ord() : 문자에 대한 ASCII 코드 값 반환
print('ord()--------')
print(ord('A'))
print(ord(' '))
print(ord('\n'))
print(ord('\t'))
print(ord('0'))


# divmod(a,b) : a를 b로 나눈 몫과 나머지 반환
print('div()-------')
print(divmod(10,3))  # 반환 값은 튜플형태(몫, 나머지)

# enumerate() : 시퀀스를 각 값에 인덱스값을 포함해서 enumerate 객체로 반환
# 시퀀스 : range(), 문자열, 리스트, 튜플
print('enumerate()-----------')
print(enumerate('hello'))
for i, c in enumerate('hello'):
    print(i, c)
for i, season in enumerate(['봄', '여름', '가을', '겨울']):
    print(i, season)


# eval(표현식) : 표현식의 연산 결과 반환
print('eval()--------')
print(eval('1+2')) # 3
print(type(eval('10'))) # integer
x = 1
print(eval('x+1')) # 2


# filter(function, iterable) : iterable 자료의 요소들을 function로 거르다(걸러내다)
print('filter()-------------')

def positive(x):
    return x > 0
print(filter(positive, [0,1,-1,10,-3,5]))
# positive 함수로 걸러낸 객체 반환
print(list(filter(positive, [0,1,-1,10,-3,5])))

def even(x):
    if x % 2 == 0:
        return x

print(list(filter(even, [1,2,3,4,5,6,7,8])))

# help() : 도움말
help(print)
help(filter)
help(input)
help(max)

# pow(x, y) : x의 y     * power의 약어
print(pow(2,10))

# range([start], stop[,step]) : 지정한 범위의 값을 반복 가능한 객체로 반환
print(range(0,5))
print(list(range(0,5)))

# map() 함수 : 리스트나, 튜플, 문자열 등 반복가능한 구조의 요소별로 지정된 함수를 적용하여 처리
# 원본은 변경하지 않고 처리 list, tuple형태로 반환
# list(map(함수, 리스트))
# tuple(map(함수, 리스트))


# 문제. 실수형 요소를 갖는 리스트를 정수형 요소리스트로 변환
# map을 이용하는 경우
# for를 이용하는 경우
number1 = [3.5, 3.4, 2.0, 4.6]

# map을 이용하는 경우
num_list1 = list(map(lambda num : int(num), number1))
print(num_list1)

# for를 이용하는 경우
num_list2 = []
for i in range(len(number1)):
    num_list2.append(int(number1[i]))
print(num_list2)



# zip(*iterable) : iterable에서 동일한 인덱스 요소를 추출하여 묶어서 반환
# 서로 다른형태의 자료구조도 묶을수 있다.
# 반환 형태는 튜플
print(zip([1,2,3],[4,5,6]))
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))

keys = ['apple','melon','banana']
vals = [250, 300, 400]

print(list(zip(keys, vals)))
print(dict(zip(keys, vals)))
