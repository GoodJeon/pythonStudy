# 에러 발생


# 0으로 나눈 경우
# ZeroDivisionError: division by zero
# print(10/0)


# 자료형
# TypeError: can only concatenate str (not "int") to str
# print('나이: ' + 23 + '살')

# NameError: name 'b' is not defined
# print(b)


# ValueError: incomplete format
# b = 10
# print('%d%' % b)

# SyntaxError: expected ':'
# if b > 10
#     print('합격')


# IndexError: list index out of range
# a = [1,2,3,4]
# print(a[4])



# UnboundLocalError: local variable 'a' referenced before assignment
# def add():
#     a = a + 1
#
# add()


# ModuleNotFoundError: No module named 'mymodule'
# import mymodule


# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# f = open('test.txt', 'r')
# data = f.read()
# f.close()


# OSError: [Errno 22] Invalid argument: 'c:\test.txt'
# f = open('c:\test.txt', 'r')
# f.close()



