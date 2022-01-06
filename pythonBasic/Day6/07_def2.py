# 함수의 정의 및 호출

def show_info():
    print('이름 : 홍길동')
    print('나이 : 20')

show_info()

def welcome(n):
    for i in range(n):
        print('welcome!')
welcome(10)


# 두 개의 수를 입력받아서 합을 구하여 출력하는 함수 작성
def sumAB(): # 리턴값이 없는 경우
    a = int(input('숫자1 입력 : '))
    b = int(input('숫자2 입력 : '))
    print(f'{a} + {b} = {a+b}')

sumAB()

def sumAB(): # 리턴값이 있는 경우에는 변수에 리턴값을 저장
    a = int(input('숫자1 입력 : '))
    b = int(input('숫자2 입력 : '))
    return a + b
result = sumAB()
print('합 :', result)
print('합 :', sumAB()) # 변수에 저장하지 않고 바로 사용
