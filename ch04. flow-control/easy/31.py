# 배달일 때만 거리(int)를 추가로 입력받으세요.
order_type = input()
price = 15000

# 배달이면 거리(km, 정수)를 추가로 입력받기
if order_type == "배달":
    distance = int(input())
    # 거리가 3km 이하면 배달비는 2000원
    if distance <= 3:
        fee = 2000
    # 거리가 3km 초과면 배달비는 3500원
    else:
        fee = 3500
    total = price + fee
    print(f"배달 주문: 음식 {price}원 + 배달비 {fee}원 = 총 {total}원")
# 포장이면 2000원 할인
elif order_type == "포장":
    fee = 2000
    total = price - fee
    print(f"포장 주문: 음식 {price}원 - 할인 {fee}원 = 총 {total}원")
# 그 외는 "잘못된 주문 방식입니다."
else:
    print("잘못된 주문 방식입니다.")