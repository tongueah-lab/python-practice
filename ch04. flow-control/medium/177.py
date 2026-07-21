# 기본료에 무게 추가, 거리 추가를 더하세요
weight = int(input())
dist = int(input())


# 기본료 3000원
basic_rate = 3000
total = basic_rate
# 무게 추가
# 2kg 이하 추가 없음
if weight <= 2:
    weight_charges = 0
    total += weight_charges
    
# 2kg 초과 ~ 10kg 이하 1000원 추가
elif 2 < weight <= 10:
    weight_charges = 1000
    total += weight_charges

# 10kg 초과 3000원 추가
else:
    weight_charges = 3000
    total += weight_charges


# 거리 추가
# 50km 이하 추가 없음
if dist <= 50:
    dist_charges = 0
    total += dist_charges
# 50km 초과 ~ 100km 이하 1500원 추가
elif 50 < dist <= 100:
    dist_charges = 1500
    total += dist_charges
# 100km 초과 3000원 추가
else:
    dist_charges = 3000
    total += dist_charges

# 무게 | 거리 출력하기
print(f"무게: {weight}kg | 거리: {dist}km")
# 택배 요금 출력하기
print(f"택배 요금: {total}원")