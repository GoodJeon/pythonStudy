# 클래스메소드
#   : 인스턴스를 통하지 않고 메서드를 클래스에서 바로 호출
#   : 메서드 내에서 클래스  변수, 클래스 메서드를 접근할 때

# @classmethod를 메서드 위에 붙임
#  : 메서드내에 인수로 cls를 지정
#  : cls = class의 약어

# # 형식
# class 클래스이름:
#     @classmethod
#     def 메서드명(cls, 매개변수들):
#         문장들
#
# # 호출형식
# 클래스이름.메서드명(인수들)


# 클래수변수이용 예.
# class Person:
#     count = 0   # 클래스변수
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
#     def printCount(self):
#         print(f'{self.count}명이 태어났습니다.')
#
# man1 = Person('Jeon')
# man2 = Person('Kang')
# man1.printCount()
# man2.printCount()



class Person:
    count = 0   # 클래스변수
    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def printCount(cls):
        print(f'{cls.count}명이 태어났습니다.')

man1 = Person('Jeon')
man2 = Person('Kang')
Person.printCount()

