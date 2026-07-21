# i = 1, while i <= n: total += i; i += 1
n = int(input())
total = 0

# i초기값은 1로 잡기
i = 1
# i부터 n까지 합하기
while i <= n:
    total += i
    # 다음 수로 이동 (인덱스 증가)
    i += 1
# 최종 합 구하기
print(f"1부터 {n}까지의 합: {total}") 