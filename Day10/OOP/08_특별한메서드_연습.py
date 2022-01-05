# 앞에서 작성한 Dog 클래스에서
# 1. 객체간의 크기를 비교하는 메서드를 작성
# 2. 객체간의 나이를 더하고, 빼고, 곱하고, 나누는 메서드 작성


class Dog:
    def __init__(self, Breed = '?', Size = '?', Age = '?', Color = '?' ):
        self.__Breed = Breed
        self.Size = Size
        self.Age = Age
        self.Color = Color

    def getBreed(self):
        return self.__Breed
    def setBreed(self, Breed):
        self.__Breed = Breed

    def getSize(self):
        return self.Size
    def setSize(self, Size):
        self.Size = Size

    def getAge(self):
        return self.Age
    def setAge(self, Age):
        self.Age = Age

    def getColor(self):
        return self.Color
    def setColor(self, Color):
        self.Color = Color

    def Eat(self):
        print(f'{self.Color} 색상의 개가 먹이를 먹습니다.')

    def Sleep(self):
        print(f'{self.Color} 색상의 개가 잠을 자고있습니다.')

    def Sit(self):
        print(f'{self.Color} 색상의 개가 앉습니다.')

    def Run(self):
        print(f'{self.Color} 색상의 개가 뛰어 다닙니다.')

    def __repr__(self):
        return f'품종: {self.__Breed}\n크기: {self.Size}\n나이: {self.Age}\n색상: {self.Color}'

    def __add__(self, other):
        return self.Age + other.Age

    def __sub__(self, other):
        return self.Age - other.Age

    def __mul__(self, other):
        return self.Age * other.Age

    def __divmod__(self, other):
        return (self.Age // other.Age, self.Age % other.Age)

    def __gt__(self, other):
        return self.Size < other.Size

    def __ge__(self, other):
        return self.Size <= other.Size

    def __lt__(self, other):
        return self.Size > other.Size

    def __le__(self, other):
        return self.Size >= other.Size

    def __eq__(self, other):
        return self.Size == other.Size

    def __ne__(self, other):
        return self.Size != other.Size

dog1 = Dog('Neapolitan Mastiff', 'Large', 5, 'Black')
dog2 = Dog('Maltese', 'Small', 2, 'White')
dog3 = Dog('Chow Chow', 'Medium')
dog4 = Dog()
# print(dog1.Breed) #  비공개필드 메소드라 오류남
print(dog3)

dog4.setBreed('Jindo')
dog4.setColor('Yellow')

dog1.Eat()
dog2.Sleep()
dog3.Sit()
dog4.Run()
print(dog1)
print(dog2)
print(dog3)
print(dog4)

# 조건1. 객체의 크기 비교
print(dog1 > dog2)
print(dog1 >= dog2)
print(dog1 < dog2)
print(dog1 <= dog2)
print(dog1 == dog2)
print(dog1 != dog2)

# 조건2. 객체간 나이 연산
print(dog1 + dog2)
print(dog1 - dog2)
print(dog1 * dog2)
print(divmod(dog1, dog2))
