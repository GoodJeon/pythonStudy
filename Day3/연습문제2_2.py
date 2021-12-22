# 문제 1
sixteenToTen = int(input('16진수 한글자 입력 : '), 16) #input을 이용해 16진수를 받으
if sixteenToTen <= 16:
    print('10진수 ==> %d' % sixteenToTen)
else:
    print('16진수가 아닙니다')


# 문제 2
changes = int(input('교환할 돈은 얼마 ? '))
cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cm = []
for i in cash:
    cm.append(changes//i)
    changes = changes % i

# print(cm)
print('50000원 {}장, 10000원 {}장, 5000원 {}장, 1000원 {}장, '
      '500원 {}개, 100원 {}개, 50원 {}개, 10원 {}개 '.format(cm[0],cm[1],cm[2],cm[3],cm[4],cm[5],cm[6],cm[7]))
print(f'바꾸지 못한 돈 ==> {changes}')




# 문제 3
from random import randint
dice1 = (randint(1, 6))
dice2 = (randint(1, 6))
print('A의 주사위 숫자는 {} 입니다.'.format(dice1))
print('B의 주사위 숫자는 {} 입니다.'.format(dice2))
if dice1 == dice2:
    print('비겼다.')
elif dice1 > dice2:
    print('A가 이겼다.')
else:
    print('B가 이겼다.')
