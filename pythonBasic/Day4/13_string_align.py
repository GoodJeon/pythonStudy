# 문자열 정렬 : 정렬 문자 <, >, ^
# 문자 : 왼쪽 정렬, 숫자 : 오른쪽 정렬


# < : 왼쪽 정렬, > : 오른쪽 정렬, ^ : 가운데 정렬
string = 'python'
num = 1234
print('{:<10}'.format(string)) # 10칸에 맞춰 왼쪽을 기준으로 정렬해라
print('{:>10}'.format(string)) # 10칸에 맞춰 오쪽을 기준으로 정렬해라
print('{:^10}'.format(string)) # 10칸에 맞춰 가운데를 기준으로 정렬해라
print('{:6d}'.format(num)) # {:6d}와 같으면 숫자는 무조건 오른쪽에 정렬됨
print('{:06d}'.format(num)) # {:06d}와 같으면 0이 나머지 영역을 채워준다.
print('{:-^10}'.format(string)) # 가운데정렬, -가 양쪽을 채워줌


# ljust(자릿수) : 왼쪽정렬
# rjust() : 오른쪽정렬
# center() : 가운데정렬

print(string.ljust(10))
print(string.rjust(10))
print(string.center(10))


