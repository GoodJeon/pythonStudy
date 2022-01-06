# 문자열 결합(삽입) : join()
# 각 문자 사이에 특정문자(열) 삽입하여 결합

a = 'aa'
print(a.join('bbb')) #baabaab

a = ','
print(a.join('1234')) # 1,2,3,4

a = '-'
print(a.join('1234')) # 1-2-3-4