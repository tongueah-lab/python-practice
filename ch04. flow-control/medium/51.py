# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
password = "python"

# 기회는 3번만
chance = 3

# 기회가 0보다 많으면 반복하기
while chance > 0:
    # 비밀번호 입력받기
    user_password = input()
    
    # 만약 비밀번호가 python이면 로그인하고 반복문 중단하기
    if user_password == password:
        print("로그인 성공!")
        break
    # 틀리면 기회 하나 빼기
    else:
        chance -= 1
        # 기회가 0이 아니라 더 남았으면 몇 번 남았는지 출력하고 반복하기
        if chance > 0:
            print("틀렸습니다. 남은 기회:", str(chance) + "번")
# 기회가 0번이면 계정 잠구기
if chance == 0:
    print("계정이 잠겼습니다")