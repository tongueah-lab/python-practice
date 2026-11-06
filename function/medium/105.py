# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인율(10), 2개면 둘째 값이 할인율(%)입니다. (정수)
parts = input().split()

# 함수 정의하기
def discount_price(price, rate=10):
    # 값 반환하기
    return price - price * rate // 100

# 토큰이 1개면 기본 할인율
if len(parts) == 1:
    print(discount_price(int(parts[0])))
# 토큰이 2개면 둘째 값이 할인율
elif len(parts) == 2:
    print(discount_price(int(parts[0]), int(parts[1])))