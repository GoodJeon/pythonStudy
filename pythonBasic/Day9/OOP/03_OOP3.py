

# 자동차 클래스
# 기능(동작)=>메소드(함수) : speedUp(), speedDown()
# 속성(상태, 값) => 변수(필드) : color, speed

# 1. 클래스 선언
# 클래스 이름 : 식별자 규칙에 정의, 대문자로 시작
class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

    def speedUp(self):
        pass

    def speedDown(self):
        pass




# 2. 객체 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
# myCar.speedup()
# 인스턴스 생성 후 필드 추가
myCar.color = 'black'
myCar.speed = 0

print(myCar.color)


# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)

print(isinstance(myCar, Car))

# 파이썬의 기본적으로 제공하는 클래스들
# int, float, str, bool, list, tuple, dict, set, tuple...

a = int(10)
print(type(a))

b = list(range(10))
print(b)
print(type(b))

c = dict(x=10, y=20)
print(type(c))

e = str(10)
print(type(e))

