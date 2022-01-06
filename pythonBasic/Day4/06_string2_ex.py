# 도시명을 입력하고 해당 도시가 있는지 유무를 출력하기
city = input('도시 입력: ')
cities = '인천 대구 대전 부산 울산 청주 춘천'

if cities.find(city) != -1:
    print('해당 도시가 있습니다.')
else:
    print('존재 하지 않는 도시입니다.')

# in 을 이용
if city in cities:
    print('해당 도시가 있습니다.')
else:
    print('존재 하지 않는 도시입니다.')
