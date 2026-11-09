# set 변환 + sorted 로 한 번에 처리.
data_sets = [
    [85, 92, 65, 85, 95, 92, 78, 65],
    [1, 2, 3, 1, 2],
    [100, 100, 100],
]
t = int(input())
scores = data_sets[t]

# 중복 제거를 오름차순으로 정렬해 공백 구분해서 출력하기
print(" ".join(map(str, sorted(set(scores)))))