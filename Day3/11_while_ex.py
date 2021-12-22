# 'stop' 문자 입력될때가지 숫자를 입력하고
# 입력된 숫자의 개수를 출력
# num = input('숫자 입력 : ')
# cnt = 0
# while num != 'stop':
#     num = int(num)
#     cnt += 1
#     num = input('숫자 입력 : ')
# print(f'숫자 개수 {cnt}')


# 7을 입력할 때까지 계속 입력하기
# 7이 입력되면 프로그램 종료
# 7 입력! 종료
num = input('숫자 입력 : ')
while num != 7:
    num = int(input('숫자 입력 : '))
print('7 입력! 종료')

# while True, 1 은 무한루프가 걸리며 빠져나올려면
# break가 필요하다.
# while 1:
#     num = input('멈추고 싶으면 맞춰보세요: ')
#     if num == '7':
#         break
# print('종료')
