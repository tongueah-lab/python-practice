# 추적 변수 두 개를 두고 for 순회로 비교 + 갱신.
data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
t = int(input())
students = data_sets[t]

# 탑 점수, 탑 이름은 점수의 [0]
top_name, top_score = students[0]
# 학생 리스트 순회하기
for name, score in students:
    # 만약 탑 점수가 점수보다 작으면
    if score > top_score:
        # 탐이름은 이름이 되고
        top_name = name
        # 탑점수는 점수가 된다
        top_score = score
# 결과 출력하기
print(f"{top_name}: {top_score}")