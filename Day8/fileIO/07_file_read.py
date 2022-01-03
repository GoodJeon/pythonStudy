# 텍스트 파일 읽기 : read() 함수
# 내용 전체를 읽어서 1개의 문자열로 반환

f = open('test2.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()
print(type(data))
print(len(data))
f.close()

for ch in data:
    print(ch)
