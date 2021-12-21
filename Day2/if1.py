# pw = int(input('비밀번호 입력 :'))

''' if pw == 1234:
     print('비밀번호가 일치합니다.') # 제어문 다음 줄부터 들여쓰기 되어있는 공간을 블럭이라 부른다.
 else:
     print('비밀번호가 일치하지 않습니다.')
'''


# if pw == 1234:
#     print('비밀번호가 일치합니다.') # 제어문 다음 줄부터 들여쓰기 되어있는 공간을 블럭이라 부른다.
# else:
#     pass



# 문제 : id와 poassword를 입력받아 모두 맞으면 로그인 성공 출력
# id : multicampus
# pw : 1234

# id = 'multicampus'
# password = 1234
# login_id = input('ID 입력 :')
# login_pw = int(input('비밀번호 입력 :'))
#
# if login_id == id and login_pw == password:
#     print('로그인 성공')
# else:
#     print('로그인 실패')

#중첩 if문
'''
if login_id == 'multicampus':
    if login_pw == 1234 :
        print('로그인 성공')
    else:
        print('비밀번호가 다릅니다.')
else:
    print('아이디가 올바르지 않습니다.')
'''

# 문제 :
# 정수를 입력받아서 홀수인지 짝수인지 판별하여 출력
# 정수 입력:
# 출력 :  홀 혹은 짝
'''
enter_int = int(input('정수를 입력하세요: '))
if enter_int % 2 == 1:
     print('홀')
else:
     print('짝')
'''
# 문제:if ~ elif
# 입력한 정수가 음수, 0, 양수인지를 확인하여 출력
'''
num = int(input('정수를 입력하세요: '))
if num > 0:
    print('양수')
elif num == 0:
    print('0')
else:
    print('음수')
'''

# 문제 : 점수를 입력받아서 학점 출력 A, B, C, D, F
point = float(input('점수를 적어주세요: '))
if point >= 90:
    print('A')
elif point >= 80:
    print('B')
elif point >= 70:
    print('C')
elif point >= 60:
    print('D')
else:
    print('F')