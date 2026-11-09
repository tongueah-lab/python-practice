# 정수 리스트를 오름차순 정렬해 공백 구분 한 줄로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 정수로 변환 후 점수 오름차순으로 만들기
result = " ".join(map(str, sorted(scores)))

# 출력하기
print(result)