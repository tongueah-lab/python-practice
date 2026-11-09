# min, max 를 먼저 구해두고 컴프리헨션 안에서 사용하세요. 각 값을 f-string의 `:.2f` 로 포맷.
data = [10, 20, 30, 40, 50, 60, 70, 80]
n = int(input())

# 최솟값 구하기
min_val = min(data[:n])
# 최댓값 구하기
max_val = max(data[:n])

# 컴프리헨션으로 min-max 정규화를 수행하기
result = [f"{(x - min_val) / (max_val - min_val):.2f}"for x in data[:n]]
# 결과 출력하기
print(" ".join(result))