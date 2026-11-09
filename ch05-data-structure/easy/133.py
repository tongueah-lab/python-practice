# max 와 min 의 차이를 직접 출력.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# max와 min 차이 출력하기
print(max(scores) - min(scores))