# 클래스 상속과 메소드 재정의 연습

# Animal 클래스 정의
# 메소드 : talk(), eat(), sleep()
# 필드 : age, leg, color, place

# 서브클래스 Dog 클래스
# 메소드 : talk() 재정의 -> '멍멍'

# 서브클래스 Cat 클래스
# 필드 :
# 메소드 : talk() 재정의 -> '야옹'

class Animal:
    count = 0

    def __init__(self, age='?', leg='?', color='?', place='?'):
        self.age = age
        self.leg = leg
        self.color = color
        self.place = place
        Animal.count += 1
        print(f'{Animal.count}번째 동물이 탄생했습니다.')
    def talk(self):
        print('hmm..')

    def eat(self):
        print('eating')

    def sleep(self):
        print('zzz...')

    def __repr__(self):
        return f'나이: {self.age}\n다리 개수: {self.leg}\n색상: {self.color}\n사는 곳: {self.place}'

class Dog(Animal):
    def __init__(self, age, leg, color, place, hairLen):
        super().__init__(age, leg, color, place)
        self.hairLen = hairLen

    def talk(self):
        print('Wal! Wal Wal!!')

    def __repr__(self):
        return f'나이: {self.age}\n다리 개수: {self.leg}\n색상: {self.color}\n사는 곳: {self.place}\n털 길이: {self.hairLen}'


class Cat(Animal):
    def __init__(self, age, leg, color, place, hairLen):
        super().__init__(age, leg, color, place)
        self.hairLen = hairLen

    def talk(self):
        print('Meow~~~~')

    def __repr__(self):
        return f'나이: {self.age}\n다리 개수: {self.leg}\n색상: {self.color}\n사는 곳: {self.place}\n털 길이: {self.hairLen}'

animal1 = Animal(place = 'sea')
print(animal1)
cat1 = Cat(3, 4, 'white', 'land', 'short')
dog1 = Dog(1, 4, 'black', 'land', 'long')

cat1.talk()
dog1.talk()

print(dog1)
print(cat1)


# 다형성(polymorphism) : 같은이름의 메서드가 다른 기능을 할 수 있도록 한 것
animals = [Cat(1,4,'white','land','long'), Cat(5,4,'gray','land','short'), Dog(2,4,'black','land', 'long')]

for animal in animals:
    animal.talk()