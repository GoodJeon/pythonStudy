

# 자동차 클래스
# 기능(동작)=>메소드(함수) : speedUp(), speedDown()
# 속성(상태, 값) => 변수(필드) : color, speed

# 1. 클래스 선언
# 클래스 이름 : 식별자 규칙에 정의, 대문자로 시작
class Car:
    color = 'red'
    speed = 0

    def speedUp(self):
        self.speed += 10


    def speedDown(self):
        self.speed -= 10

# self : 인스턴스가 사용하는 것(자신)
#        기존의 함수와 구분



# 2. 객체 생성
myCar = Car()
yourCar = Car()

# 3. 객체(인스턴스) 사용
# 메서드 호출 : 인스턴스.메서드()
# myCar.speedup()
# 인스턴스 생성 후 필드 추가
myCar.color = 'black'

print(myCar.color)
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)
myCar.speedUp()
print(myCar.speed)

