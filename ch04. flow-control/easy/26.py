# 회원일 때만 VIP 여부를 input()으로 추가로 받으세요.
is_member = input()

# 회원이면 VIP 여부 확인하기
if is_member == "Y":
    # VIP 여부를 input() 추가로 받기
    VIP = input()
    # VIP이면 "20% 할인 적용" 출력하기
    if VIP == "Y":
        print("20% 할인 적용")
    # VIP가 아니면 "10% 할인 적용" 출력하기
    else:
        print("10% 할인 적용")
# 회원이 아니면 "할인 없음" 출력하기
else:
    print("할인 없음")