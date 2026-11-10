# 문제마다 출력 후 input, 채점, 점수 누적
score = 0

# 문제 정리하기
questions = [
    (1, 12, 8),
    (2, 35, 17),
    (3, 99, 1),
    (4, 46, 27),
    (5, 58, 34)
]

# 문제 수, 숫자들 반복하기
for num, a, b in questions:
    # 문제 출력하기
    print(f"문제 {num}: {a} + {b} = ?")
    # 답 입력받기
    user_answer = int(input())
    # 정답은 문제 수 더하기
    correct = a + b

    # 만약 정답이면 20점 누적하고 정답이라고 출력하기
    if user_answer == correct:
        score += 20
        print("정답!")
    # 틀리면 오답과 정답 출력하기
    else:
        print(f"오답! 정답은 {correct}입니다")

# 최종 점수 출력하기
print("=== 최종 점수:", score, "/ 100 ===")