# 각 감가율을 따로 계산한 뒤 합산하고 최저가를 체크하세요.

# '신차 가격' 입력받기
new_price = int(input())
# '연식' 입력받기
year = int(input())
# '주행거리' 입력받기
km = float(input())
# '사고 유무' 입력받기
accident = input()

######################################

# 연식이 3년 이하면 year * 10 하기
if year <= 3:
    year_result = year * 10
# 연식이 7년 이하면 3 * 10 + (year - 3) * 7
elif year <= 7:
    year_result = 3 * 10 + (year - 3) * 7
# 연식이 7년 초과면 3 * 10 + 4 * 7 + (year - 7) * 5
else:
    year_result = 3 * 10 + 4 * 7 + (year - 7) * 5
######################################

# 주행거리가 5km 이하면 0
if km <= 5:
    km_result = 0
# 주행거리가 10km 이하면 5
elif km <= 10:
    km_result = 5
# 주행거리가 10km 초과면 10
else:
    km_result = 10
######################################

# 사고가 Y 또는 y면 15
if accident == "Y" or accident == "y":
    accident_result = 15
# 아니면 0
else:
    accident_result = 0
#######################################

# 총 감가율 = 세 감가율 합
total_discount = year_result + km_result + accident_result
# 최종 가격 = int(new_price * (1 - total_discount / 100))
total = int(new_price * (1 - total_discount / 100))

# 감가 내역 출력하기
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_result}%")
print(f"주행거리 감가: {km_result}%")
print(f"사고 감가: {accident_result}%")
print(f"총 감가율: {total_discount}%")


# 최소 가격 = int(new_price * 0.1)
min_price = int(new_price * 0.1)
if total < min_price:
    print(f"예상 중고차 가격: {min_price}만원")
else:
    print(f"예상 중고차 가격: {total}만원")