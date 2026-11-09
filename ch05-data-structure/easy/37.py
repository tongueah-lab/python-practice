# 컴프리헨션 표현식 안에서 `min(...)` 을 호출해 한 번에 처리.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
t = int(input())
scores = data_sets[t]

# 각 점수에 10을 더하되 100점을 넘기면 100으로 자른다
result = [min(score + 10, 100) for score in scores]
# 결과 출력하기
print(" ".join(str(x) for x in result))