# 1. 텍스트파일로 되어 있는 가사의 단어 카운트
# 파일 입력 -> 카운트 계산 -> 화면 출력

# f = open('yesterday.txt', 'r')
# yesterday = f.readlines() # 행 별로 리스트에 저장
# # yesterday2 = f.read() # 문자열로 들어온다. 바로 스플릿 가능
#
# f.close()
# words = []  # 단어 목록에 해당하는 리스트 생성
# # words2 = yesterday2.split()
#
# for line in yesterday:
#     line = line.split()
#     for w in line:
#         words.append(w.lower()) # 소문자로변경하여 words에 append
#
# wordL = list(set(words)) # 중복되는 단어들을 set로 없애주고 다시 리스트로 만듦
# wordL.sort() # 알파벳 순으로 정렬
#
# wordDict = dict() # 사전 생성
# for w in wordL:
#     wordDict[w] = words.count(w)
#
# for w in wordDict.items():
#     print(f"'{w[0]}' : {w[1]}")

with open('yesterday.txt', 'r') as f:
    yesterday = f.read().lower().replace(',', '')
    yesterday = yesterday.split()
    wordDict = {}
    words = sorted(list(set(yesterday)))

for w in words:
    wordDict[w] = yesterday.count(w)
for w in wordDict.items():
    print(f"'{w[0]}' : {w[1]}")



# 2.
# 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# 한줄의 두 숫자를 더한 연산 결과를 파일에 저장하기
# 파일 입력 -> 계산 -> 파일 출력

def sum(input_file, output_file):
    with open(input_file, 'r') as f: # list_num.txt 파일 읽어들이기
        data = f.readlines()

    with open(output_file, 'w') as f:
        for d in data:
            if d.replace('\n', '') != '': # \n가 있는 것을 공백으로 바꿔주고, d가 빈 문자열이 아니면
                value1, value2= d.split() # 언패킹: d를 나눠 value1과 value2에 저장
                result = int(value1) + int(value2) # 두 값을 정수형으로 변경 후 더해준다.
                f.write(f'{value1} + {value2} = {result}\n') # 출력 예시처럼 출력
            else:
                continue


if __name__ == '__main__': # main : 프로그램 실행 코드
    sum('list_num.txt', 'list_calcul.txt')



# 3. 회원명단을 입력받아 저장하거나, 회원명단파일을 열어 저장되어 있는 회원 명단을 출력하는 프로그램 작성
# 키보드 입력 -> 파일 출력 -> 파일입력 -> 화면 출력

def input_member(input_file):
    with open(input_file, 'w', encoding='utf-8') as f:
        while True:
            member = input('멤버를 입력하세요. (종료는 q) : ')
            if member == 'q':
                break
            else:
                f.write(member+'\n')




def output_member(output_file):
    with open(output_file, 'r', encoding='utf-8') as f:
        print(f.read())

while True:
    sel = input('저장 1, 출력 2, 종료 q : ')
    if sel == '1':
        input_file = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
        input_member(input_file)
        print('저장되었습니다.')
    elif sel == '2':
        output_file = input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(output_file)
    elif sel == 'q':
        break
    else:
        print('잘못 입력하셨습니다.')

