# N번 반복하며 점수를 입력받습니다. 범위를 벗어나면 안내 출력 후 continue, 유효한 점수만 누적합에 더하세요.
# 반복문 종료 후 최종 합계를 한 줄 출력합니다.
n = int(input())
total = 0

# n번 반복하기
for _ in range(n):
    score = int(input())
    # 0 이상 100 이하인 점수만 유효함.
    if 0 <= score <= 100:
        # 유효한 점수는 합계에 누적함.
        total += score
    # 유효하지 않은 점수가 들어오면
    else:
        # 무효: X 형식으로 출력하고
        print("무효:", score)

# 유효 점수 합 출력하기
print("유효 점수의 합:", total)