# 문제마다 출력 후 input, 채점, 점수 누적
score = 0

# 1번 문제 출력하기
print("문제 1: 12 + 8 = ?")
# 답 입력받기
result = int(input())
# 답이 20이면 정답! 출력하기
if result == 20:
    # 점수 누적하기
    score += 20
    print("정답!")
# 틀리면 오답과 답 출력하기
else:
    print("오답! 정답은 20입니다")

# 2번 문제 출력하기
print("문제 2: 35 + 17 = ?")
# 답 입력받기
result = int(input())
# 답이 52이면 점수 누적하고 정답! 출력하기
if result == 52:
    score += 20
    print("정답!")
# 틀리면 오답과 답 출력하기
else:
    print("오답! 정답은 52입니다")

# 3번 문제 출력하기
print("문제 3: 99 + 1 = ?")
# 답 입력받기
result = int(input())
# 답이 100이면 점수 누적하고 정답! 출력하기
if result == 100:
    score += 20
    print("정답!")
# 틀리면 오답과 답 출력하기
else:
    print("오답! 정답은 100입니다")

# 4번 문제 출력하기
print("문제 4: 46 + 27 = ?")
# 답 입력받기
result = int(input())
# 답이 73이면 점수 누적하고 정답! 출력하기
if result == 73:
    score += 20
    print("정답!")
# 틀리면 오답과 답 출력하기
else:
    print("오답! 정답은 73입니다")

# 5번 문제 출력하기
print("문제 5: 58 + 34 = ?")
# 답 입력받기
result = int(input())
# 답이 92이면 점수 누적하고 정답! 출력하기
if result == 92:
    score += 20
    print("정답!")
# 틀리면 오답과 답 출력하기
else:
    print("오답! 정답은 92입니다")

# 최종 점수 출력하기
print("=== 최종 점수:", score, "/ 100 ===")
