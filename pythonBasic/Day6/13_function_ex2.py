# 문제
# 지불액 계산:
#   주문액이 10만원 이상이면 10% 할인
#   주문액이 5만원이상 10만원 미만이면 5% 할인
#   주문액인 5만원미만이면 할인 없음

def order(price, quantity):
    amount = price * quantity
    if amount >=  100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    else:
        discount = 0
    result = amount - discount
    return amount, discount, result

price = int(input('상품가격 입력: '))
quantity = int(input('주문수량 입력: '))
amount, discount, result = order(price, quantity)

print(f'주문액: {amount}원')
print(f'할인액: {int(discount)}원')
print(f'지불할 금액: {int(result)}원')

