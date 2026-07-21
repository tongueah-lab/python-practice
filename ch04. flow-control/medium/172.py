# 7일 초과분에 대해 일당 200원 부과
days = int(input())

# 7일 이내면 무료
if days <= 7:
    rental_fee = 0
# 8일 부터는 일당 200원 추가 
else:
    rental_fee = (days - 7) * 200

# 대여 일수 출력하기
print(f"대여 일수: {days}일")
# 대여료 출력하기
print(f"대여료: {rental_fee}원")