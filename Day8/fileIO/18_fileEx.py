# 1.
# 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# 한줄의 두 숫자를 더한 연산 결과를 파일에 저장하기

input_file = 'list_num.txt'
f = open(input_file, 'r', encoding='utf-8')
lines = f.readlines()
print(lines)

a = []
# 줄 별로 나눴다.
for line in lines:
    b = line.split()
    if b != []:
        a.append(b)

print(a)

b = []
for i in a:
    sum = 0
    for j in i:
        sum += int(j)
    if sum != 0:
        b.append(sum)
print(b)

f.close()


f = open('list_calcul.txt', 'w', encoding='utf-8')
for w in range(len(a)):
    f.write((f'{a[w][0]}+{a[w][1]}={b[w]}\n'))

f.close()








# 2. 텍스트파일로 되어 있는 가사의 단어 카운트
