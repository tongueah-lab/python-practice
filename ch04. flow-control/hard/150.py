# while True와 if/elif로 구현하세요.
parked = 0
max_cars = 10
total_income = 0
rate = 1000


# 주차장 관리하기
while True:
    print("===== 주차장 관리 =====")
    print("1. 입차\n2. 출차\n3. 현황 조회\n4. 종료")
    
    menu = input()
    # 입차(1) 메뉴를 입력하면
    if menu == "1":
        # 만차면 만차라고 출력하기
        if parked >= max_cars:
            print("주차장이 만차입니다!")
        # 아니면 입차되었다는 말과 현재 주차 현황 출력하기
        else:
            parked += 1
            print(f"차량이 입차되었습니다. (현재 주차: {parked}/{max_cars}대)")


    # 출차(2) 메뉴를 입력하면
    elif menu == "2":
        # 주차된 차가 없으면 주차 차량 없다고 출력하기
        if parked == 0:
                print("주차된 차량이 없습니다.")
        # 있으면 시간 입력받기
        else:
            parked_time = input()
            # 요금 = max(0, 시간) * 1000 요금 계산하기
            fee = max(0, int(parked_time)) * rate
            total_income += fee
            # 주차 요금과 출차되었다는 말과 현재 주차 현황 출력하기(총 수입 누적)
            print(f"주차 요금: {fee}원")
            parked -= 1
            print(f"차량이 출차되었습니다. (현재 주차: {parked}/{max_cars}대)")
    
    # 조회(3) 메뉴를 입력하면
    elif menu == "3":
        # 현재 주차 현황 출력하기
        print(f"현재 주차: {parked}/{max_cars}대")
        # 빈 자리 출력하기
        empty_spots = max_cars - parked
        print(f"빈 자리: {empty_spots}대")
        # 총 수입 출력하기
        print(f"총 수입: {total_income}원")


    # 종료(4) 메뉴를 입력하면
    elif menu == "4":
        # 시스템 종료한다는 말과 반복문 종료하기
        print("시스템을 종료합니다.")
        break
    # 그 외면 잘못된 메뉴라고 출력하기
    else:
        print("잘못된 메뉴입니다.")
    # 한 줄씩 띄우기
    print()