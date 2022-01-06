# 내부 함수 : 함수 안에 있는 함수
# 함수가 정의된 그 범위 안에서만 사용가능


def outFunc(x, y):
    def inFunc(a, b):
        return a+b
    return inFunc(x, y)

print(outFunc(10, 20))
# print(inFun(10, 20)) # 내부 함수이기 때문에 쓸 수 없다.
