# append() : 파일 끝에 내용을 추가


f = open('test2.txt', 'a', encoding='utf-8')


appendData = '\n\nPython Programming'
f.write(appendData)


f = open('test2.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
