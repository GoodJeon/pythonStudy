# 파일 내에서 검색
# read() 함수 사용

f = open('test2.txt', 'r', encoding='utf-8')
data = f.read()
value = input('검색 값 입력: ')
if value in data:
    print('Exist!')
else:
    print('Not Exist!')

f.close()
