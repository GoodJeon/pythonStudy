# 인스턴스(instance) 변수 : 필드

# 클래스 변수 : 여러 인스턴스가 공유하는 변수
class Car:
    color = ''
    speed = 10
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1
        print(f'자동차 {Car.count}대가 생산되었습니다.') # Car.count가 클래스변수

car1 = Car()
# print(car1.count)
print(Car.count)
car2 = Car()
print(Car.count)
car1.speed # 인스턴스 변수 : 필드
car2.speed
# print(car1.count)
# print(car2.count)

car3 = Car()