# 바깥 if는 회원/비회원, 안쪽 if는 시간 분기로 작성하세요.
is_member = input() == "True"
hours = int(input())


# 회원이면,
if is_member:
    # 1시간 이하면 "무료" 출력하기
    if hours <= 1:
        print("무료")
    # 1시간 초과하면,
    else:
        # 초과 1시간 당 1000원 "요금" 출력하기
        fee = (hours - 1) * 1000
        print(f"요금: {fee}원")
# 비회원이면
else:
    basic_fee = 2000
    # 1시간 이하면 요금 출력하기
    if hours <= 1:
        print(f"요금: {basic_fee}원")
    # 1시간 초과하면 추가 요금까지 출력하기
    else:
        fee = basic_fee + (hours - 1) * 2000
        print(f"요금: {fee}원")