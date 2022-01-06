#  문제: 각 학생별 점수 리스트 생성
# 순서대로 국어, 수학, 영어 점수다
kim = [90, 85 , 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 70]

students = [kim, choi, kang, lee]
students_name = ['kim', 'choi', 'kang', 'lee']

# 학생별 총점과 평균점수 출력
# 과목별 총점과 평균점수 출력


# print('kim 총점: {} 평균: {:.2f}'.format(sum(kim), sum(kim) / len(kim)))
# print('choi 총점: {} 평균: {:.2f}'.format(sum(choi), sum(choi) / len(choi)))
# print('kang 총점: {} 평균: {:.2f}'.format(sum(kang), sum(kang) / len(kang)))
# print('lee 총점: {} 평균: {:.2f}'.format(sum(lee), sum(lee) / len(lee)))

for i in range(len(students)):
    students_sum = sum(students[i])
    print(students_name[i], '총점 :', students_sum, '평균 :' , round(students_sum/len(students[i]), 2))

row = len(students)
col = len(students[0])

sub_name = ['kor', 'math', 'english']
for c in range(col):
    sub_sum = 0
    for d in range(row):
        sub_sum += students[d][c]
    print(sub_name[c], '과목 총점 :', sub_sum)
    print(sub_name[c], '과목 평균 :', sub_sum/len(students))

#
# kor = []
# math = []
# eng = []
#
# for r in range(row):
#         kor.append(students[r][0])
#         math.append(students[r][1])
#         eng.append(students[r][2])
#
# print('kor 총점: {}, 평균: {}'.format(sum(kor), sum(kor)/len(kor)))
# print('math 총점: {}, 평균: {}'.format(sum(math), sum(math)/len(math)))
# print('eng 총점: {}, 평균: {}'.format(sum(eng), sum(eng)/len(eng)))
