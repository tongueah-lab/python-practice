# 월/일 조합으로 별자리 판별
month = int(input())
day = int(input())
sign = ""

# 물병자리 날짜 입력하고 운세 적기
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "물병자리"
    result = "창의적인 아이디어가 떠오르는 날이에요!"

# 물고기자리 날짜 입력하고 운세 적기
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "물고기자리"
    result = "감성이 풍부해지는 하루입니다!"

# 양자리 날짜 입력하고 운세 적기
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "양자리"
    result = "도전하면 좋은 결과가 있어요!"

# 황소자리 날짜 입력하고 운세 적기
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "황소자리"
    result = "꾸준한 노력이 빛을 발해요!"

# 쌍둥이자리 날짜 입력하고 운세 적기
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    sign = "쌍둥이자리"
    result = "소통이 활발해지는 날이에요!"

# 게자리 날짜 입력하고 운세 적기
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    sign = "게자리"
    result = "새로운 만남이 기다리고 있어요!"

# 사자자리 날짜 입력하고 운세 적기
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "사자자리"
    result = "리더십을 발휘할 기회가 와요!"

# 처녀자리 날짜 입력하고 운세 적기
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "처녀자리"
    result = "꼼꼼함이 행운을 가져다줘요!"

# 천칭자리 날짜 입력하고 운세 적기
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "천칭자리"
    result = "균형 잡힌 판단이 중요한 날이에요!"

# 전갈자리 날짜 입력하고 운세 적기
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "전갈자리"
    result = "자신감을 가지면 좋은 일이 생겨요!"

# 사수자리 날짜 입력하고 운세 적기
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "사수자리"
    result = "모험을 즐기면 행운이 따라와요!"

# 염소자리 날짜 입력하고 운세 적기
else:
    sign = "염소자리"
    result = "성실함이 큰 보상을 가져다줘요!"

# 별자리 출력하기
print(f"당신의 별자리는 {sign}입니다!")
# 운세 출력하기
print(f"오늘의 운세: {result}")