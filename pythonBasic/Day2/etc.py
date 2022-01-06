# 입력 내용이 긴 경우 여러 줄에 작성해야 하는 경우에
# ()괄호나 \백슬래쉬를 사용한다.

sum = (1 + 2 + 3 + 4 +
   5 + 6 + 7)
print(sum)
sum = 1 + 2 + 3 + 4 + \
   5 + 6 + 7
print(sum)

# 한줄로 인식
print("긴 문장으로 표현할       "
      " 두번째 "
      " 세번째")
# 여러 줄로 출력하고 싶으면 \n 을 사용
print("긴 문장으로 표현할       \n"
      " 두번째 \n"
      " 세번째")

# 이스케이핑(Escaping)
# escpae character
# \n : 줄바꿈
# \t : tab
# \' : '
# \" : "
# \\ : \

print('don\'t')
print('123\t 456')
print('He said, "yes"') # '""'
print("He said, \"yes\"") # "\"\""
print('c:\\pythonStudy\\day2') # \\
print(r'c:\pythonStudy\day2') # 앞에 r을 사용하면 특수문자 의미 제거

# 2개 명령어(문장)을 한줄에 입력할때
# 세미콜론(;)을 사용
print("hi") ; print("bye")

# print문 뒤의 default 값은 '\n'이다.
# 변경을 원하면 end문을 사용.
print('apple\nbanana\nmelon')
print('apple', end='')
print('banana', end='*')
print('melon')
