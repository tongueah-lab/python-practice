# if/elif로 모드 분기 후 while로 변경 과정 출력
current_temp = int(input())
target_temp = int(input())


# 현재 온도 < 목표 온도이면 난방 모드 시작하기
if current_temp < target_temp:
    print("난방 모드를 시작합니다.")
    # 현재 온도에서 목표 온도까지 올라갈 때까지 반복하기
    while current_temp < target_temp:
        # 현재 온도 -> 다음 온도 출력하기
        print(f"현재 온도: {current_temp}도 → {current_temp + 1}도")
        # 현재 온도 1증가
        current_temp += 1

    # 도달 시 목표 온도에 도달했다고 출력하기
    print(f"목표 온도 {target_temp}도에 도달했습니다!")

# 현재 온도 > 목표 온도이면 냉방 모드 시작하기
elif current_temp > target_temp:
    print("냉방 모드를 시작합니다.")
    # 현재 온도에서 목표 온도까지 내려갈 때까지 반복하기
    while current_temp > target_temp:
        # 현재 온도 -> 다음 온도 출력하기
        print(f"현재 온도: {current_temp}도 → {current_temp - 1}도")
        # 현재 온도 1빼기
        current_temp -= 1

    # 도달 시 목표 온도에 도달했다고 출력하기
    print(f"목표 온도 {target_temp}도에 도달했습니다!")

# 현재 온도랑 목표 온도가 같으면 이미 목표 온도라고 출력하기
else:
        print("이미 목표 온도입니다.")