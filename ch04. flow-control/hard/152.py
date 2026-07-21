# # while True로 반복, if/elif로 경우 분기
current = 1

# 엘리베이터 반복하기
while True:
    # 현재 층 출력하기
    print(f"현재 층: {current}층")
    # 지하면 B1 출력하기
    if current == -1:
        print()
    # 이동할 층 입력하기
    moving_floor = int(input())
    # 입력이 0이면 엘리베이터 종료한다고 출력하고 반복문 종료하기
    if moving_floor == 0:
        print("엘리베이터를 종료합니다.")
        break

    # 범위(-1 ~ 10)밖이면 이동할 수 없는 층이라고 출력하기
    elif moving_floor < -1 or moving_floor > 10:
        print("이동할 수 없는 층입니다. (-1 ~ 10)") 
        print()
        continue

    # 현재 층과 같으면 이미 해당 층에 있다고 출력하기
    elif current == moving_floor:
        print("이미 해당 층에 있습니다.")
        print()
        continue

    # 현재 층보다 이동할 층이 더 크면 1씩 증가하기
    if current < moving_floor:
        for i in range(1, moving_floor + 1):
            print(f"{i}층", end = " ")
            # 현재 층이랑 이동할 층이 같지 않으면 화살표 멈추기
            if i != moving_floor:
                print("→", end = " ")
    # 현재 층보다 이동할 층이 더 작으면 1씩 감소하기
    else:
        for i in range(current, moving_floor -1, -1):
            print(f"{i}층", end = " ")
            # 현재 층이랑 이동할 층이 같지 않으면 화살표 멈추기
            if i != moving_floor:
                print("→", end = " ")
    # 몇 층인지 출력하기
    print(f"\n{i}층에 도착했습니다.")
    # 빈 줄 출력하기
    print()
    # 현재 층 = 이동할 층
    current = moving_floor