# while True, if/elif로 구현하세요.

# 초기 보유 0
mileage = 0
# 총 적립 0
total_earned = 0
# 총 사용 0
total_used = 0
# 적립률 5%
rate = 5


# 반복문 시작하기
while True:
    # 마일리지 시스템 출력하기
    print("===== 마일리지 시스템 =====")
    print("1. 구매 (마일리지 적립)\n2. 마일리지 사용\n3. 마일리지 조회\n4. 종료")
    # 메뉴 입력받기
    menu = int(input())

    # 메뉴 1을 선택하면 금액 입력받기
    if menu == 1:
        price = int(input())
        # 0 이하면 양수여야한다고 출력하기
        if price <= 0:
            print("구매 금액은 양수여야 합니다.")
        # 아니면 적립 후 메시지 출력하기
        else:
            earned = price * rate // 100
            total_earned += earned
            print(f"{earned} 마일리지가 적립되었습니다!")
         
    
    # 메뉴 2를 선택하고 
    elif menu == 2:
        # 보유가 0이면 마일리지 없다고 출력하기
        if mileage == 0:
            print("보유 마일리지가 없습니다.")
        
        # 아니면 사용 값 입력받기
        else:
            mileage_price = int(input())
            # 0 이하면 1 이상의 값 입력해달라고 출력하기
            if mileage_price <= 0:
                print("1 이상의 값을 입력해 주세요.")
            # 보유 보다 크면 마일리지 부족하다고 출력하기
            elif mileage < mileage_price:
                print(f"마일리지가 부족합니다. (보유: {mileage})")
            # 성공이면 마일리지 사용했다고 출력하기
            else:
                # 남은 마일리지 출력하기
                mileage -= mileage_price
                total_used += mileage_price
                print(f"{mileage_price} 마일리지를 사용했습니다.")
                print(f"남은 마일리지: {mileage}")
    
    # 메뉴 3을 선택하면 보유 마일리지 출력하기
    elif menu == 3:
        print(f"보유 마일리지: {mileage}")
        # 총 적립/ 총 사용 출력하기
        print(f"총 적립: {total_earned} / 총 사용: {total_used}")

    # 메뉴 4를 선택하면 감사 인사 출력 후 반복문 종료하기
    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break

    # 그 외는 잘못된 메뉴라고 출력하기
    else:
        print("잘못된 메뉴입니다.")
    
    # 빈 줄 하나 씩 출력하기
    print()