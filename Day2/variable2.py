# 화씨 온도를 섭씨 온도로 변환하기

fTemp = 80
cTemp = (fTemp - 32) * 5 / 9

print(cTemp)

# 포매팅
print('%f' % cTemp) # default : 소수점 이하 6자리
print('%.2f' % cTemp) # 소수점 이하 2자리
print('%5.2f' % cTemp)

# format()함수
#   format(실수, '전체자리수.소수이하자리수<서식기호>')
print(format(cTemp, '.2f')) # print('%.2f' % cTemp)와 같다.

# 포맷을 이용해 2개 이상의 값 출력
print('화씨: %d\n섭씨: %f' % (fTemp, cTemp))
