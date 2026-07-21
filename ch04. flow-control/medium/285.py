# 무한 루프 안에서 0 입력 시 BYE 출력 후 break, 그 외는 범위별 분기 후 카운트.

# 예약 카운트 초기화하기
reservation_count = 0

# 참이 될 때까지 반복하기
while True:
    # 좌석 번호 입력받기
    seat_number = int(input())

    # 0이 입력되면 bye를 출력한 뒤 반복 종료하기
    if seat_number == 0:
        print("BYE")
        break
    # 1~10 비즈니스석 예약 출력 후 카운트 세기
    elif 1 <= seat_number <= 10:
        print("비즈니스석 예약")
        reservation_count += 1
    # 11~20 일반석 예약 출력 후 카운트 세기
    elif 11 <= seat_number <= 20:
        print("일반석 예약")
        reservation_count += 1
    # 21~30 이코노미석 예약 출력 후 카운트 세기
    elif 21 <= seat_number <= 30:
        print("이코노미석 예약")
        reservation_count += 1
    # 그 외는 잘못된 좌석 출력하고 다음 입력으로 진행
    else:
        print("잘못된 좌석")
# 총 예약: n건 출력하기
print(f"총 예약: {reservation_count}건")