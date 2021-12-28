# Mutable : 변경 가능
# immutable : 변경 불가능
# 수치형, 문자열, 튜플 = immutable
# 리스트, 딕셔너리 = mutable





# 수치형, 문자열 변경 불가능(immutable)
x = '123'
y = x
y += '4'
print(x)
print(y)
print('x id', id(x))
print('y id', id(y))


# 튜플은 변경불가능(immutable)
x = (1, 2)
y = x
y = y + (3,)
print(x)
print(y)
print('x id', id(x))
print('y id', id(y))


# 리스트는 변경가능(mutable)
x = [1, 2]
y = x
y = y.append(3)
print(x)
print(y)
print('x id', id(x))
print('y id', id(y))


# 딕셔너리는 변경가능(mutalbe)
x = {1:2}
y = x
y[2] = 3
print(x)
print(y)
print('x id', id(x))
print('y id', id(y))
