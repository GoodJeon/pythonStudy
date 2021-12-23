# % 서식문자열 : %s, %d, %f, %c
tea = 'coffee'
n = 5
s1 = '나는 %s를 좋아해요. 하루에 %d잔 마셔요' % (tea, n)
print(s1)

# format()함수 사용
print(format(3.141592, '5.2f'))

# string.foramt()
tea = 'coffee'
n = 5
s2 = '나는 {}를 좋아해요. 하루에 {}잔 마셔요'.format(tea, n)
print(s2)
## 위치 인덱스
s2 = '나는 {0}를 좋아해요. 하루에 {1}잔 마셔요'.format(tea, n)
print(s2)
## 변수이름 지정 가능
s2 = '나는 {tea}를 좋아해요. 하루에 {n}잔 마셔요'.format(tea = 'coke', n = 5)
print(s2)
## 실수형 응용
print('{0:.2f} {1:5.8f} {2:05f} '.format(3.14, 3.14, 3.14))

# f'string 사용
# 3.6 이상
tea = 'coffee'
n = 5
s3 = f'나는 {tea}를 좋아해요. 하루에 {n}잔 마셔요'
print(s3)


name = 'kmlee'
phone = '123-1234'
s = name + phone
print(s)

print(f'이름은 {name}이고, 폰번호는 {phone}')
print('이름은 {}이고, 폰번호는 {}'.format(name, phone))


for month in ['1월', '2월', '3월']:
    print(f'이번 달은 {month}입니다.')