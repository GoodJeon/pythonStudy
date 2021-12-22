# 문제 1
# 1)
for i in range(5, 0, -1):
    print('☆' * i)
print('-----------')

# 2)
for i in range(1, 10, 2):
    for j in range(8-i):
        print(' ', end = '')
    print('☆' * i)

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