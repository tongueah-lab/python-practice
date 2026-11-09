# zip 으로 두 list 원소를 동시에 받아 순회.
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

# zip로 이름과 점수를 짝지어 이름: 점수 형식으로 출력하기
for name, score in zip(names, scores):
    print(f"{name}: {score}")