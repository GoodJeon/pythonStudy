# lambda(람다)함수 : 함수를 한줄로 간단하게 작성

def add(x,y):
    return x + y

print(add(10, 20))

add2 = lambda x,y :  x+y
print(add2(10,20))

# 매개변수에 기본값을 설정

add3 = lambda x=10,y=10 :  x+y
print(add3(10,20))
print(add3())



# 문제. 리스트의 각 요소에 10을 더하는 함수
# def add10(num):
#     for i in range(len(num)):
#         num[i] += 10

num = [1,3,4,10]
# add10(num)
# print(num)


# 10을 더하는 함수
def add10(num):
    return num + 10
# lambda num : num+10
print(num)

for i in range(len(num)):
    num[i] = add10(num[i])

print(num)



# map() 함수
num2 = list(map(add10, num))
print(num2)

# lambda 함수 & map()
num3 = list(map(lambda num: num + 10 , num))
print(num3)



# (lambda 매개변수들: 식)(인수들)
# 람다 표현식을 변수에 할당하지 않고 그 자체를 호출해서 사용
(lambda x:x+10)(25)

# 람다 표현식안에서 변수 생성 불가
# (lambda x : y=10; x+y)(5)

y = 10
(lambda x : x+y)(5)


# 문제2. 두 리스트의 각 자리수의 값을 합해서 새로운 리스트를 생성

list1 = [1,2,3,4]
list2 = [10,20,30,40]

def addList(x,y):
    list = []
    for i in range(len(x)):
        list.append(x[i] + y[i])
    return list
new_list = addList(list1,list2)
print(new_list)

# lambda & map 사용
new_list2 = list(map(lambda x,y : x + y, list1,list2))
print(new_list2)