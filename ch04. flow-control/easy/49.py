# while saved < goal: 현재 상태 출력 → 동전 입력 → saved 누적
goal = int(input())
saved = 0

# 누적금이 목표액 보다 적으면 반복 하기
while saved < goal:
    # 현재 누적금이랑 목표액 출력하기
    print(f"현재: {saved}원 / 목표: {goal}원")
    # 동전 입력 받기
    coin = int(input())
    # 입력된 동적들을 누적합하기
    saved += coin
    # 만약 누적금이 목표액 이상이면 현재를 출력하고 총 금액 출력하기
    if saved >= goal:
        print(f"현재: {saved}원 / 목표: {goal}원")
        print(f"목표 달성! 총 {saved}원을 모았습니다.")