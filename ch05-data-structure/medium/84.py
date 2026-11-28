# values 한 번 변수로 받아 4번 사용해도 OK.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 점수의 합 구하기
total = sum(scores.values())
# 점수의 평균 구하기
avg = total / len(scores)
# 점수의 최고 구하기
max_score = max(scores.values())
# 점수의 최저 구하기
min_score = min(scores.values())

# 합 출력하기
print(f"합계: {total}")
# 평균 출력하기
print(f"평균: {avg:.1f}")
# 최고 출력하기
print(f"최고: {max_score}")
# 최저 출력하기
print(f"최저: {min_score}")