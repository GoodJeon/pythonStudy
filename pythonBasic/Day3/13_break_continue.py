# while & continue

# for문 시작이 0인데 break는 바로 나머지가 0인 0이 나오자마자 명령이 종료된다.
for i in range(10):
    if i % 2 == 0:
        break
    print(i)

print('---------------')
# continue는 다음 반복을 수행하게 한다
# 짝수를 제외한 1 3 5 7 9 출력
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('-------------')
i = 1
while i < 10:
    if i % 2 == 0:
        break
    print(i)
    i += 1

print('-----------------')
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

