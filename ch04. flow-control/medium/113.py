# while True 안에서 guess 입력, tries += 1, 비교/break
answer = 42
tries = 0
print("=== 숫자 맞추기 게임 (1~100) ===")


# 반복하기
while True:
    # 추측 정답 입력받고 시도 횟수 세기
    guess = int(input())
    tries += 1

    # 입력 값이 정답보다 작으면 UP! 출력 하기
    if guess < answer:
        print("UP!")

    # 입력 값이 정답보다 크면 DOWN! 출력 하기
    elif guess > answer:
        print("DOWN!")
            
    # 정답을 맞추면 정답이라고 출력 후 반복문 종료하기
    else:
        print(f"정답입니다! 시도 횟수: {tries}번")
        break