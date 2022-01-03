# 이진파일(binary file) : 글자가 아닌비트 단위로 의미가 있는 파일
# - 그림파일, 음악파일, 동영상파일, 엑셀파일, 한글파일, 실행(exe)파일


# 텍스트 파일 : 메모장으로 열고 내용이 보이는 파일


# # 이진파일 읽기
# open('이진파일이름','rb')
# read(1) : 1바이트 씩 읽기
#
# # 이진파일 쓰기
# open('이진파일이름', 'wb')
# write()


# 이진파일 복사 (읽고 쓰기)
f1 = open('c:/windows/notepad.exe', 'rb')
f2 = open('c:/Temp/notepad.exe', 'wb')
while True:
    inStr = f1.read(1)
    if not inStr:  # 파일의 끝(더 이상 읽을게 없음)
        break
    else:
        f2.write(inStr)

f1.close()
f2.close()

