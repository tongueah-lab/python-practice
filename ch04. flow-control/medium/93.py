# while + if/elif + break/continue를 사용하세요.
money = int(input())

# 반복하기
while True:
    # 잔액이 500원 미만이면 반복 종료하기
    if money < 500:
        break
    # 500원 미만이 아니면 음료 반복하기
    else:
        # 음료판 적기
        print(f"잔액: {money}원\n1. 물 (500원)\n2. 주스 (1000원)\n3. 커피 (1500원)")
        # 음료 번호 입력받기
        number = int(input())
        # 1번은 물이고 가격은 500원
        if number == 1:
            result = "물"
            price = 500
            # 잔액 >= 가격이면 잔액 차감 후, 물 선택했다고 출력하기
            if money >= price:
                money -= price
                print(f"{result}를 선택했습니다.")
            # 그렇지 않으면 잔액 부족 출력하고 반복문 종료하기
            else:
                print("잔액이 부족합니다.")
                break
        # 2번은 주스이고 가격은 1000원
        elif number == 2:
            result = "주스"
            price = 1000
            # 잔액 >= 가격이면 잔액 차감 후 주스 선택했다고 출력하기
            if money >= price:
                money -= price
                print(f"{result}를 선택했습니다.")
            # 그렇지 않으면 잔액 부족 출력하고 반복문 종료하기
            else:
                print("잔액이 부족합니다.")
                break
        # 3번은 커피이고 가격은 1500원
        elif number == 3:
            result = "커피"
            price = 1500
            # 잔액 >= 가격이면 잔액 차감 후 커피 선택했다고 출력하기
            if money >= price:
                money -= price
                print(f"{result}를 선택했습니다.")
            # 그렇지 않으면 잔액 부족 출력하고 반복문 종료하기
            else:
                print("잔액이 부족합니다.")
                break
        # 선택이 1/2/3이 아니면 잘못된 선택이라고 출력하고 다시 반복하기
        else:
            print("잘못된 선택입니다.")
            continue
# 반복문 종료 후 남은 금액 출력하기
print(f"남은 금액: {money}원")