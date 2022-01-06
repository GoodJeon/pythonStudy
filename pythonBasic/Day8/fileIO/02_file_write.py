# # 텍스트 파일에 쓰기

# data = 'Hi'
# f = open('file2.txt', 'w')
# f.write(data)  # 파일에 data의 내용인 Hi를 작성
# f.close()

# data = '안녕하세요'
# f = open('file2.txt', 'w') # 코딩 형식이 ANSI여서한글이 깨져서 보인다.
# f.write(data)  # 파일에 data의 내용인 안녕하세요를 작성
# f.close()

data = '안녕하세요'
f = open('file3.txt', 'w', encoding='utf-8') # 코딩 형식이 utf-8이여서 한글이 잘 보인다.
f.write(data)  # 파일에 data의 내용인 안녕하세요를 작성
f.close()