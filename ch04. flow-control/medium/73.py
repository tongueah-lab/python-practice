# 구간별로 나눠 계산하세요.
usage = int(input())

# 전기를 100이하 사용한 만큼 전기 요금 계산하기
if usage <= 100:
    charge = usage * 60
# 전기를 100 이상 200 이하 사용한 만큼 전기 요금 계산하기
elif 100 < usage <= 200:
    charge = 100 * 60 + (usage - 100) * 120
# 전기를 200 초과 사용한 만큼 전기 요금 계산하기
else:
    charge = 100 * 60 + 100 * 120 + (usage - 200) * 190

# 부가세 계산하기
tax = int(charge * 0.1)
# 총 납부 금액 계산하기
total = charge + tax

# 전기 요금, 부가세, 총 납부 금액 출력하기
print(f"전기 요금: {charge}원")
print(f"부가세 (10%): {tax}원")
print(f"총 납부 금액: {total}원")