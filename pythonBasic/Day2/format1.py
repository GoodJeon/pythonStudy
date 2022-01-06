# 연습문제90
# 총점과 평균을 구해서 출력하기

kor = 90
eng = 80
math = 80
tot = kor + eng + math
avg = tot / 3
#총점:250  , 평균: 83.33
print('총점: %d' % tot, '평균: %.2f' % avg)
print('총점: %d 평균: %.2f' % (tot, avg))
print('총점: {} 평균: {}'.format(tot, round(avg, 2)))
print(f'총점: {tot} 평균: {round(avg, 2)}')
