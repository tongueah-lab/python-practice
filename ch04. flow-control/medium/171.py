# 횟수에 따라 등급을 구분하세요
count = int(input())

# 60회 이상 A
if count >= 60:
    result = "A"
# 45회 이상 B
elif count >= 45:
    result = "B"
# 30회 이상 C
elif count >= 30:
    result = "C"
# 15회 이상 D
elif count >= 15:
    result = "D"
# 15회 미만 F
else:
    result = "F"

# 횟수에 따라 등급 출력하기
print(f"횟수: {count}회 → 등급: {result}")