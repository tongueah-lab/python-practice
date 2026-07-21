# while True와 if/elif/break를 사용하세요.
total = 0

# 메뉴판 반복하기
while True:
    print("--- 메뉴 ---")
    print("1. 아메리카노 (4000원)\n2. 카페라떼 (4500원)\n3. 녹차 (3500원)\n0. 주문 완료")

    # 메뉴 번호 입력받기
    number = int(input())

    # 1번을 선택하면 아메리카노
    if number == 1:
        price = 4000
        print("아메리카노를 추가했습니다.")
    
    # 2번을 선택하면 카페라떼
    elif number == 2:
        price = 4500
        print("카페라떼를 추가했습니다.")
    elif number == 3:
        price = 3500
        print("녹차를 추가했습니다.")
    # 0이면 반복문 종료하기
    elif number == 0:
        break
    # 주문한 메뉴들 가격 누적 합하기
    total += price
# 총 주문 금액 출력하기
print(f"총 주문 금액: {total}원")
    
    