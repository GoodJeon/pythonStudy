# literal: 정수, 실수, 문자, 문자열, 논리값
# 정수 리터럴
'''
여러줄 주석 블록(block)
'''
a = 49
b = 0b110001 # 2진수
c = 0o61    # 0b110001 8진수로 오른쪽부터 3자리씩 끊자.
d = 0x1f2c  # 0b0001111100101100 # 16진수로 오른쪽부터 4자리씩 끊자.
e = 0x31

print(a, b, c, d, e)



# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234e-5
f4 = 1.234e5
print(f1, f2, f3, f4)

# 문자 리터럴
c1 = 'a'
c2 = 'B'

print(c1, c2)

# 문자열 리터럴
str1 = '이경미'
str2 = "Hello"
str3 = '''안녕하세요
반갑습니다'''
str4 = """여러 줄로 나누어
사용할 수 있어요"""

print(str1, str2)
print(str3)
print(str4)

# 논리값 리터럴: True False

t = True
f = False
print(t, f)

# 특수 리터럴 : None
name = '전동준'
phone = ''
address = None

print(name, phone, address)
print(type(address)) # noneType
print(type(phone)) # str


