# extend() : 리스트 확장
a = [1,2,3]
a.extend([4,5]) # a리스트의 뒤에 4,5값을 추가할수있다. 값 그대로 추가
print(a)
a.append(9) # 9라는 값을 추가
print(a)
a.append([-1,10]) # [-1,10]이라는 리스트를 추가하는 것
print(a)
a.insert(3,[1,2]) # 하위리스트로 추가된다.
print(a)

# extend는 append와 insert와 다르게 []로 값을 추가해줄 경우 하위 리스트가 아닌 값으로 각각 들어간다.
