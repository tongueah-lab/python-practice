# 두 함수 호출만으로 한 줄씩 출력하면 됩니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 40],
    [42],
]
t = int(input())
scores = data_sets[t]

# 최댓값 구하기
max_score = max(scores)
print(f"최고: {max_score}")

# 최솟값 구하기
min_score = min(scores)
print(f"최저: {min_score}")