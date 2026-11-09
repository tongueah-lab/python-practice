# 컴프리헨션 한 줄로 필터링.
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [-3, 10, -5, 20, 0],
    [-1, -2, 0, -3],
]
t = int(input())
data = data_sets[t]

# 양수만 추출하기
positives = [num for num in data if num > 0]

# 한 줄로 출력하기
print(" ".join(str(num) for num in positives))