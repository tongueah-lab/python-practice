# for + if + 누적 변수를 사용하세요.
total = 0
best = 0

# 5명의 점수를 반복하기
for i in range(5):
    # 점수 입력받기
    score = int(input())
    # 점수를 누적하고 다 더하기
    total += score

    # 만약 점수가 최고점보다 클 때마다
    if score > best:
        # 최고점 변수에 점수가 클 때마다 저장하기
        best = score

# 평균은 점수 합계 나누기 5
avg = total / 5

# 평균 출력하기
print(f"평균: {avg}")
# 최고점 출력하기
print(f"최고점: {best}")