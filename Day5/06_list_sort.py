# list의 정렬 : 리스트.sort(), 리스트.reverse()
# sorted(리스트) : 원본 리스트를 건들이지 않고 새로운 리스트를 만들어주는 함수

scores = [90, 78, 81, 64, 99]
print('정렬전 : ', scores)
scores.sort()
print('정렬후 : ', scores)

scores = [90, 78, 81, 64, 99]
scores.sort(reverse=True) # 내림차순 정렬
print('내림차순 정렬후 : ', scores)

scores = [90, 78, 81, 64, 99]
scores.reverse()  # 기존 scores 리스트를 역순으로 바꿈
print('reverse() 적용 후 : ', scores)

scores = [90, 78, 81, 64, 99]
result = sorted(scores) # 정렬해주는 함수
print(result)
print(scores)

#메소드는 원본 수정시, 함수는 원본그대로 유지시 쓴다고 생각하면 된다!


# .sort(key=)

chr = ['b','A','e','C']
chr.sort()
print(chr) # 대문자 -> 소문자 오름차순으로 출력(ASCII코드에서 대문자가 먼저나와서)

chr = ['b','A','e','C']
chr.sort(reverse=True)
print(chr) # 소문자 -> 내림차순으로 출력

# 대소문자 구분없이 알파벳순으로  정렬
chr = ['b','A','e','C']
print(chr)
chr.sort(key=str.lower)
print(chr)

#대소문자 구분없이 알파벳역순으로 정렬
chr = ['b','A','e','C']
print(chr)
chr.sort(key=str.lower, reverse=True)
print(chr)

