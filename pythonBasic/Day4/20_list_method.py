# 함수 : 함수이름()
#         함수이름()으로만 호출해서 사용
# ex)      input(), print(), len(), del(), : 내장함수(예약어)
#         사용자 정의 함수

# 메소드 : 메소드이름()
# 클래스의 멤버인 객체를 통해서 사용
# ex) string객체이름.join(), .find()

# 리스트에서 사용되는 함수 :
# len() => 리스트의 길이 반환(원소의 개수)
a = [1,2,3,4,5]
print(len(a))

# 리스트에서 사용되는 메소드 :
# .count() => 리스트 내의 특정한 요소의 개수를 세기
b = [1,3,2,3,2,3,3,3,1,2,3,3,3]
print(b.count(3))
# 리스트의 요소를 추가 : .append(), .insert()
a.append(6)
print(a)    # .append()는 리스트의 끝에 원하는 값을 추가해준다.
a.insert(6, 7)
print(a)    # .insert(지정위치, 추가하고싶은 값)는 원하는 위치에 값을 추가해준다.

values = [] # 빈 리스트 생성
values.append(10)
values.append(20)
values.append(30)
values.append(40)
print(values)


# 예. 10명의 학생의 점수를 입력받아서 리스트를 생성하고 값을 출력
scores = []
for i in range(10):
    scores.append(int(input('점수입력: ')))
for score in scores:
    print(score, end = ' ')





