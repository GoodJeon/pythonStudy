from datetime import date, datetime, timedelta

print(date.today()) # 2021-12-23
print(datetime.today()) # 2021-12-23 ~현재시각(ms까지)~

today = date.today()
year = today.year
month = today.month
day = today.day
print(f'연도 : {year}\n월 : {month}\n일 : {day}')
print('연도 : {0}\n월 : {1}\n일 : {2}'.format(year, month, day))
#print(datetime.today())
current_hour = datetime.now().time().hour # 현재 시간 가져오기
current_minute = datetime.now().time().minute # 현재 분 가져오기
current_second = datetime.now().time().second # 현재 초 가져오기
current_microsecond = datetime.now().time().microsecond # 현재 미리세컨즈 가져오기

# 날짜 계산 :timedelta() 함수 사용
print(today + timedelta(days = -1)) # 어제 날짜
print(today + timedelta(days = 1)) # 내일 날짜
print(today + timedelta(days = -7)) # 일주일 이전 날짜
print(today + timedelta(days = 7)) # 일주일 이후 날짜


cur_now = datetime.now()
print(cur_now + timedelta(hours = -1)) # 현재부터 1시간 전
print(cur_now + timedelta(days = 1, hours = 2)) # 현재부터 26시간 뒤

# strftime()함수 : 날짜 형식을 문자열로 반환
# m = month, M = minute
# H : 24 시간, I : 12시간
# p = AM,PM(오전,오후)
print(today.strftime('%Y-%m-%d %H:%M:%S')) # today가 date.today라 00시00분00초로 나옴
print(today.strftime('%Y-%m-%d %I:%M:%S %p'))

# strptime() 함수 : 문자열을 날짜형식으로 반환
today = '2020-06-20 17:40:20'
transToday = datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
print(transToday)
print(type(transToday)) # class 'datetime.datetime'
