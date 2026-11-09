# 빈 dict를 만든 뒤 `d[key] = value` 형태로 새 항목을 추가하세요.
# dict 순회 순서는 삽입 순서와 동일합니다.
n = int(input())

# 학생 리스트 만들기
students = {}

# 학생 반복하기
for _ in range(n):
    # 이름 입력받기
    name = input()
    # 점수 입력받기
    score = int(input())
    # 학생 이름 = 점수
    students[name] = score
# 이름, 점수 묶어서 출력하기
for name, score in students.items():
    print(f"{name}: {score}")