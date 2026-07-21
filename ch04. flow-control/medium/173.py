# 사이즈별 단가를 정하고, 3판 이상이면 10% 할인
size = input()
qty = int(input())

# 총합 초기화하기
total = 0
# 사이즈가 S 면 가격 8000원
if size == "S":
    price = 8000
    # S 수량 확인하기
    total += price * qty

# 사이즈가 M 이면 가격 12000원
elif size == "M":
    price = 12000
    # M 수량 확인하기 
    total += price * qty

# 사이즈가 L 이면 가격 15000원
else:
    price = 15000
    # L 수량 확인하기
    total += price * qty

# 사이즈랑 수량 출력하기
print(f"사이즈: {size} | 수량: {qty}판")


# 피자가 3판 이상이면 10% 할인하기
if qty >= 3:
    discount_price = int(total * 0.10)
    # 총액 구해서 총액이랑 10% 할인 했다고 출력하기
    total = total - discount_price
    print(f"총액: {total}원")
    print("(10% 할인 적용)")

# 3판 이상이 아니어도 총액 출력하기
else:
    print(f"총액: {total}원")
