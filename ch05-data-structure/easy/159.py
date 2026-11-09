# 차집합 결과를 정렬 후 출력.
s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B"},
    set(),
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 차집합 구하기
result = s1 - s2
# 공백 구분 후 사전순으로 출력하기
print(" ".join(sorted(result)))