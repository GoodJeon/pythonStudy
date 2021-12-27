# 문제 1
# 1)
for i in range(5, 0, -1):
    print('☆' * i)
print('-----------')

# 2)
# 최재영
for y in range(1, 10, 2):
    string = '☆' * y
    print(string.center(10))

# 조성헌
print('---조성헌---')
n = 0
for i in range(1,10,2):
    result=i * '☆'
    n += 1
    print((5-n)*' '+result+(5-n)*' ')

# 윤형석
print('------윤형석-----')
for i in range(1,10,2):
    print(' '*(4-i//2)+'☆'*i)

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for k in range(1, 2*i):
        print('☆', end='')
    print()




# 문제 2
num = int(input('숫자 입력 : '))
if num == 7:
    print('7 입력! 종료')
else:
    while True:
        re = int(input('다시 입력 : '))
        if re == 7:
            print('7 입력! 종료')
            break


# 문제 3
currency = 10000
song = 0

while True:
    if currency != 0:
        song += 1
        currency -= 2000
        print(f'노래를 {song}곡 불렀습니다.')
    else:
        print('잔액이 없습니다. 종료합니다.')
        break
    print(f'현재 {currency}원 남았습니다.')