# //(몫)과 %(나머지)를 사용해 큰 동전부터 차례대로 계산하세요.
amount = int(input())

# 금액이 몇 개의 500원으로 나눠지는지와 나눈 후 남은 갯수

amount_500 = amount // 500
remain_500 = amount % 500
# 남은 금액이 몇 개의 100원으로 나눠지는지와 나눈 후 남은 갯수
amount_100 = remain_500 // 100
remain_100 = remain_500 % 100 
# 또 남은 금액이 몇 개의 50원으로 나눠지는지와 나눈 후 남은 갯수
amount_50 = remain_100 // 50
remain_50 = remain_100 % 50
# 또 또 남은 금액이 몇 개의 10원으로 나줘지는지와 나눈 후 남은 갯수
amount_10 = remain_50 // 10

# 총 동전 수 더하기
total = amount_500 + amount_100 + amount_50 + amount_10

print(f"{amount}원 → 동전 변환:")
print(f"500원: {amount_500}개")
print(f"100원: {amount_100}개")
print(f"50원: {amount_50}개")
print(f"10원: {amount_10}개")
print(f"총 동전 수: {total}개")