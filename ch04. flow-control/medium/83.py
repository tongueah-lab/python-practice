# for + 누적 변수를 사용하세요.

# 학생 수 N명 입력받기
n = int(input())

# total = 0 잡기
total = 0

# 1명부터 n명까지 반복하기
for i in range(n):
    # 점수 입력받기
    score = int(input())
    # 점수들을 누적 합하기
    total += score
# 평균 구하기
avg_total = total/n
# 평균 점수 출력하기
print(f"평균 점수: {avg_total}")