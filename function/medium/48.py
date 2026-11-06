# 첫 값=초기 잔액, 나머지=증감액. 예: "1000 100 -50 200" → balance=1000, changes=[100,-50,200]
parts = input().split()
balance = int(parts[0])
changes = [int(x) for x in parts[1:]]


# 증감액을 박아 전역 balance에 더하는 함수 정의하기
def apply(amount):
    global balance
    balance += amount

# 모든 증감 적용하기
for change in changes:
    apply(change)

# 최종 balance 출력하기
print(balance)