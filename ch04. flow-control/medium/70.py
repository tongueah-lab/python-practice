# if/elif/else + or 연산자를 사용하세요.
month = int(input())

# 3,4,5월 중에 하나면 봄 인사 출력하기
if month == 3 or month == 4 or month == 5:
    result = "봄입니다.\n따뜻한 봄이에요! 꽃구경 가세요 🌸"
# 6,7,8울 중에 하나면 여름 인사 출력하기
elif month == 6 or month == 7 or month == 8:
    result = "여름입니다.\n더운 여름이에요! 시원하게 보내세요 🌊"
# 9,10,11월 중에 하나면 가을 인사 출력하기
elif month == 9 or month == 10 or month == 11:
    result = "가을입니다.\n선선한 가을이에요! 단풍 구경 가세요 🍂"
# 12,1,2월 중에 하나면 겨울 인사 출력하기
elif month == 12 or month == 1 or month == 2:
    result = "겨울입니다.\n추운 겨울이에요! 따뜻하게 입으세요 ⛄"
# 그 외 입력이면 "잘못된 입력입니다." 출력하기
else:
    result = "잘못된 입력입니다."

# 출력하기
print(result)