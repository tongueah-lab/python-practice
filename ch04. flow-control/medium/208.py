# N개 상품 가격을 입력받아 조건부 할인 후 총액을 출력하세요.
n = int(input())


# 총합 초기값 초기화하기
total = 0

# 상품 n번 반복하기
for i in range(n):
    # 가격 입력받기
    price = int(input())
        
    # 가격이 10000원 이상이면
    if price >= 10000:
        # 20% 할인을 적용하고 합산하기
        price = price - (price * 0.20)
        total += price
    # 10000원 미만 상품은 원래 가격 그대로 합산하기
    else:
        total += price

# 총액 출력하기
print(f"총액: {int(total)}원")