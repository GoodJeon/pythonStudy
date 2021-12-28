# 문제 : 파티에 참석한 사람이 다음과 같을 때 집합 생성하고 다음과 같이 출력
# 파티에 참석한 모든 사람
# {'몽룡', 'Park', 'Kim', 'Lee', '길동'}
# ----------------------
# 2개의 파티에 모두 참석한 사람
# {'Park'}
# ----------------------
# 파티A에만 참석한 사람
# {'Kim', 'Lee'}
# ----------------

# 파티B에만 참석한 사람
# {'몽룡', '길동'}

partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}
# partyA = set(['Park','Kim','Lee'])
# partyB = set(['Park','길동','몽룡'])
print('파티에 참석한 모든 사람')
print(partyA.union(partyB))
print('--------------------')
print('2개의 파티에 모두 참석한 사람')
print(partyA.intersection(partyB))
print('--------------------')
print('파티A에만 참석한 사람')
print(partyA.difference(partyB))
print('--------------------')
print('파티B에만 참석한 사람')
print(partyB.difference(partyA))