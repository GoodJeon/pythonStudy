# 연습문제
# 두 정수를 입력받아 사칙 연산 결과 출력하기

num1 = input('첫번째 정수를 입력하시오: ')
num2 = input('두번째 정수를 입력하시오: ')
plus = int(num1) + int(num2)
minus = int(num1) - int(num2)
multi = int(num1) * int(num2)
division = int(num1) / int(num2)
result = [plus, minus, multi, division]
print(result)

print('두 정수의 합은 %d입니다.' % plus)
print('두 정수의 차는 %d입니다.' % minus)
print('두 정수의 곱은 %d입니다.' % multi)
print('두 정수의 나누기는 %d입니다.' % division)
print('합 차 곱 분 : %d %d %d %d' % (plus, minus, multi, division))
