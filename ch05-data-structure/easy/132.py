# min 위치를 찾아 이름 출력.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 리스트에서 최저점 찾기
min_scores = min(scores)

# 최저점 위치 찾기
min_index = scores.index(min_scores)

# 최저점 학생 이름 출력하기
print(names[min_index])