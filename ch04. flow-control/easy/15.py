# if/elif/else로 등급을 판정하세요.
score = int(input())

# 점수가 90점 이상이면 "A"
if score >= 90:
    result = "A"
# 점수가 80점 이상이면 "B"
elif score >= 80:
    result = "B"
# 점수가 70점 이상이면 "C"
elif score >= 70:
    result = "C"
# 점수가 60점 이상이면 "D"
elif score >= 60:
    result = "D"
# 점수가 60점 미만이면 "F"
else:
    result = "F"
# "점수: " 출력하기
print(f"점수: {score}")
# "등급: " 출력하기
print(f"등급: {result}")