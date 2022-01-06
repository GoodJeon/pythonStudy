# 예외 처리
# 에러 종류와 상관 없이 에러가 발생하면 처리하기




# 예외 처리 형식
# try:
#     에러가 발생할 문장들
# except 예외처리클래스 as e:
#     에러가 발생하면 처리하는 문장들
# else:
#     에러가 발생하지 않으면 처리하는 문장
# finally:
#     에러와 상관없이 항상 수행하는 문장



# 에러의 종류와 상관없이 에러를 처리하는 경우
# 예제. 0으로 나누는 경우 처리
try:
    print(10/0)
    print('나이: ' + 23 + '살')
except ZeroDivisionError as e: # as e는 에러 메시지 변수
    print('0으로 나눌 수 없습니다.', e)
except TypeError as e:
    print('형식이 잘못지정되었습니다.', e)


# 에러 종류 명시 처리
try:
    print(10/0)
except ZeroDivisionError as e: # as e는 에러 메시지 변수
    print('0으로 나눌 수 없습니다.', e)

# ValueError
try:
    num = int(input('숫자를 입력하세요'))
except ValueError as e:
    print('숫자가 아닙니다.', e)


# 에러종류 여러 개 동시 처리
try:
    print(10/0)
    print('나이: ' + 23 + '살')
except (ZeroDivisionError, TypeError) as e: # as e는 에러 메시지 변수
    print('0으로 나눌 수 없습니다.', e)
    print('형식이 잘못지정되었습니다.', e)

try:
    f = open('file2.txt', 'r', encoding = 'utf-8')
except FileNotFoundError:
   pass
else:
    data = f.read()
    print(data)
    f.close()
finally:
    print('End----')