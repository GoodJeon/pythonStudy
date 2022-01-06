# 정해진 횟수만큼 반복
# for 변수 in [list] or (range) :
#     반복문장1
#     반복문장2
#     ...

for name in ['apple', 'banana', 'melon']:
    print(name)

# range(시작값, 끝값+1)
# range(끝값+1) : 0~끝값
# range(시작값, 끝값+1, 간격)
for number in range(10): #range(10)일 때 0부터 9까지 출력
    print(number)


for number in range(1, 10):  # 1 ~ 9 까지
    print(number)

for number in range(1, 10, 2): # 1부터 0까지 2간격으로 출력
    print(number)

for number in [1, 3, 5, 7, 9]: # 1부터 0까지 2간격으로 출력
    print(number)

for number in range(9, 0, -2): # 1부터 0까지 2간격으로 출력
    print(number)