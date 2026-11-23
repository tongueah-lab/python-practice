# (점수, 이름) tuple 의 자연스러운 정렬을 활용하세요.
data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]
t = int(input())
students = data_sets[t]

# 학생 리스트 정렬하기
students.sort()

# 학생 리스트에서 점수 이름 순회하고 출력하기
for score, name in students:
    print(f"{name}: {score}")