# 객체 지향 프로그래밍 (Object Oriented Programming)
# 함수처럼 어떤 기능을 함수 코드에 묶어두지 않고 객체에 기능을 정의하는 것
# 함수와 변수를 함께 가지고 있도록 구성
# 코드의 재사용성


# 객체 : 함수(fucntion) + 데이터(변수)

# 예. TV : 끄다, 켜다, 채널을 변경, 가격

# String

str1 = 'I love you' # 문자열 객체
print(type(str1))
print(str1.split())

x = 100
print(type(x))


# 클래스(class) : 객체를 만들어내는 틀
#               객체가 가지는 기본 정보를 담은 코드
#               클래스는 일종의 설계도 코드
# 인스턴스(instance) : 클래스로부터 생성된 객체
#               클래스에 의해 실제로 생성되는 객체
#               어떤 클래스의 객체인지 관계 위주로 설명할 때 많이 사용
# 클래스 : 메소드(함수) + 필드(변수)

# 계산기 : 함수와 변수

result = 0

def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(10))
print(adder(5))



# 계산기가 여러개 필요할 경우
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(10))
print(adder1(5))
print(adder2(2))
print(adder2(4))
print(adder2(7))
# 계산기가 여러개 필요한 경우 함수와 변수를 여러개 생성

# 클래스로 계산기 정의

class Calculator:
    def __init__(self):
        self.result = 0


    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
print(type(cal1))
print(cal1.adder(3))
print(cal1.adder(5))
