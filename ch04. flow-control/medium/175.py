# 나이로 기본 요금을 정하고, 오후면 50% 추가
age = int(input())
time_slot = input()

# 7세 이하는 무료
if age <= 7:
    price = 0
# 14 ~ 18세 (청소년)는 5000원
elif 14 <= age <= 18:
    price = 5000
# 8 ~ 13세 (어린이)는 3000원
elif 8 <= age <= 13:
    price = 3000
# 19세 이상 (성인)은 8000원
else:
    price = 8000
# 오후면 기본 요금의 50% 추가(무료 대상은 그대로 무료)
if age > 7 and time_slot == "오후":
    price = int(price * 0.5) + price

# 나이랑 시간대 출력하기
print(f"나이: {age}세 | 시간대: {time_slot}")
# 입장료 출력하기
print(f"입장료: {price}원")