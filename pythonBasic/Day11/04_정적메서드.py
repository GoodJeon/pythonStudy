# 정적메서드(Static Method)
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# 메서드 위에 @staticmethod를 붙임
# 매서드에 self를 넣지 않음
#   : 인스턴스 변수, 인스턴스 메서드가 필요없을 때
# 순수함수로 만들어서 사용할 때


class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

calc1 = Calc()
calc2 = Calc()
# print(calc1.add(3, 2))
# print(calc2.add(3, 2))
# 인스턴스를 생성하여 메서드를 호출하지 않고
# 정적메서드 호출방식 : 클래스이름.정적메서드(*args)

print(Calc.mul(10, 20))
