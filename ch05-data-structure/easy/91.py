# 출력 시 set 을 정렬해 일관된 순서로 표시.
a_sets = [
    {"윤서", "지우", "민준"},
    {"a", "b", "c"},
    {"1", "2", "3"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"x", "y", "z"},
    set(),
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# a 와 b의 합집합 구하기
union_set = a | b

# 띄어서 구분해서 사전순 정렬해서 출력하기
print(" ".join(sorted(union_set)))