# 구구단의 단수를 입력하면받아서 구구단을 출력하기
# 단수 입력 : 5
# 5 * 1 = 5
# 5 * 2 = 10
# ...
# ...
# 5 * 9 = 45

num = int(input('단수 입력 : '))
for i in range(1, 10):
    print(f'{num} * {i} = {num*i}')
