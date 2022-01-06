# 파일 또는 디렉토리 존재 여부 확인

import os.path

print(os.path.exists('c:/pythonStudy')) #폴더가 있어서 True값 반환
print(os.path.exists('c:/pythonStudy/test.txt')) #해당 경로에 test.txt가 없어서 False 반환

# 디렉터리인지 파일인지 구분


print(os.path.isdir('c:/pythonStudy')) # 해당 폴더가 존재하기에 True
print(os.path.isfile('c:/pythonStudy')) # 해당 이름의 파일이 없기에 False



