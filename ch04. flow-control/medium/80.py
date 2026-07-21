# for + 누적 변수를 사용하세요.
n = int(input())

# 합계는 0으로 잡는다.
total = 0
# 변수 i에 1부터 n+1까지 넣는다.
for i in range(1, n +1):
    # 누적되면서 더해진다.
    total += i
# 최종 합 출력하기
print(f"1부터 {n}까지의 합: {total}")