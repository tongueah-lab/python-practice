# `points[n-1]` 으로 N번째 tuple을 얻고, 그 tuple을 다시 인덱스 또는 언패킹으로 분리합니다.
points = [(1, 2), (3, 4), (5, 6), (7, 8), (-1, -2)]

# n 입력받기
n = int(input())

# x: n, y: n-1 형식으로 만들기
x, y = points[n - 1]

# x 결과 출력하기
print(f"x: {x}")
# y 결과 출력하기
print(f"y: {y}")