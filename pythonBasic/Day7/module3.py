# 모듈 참조 형식 1
import calculator

if __name__ == '__main__':
    print('03_module3.py------')
    print(calculator.add(10,3))
else:
    print(calculator.sub(10, 3))
# 모듈 참조 형식 2
# from calculator import add, sub
# print(add(10,3))
# print(div(10,3)) 오류 발생

# 모듈 참조 형식 3
# from calculator import *
# print(add(10,3))
# print(div(10,3))

# 모듈 참조 형식 4
# from Day7.modules import calculator as cal
#
# print(cal.add(10,20))