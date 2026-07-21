# 나이별 요금 결정 후 단체 할인을 판단하세요.
age = int(input())
group_count = int(input())

# 3살 이하면 0원
if age <= 3:
    price = 0
# 12살 이하면 15000원
elif age <= 12:
    price = 15000
# 18살 이하면 20000원
elif age <= 18:
    price = 20000
# 64살 이하면 30000원
elif age <= 64:
    price = 30000
# 그 외는 10000원
else:
    price = 10000

# 나이에 맞는 "기본 입장료: " 출력하기
print(f"기본 입장료: {price}원")

# 인원 수가 10명 이상이면
if group_count >= 10:
    # 단체 할인 20% 할인 적용하기
    price = int(price * 0.8)
    # "단체 할인 적용 (20%)!" 출력하기
    print("단체 할인 적용 (20%)!")
    # "1인 할인가: " 출력하기
    print(f"1인 할인가: {price}원")

# 계산된 총 입장료 출력하기
print(f"총 입장료: {price * group_count}원")