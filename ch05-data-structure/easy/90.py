# `set(list)` 로 변환하면 중복이 자동 제거됩니다.
datasets = [
    ["apple", "banana", "apple", "cherry"],
    [1, 2, 1, 2, 1, 2, 3],
    ["A", "B", "C", "D", "E"]
]
t = int(input())

# 길이 수를 세고 set으로 중복 제거하기
print(len(set(datasets[t])))