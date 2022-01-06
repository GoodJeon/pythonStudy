# 상속(inheritance)
# 부모클래스(super class): 상속을 해주는 클래스
# 자식클래스(sub class): 상속을 받는 클래스

# 자동차 클래스

class Car:
    speed = 0
    color = ''

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed}으로 주행합니다.')


# 트럭 클래스

class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)
        self.load = load

    def drive(self):
        print(f'시속 {self.speed}으로 {self.load}양의 짐을 싣고 주행합니다.')


    def loading(self):
        print(f'최대 {self.load}양의 짐을 운반할 수 있는 트럭')

truck1 = Truck(10, 'red', 1000)
truck1.drive()


# 승용차 클래스 Vehicle : 좌석(seat)

class Vehicle(Car):
    def __init__(self, speed, color, seat):
        super().__init__(speed, color)
        self.seat = seat

    # 메소드 재정의 (오버라이딩)
    def drive(self):
        print(f'시속 {self.speed}으로 {self.seat}인을 태우고 주행합니다.')

vehicle1 = Vehicle(30, 'whilte', 5)
vehicle1.drive()
truck1.loading()

car1 = Vehicle(20, 'yellow', 10)
car1.drive()