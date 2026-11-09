# 최댓값 위치를 찾아 이름 리스트에서 같은 인덱스 학생 출력.
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


# 리스트에서 최고점 찾기
max_score = max(scores)

# 최고점 위치 찾기
max_index = scores.index(max_score)

# 최고점 학생 이름 결과 출력하기
print(names[max_index])