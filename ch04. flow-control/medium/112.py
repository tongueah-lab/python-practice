# 30분 초과분을 10분 단위로 올림 청구
print("=== 주차 요금 계산기 ===")
enter_time = int(input())
exit_time = int(input())
parked = exit_time - enter_time

basic_charge = 2000

# 주차 시간 출력하기
print(f"주차 시간: {parked}분")
# 기본 요금 출력하기
print(f"기본 요금: {basic_charge}원")


# 30분 초과 시에만 추가 시간 출력하기
if parked > 30:
    additional_time = parked - 30
    
    
    # 올림 계산을 위해 (additional_time + 9) // 10 사용 (10분 단위)
    rounded_additional_time = (additional_time + 9) // 10    
    additional_charge = rounded_additional_time * 500
    print(f"추가 시간: {additional_time}분")
    print(f"추가 요금: {additional_charge}원")
# 30분 이하면 0원이지만 라인은 항상 출력하기
else:
    additional_charge = 0
    print(f"추가 요금: {additional_charge}원")
# 총 요금 출력하기
total = basic_charge + additional_charge
print(f"총 요금: {total}원")