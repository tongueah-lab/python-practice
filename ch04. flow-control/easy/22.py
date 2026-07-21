# float로 입력받아 구간별 옷차림을 결정하세요.
temp = float(input())

# 5도 미만은 "패딩, 두꺼운 목도리"를 출력하기
if temp < 5:
    result = "패딩, 두꺼운 목도리"
# 5도 이상 10도 미만은 "코트, 니트" 출력하기
elif temp < 10:
    result = "코트, 니트"
# 10도 이상 20도 미만은 "자켓, 가디건"을 출력하기
elif temp < 20:
    result = "자켓, 가디건"
# 20도 이상 28도 미만은 "반팔, 얇은 셔츠"를 출력하기
elif temp < 28:
    result = "반팔, 얇은 셔츠"
# 그 이상은 "민소매, 반바지" 출력하기
else:
    result = "민소매, 반바지"

# "현재 기온: ", "옷차림: " 출력하기
print(f"현재 기온: {temp}°C")
print(f"추천 옷차림: {result}")
