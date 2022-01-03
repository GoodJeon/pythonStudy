# with 문
# with문이 종료됨 파일 객체는 자동으로 close()
# with open(파일명, 열기모드, 인코딩) as 파일 객체 :
#       수행코드

file = 'test3.txt'
data = 'Python Programming'
with open(file, 'a', encoding='utf-8') as f: # f = open('test3.txt', 'w', encoding='utf-8')
    f.write(data+'\n')


