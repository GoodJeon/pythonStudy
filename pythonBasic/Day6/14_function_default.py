# 디폴트 매개변수
# 매개변수의 기본값을 지정
# 디폴트는 매개변수는 반드시 뒤에 적어줘야한다.

def greet(name, msg):
    print(name + '!' + msg)

def greetThanks(name, msg = '고마워:)'): # 매개변수 msg를 default해준다.
    print(name + '!' + msg)

greet('홍길동', '안녕')
greetThanks('임꺽정')
greetThanks('임꺽정', '안녕') # 인자2에 다른것을 적어줘도 잘 실행된다.

def gr(name = '형씨', msg = '누구쇼?'):
    print(name, '!', msg)
gr()  # 매개변수를 디폴트로 다 지정해버리면 인자를 넣지않아도 잘 실행된다.





def showInfo(name, year = 1, age=20):
    print(name, year, age)
showInfo('홍길동', 3, 10)
showInfo('홍길동', 3)
showInfo('홍길동')


print('hi', end = '#')
