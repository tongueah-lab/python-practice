# 반복문으로 각 음료 가격을 입력받아 포인트를 누적하세요
n = int(input())

# 총 적립 포인트 초기화하기
total_points = 0

# 음료 반복하기
for i in range(n):
    # 가격 입력받기
    price = int(input())

    # 각 음료 가격의 5% 포인트 계산 후 누적 (정수 나눗셈으로 부동소수점 오차 방지)
    total_points += price * 5 // 100

    
    # # 각 음료 가격의 5% 포인트 계산하기
    # point = int(price * 0.05)
    # # 포인트 누적하기
    # total += point
    
# # 스탬프는 3잔마다 1개
stamp = n // 3

# 총 구매 출력하기
print(f"총 구매: {n}잔")
# 총 적립 포인트 출력하기
print(f"총 적립 포인트: {total_points}점")
# 스탬프 출력하기
print(f"스탬프: {stamp}개")