# 리스트 인덱싱(indexing)
# : 리스트에서 인덱스 연산자를 통하여 요소를 참조/접근하는 방법

a = [1, 'apple', 3.5, [10,20,30], True]

print(a[0]) # a라는 리스트의 첫번째 요소 : 1
print(a[-1]) # a라는 리스트의 마지막 요소 : True
print(a[-5]) # 뒤에서부터 앞으로 5번째의 요소 : 1
print(a[3]) # 네번째 요소 [10,20,30]
print(a[3][0]) # 2차원 리스트로 [10,20,30]의 10을 가져온다.

b = ['apple', 'banana', 'melon']
c = [a, b] # [[1, 'apple', 3.5, [10, 20, 30], True], ['apple', 'banana', 'melon']]
print(c)   #                a리스트                            b리스트
print(c[0][3][1])


