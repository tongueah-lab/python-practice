# `for name, score in students:` 형태로 각 tuple을 두 변수로 한 번에 받아 순회하세요.
students = [
    ("윤서", 85),
    ("지우", 92),
    ("민준", 65),
    ("서윤", 78),
    ("도윤", 95),
]
target = input()

# 학생 리스트에서 이름, 점수 순회하기
for name, score in students:
    # 만약 타겟을 찾으면
    if name == target:
        # 타겟의 점수 출력하기
        print(f"점수: {score}")
        # 반복문 멈추기
        break
# 타겟을 찾지 못하면 '학생 없음' 출력하기
else:
    print("학생 없음")