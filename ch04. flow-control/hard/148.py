# while True와 if/elif로 메뉴 분기를 구현하세요.
balance = 100000
withdraw_limit = 500000

# 시스템 반복하기
while True:
    # 메뉴판 출력하기
    print("===== ATM =====")
    print("1. 입금\n2. 출금\n3. 잔액조회\n4. 종료")
    # 메뉴 입력받기
    menu = input()

    # 입금(1)을 누르면 금액 입력받기
    if menu == "1":
        price = int(input())
        # 양수면 잔액에 더한 후 현재 잔액 출력하기
        if price > 0:
            balance += price
            print(f"{price}원이 입금되었습니다.")
            print(f"현재 잔액: {balance}원") 
        # 아니면 입금액은 양수여야 한다고 출력하기
        else:
            print("입금액은 양수여야 합니다.")
    
    # 출금(2)을 누르면 금액 입력받기
    elif menu == "2":
        price = int(input())
        # 양수가 아니면 출금액은 양수여야 한다고 출력하기
        if price <= 0:
            print("출금액은 양수여야 합니다.")
        # 한도 초과면 1회 출금 한도를 초과했다고 출력하기
        elif price > withdraw_limit:
            print("1회 출금 한도(500000원)를 초과했습니다.")
        # 잔액 부족이면 잔액이 부족하다고 하고 현재 잔액 출력하기
        elif price > balance:
            print(f"잔액이 부족합니다. 현재 잔액: {balance}원")
        # 성공이면 금액원이 출금 되었다고하고 현재 잔액 출력하기
        else:
            balance -= price
            print(f"{price}원이 출금되었습니다.")
            print(f"현재 잔액: {balance}원")
    # 조회(3)을 누르면
    elif menu == "3":
        # 현재 잔액 출력하기
        print(f"현재 잔액: {balance}원")
    # 종료(4)를 누르면 
    elif menu == "4":
        # 이용해 주셔서 감사합니다.라고 출력 후 반복문 종료하기
        print("이용해 주셔서 감사합니다.")
        break
    # 그 외는 번호를 누르면
    else:
        # 잘못된 메뉴이고 다시 선택하라고 출력하기
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")
    # 빈 줄 출력하기
    print()