# `reverse=True` 인자가 핵심입니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 내림차순 정렬 후 공백으로 연결하기
result = " ".join(map(str, sorted(scores, reverse=True)))
# 내림차순으로 출력하기
print(result)