# 리스트 복사

# 얕은 복사(shadow copy): 실제 리스트가 복사되지 않고 참조값(주소)만 복사
a = [1,2,3,4]
b = a # b도 a가 저장한 주소를 똑같이 저장한거라
print(a)
print(b)
a[-1] = 100  # a리스트의 마지막 요소를 바꾸면
print(a)
print(b)   # b리스트의 마지막 요소도 같이 바뀐다.
b[0] = 0.5  # b도 수정해봤더니
print(b)
print(a) # a도 같이 수정된다.


# 깊은 복사(deep copy) : 실제 리스트가 복사된다.
# 리스트 복사본을 새로 생성하여 반환
# list()함수 또는 copy모듈의 deepcopy()함수 사용
print('deepcopy start------------------')
c = list(a) # a리스트의 값을 그대로 c리스트에 복사
print(c)
c[0] = 'apple'
print(c)
print(a) # c만 바뀐것을 확인할 수 있다.

import copy

d = ['a', 'b', 'c']
e = copy.deepcopy(d)
print(e)
e[0] = 1
print(e)
print(d)

