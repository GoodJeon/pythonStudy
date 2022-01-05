# 앞서 작성한 Dog 클래스에서
# 1. 디폴트 매개변수를 갖는 생성자를 정의
# 2. 필드 중 breed는 비공개필드로 정의
# 3. 필드의 값을 가져오고, 변경하는 메서드를 정의
# 4. sleep(), sit(), run(), eat() 메소드의 내용을 정의
#    잠자기,    앉다,  뛰다,   먹다 등의 내용이 출력되도록 정의

# 5. 인스턴스를 생성하되, 인수를 수를 다양하게 입력하여 생성하는 코드 작성
# 6. 인스턴스를 이용하여 개의 정보를 출력하기
# -품종, 나이, 색상, 크기 등의 정보를 출력

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

dog1 = Dog('Neapolitan Mastiff', 'Large', '5 Years', 'Black')
dog2 = Dog('Maltese', 'Small', '2 Years', 'White')
dog3 = Dog('Chow Chow', 'Medium', '3 Years', 'Brown')
dog4 = Dog()
# print(dog1.Breed) #  비공개필드 메소드라 오류남


dog4.setBreed('Jindo')
dog4.setColor('Yellow')

dog1.Eat()
dog2.Sleep()
dog3.Sit()
dog4.Run()

def dogInfo(name):
    print(f'품종: {name.getBreed()}')
    print(f'크기: {name.getSize()}')
    print(f'나이: {name.getAge()}')
    print(f'색상: {name.getColor()}')

dogInfo(dog1)
dogInfo(dog2)
dogInfo(dog3)
dogInfo(dog4)
