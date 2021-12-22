#문제 : 1부터 10가지 더하기
sum = 0
for i in range(1, 11):
    sum += i
    print(i, sum)

# A) 1 2 3 4 5 6 7 8 9 10
# sumX = 0 + 1
# sumX = 0 + 1 + 2
# sumX = 0 + 1 + 2 + ... + 10
# for x in range(1, 11):
#     sumX = sumX + x

# 대입연산자 : += -= /=
# x += 1 : x = x + 1
# x -= 1 : x = x - 1
# x += 2 : x = x + 2


# 문제 : 1~10 까지의 홀수만 더한 결과 출력
sum = 0
for i in range(1,101, 2):
    sum += i
    print(i, sum)

sum = 0
for i in range(1, 101):   # 나누기 때문에 연산횟수가 더 많다.
    if i % 2 == 1:
        sum += i
    print(i,sum)


# 1 ~ 100 사이 정수 중 홀수와 짝수의 합을 각각 구하여 출력하기
sum1 = sum2 = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum1 += i
    else:
        sum2 += i
    print('정수: %d' % i, '홀수합: %d' % sum1, '짝수합: %d' % sum2)

# 연산을 더 줄일 수 있는 방법
a = b = 0
for i in range(1, 101, 2):
    a += i
    b += i+1
print(a, b)


#1~100 사이의 3의 배수 출력하고 더하기
sum3 = 0
for i in range(3, 101, 3):
    sum3 += i
    print(i, sum3)
print(sum3)

sumI = 0
for i in range(100):
    if i % 3 == 0:
        sumI += i
        print(i)
print(sumI)