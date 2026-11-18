# 조건 표현식을 dict comp 값 자리에 두고, zip 으로 짝 지어 순회하세요.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [100, 55, 72],
    [85],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 새 딕셔너리 만들기
result = {}
# zip로 이름 점수 동시 순회하기
for name, score in zip(names, scores):
    # 90이상 A, 80이상 B, 70이상 C, 그 외 F 판정하기
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    # 새딕셔너리에 이름과 점수 넣기
    result[name] = grade

# 새 딕셔너리 순회하기
for name, grade in result.items():
    # 이름: 등급 출력하기
    print(f"{name}: {grade}")