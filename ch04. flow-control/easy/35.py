# for + range(1, n+1)로 누적합을 구한 뒤, print("1부터", n, "까지의 합:", total)로 출력하세요.
n = int(input())

# 합계는 0으로 잡는다.
total = 0
# 1부터 n까지 반복한다.
for i in range(1, n + 1):
    # 값들이 누적되면서 합해진다.
    total += i
# "1부터 {n}까지의 합: "을 출력한다.
print("1부터", n, "까지의 합:",  total)