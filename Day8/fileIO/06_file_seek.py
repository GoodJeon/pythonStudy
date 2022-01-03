# 파일 내에서 검색
# seek(offset, whence) :
#  - offset : 상대 위치
#            시작 위치로부터 열의 위치
#  - whence : 위치
#             0 : 파일 시작 위치, 1 : 현재위치,  2 : 파일의 끝
# seek(0,0) : 시작위치로부터 0열의 위치 => 0행 0열
# seek(10,0) : 시작위치로부터 오른쪽으로 10열의 위치 => 0행 10열
# sekk(0,2) : 파일의 끝으로부터 0열의 위치 =>


f = open('test2.txt', 'r', encoding='utf-8')
# f.seek(0,0) # 0행 0열
# f.seek(10,0) # 0행 10열
# f.seek(0,2) # 파일의 마지막 위치
# f.seek(14,0)
# f.seek(17,0)
# lines = f.readlines()

f.seek(0,0)
line  = f.readline()
print(line)


f.seek(9,0)
line  = f.readline()
print(line)


f.seek(17,0)
line  = f.readline()
print(line)

f.close()


# \r : carriage return
# \n : line feed
# 01234\r\n
# abcde\r\n
# 가나다라마 : 2바이트씩