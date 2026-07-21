# 층수를 입력받아 각 층의 요금과 누적 요금을 출력하세요.
n = int(input())

# 가격 초기화하기
price = 0
# 전체 초기화하기
total = 0

# 1부터 n까지 반복하기
for i in range(1, n + 1):
    # 층마다 100원씩 곱하고 누적하기
    price = i * 100
    total += price

    # 출력하기
    print(f"{i}층: {price}원 (누적: {total}원)")