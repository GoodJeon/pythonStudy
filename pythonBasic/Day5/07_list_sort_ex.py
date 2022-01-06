# 학생 n명의 점수를 입력받아서 리스트로 생성하고 총점과 평균을 계산하여 출력하기
# 80점 이상의 학생 수도 출력하기
# 성적을 내림차순으로 정렬

scores = []
sum = 0
high = 0
n = int(input('학생들의 수는?!'))
for i in range(1, n+1):
    scores.append(int(input(f'학생 {i} 점수 입력 : ')))
    sum += scores[i-1]
    if scores[i-1] >= 80:
        high += 1

avg = sum / n

print('총점 : {:d}\n평균 : {:.2f}'.format(sum, avg))
print('80점 이상의 학생 수는 {}명 이다.'.format(high))

# scores.sort(reverse=True)
sort_scores = sorted(scores, reverse=True)
print(sort_scores)
