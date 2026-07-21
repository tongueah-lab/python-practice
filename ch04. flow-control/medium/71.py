# 거리 계산 후 야간 여부를 추가 판단하세요.
distance = float(input())
hour = int(input())


# 기본 요금 4800원
basic_rate = 4800
# total을 기본 요금으로 초기화하기
total = basic_rate
# 기본 요금 출력하기
print(f"기본요금: {basic_rate}원")
# 만약 거리가 2km 초과 되면
if distance > 2:
    # 추가 요금 받기
    additional_charges = int((distance - 2) * 1000)
    # total += 추가 요금하기
    total += additional_charges
    # 추가 요금 출력하기
    print(f"추가요금: {additional_charges}원")
# 2km 이하면
else:
    # 추가 요금은 없음
    additional_charges = 0
    # 추가 요금 0원 출력하기
    print(f"추가요금: {additional_charges}원")
# 야간 할증은 10시 이후부터 6시 전까지면
if hour >= 22 or hour < 6:
    # 야간 요금 받기
    night_surcharge = int(total * 0.2)
    # 야간 할증이면 합계에 더하기
    total += night_surcharge
    # 야간 할증 출력하기
    print(f"야간 할증 (20%): {night_surcharge}원")
# 총 택시비 출력하기
print(f"총 택시비: {total}원")