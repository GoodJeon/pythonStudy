def gbb_game(you_n):
    from random import randint
    com_n = randint(1, 3)
    if com_n - you_n == 1 or com_n - you_n == -2:
        print('컴퓨터가 이겼습니다.')
    elif com_n == you_n:
        print('비겼습니다.')
    else:
        print('당신이 이겼습니다.')
    print(f'COM : {com_n}')

def input_num():
    you_n = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(you_n)
