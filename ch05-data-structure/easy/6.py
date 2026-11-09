# `not in` 으로 명단에 없는 경우를 먼저 분기하세요.
attendance = ["윤서", "민준", "도윤", "예준"]
name = input()

# 출석 명단에 이름이 없으면
if name not in attendance:
    # 결석이라고 출력하기
    print("결석")
# 이름이 있으면
else:
    # 출석이라고 출력하기  
    print("출석")