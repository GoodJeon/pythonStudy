# 리스트 반환
# 3명 이름을 입력 받아서 리스트에 저장하고 리스트를 받환하는 함수
# get_names()

def get_names():
    names = []
    for i in range(3):
        name = input('이름 입력: ')
        names.append(name)
    return names

# nameList = get_names()
# print(nameList)
# print(type(nameList))

# 이름과 나이를 입력받고 그 정보를 딕셔너리 형식으로 반환
# get_info()

def get_info():
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))
    info = {'name' : name, 'age' : age}
    return info

# std_info = get_info()
# print(std_info)
# print(type(std_info))


# 반환값이 없어서 그냥 바로 출력만 되고 변수에 저장이 안된다.
def hello():
    print('hello!!!')

result = hello() # 변수에 저장이 안됌. 반환값이 없어서.
print(result) # None


