# 나이 구간별로 구분과 요금을 정하세요.
age = int(input())

# 7세 이하는 무료이고 0원이다
if age < 8:
    age_group = "무료"
    price = 0
# 8~13세는 어린이고 5000원이다
elif age < 14:
    age_group = "어린이"
    price = 5000
# 14~19세는 청소년이고 8000원이다
elif age < 20:
    age_group = "청소년"
    price = 8000
# 20~64세는 성인이고 12000원이다
elif age < 65:
    age_group = "성인"
    price = 12000
# 65세 이상은 경로이고 5000원이다
else:
    age_group = "경로"
    price = 5000

print(f"나이: {age}세")
print(f"구분: {age_group}")
print(f"요금: {price}원")