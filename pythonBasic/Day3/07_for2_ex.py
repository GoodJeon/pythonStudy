# 숫자 10개를 입력 받아서 양, 음, 0의 개수 출력
# 숫자1입력 : -3
# 숫자2입력 : 0
# 숫자3입력 : 0
# 숫자4입력 : 8
# 숫자5입력 : 3
# 숫자6입력 : -4
# 숫자7입력 : 0
# 숫자8입력 : -6
# 숫자9입력 : -1
# 숫자10입력 : 7
a = 0
b = 0
c = 0

for i in range(1, 11):
    num = int(input('숫자%d입력 : ' % i))
    if num > 0:
        a += 1
    elif num < 0:
        b += 1
    elif num == 0:
        c += 1
print('---------------')
print('양의 개수 : %d' % a)
print('음의 개수 : %d' % b)
print('0의 개수 : %d' % c)