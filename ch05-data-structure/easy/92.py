# 빈 교집합도 자연스럽게 빈 줄로 출력됨.
a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y", "z"},
]
b_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"c", "d", "e", "f"},
    {"1", "2", "3"},
]
t = int(input())
a = a_sets[t]
b = b_sets[t]

# 교집합 구하기
common_elements = a & b
# 정렬해 공백 구분 후 한 줄로 출력하기
print(" ".join(sorted(common_elements)))