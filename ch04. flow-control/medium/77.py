# 유효성 검사 후 이름 변환과 승패 판정을 수행하세요.
user = int(input())
computer = 2


# 만약 user < 1 또는 user > 3 이면 잘못입력했다고 출력하기
if user < 1 or user > 3:
    result = "잘못된 입력입니다. 1, 2, 3 중에서 선택하세요."
    print(result)
# 그 외면 게임 시작하기
else:
    # user == 2:이면 바위이고 무승부입니다! 😐 출력하기
    if user == 2:
        user_name = "바위"
        result = "무승부입니다! 😐"
    # user == 3: 이면 보이고 축하합니다! 당신이 이겼습니다! 🎉 출력하기
    elif user == 3:
        user_name = "보"
        result = "축하합니다! 당신이 이겼습니다! 🎉"
    # user == 1: 이면 가위이고 아쉽게도 졌습니다. 😢 출력하기
    elif user == 1:
        user_name = "가위"
        result = "아쉽게도 졌습니다. 😢"
    # 나의 선택과 컴퓨터의 선택을 보여주고 결과 출력하기
    print(f"당신: {user_name} / 컴퓨터: 바위")
    print(result)
    