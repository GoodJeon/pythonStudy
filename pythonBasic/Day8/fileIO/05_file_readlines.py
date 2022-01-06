# 텍스트 파일 읽기
# readlines() : 전체 라인을 읽어오기
# 리스트로 반환


# f = open('test.txt','r',encoding='utf-8')
# lines = f.readlines()
# print(lines)
# f.close()

# f = open('test.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     print(line, end='')
# f.close()

f = open('test.txt', 'r', encoding='utf-8')
for line in f:   # f.readlines()를 자동 수행
    print(line, end='')
f.close()
