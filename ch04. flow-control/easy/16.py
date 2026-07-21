# 월을 계절로 변환하세요.
month = int(input())

# 3, 4, 5월은 "봄"
if 3 <= month < 6:
    result = "봄"
# 6, 7, 8월은 "여름"
elif 6 <= month < 9:
    result = "여름"
# 9, 10, 11월은 "가을"
elif 9 <= month < 12:
    result = "가을"
# 12, 1, 2월은 "겨울"
else:
    result = "겨울"
# "{month}월은 (result)입니다." 가 출력되게 하기
print(f"{month}월은 {result}입니다.")