# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = input().split()

# 총액 계산 함수 정의하기
def total_price(unit_price, count=1):
    # 값 반환하기
    return unit_price * count

# 토큰이 1개면 기본 수량(1)
if len(parts) == 1:
    print(total_price(int(parts[0])))
# 2개면 둘째 값이 수량임
else:
    print(total_price(int(parts[0]), int(parts[1])))