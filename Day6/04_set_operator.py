# set의 연산
A = {1,2,3}
B = {3,4,5}

# 1) 교집합 & (intersection)
C = A & B
print(C) # 교집합은 3
C = A.intersection(B)
print(C)

# 2) 합집합 | (union)
C = A | B
print(C) # 합집합은 1,2,3,4,5
C = A.union(B)
print(C)

# 3) 차집합 - (difference)
C = A - B
print(C) # 1,2
D = B - A # 4,5
print(D)
C = A.difference(B)
print(C)
D = B.difference(A)
print(D)

