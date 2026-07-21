# 잔액이 가격보다 적으면 "잔액이 부족합니다"를 출력하세요.
price = int(input())
balance = int(input())

# 잔액이 가격보다 적으면 "잔액이 부족합니다" 출력하기
if balance < price:
    print("잔액이 부족합니다")