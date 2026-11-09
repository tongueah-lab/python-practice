# 합 계산 후 평균은 합 / 길이.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 값들의 합 구하기
total = sum(scores.values())

# 항목 개수 구하기
num = len(scores)

# 평균 구하기
avg = total / num

# 합계 출력하기
print(f"합계: {total}")
# 평균 출력하기
print(f"평균: {avg:.1f}")