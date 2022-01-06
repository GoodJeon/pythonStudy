# 클래스 구현과정
# 1단계 : 클래스 정의(선언)

# class 클래스명:
#     def __init(self):
#         self.필드명1 = 초기값
#         self.필드명2 = 초기값
#         self.필드명3 = 초기값
#
#     def 메소드명1(self, 매개변수, ...):
#         pass
#         return

    # 메소드 정의는 함수를 정의하는 것과 동일

# 2단계 : 객체생성(인스턴스 생성), 변수선언과 비슷
# 객체변수명 = 클래스명() # <- 생성자 함수

# 3단계 : 객체이용, 메소드, 필드값변경, 필드값 사용
# 객체변수명.메소드()
# 변수나 함수와 다르게 구별하기 위해서
# 객체이름.변수명
# 객체이름.메소드명



# 객체와 인스턴스
# 객체 : 객체만 지칭할 때는 객체(object)라고 하고
# 인스턴스 : 클래스와 연관지어서 부를 때


# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)

print(isinstance(myCar, Car))

# 파이썬의 기본적으로 제공하는 클래스들
# int, float, str, bool, list, tuple, dict, set, tuple...

a = int(10)
print(type(a))

b = list(range(10))
print(b)
print(type(b))

c = dict(x=10, y=20)
print(type(c))

e = str(10)
print(type(e))
