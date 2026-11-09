# values 의 합을 한 번에 구합니다.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 모든 값의 합계를 한 줄로 출력하기
print(sum(scores.values()))