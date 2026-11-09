# `in` 연산자로 set 멤버십을 검사하세요.
members = {"윤서", "지우", "민준", "서윤", "도윤"}
name = input()

# 멤버 명단에 이름이 있으면
if name in members:
    # 있음
    print("있음")
# 없으면
else:
    # 없음
    print("없음")