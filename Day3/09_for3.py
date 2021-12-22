# 중첩 for
for y in range(3):
    for x in range(5):
        print(x, end = " ")
    print()


# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
n = 0
for y in range(1, 4):
    for x in range(n, n+4):
        print(x+n, end = " ")
    n += 4
    print()

for y in range(3):
    for x in range(1, 5):
        print(x + y * 4, end = " ")
    print()


# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
n = 0
for y in range(1, 5):
    for x in range(1, 6):
        print(x+n, end = " ")
    n += 5
    print()