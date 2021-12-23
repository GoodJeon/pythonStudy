# 문자열 인덱싱(indexing)
# 인덱스로 문자의 위치를 나타내는 것
# 인덱스(첨자) ; 문자의 위치, 0부터 시작
# string[0]: 인덱스 0번째 문자(첫 번째 문자)
# string[-1]: 마지막 문자



# 슬라이싱(slicing) : 연산자 => 범위 지정
# 문자열 중에서 일부분을 추출하는 것
# 인덱스 사용
# string[n] : 인덱스 n번째 문자
# string[0:n] 0부터 n-1번째까지의 문자열
# string[n:]: n부터 끝까지
# string[:n]: 0부터 n-1까지
# string[-1:]:  마지막 문자
# string[:-1]: 처음부터 마지막까지

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)
print(crawling[0])
print(crawling[-1])
print(crawling[0:4]) # 0~3번째 까지의 문자들
print(crawling[17:])
print(crawling[:18])
print(crawling[-1:]) # 마지막에서 끝까지
print(crawling[:-1])
print(crawling[10:10+5])
