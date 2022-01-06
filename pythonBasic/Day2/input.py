# 입력 함수 : input('프롬프트 문자열')
# 키보드로부터 값을 입력 받아서 처리하기 위해
# input으로 받은 값은 항상 데이터 유형은 문자열(str)

x = 100
y = 300

print(x+y)

name = input('이름: ')
age = input('나이: ')
# print(name)
# print(age)
print(type(name))
print(type(age))
print('이름은 %s이고, 나이는 %s입니다.' % (name, age))
print('이름은 %s이고, 나이는 %d입니다.' % (name, int(age)))