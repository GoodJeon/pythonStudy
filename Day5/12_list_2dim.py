# 2차원 리스트

data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14]]
print(data)

for row in data :
    print(row)

row = len(data) # 콤마로 구분되는 데이터의 길이
col = len(data[0])

for r in range(row):
    for c in range(col):
        print(data[r][c], end = '\t')
    print()