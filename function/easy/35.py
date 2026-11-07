# 첫 값=가격(price0), 둘째 값=전역 세율 rate. 예: "1000 10" → price0=1000, rate=10
parts = input().split()
price0 = int(parts[0])
rate = int(parts[1])

# 함수 정의하기
def apply(price):
    # 값 반환하기
    return price + price * rate // 100
# 출력하기
print(apply(price0))