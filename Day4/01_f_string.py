# f'string 사용
# 3.6 이상
tea = 'coffee'
n = 5
s1 = f'나는 {tea}를 좋아해요. 하루에 {n}잔 마셔요'
print(s1)


name = 'kmlee'
phone = '123-1234'
s = name + phone
print(s)

print(f'이름은 {name}이고, 폰번호는 {phone}')
print('이름은 {}이고, 폰번호는 {}'.format(name, phone))
