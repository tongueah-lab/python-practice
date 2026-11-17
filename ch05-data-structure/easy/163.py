# `existing.add(name)` 으로 추가하면 중복은 자동으로 무시됩니다.
existing = {"윤서", "지우", "민준"}
n = int(input())

# n번 반복하기
for _ in range(n):
    # 추가 등록자 이름 입력받기
    name = input()
    # 이름 추가하기
    existing.add(name)

# n명 추가 후 고유 학생 수 출력하기
print(f"고유 학생 수: {len(existing)}")