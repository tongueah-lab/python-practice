# while True 안에서 음수면 break, 아니면 total에 누적.
total = 0

# 숫자를 계속 입력받기
while True:
    num = int(input())
    # 만약 음수면 중단하기
    if num < 0:
        break
    # 아니면 total에 누적하기
    total += num
# 합계 출력하기
print("합계:", total)
