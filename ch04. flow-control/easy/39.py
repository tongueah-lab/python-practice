# 누적 곱 변수의 초깃값은 1로 두세요.
n = int(input())

# 곱 변수의 초깃값은 1로 두기
total = 1
# 1부터 N까지 반복 출력하기
for i in range(1, n + 1):
    # 곱하면서 합 누적하기
    total *= i
# 결과 출력하기
print(f"{n}! = {total}")