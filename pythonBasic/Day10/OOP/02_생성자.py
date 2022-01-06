# 생성자(constructor)
# : 인스턴스 생성
# : 필드값을 초기화 함수

# 생성자를 정의할 때 : __init__()
# 생성자를 호출(사용) == 인스턴스를 만드는 것


# 생성자의 형식
# class 클래스명:
#     def __init__(self, *args):
#         # 이 부분에 필드 초기화 코드 입력

# self : 클래스에서 생성된 인스턴스에 접근 (인스턴스 자신)
#       인스턴스가 생성된 후 해당 인스턴스 이름으로 값을 할당하거나 메서드 호출
#       클래스 내에서 self 호출
#       생성된 인스턴스 이름과 클래스 내의 self가 같은 역할을 함


# 참고
# _ : 변수에 특별한 이름을 부여하지 않고 사용하려고 할 때
#
# for _ in range(10):
#     print('Hello')

# __(2개 사용) : 특수한 예약함수(메소드),변수에 사용

# if __init__ == '__main__':


# 기본 생성자 : 생성자에 self만 있고, 다른 매개변수가 없음
#class 클래스명:
#   def __init__(self):
#       pass

class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'red'

car1 = Car()
print(f'자동차의 색상은 {car1.color}')
print(f'자동차 속도는 {car1.speed}')


# 매개변수가 있는 생성자
# class 클래스명:
#   def __init__(self, *args):
#       pass

class Car1():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

# myCar = Car1() : 인수를 지정하지 않아서 TypeError 오류 발생
myCar = Car1(20, 'black')
print(f'자동차의 색상은 {myCar.color}')
print(f'자동차의 속도는 {myCar.speed}')

# 디폴트 매개변수를 사용하는 생성자
# class 클래스명:
#     def __init__(self, arg1 = value1, arg2 = value2):
#         pass

class Car2():
    def __init__(self, color='black', speed=0):
        self.speed = speed
        self.color = color

yourCar = Car2()
print(yourCar.speed)
print(yourCar.color)
ourCar = Car2('White')
print(ourCar.speed)
print(ourCar.color)



class Car3():
    def __init__(self, color='red', speed=0):
        self.speed = speed
        self.color = color

    def drive(self):
        self.speed = 50

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10




myCar4 = Car3()
print('초기 속도', myCar4.speed)
myCar4.drive()
print('drive()수행 후 속도', myCar4.speed)
myCar4.speedUp()
print('speedUp()수행 후 속도', myCar4.speed)
myCar4.color = 'white'
print(myCar4.color)
