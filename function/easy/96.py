# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인(0), 2개면 둘째 값이 할인액입니다. (값은 정수)
parts = input().split()

# 함수 정의하기
def final_price(price, discount = 0):
    # 값 반환하기
    return price - discount
# 토큰이 1개면 기본 할인
if len(parts) == 1:
    print(final_price(int(parts[0])))
# 2개면 둘째 값이 할인
else:
    print(final_price(int(parts[0]), int(parts[1])))