# zip 은 짧은 쪽 길이까지만 짝지어 줍니다.
names_sets = [
    ["A", "B", "C", "D", "E"],
    ["윤서", "지우", "민준"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78],
    [85, 92, 65],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 두 개 이상의 시퀀스를 묶기
pairs = zip(names, scores)

# 이름 점수 순회하고 이름: 점수 출력하기
for name, score in pairs:
    print(f"{name}: {score}")