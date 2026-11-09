# 사본을 만든 후 사본에만 정렬을 적용해야 원본이 보존됩니다.
data_sets = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 3, 1],
    [7],
]
t = int(input())
original = data_sets[t]

# 원본 전체 복사하기
copy = original[:]
copy.sort()

# 원본, 정렬, 원본 출력하기
print(f"원본: {' '.join(map(str, original))}")
print(f"정렬: {' '.join(map(str, copy))}")
print(f"원본: {' '.join(map(str, original))}")
