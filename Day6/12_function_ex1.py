# 산술연산 함수 작성
# add() : 두 수 더하기
# sub() : 두 수 뺴기
# mul() : 곱하기
# div() : 나누기
# mod() : 나머지

# a=9, b=3
# 두 개의 숫자를 전달받아서 연산 결과 반환

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2



def printArithm(a,b):
    print(f'{a} + {b} = {add(a,b)}')
    print(f'{a} - {b} = {sub(a, b)}')
    print(f'{a} * {b} = {mul(a, b)}')
    print(f'{a} / {b} = {div(a, b):.2f}')
    print(f'{a} % {b} = {mod(a, b)}')

printArithm(3,5)




