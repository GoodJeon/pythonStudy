# 파이썬이 처리하는 자료형(data Type)
# 정수(int), 실수(float), 문자열(str), 불리언(bool)

# 정수 : 2진수 10진수, 8진수, 16진수
# 실수 : 3.14 1.2e3   5.2e-5
# 문자열 : ' ' " "
# 불리언(논리) : True False

a = 100
b = 3.14
c = 'name'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형변환 :
# str() : 문자열로 변환
print(type(str(100)))
str1 = str(3.14)
print(str1 + ' pie')

# int() : 정수형으로 변환
str2 = '123'
num1 = int(str2)
print(type(num1))
print(num1 * 2)

# float() : 실수형으로 변환
num2 = float(str1)
print(type(num2))
print(num2 + 4)
print(num2 + 10)

#int(x, y) y인자가 2면 x를 2진수로 생각 8이면 8 16이면 16
print(int('1010', 2)) # 2^3 * 1 + 2^1 * 1 = 10
print(int('1010', 8)) # 8^3 * 1 + 8^1 * 1 = 520
print(int('1010', 16)) # 16^3 * 1 + 16^1 * 1 =4112
