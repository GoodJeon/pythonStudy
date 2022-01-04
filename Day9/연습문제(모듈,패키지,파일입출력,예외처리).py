# 1. 다음 코드를 람다 함수 형태로 수정할 때, 알맞은 코드를 작성하시오.
# def f(x, y):
#     return x ** y
f = lambda x, y : x ** y
print(f(2,3))


# 2. 다음과 같이 리스트 컴프리헨션으로 되어 있는 코드를 람다(lambda) 함수와 map() 함수를 사용해 표현하시오.
# ex = [1, 2, 3, 4, 5]
# [value **2 for value in ex]
ex = [1, 2, 3, 4, 5]
ex2 = []
for value in ex:
    ex2.append(value ** 2)
print(ex2)

ex3 = list(map(lambda i : i ** 2, ex))
print(ex3)



# 3. 패키지(packages)에 대한 설명 중 틀린 것은? 3번
# (1) 다양한 모듈의 합으로 디렉터리로 연결된다.
# (2) 하나의 대형 프로젝트를 만드는 코드의 묶음이다.
# (3) 개별 .py 파일을 의미한다.
# (4) 다양한 오픈소스들이 관리되는 방법이다.
# (5) __init__, __main__ 등 키워드 파일명이 사용된다.


# 4. 'game'이라는 패키지가 만들고 싶다고 가정하자. 패키지를 만들기 위해
# 디렉터리별로 필요한 모듈을 구현하고자 한다.
# 다음 그림에서 빈칸에 들어가야 할 파일은? 3번
# (1) __main__ (2) import game (3) __init__.py (4) __main__.py (5)__init__



# 5. 모듈을 호출하는 방법이 아닌 것은? 2번
# (1) import os (2) import os as * (3) from os import listdir
# (4) from os import * (5) import os as linuxos


# 6. 두 코드 파일인 ‘fah_converter.py’와 ‘module_ex.py’는 같
# 은 디렉터리에 있다. 다음과 같은 결과값을 얻기 위해 빈칸에
# 들어갈 적합한 코드를 쓰시오.
# 답: import fah_converter as fah


# 7. 다음과 같이 game 패키지를
# 만들었다. 모듈 render.py에 있는
# render_test() 함수를 패키지 내
# 에서 다른 디렉터리의 사용하려
# 고 한다. 부모 디렉터리(game)를
# 기준으로 호출하는 방법은?
# 답 : from graphic import render


# 8. 다음과 같이 ‘hello_python.txt’ 파일을 수정하고자 한다. 빈
# 칸에 들어가야 하는 코드를 쓰시오.
# 답 : (가) a , (나) write



# 9. 파이썬은 파일 처리를 위해 open() 함수를 사용한다.
# “파일 열기 모드”에 따라 들어갈 값을 쓰시오.
#
# f = open("<파일 이름>", "파일 열기 모드")
# f.close()
# 답 : (가) w, (나) a, (다) r


# 10. ‘calculator_input.py’는 사칙연산 프로그램이다.
# 다음 빈칸을 채워 프로그램을 완성하시오.
# 답 : from calculator import sum_func, mutiply_func, minus_func, devide_func



## 11. 다음 코드의 실행 결과를 쓰시오
# 답 :
# 7
# 3
# 2
# 1
# 1
# 1
# 종료되었습니다.



# 12.  다음 코드를 실행했을 때, 가장 마지막에 출력되는 값은?
# 답: 5번


# 13. 다음 각각의 예외 처리에 적합한 내장 예외(built-in
# exception)를 순서대로 실행한 결과값이 바르게 짝지어진 것은?
# 답: 4번

# 14. 다음 중 예외(exception)의 이름과 내용이 잘못 짝지어진 것은?
# 답: 다 맞는거 같은데...


# 15. 파일의 종류에 대한 설명으로 틀린 것은?
# 답 : 4번

# 16. 다음과 같이 코드를 작성하고 실행하면 ‘숫자를 넣어주세요:’가 출력된다.
# 여기에서 문자를 입력하는 경우, 예측되는 실행 결과를 쓰시오.
# 답 : 숫자가 아닙니다.



# 17. try ~ except 문에서 사용되는 예외의 종류에 대한
# 설명이다. 예외를 적어보자.
# 답 : (1) NameError, (2) 모르겠음. , (3) 모르겠음., (4) : KeyError


# 18.다음 코드의 실행 결과를 쓰시오
# for i in range(3):
#   try:
#       print(i, 3// i)
#   except ZeroDivisionError:
#       print("Not divided by 0")

# 답 :
# Not dvided by 0
# 1 3
# 2 1


# 19. 다음 코드는 파이썬에서 ‘i_have_a_dream.txt’ 파일을 읽어
# 오는 코드이다. 같은 기능을 하는 코드를 with 구문과 함께 사
# 용하여 작성하시오.
# f = open("i_have_a_dream.txt", "r")
# contents = f.read()
# print(contents)
# f.close()

# 답 :
# with open('i_have_a_dream.txt', 'r') as f:
#     contents = f.read()
#     print(contents)
