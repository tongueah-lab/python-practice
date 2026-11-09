# 방향 중요 — 학생은 a - b 임을 확인.
a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"c", "d", "e"},
    {"x", "y", "z"},
]
t = int(input())
a = a_sets[t]
b = b_sets[t]


# 차집합 구하기
a_only = a - b
# 정렬해 공백 구분 후 한 줄로 출력하기
print(" ".join(sorted(a_only)))