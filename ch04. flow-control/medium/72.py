# 먼저 등급을 판별한 뒤 수료 여부를 판단하세요.
score = int(input())
attendance = int(input())

# 점수가 90점 이상이면 "A"
if score >= 90:
    grade = "A"
# 80점 이상이면 "B"
elif score >= 80:
    grade = "B"
# 70점 이상이면 "C"
elif score >= 70:
    grade = "C"
# 60점 이상이면 "D"
elif score >= 60:
    grade = "D"
# 60점 미만이면 "F"
else:
    grade = "F"

# "등급: " 출력하기
print(f"등급: {grade}")

# 등급이 F이면 "미수료 - 성적 미달 (60점 이상 필요)" 출력하기
if grade == "F":
    print("미수료 - 성적 미달 (60점 이상 필요)")
# F가 아니고 출석률이 80점 미만이면 "미수료 - 출석률 부족 (80% 이상 필요)" 출력하기
elif attendance < 80:
    print("미수료 - 출석률 부족 (80% 이상 필요)")
# 그 외 다 통과하면 "수료를 축하합니다!" 출력하기
else:
    print("수료를 축하합니다!")
