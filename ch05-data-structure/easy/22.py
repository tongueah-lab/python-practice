# 한 슬라이스에 시작 1과 끝 -1을 함께 지정합니다.
data_sets = [
    [10, 20, 30, 40, 50, 60, 70, 80],
    [1, 2, 3, 4, 5],
    [10, 20],
]
t = int(input())
data = data_sets[t]

# 정수로 변환 후 1부터 -1까지 슬라이싱하기
result = " ".join(map(str, data[1:-1]))

# 출력하기
print(result)