# 리스트에서 in / not in

num = [1,2,4,5,7]

result = 2 in num # 왼쪽이 찾는 요소 오른쪽이 찾는 곳
print(result) # 2가 있으므로 True

result = -10 in num
print(result) # -10이 없으므로 False

result = -10 not in num
print(result) # -10이 없으므로 True



