# 반환값

# 문제1. 사각형의 넓이 계산하는 함수 getArea()
# 매개변수(parameter) : 가로(width), 세로(height)
# 넓이를 반환
def getArea(width, height):
    area = width * height
    return area

print(getArea(3, 5))

# 문제2. 사각형의 넓이 계산하는 함수 getArea()
# 가로 세로 길이 입력받기
# 넓이를 반환
def getArea():
    width = int(input('가로 길이 : '))
    height = int(input('세로 길이 : '))
    area =  width * height
    print(f'가로 : {width}, 세로 : {height}, 사각형 넓이 : {area}')
    return area

getArea()

# 반환값이 여러 개인 경우
def multi_return():
    return 1, 2, 3

# 반환된 여러개의 값을 하나의 변수에 저장
result = multi_return() # 튜플 형식으로
print(result)
print(type(result))

# 반환된 여러개의 값을 여러 변수로 각각 받기ㅇ
a, b, c = multi_return()
print(a,b,c)
