# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())

# n부터 0까지 -1씩 빼기
for i in range(n, 0, -1):
    # step을 하나씩 빼면서 곱하기
    print("*" * i)