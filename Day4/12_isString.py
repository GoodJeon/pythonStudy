# 문자열 구성 파악
# isalpha() : 문자 여부 결과 반환(True, False)
# isdigit() : 숫자 여부 결과 반환
# isspace() : 하나의 문자에 대하여 공백 여부 결과 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자여부
# isupper() : 대문자여부

string = '내 이름은 djjeon 이고 나이는 12 입니다'
str_split = string.split()
for result in str_split:
    if result.isdigit():
        print('숫자군요')
    else:
        print('숫자가 아니네요')

# 입력된 문자열에서 알파벳, 숫자, 스페이스, 기타의 개수를 각각 계산하여 출력하기
# 문장을 입력하세요 : 내이름은 djjeon 이고 내 메일은 djjeon@email.com 입니다.
sentence = input('문장을 입력하세요 : ')
alpha = 0
digit = 0
space = 0
special = 0

for i in sentence:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        special += 1

print(f'알파벳 : {alpha}개\n숫자 : {digit}개\n공백 : {space}개\n나머지 : {special}개')

