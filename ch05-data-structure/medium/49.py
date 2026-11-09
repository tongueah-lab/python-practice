# 한 줄에 두 개의 for 를 두는 이중 컴프리헨션을 사용하세요.
grids = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3], [4, 5, 6]],
    [[1], [2], [3]],
]
t = int(input())
grid = grids[t]

# 이중 컴프리헨션으로 바깥 for를 먼저 적고 안쪽 for 적기
flattened = [x for row in grid for x in row]
# 출력하기
print(" ".join(map(str, flattened)))