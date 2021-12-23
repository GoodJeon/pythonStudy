# 리스트(list)
# 동일한 이름을 갖는 원소들의 연속 저장 영역
# 여러 개의 데이터가 저장되어 있는 장소 (집합적 자료형)
# 각 원소는 인덱스(index)로 구분(인덱스:0부터 시작)
# 원소(값) 변경 가능
# 대괄호[] 사용
#    리스트 = [값1, 값2, ....]
#    scores = [32,56,64,72,12]

# 리스트의 특징
# 리스트의 크기는 가변적 - 삽입, 삭제, 변경
# 다양한 형식의 데이터 : 숫자, 문자열, 논리
# 리스트 : [ ]
# 다양한 종류의 데이터를 하나의 리스트 안에 저장 가능
# myList = [12, 'dog', 180.14] # int, str, float
# myList = [12, 'dog', 180.14, '홍길동'] # int, str, float, str

# 리스트 생성
list1 = []    # 빈 리스트 생성
print(list1)    # [] <- 비어있는 리스트
print(type(list1))    # <class 'list'>
list2 = list()    # 빈 리스트 생성
print(list2)    # [] <- 비어있는 리스트
print(type(list2))    # <class 'list'>
list3 = [1, 2, 3]    # 값을 넣어서 리스트생성 가능
print(list3)    # [1,2,3]
list4 = [1, 'apple', 3.5, [10,20,30], True]    # 다양한 형식을 입력가능
print(list4)

# 각 요소들을 따로따로 프린트하고 싶다!
for i in list4:
    print(i, end = ' : ')
    print(type(i))

# 리스트의 문자열 길이를 활용 : len(리스트이름)
# 리스트 인덱싱 : 리스트의 인덱스를 이용하여 접근 : 리스트명[indexId]
print('문자열의 길이 : ', len(list4))   # 리스트의 길이가 5인것을 확인할 수 있다.
for i in range(0, len(list4)):
    print(list4[i], end = ' : ')
    print(type(list4[i]))

# 리스트의 각각의 값은 변수에 저장 가능
nums = [1,2,3]
a,b,c = nums # 변수의 개수와 리스트의 길이가 같다면 자동 할당 가능!
print(a)
print(b)
print(c)
