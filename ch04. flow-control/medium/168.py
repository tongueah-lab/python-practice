# 거래 종류를 판별하여 잔액을 관리하세요.
balance = int(input())


# 거래 3번 반복하기
for _ in range(3):
    # 거래 입력받기
    transaction = input().split()
    # 입금이면
    if transaction[0] == "입금":
        # 금액 더하고 잔액 출력하기
        balance += int(transaction[1])
        print(f"입금 완료: 잔액 {balance}원")
    # 출금이지만
    elif transaction[0] == "출금":
        # 잔액이 충분하면 빼고 잔액 출력하기
        if int(transaction[1]) <= balance:
            balance -= int(transaction[1])
            print(f"출금 완료: 잔액 {balance}원")
        # 부족하면 잔액 출력하기
        else:
            print("출금 실패: 잔액 부족")
    # 조회이면
    elif transaction[0] == "조회":
        # 현재 잔액 출력하기
        print(f"현재 잔액: {balance}원")
# 최종 잔액 출력하기
print(f"최종 잔액: {balance}원")