# "N의 약수: "를 end=" "로 출력한 뒤, 1부터 N까지 나머지가 0인 수를 end=" "로 출력하세요.
n = int(input())

print(f"{n}의 약수: ", end = "")
# 1부터 n + 1까지 반복하기
for i in range(1, n + 1):
    # i가 반복하면서 n을 나누는데 0으로 나누어 떨어지면 약수
    if n % i == 0:
        # 약수 출력하기
        print(i, end =" ")
