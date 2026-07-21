# while True와 if/elif로 구현하세요.
borrowed = 0
max_books = 5

# 대출 시스템 반복하기
while True:
    # 도서관 대출 시스템 메뉴 출력하기
    print("===== 도서관 대출 시스템 =====")
    print("1. 대출\n2. 반납\n3. 대출현황 조회\n4. 종료")
    # 메뉴 입력받기
    menu = input()

    # 만약 대출(1)을 입력하면
    if menu == "1":
        # 권 수 입력받기
        number = int(input())
        # 만약 권 수가 0 이하면 1권 이상 입력해달라고 출력하기
        if number <= 0:
            print("1권 이상 입력해 주세요.")
        # 한도 초과(max_books)면 대출 한도 초과 출력하고 대출 가능 권수 출력하기
        elif borrowed + number > max_books:
            available = max_books - borrowed
            print(f"대출 한도 초과! 추가 대출 가능 권수: {available}권")
        # 성공이면 몇 권을 대출했는지 더하고 출력하기
        else:
            borrowed += number
            print(f"{number}권을 대출했습니다. (현재 대출: {borrowed}권)")
    
    # 반납(2)를 입력하면
    elif menu == "2":
        # 현재 대출(borrowed)이 0이면 대출한 도서가 없다고 출력하기
        if borrowed == 0:
            print("현재 대출한 도서가 없습니다.")
        # 권 수 입력받기
        else:
            number = int(input())
            # 0 이하면 1권 이상 입력해달라고 출력하기
            if number <= 0:
                print("1권 이상 입력해 주세요.")
            # 대출보다 많으면 반납할 수 없고 현재 대출 출력하기
            elif number > borrowed:
                print(f"대출 권수보다 많이 반납할 수 없습니다. (현재 대출: {borrowed}권)")
            # 성공이면 몇 권을 반납할 수 있고 현재 대출 출력하기
            else:
                borrowed -= number
                print(f"{number}권을 반납했습니다. (현재 대출: {borrowed}권)")
    
    # 조회(3)을 입력하면
    elif menu == "3":
        # 현재 대출 출력하기
        print(f"현재 대출 권수: {borrowed}권")
        # 추가 대출 가능 출력하기
        print(f"추가 대출 가능: {max_books - borrowed}권")
    
    # 종료(4)를 입력하면 감사인사 출력 후 반복문 종료하기
    elif menu == "4":
        print("이용해 주셔서 감사합니다.")
        break

    # 그 외를 입력하면 다시 선택해달라고 출력하기
    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")

    # 한 줄 씩 띄우기
    print()