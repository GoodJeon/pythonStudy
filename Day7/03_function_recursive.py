# 재귀 함수호출 : 자기함수 호출

# 문제1. 팩토리얼 계산
# 3! = 3 * 2 * 1  0! = 1



# 반복문을 사용해서 구상

def factorial(n):
    fac = 1
    for i in range(n, 0, -1):
        fac *= i
    return fac








# fac(n) = n * fac(n-1)
# fac(n-1)! = (n-1) * fac(n-2)
# fac(1) = 1
#
# fac(n) = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input('숫자입력: '))
print(f'{n}! = {factorial(n)}')


# 5! => fact(5) -> 5 * fact(4) -> 4 * fact(3) -> 3 * fact(2) -> 2 * fact(1) -> 1
# 5! <- fact(5) <- 5 * 4 * 3 * 2 * 1 <- 4 * 3 * 2 * 1 <- 3 * 2 * 1 <- 2 * 1 <- 1

# 주의 : RecursionError: maximum recursion depth exceeded while calling a Python object
def selfCall():
    print('hello', end = ' ')
    selfCall()

# selfCall()

# 반복문 이용
def count(number):
    for i in range(number, 0, -1):
        print(i, end = ' ')

count(5)


# 재귀함수 이용
def selfCount(number):
    if number >= 1:
        print(number, end = ' ')
        return selfCount(number - 1)
    else:
        return

selfCount(5)



