# Set : 집합 형태의 자료 구조 (집합 자료형)

# set 생성
s1 = {1, 2, 3, 4, 5}
s2 = set([3,4,7,8,9])
s3 = set()
print(s1)
print(s2)
print(type(s1))
print(type(s2))
print(dir(s1))

# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__',
#  '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
#  '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
#  '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update',
#  'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
#  'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# set의 특징
# 중복을 허용하지 않음 : unhashable typed
# 순서가 없음
# 수를 적으면 알아서 정렬해서 저장해준다.
# 딕셔너리에서 키값만 저장한다고 생각하면 된다.
s4 = {1,3,2,2,5,4,3}
print(s4)

# 인덱스 사용 불가 : 이미 포함되어 있는 요소를 변경할 수 없음
# 추가, 삭제 가능

## 하나 씩 추가할 때 : add()
s4.add(10) # 10을 추가
print(s4) # 10이 추가된걸 확인

## 여러 개 추가할 때 update()
s4.update([6,7]) # 리스트형태로 6 7을 추가
print(s4)



## 요소 삭제 :
## .remove()는 삭제할 값이 없으면 에러, .discard()는 요소 값이 없는 경우 에러가 없다.
s4.remove(1)
s4.discard(20)
print(s4) # 1이 삭제된 것을 확인할 수 있다.
## 요소 전체 제거 .clear() = > 빈 집합 만들기
s4.clear()
print(s4)
## 집합 자체를 제거 del
del s6



# 집합 안에 변경가능한 항목 포함 불가능
#      : 리스트 포함 불가, 튜플 포함 가능

# s5 = {1, 2, [3, 4]} # 리스트가 포함되어있어 에러
s6 = {1,2,(3,4)} # 튜플로는 가능
print(s6) # {1,2,(3,4)}
