# 학생 10명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기
# 80점 이상의 학생 수도 출력하기
scores = []
sum = 0
high = 0
for i in range(10):
    scores.append(int(input(f'학생 {i+1} 점수 입력 : ')))
    sum += scores[i]
    if scores[i] >= 80:
        high += 1

avg = sum / 10

print('총점 : {:d}\n평균 : {:.2f}'.format(sum, avg))
print('80점 이상의 학생 수는 {}명 이다.'.format(high))