# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 tax, ship 이 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# 함수 정의하기
def price_with_options(base, tax=10, ship=0):
    # 값 반환하기
    return base + base * tax // 100 + ship

# 토큰 1개
if len(parts) == 1:
    print(price_with_options(int(parts[0])))
elif len(parts) == 2:
    print(price_with_options(int(parts[0]), int(parts[1])))
elif len(parts) == 3:
    print(price_with_options(int(parts[0]), int(parts[1]), int(parts[2])))