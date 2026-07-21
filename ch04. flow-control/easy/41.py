# 누적 곱 변수의 초깃값은 1로 두고, count번 반복하며 입력받은 숫자를 곱하세요.
count = int(input())

total = 1
# 곱 변수의 초깃값은 1로 두기
for _ in range(count):
    # i변수 잡기
    i = int(input())
    # 누적된 합을 계속 곱하기
    total *= i
# 최종 누적 곱 출력하기
print(f"누적 곱: {total}")