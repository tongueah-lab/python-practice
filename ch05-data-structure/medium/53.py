# `{x: x*x for x in range(1, n+1)}` 형태로 한 줄에 dict 를 만들고, items() 로 순회 출력하세요.
n = int(input())

# 1부터 n까지 제곱하기
square_table = {num: num * num for num in range(1, n + 1)}

# items()로 순회 출력하기
for num, square in square_table.items():
    print(f"{num}: {square}")