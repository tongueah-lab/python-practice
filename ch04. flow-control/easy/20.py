# 1~7 외의 입력은 else로 처리하세요.
day = int(input())

# 1은 월요일로 출력하기
if day == 1:
    result = "월요일"
# 2는 화요일로 출력하기
elif day == 2:
    result = "화요일"
# 3은 수요일로 출력하기
elif day == 3:
    result = "수요일"
# 4는 목요일로 출력하기
elif day == 4:
    result = "목요일"
# 5는 금요일로 출력하기
elif day == 5:
    result = "금요일"
# 6은 토요일로 출력하기
elif day == 6:
    result = "토요일"
# 7은 일요일로 출력하기
elif day == 7:
    result = "일요일"
# 범위 벗어나면 "잘못된 입력입니다."를 출력하기
else:
    result = "잘못된 입력입니다."

if result != "잘못된 입력입니다.":
    print(f"{day} → {result}")
else:
    print("잘못된 입력입니다.")