# 문자열에서 사용되는 연산 함수(메소드)들

# len() : 문자열 길이 반환
string = 'programming'
print(len(string))

# .count() : 문자열 내에 들어있는 특정 문자(열)의 개수 반환
print(string.count('m')) # programming에는 m이 두개다!
print(string.count('r')) # r도 2개!
print(string.count('ing')) # ing는 1개다


# .find() : (찾을문자[, start [,end]])
# 문자열 내에서 특정 문자(열)이 존재하는지 여부와 문자열의 시작 위치를 반환
crawling = 'Data crawling is fun'
print(crawling.find('is')) #is가 14번째 위치에 있는 것을 확인시켜준다
print(crawling.find('parsing')) # 찾는 문자열이 없는 경우 -1을 반환
print(crawling.find('is', 15))
print(crawling.find('is', 5, 10))


# .index() : (찾을문자[, start [,end]])
# 문자열 내에서 특정문자열의 시작 위치를 반환
# 찾는 문자열이 없으면 에러를 반환
print(crawling.index('is'))
# print(crawling.index('parsing')) # 에러가 발생한다


# split() : 구분자(공백, 세미콜론, 콜론, 콤마...)를 기준으로 문자열 나눔
# 리스트로 반환

cities = '인천 대구 대전 부산 울산 청주 춘천'
cities_split = cities.split()
print(cities_split)

names = '성춘향;변학도;이몽룡;방자'
names_split = names.split(';')
print(names_split)

for name in names_split:
    print(name)

