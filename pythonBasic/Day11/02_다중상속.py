# 다중상속 : 여러클래스에서 상속을 받음

# 형식
# class 클래스이름(부모클래스1, 부모클래스2, ...):
#     pass



class Person:
    def __init__(self, name = '?', age = 0):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"hi. i'm {self.name}")

class University:
    def __init__(self, department = '', grade = ''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print('학점관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

kim = Undergraduate()
kim.name = 'Kim'
kim.age = 20
kim.greeting()
kim.manageScore()
kim.study()