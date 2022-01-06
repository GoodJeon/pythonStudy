# 특별한 메서드(Magic Method)
# __메서드이름__  : 미리 정의되어있는 메서드

# __ge__() : >=
# __gt__() : >
# __lt__() : <
# __le__() : <=
# __ne__() : !=
# __eq__() : ==

# __init__() : 생성자
# __repr__() : 인스턴스 print()문으로 출력
# __add__() : +
# __del__() : 소멸자, 인스턴스를  삭제


# 선(line) 클래스
# 필드 : 길이, 색상, 두께
# 메소드 : 더하기, 크기비교, 빼기

class Line:
    def __init__(self, length=0):
        self.length = length
        print(f'{self.length}의 길이 선분이 생성되었습니다.')

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __mul__(self, other):
        return self.length * other.length


    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self, other):
        return self.length != other.length

    def __repr__(self):
        return '선의 길이: ' + str(self.length)

    # def __del__(self):
    #     print(self.length, '길이의 선분이 삭제되었습니다.')


line1 = Line(10)
line2 = Line(5)
print('line1: ', line1.length)
print('line2: ', line2.length)
print('line1 + line2 = ', line1 + line2)
print('line1 > line2 = ', line1 > line2)
print('line1 == line2 = ', line1 == line2)
print(line1)
print(line2)