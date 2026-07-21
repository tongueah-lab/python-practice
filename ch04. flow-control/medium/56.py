# while True 안에서 메뉴를 먼저 출력한 뒤 input()으로 선택을 받으세요.

# 메뉴판 반복하기
while True:
    print("===== 메뉴 =====")
    print("1. 인사\n2. 날씨\nq. 종료")
    print("================")

    # 메뉴판 번호 입력받기
    number = input()
    # 만약 1번을 선택하면 인사하기
    if number == "1":
        print("안녕하세요!")
    # 2번을 선택하면 날씨 말하기
    elif number == "2":
        print("오늘 날씨가 좋습니다!")
    # q를 선택하면 프로그램 종료 말하면서 반복문 종료하기
    elif number == "q":
        print("프로그램을 종료합니다")
        break
    # 그 외는 잘못된 입력이라고 알리기
    else:
        print("잘못된 입력입니다")