# 통화를 선택한 뒤 환율에 맞게 계산하세요.
currency = int(input())
krw = int(input())

# 만약 통화를 1=달러를 선택하면
if currency == 1:
    # 달러로 계산하기
    exchange_amount = krw / 1350
    # 실수 결과 값을 .뒤에 2개까지 출력되게 하기
    print(f"환전 금액: {round(exchange_amount, 2)} 달러")

# 통화를 2=엔을 선택하면
elif currency == 2:
    # 엔으로 계산하기
    exchange_amount = krw / 9
    # 엔 환전 출력하기
    print(f"환전 금액: {exchange_amount} 엔")

# 통화를 3=유로를 선택하면
elif currency == 3:
    # 유로로 계산하기
    exchange_amount = krw / 1450
    # 유로 환전 출력하기
    print(f"환전 금액: {exchange_amount} 유로")

# 그 외는 "잘못된 통화 선택입니다" 출력하기
else:
    print("잘못된 통화 선택입니다.")

# 유효한 통화(1~3)일 때만
if 1 <= currency <= 3:
    # 수수료 계산하기
    fee = int(krw * 0.015)
    # 수수료 출력하기
    print(f"수수료 (1.5%): {fee}원")
    # 실 지불 금액 계산하기
    total = krw + fee
    # 실 지불 금액 출력하기
    print(f"실 지불 금액: {total}원")