# 리스트 멤버십 검사에는 `in` 연산자를 사용합니다.
members = ["윤서", "지우", "민준", "서윤", "도윤"]
name = input()

# 리스트 멤버들 안에 회원이 있으면
if name in members:
    # 있다고 출력하기
    print("있음")
# 없으면 없다고 출력하기
else:
    print("없음")