class Person:
    def __init__(self, name = '?', age = 0):
        self.name = name
        self.age = age

    def greeting(self):
        print("hi")


class Student(Person):
    def __init__(self, name = '?', age = 0, department = '?', grade = 0):
        super().__init__(name, age)
        self.department = department
        self.grade = grade

    def study(self, subject):
        print(f'{subject} 공부 중')


p1 = Person('jobs', 20)
p1.greeting()
s1 = Student('jdj', 1, 'eco', 3)
s2 = Student()

s1.study('수학')