# 리스트 연산
## 리스트 합치기 : +
## 리스트 곱하기 : * (반복)
## 리스트 내용 변경

fruits = ['apple', 'banana', 'melon']
a = [1, 'apple', 3.5, [10,20,30], True]
b = fruits + a # fruits 리스트와 a 리스트 합치기.
print(b)
c = fruits * 3
print(c) # fruits 리스트를 3번 반복한 새로운 리스트가 생긴다.


a[3] = 'melon'
print(a) # a리스트의 [10,20,30]이 'melon'으로 바뀜~
a[1:3] = [10,11,12]
print(a) # 'apple', 3.5, 'melon' => 10, 11 ,12
a[0] = [-1,-4] # 인덱싱한 부분만 바뀐다
print(a) # 1 => [-1, -4]