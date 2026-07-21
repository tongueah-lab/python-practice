# N명에 대해 이름, 상태를 반복 입력받아 분류
n = int(input())
present = 0
absent = 0

# n명 반복하기
for i in range(n):
    # 이름 반복 입력받기
    name = input()
    # 상태 반복 입력받기
    state = input()
    # 상태가 1이면 출석이고 카운트 세기
    if state == "1":
        result = "출석"
        present += 1
    # 0이면 결석이고 카운트 세기
    else:
        result = "결석"
        absent += 1
    # 이름이랑 상태 출력하기
    print(f"{name} - {result}")

# 출석, 결석 몇 명인지 출력하기
print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")
