# 리스트의 요소 제거
# remove(값) : 지정한 값을 제거, 제일 처음 만나는 값만 제거, 동일한 값은 한번에 제거할 수 없음
# pop() : 마지막의 요소 값을 제거
# pop(index) : index 위치 요소값을 제거할 수 있다.

x = ['apple', 'banana', 'coconut', 'melon', 'banana', 'apple']
print(x)
x.remove('melon') # 리스트 안의 멜론 삭제
print(x)
x.remove('banana') # 리스트 안에 있는 처음 바나나를 삭제, 첫 해당값을 삭제해준다.
print(x)
n = x.count('banana')
for i in range(n): # for문을 사용해 있는 바나나를 모두 제거!
    x.remove('banana')
print(x)



y = [1,3,5,1,10]
last = y.pop() #y의 가장 마지막 값 10을 last에 저장해줄 수도 있다.
print(y)
print(last)
y.append(-10)
print(y)
rm = y.pop(3) # y리스트의 3위치에 있는 1을 빼고 rm에 들어감
print(y) # [1,3,5,-10]
print(rm) # 1
# y.remove(0) 없는 0값은 지워지지않고 에러가 난다.
y[3] = 'list' # y리스트의 3번위치 값을 list로 변경
print(y)

y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
y.pop()
print(y)
