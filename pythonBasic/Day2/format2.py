# .format() 함수와 {}를 사용하여 서식 지정

print(format(1234.567, '10.2f'))
print('name:{}, phone:{}'.format('전동준', '010-1234-5678')) # default : 위치값 0,1,2...
print('name:{1}, phone:{0}'.format('010-1234-5678', '전동준'))
print('{0:d} {1:f}'.format(100, 123)) #{위치값:type지정}
print('{0:d} {1:5d} {2:10d}'.format(123, 123, 123))
print('%d %5d %10d' % (123, 123, 123))


