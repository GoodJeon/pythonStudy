# 연습문제1
# 현금이 5,000원이 있고, 사탕 가격이 120원인 경우
# 최대한 살 수 있는 사탕의 개수와 나머지 돈은 얼마인가?

cash = 5000
candy_price = 120
num_candies = cash // candy_price
change = cash % candy_price
print(f'사탕의 개수: {num_candies}개')
print(f'잔돈: {change}원')
