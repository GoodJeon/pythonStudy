# 2021-12-20 변수
# 1) 레퍼런스 : 값(객체)이 저장된 메모리의 위치를 가리키는 레퍼런스(reference:참조)다.
# 2) 동적 타이핑 : 값의 형에 따라서 고정되지 않고, 동적으로 자료 유형을 매핑해서 사용
#    type 검사(자료형이 지정되어 있지 않다.)
# 3) 변수는 이름을 가지고 있다.
# 4) 변수에는 다른 값을 저장할 수 있다.(값 변경 가능) 
# 5) 변수는 선언이 필요없다.(java는 형식 지정 필요)


# 자바 : int x
#       x = 100.0
# 정수형으로 지정해놨는데 부동소숫점으로 대입시키면 오류난다.


x = 10
print(x)
id(x) # 변수가 가리키는 값(객체)의 주소
type(x) # 변수가 가리키는 값의 형식

y = 'hello'
print(y)
y = 'haha'
print(y)
y = 100
print(y)
y = 10.5

y = [10, 30, 40]
id(y)
type(y)

z = y


# 변수 이름
# 1) 대소문자 구분 : C 언어 기반
#    X, x
# 2) 영문자, 숫자, 밑줄(_)
# 3) 중간에 공백 x
#       snail : std_name
#       comel : stdName
# 4) 예약어는 변수명을 사용할 수 없다.

#import keyword
#keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#len(keyword.kwList)
# 35


# 변수에 값 저장 : 할당(assign)
# 변수 = 값
a = 100

# 변수1, 변수2, 변수3 = 값1, 값2, 값3
a, b, c = 1, 2, 3

# 변수1 = 변수2 = 변수3 = 값1
a = b = c = 100

# 변수값 교환(swap)
a, b = b, a


# 변수 삭제: del 변수명
del x



# 문제 : 자신의 이름과 나이를 변수에 저장한 후
# print()를 이용하여 한 줄에 출력하시오.
name = '전동준'
age = 27
print(name, age)
# name, age = '전동준', 27
# print(name + ' ' + str(age))
print(name, age)


name = '전동준'
id = 14016049
level = 4
grade = 'A'
avg = 93.5

print("성명 : {0}".format(name))
print("학번 : {0}".format(str(id)))
print("학년 : {0}".format(str(level)))
print("학점 : {0}".format(grade))
print("평균 : {0}".format(str(avg)))



# ---------------------
# 포맷 코드 사용

# 형식 : print('서식' % 값)
# 형식 : print('문자열 %d 문자열' % 변수)
# 서식  : %d %f %s %c %o %x %%
rate = 80
print('출석율은 %.2f%%' % rate)
name = '전동준'
age = 27
print('나이 : %d살' % age)
print('이름 : %s' % name)
