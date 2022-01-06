# 앞에서 작성한 Car 클래스에서 다음의 두가지 메소드를 추가하시오.
# speedUp(증가할 속도량)
# speedDown(감소할 속도량)

class Car:
    def __init__(self, modelN, speed=0, color='white'):
        self.modelN = modelN
        self.speed = speed
        self.__color = color # 클래스 내에서만 사용하는 비공개필드

    def __modelN(self):
        print(self.modelN)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def printInfo(self):
        self.__modelN()
        print(self.getColor())

    def speedUp(self, x):
        if self.speed >= 140:
            print('과속입니다. 속도를 줄이세요!')
        else:
            self.speed += int(x)
        return self.speed

    def speedDown(self, x):
        if self.speed > 0:
            self.speed -= int(x)
        else:
            self.speed = 0
            print('정지했습니다!')


car1 = Car('5시리즈')
print(car1.speed)
car1.speedUp(123)
print(car1.speed)

