# 점수가 동률인 경우 이름 알파벳순으로 자동 정렬됨.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"A": 50, "B": 50, "C": 50},
]
t = int(input())
scores = data_sets[t]

# 컴프리헨션으로 하기
pairs = [(s, n) for n, s in scores.items()]

# 정렬하기
pairs = sorted(pairs)
# 순회하기
for s, n in pairs:
    # 이름: 점수 출력하기
    print(f"{n}: {s}")