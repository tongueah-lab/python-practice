# while True, if/elif로 구현하세요.
last_issued = 0
last_called = 0


# 은행 시스템 반복하기
while True:
    
    # 은행 메뉴 출력하기
    print("===== 은행 대기번호 =====")
    print("1. 번호 발급\n2. 다음 고객 호출\n3. 대기인원 확인\n4. 종료")
    
    # 메뉴 번호 입력받기
    menu = int(input())

    # 실제 대기 인원 = 발급 수 - 호출 수
    waiting = last_issued - last_called
    
    # 만약 1번을 누르면 마지막 발급 번호를 1더하고 출력하기
    if menu == 1:
        last_issued += 1
        print(f"대기번호 {last_issued}번이 발급되었습니다.")

    # 2번을 누르고 대기인원이 없으면 없다고 출력하기
    elif menu == 2:
        if waiting <= 0:
            print("대기 중인 고객이 없습니다.")
        # 아니면 마지막 호출을 1 더하고 오라고 출력하기
        else:
            last_called += 1
            print(f"{last_called}번 고객님, 오세요!")
        

    # 3을 누르면 현재 대기인원 출력하기
    elif menu == 3:
        print(f"현재 대기인원: {waiting}명")
    
    # 4를 누르면 종료 메시지 출력 후 반복 종료하기
    elif menu == 4:
        print("시스템을 종료합니다.")
        break
    
    else:
        print("잘못된 메뉴입니다.")
    
    # 빈 줄 하나 출력
    print()