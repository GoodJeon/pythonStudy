# 상품 가격, 주문 수량을 입력받아서 주문액을 계산하여 반환하는 함수 작성
# 함수명 : order()

# 출력 예시
# 상품가격 입력 :
# 주문수량 입력 :
# ----------------
# 상품 가격 : 1000원
# 주문 수량 : 10개
# 주문액 : 10000원

def order():
    price = int(input('상품 가격 입력 : '))
    quantity = int(input('주문 수량 입력 : '))
    amount = price * quantity
    return price, quantity, amount

# price, quantity, amount = order()
# print('-----------------')
# print(f'상품 가격 : {price}원\n주문 수량 : {quantity}개\n주문액 : {amount}원')
result = order()
print('-----------------')
print(f'상품 가격 : {result[0]}원\n주문 수량 : {result[1]}개\n주문액 : {result[2]}원')