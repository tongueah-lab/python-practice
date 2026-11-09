# values 의 합을 항목 수로 나눠 평균.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 값들의 시퀀스 반환하기
values = scores.values()
# 평균 값 구하기
avg_score = sum(values) / len(values)
# 소수점 첫째 자리까지 출력하기
print(f"평균: {avg_score:.1f}")