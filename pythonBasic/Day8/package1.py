# 패키지(package)
# : 모듈들을 모아놓은 디렉터리(폴더)

# 일반적인 디렉터리와 차이점
# 패키지는 디렉터리 안에 __init_.py 존재 (빈파일)

# 패키지를 사용할 경우 모듈 import
# import 패키지.모듈
# import 패키지.모듈 as 별칭
# from 패키지.모듈 import 함수
# from 패키지.모듈 import **



# 패키지를 파이참 구성하는 방법
# [파일] - [New] - [Python Package] - package 이름 입력
# 패키지가 생성되면 __init__.py 확인




# import 패키지.모듈
# import mypack.pack1.module11
# mypack.pack1.module11.func12()


# import 패키지.모듈 as 별칭
import mypack.pack1.module11 as mm1
mm1.func12()


# from 패키지.모듈 import 함수
from mypack.pack1.moduel12 import func111, func11
func111()
func11()


# from 패키지.모듈 import
from mypack.pack1.module11 import *
func12()

