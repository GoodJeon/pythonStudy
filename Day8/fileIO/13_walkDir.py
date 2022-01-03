# 디렉터리 목록 보기

import os

for dirName, subDir, fnames in os.walk('c:/pythonStudy/Day8'):
    print(fnames)
    for fname in fnames:
        # print(os.path.join(dirName, fname))
        print(fname)