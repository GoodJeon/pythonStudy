# readline() : 한줄 씩 읽어오기

# 한줄만 출력
f = open('test.txt', 'r', encoding='utf-8')
line = f.readline()  # 첫번째 라인 1개 읽기
print(line)
f.close()


# 한줄 씩 끝까지 읽어오기
f2 = open('test.txt', 'r', encoding='utf-8')

while True:
    line = f2.readline() # .readline() 뒤에는 \n가 내재되어있다고 생각하면 된다.
    if not line:
        break
    print(line, end='') # end=''를 사용함으로 한줄의 공백들이 사라진다.

f2.close()

