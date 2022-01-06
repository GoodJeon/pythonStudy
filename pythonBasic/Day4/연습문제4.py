# 1. 다음과 같이 이메일주소를 입력받아 이메일 형식인지 아닌지를 판별하여 출력하기

inp = input('이메일 입력 : ')
# inp에 이메일 주소를 받는다.
letter, digit, space, alpha, dot, etc = 0, 0, 0, 0, 0, 0
# 순서대로 문자, 숫자, 공백, @, ., 그 외 특수기호를 나타낸다.

for i in inp:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    elif i == '@':
        alpha += 1
    elif i == '.':
        dot += 1
    else:
        etc += 1

# 이메일 형식이 아닌경우는
# 1  @ 없는경우 :  alpha == 0
# 2  . 없는경우 :  dot == 0
# 3  @이 .의 오른쪽에 위치한 경우 :  inp.find('@') > inp.find('.')
# 4  @과 .의 사이에 문자가 없는 경우 :  inp.find('@') + 1 == inp.find('.')
# 5  @앞에 문자가 없는 경우 :  inp[0] == '@'
# 6  .뒤에 문자가 없는 경우 :  inp[-1] == '.'
# 7  @가 두 번 이상 있는 경우 :  alpha > 1
# 8  .가 두 번 이상 있는 경우 :  dot > 1
# 9  공백이 있는 경우 :  space > 0
# 10  .뒤에 숫자나 특수문자가 있는 경우
# 11  @과 . 사이에 숫자나 특수문자가 있는 경우
# 12  @과. 외에 잡다한 특수문자가 들어갔을 경우 :  etc > 0
# ======== 이정도로 정리해 볼 수 있다.

# 그 반대의 경우에 제대로된 이메일이 나온다는 것인데,
# 그렇다면 제대로된 이메일은 이런 조건이 필요하다.
# alpha == 1      : '@'가 1개만 존재해야한다.
# dot == 1    : '.'가 1개만 존재해야한다.
# etc == 0    : 기타 특수문자가 없어야한다.
# space == 0     : 공백이 없어야한다.
# inp.find('@') < inp.find('.')     : '.'이 무조건 '@' 오른쪽에 위치해야한다.
# inp[0] != '@'      : '@'가 가장 왼쪽에 위치하면 안된다.
# inp[-1] != '.'     : '.'이 맨 뒤에 위치하면 안된다.
# inp[inp.find('.') + 1].isalpha()   : '.' 뒤에 위치한 것이 문자여야 한다.(숫자는x)
# inp[inp.find('@') + 1].isalpha()   : '@'과 '.' 사이에는 문자가 와야한다.(숫자는x)



if alpha == 1 and dot == 1 and etc == 0 and space == 0 and inp.find('@') < inp.find('.') \
        and inp[0] != '@' and inp[-1] != '.' and inp[inp.find('.') + 1].isalpha() \
        and inp[inp.find('@') + 1].isalpha():
    print('올바른 이메일입니다.')
else:
    print('이메일 형식이 아닙니다.')
print(f'입력한 이메일 : {inp}')





# 2. 다음 예와 같이 패턴이 있는 문자열에서 숫자만 추출해서 총 합계 구하기
str_data = "{a1:20},{a2:30},{a3:15},{a4:50},{a5:-14},{a6:15},{a7:20},{a8:70},{a9:-100}"
a = str_data.split(',')
b = []
sum = 0
for i in a:
    b.append(i[4:]) #앞에 같은패턴 날리기
print(b) # 리스트 확인. 이제 뒤에 하나씩을 날려야한다.
c = []
for i in b:
    c.append(int(i[:-1])) # 뒤에 }을 날리고 숫자로 합해버리기
print(c) # 리스트 확인. 이제 for문을 사용해 더해주자.
for i in c:
    sum += i
print(f'총합은 {sum}입니다.')


# 3. 다음과 같이 입력한 숫자만큼의 하트를 출력하도록 작성하시오.
# - for문과 문자열 사용
# - 하트문자 : ‘\u2665’
# print('\u2665') # 하트문자가 제대로 출력이 되는지 확인
heart = '\u2665'
num = input('숫자 여러개를 입력하세요.')
lnum = len(num)
a = []
for i in range(lnum):
    a.append(num[i])
# print(a) # a에 잘 들어간거
for h in a:
    print(heart.lstrip() * int(h))
