# 파일 압축 및 풀기

import zipfile

# 파일 압축

new = zipfile.ZipFile('c:/pythonStudy/Day8/Day8.zip', 'w')
new.write('c:/pythonStudy/Day8/fileIO/test2.txt', compress_type=zipfile.ZIP_DEFLATED)
new.close()


# 파일 압축 풀기
ext = zipfile.ZipFile('c:/pythonStudy/Day8/Day8.zip', 'r')
ext.extractall('c:/pythonStudy/')
ext.close()


