# for + if(i % m == 0) + 누적 변수를 사용하세요.
n = int(input())
m = int(input())

# 합 초기화하기
total = 0

# 1부터 n까지 반복하기
for i in range(1, n + 1):
    # m의 배수이면 합산
    if i % m == 0:
        total += i
# 합 출력하기
print(f"1부터 {n}까지 {m}의 배수의 합: {total}")