# 연습문제
# 출력결과
# 국어점수 입력 : 90
# 영어점수 입력 : 90
# 수학점수 입력 : 70
# 총점 : 250
# 평균 : 83.33

kor = int(input("국어점수를 입력해주세요: "))
eng = int(input("영어점수를 입력해주세요: "))
math = int(input("수학점수를 입력해주세요: "))
tot = kor + eng + math
avg = tot / 3
print('총점: %d\n평균: %.2f' % (tot, avg))

# 연습문제2
# BMI 지수 계산
# 몸무게/(키*키)
# 몸무게(kg):
# 키(미터):
# 출력
# 당신의 BMI는 OO이며, OOO입니다.
weight = input('몸무게(kg): ')
height = input('키(m): ' )
BMI = float(weight) / (float(height) ** 2)
if BMI < 18.5:
    a = '저체중'
elif 18.5 < BMI <= 22.9:
    a= "정상"
elif 23 < BMI <= 24.9:
    a= "과체중"
elif 25 < BMI <= 29.9:
    a = "경도비만"
elif 30 < BMI <= 39.9:
    a = "중등도비만"
else:
    a = "고도비만"
print('당신의 BMI는 %.2f이며, %s입니다.' % (BMI, a))