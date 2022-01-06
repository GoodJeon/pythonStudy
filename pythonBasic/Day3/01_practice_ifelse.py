# 연습문제 - if
# 1. 정수 3개를 입력받아서 제일 큰 수를 출력하기

#[실행결과]
# 정수1 입력 : 3
# 정수2 입력 : 9
# 정수3 입력 : 7
# 제일 큰 수 : 9

num1 = int(input('정수1 입력: '))
num2 = int(input('정수2 입력: '))
num3 = int(input('정수3 입력: '))
if num1 > num2 and num1 > num3:
    a = num1
elif num2 > num1 and num2 > num3:
    a = num2
else:
    a = num3
print('제일 큰 수 :', a)



# 2. 도형을 선택해서 면적 구하기
# [실행결과1]
# 도형 입력(1: 사각형, 2: 삼각형, 3: 원)) : 1
# 가로 입력 : 10
# 세로 입력 : 20
# 사각형의 면적 = 200.00
# [실행결과2]
# 도형 입력(1: 사각형, 2: 삼각형, 3: 원) : 2
# 밑변 입력 : 10
# 높이 입력 : 20
# 삼각형의 면적 = 100.00
# [실행결과3]
# 도형 입력(1:사각형, 2: 삼각형, 3: 원): 3
# 반지름 입력: 10
# 원의 면적 = 314.16


figure = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))
if figure == 1:
    width = int(input('가로 입력: '))
    vertical = int(input('세로 입력: '))
    area = width * vertical
    print('사각형의 면적 = %.2f' % area)
elif figure == 2:
    base = int(input('밑변 입력: '))
    height = int(input('높이 입력: '))
    area = base * height / 2
    print('삼각형의 면적 = %.2f' % area)
elif figure == 3:
    radius =int(input('반지름 입력: '))
    PI = 3.141592
    area = radius ** 2 * PI
    print('원의 면적 = %.2f' % area)
else:
    print('1, 2, 3 중 선택하시오')

