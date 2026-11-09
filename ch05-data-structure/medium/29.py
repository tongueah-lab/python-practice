# 두 슬라이스 `data[:k]` 와 `data[k:]` 로 한 번에 분할합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
p = int(input())

# 분할 위치 구하기
k = len(data) * p // 100
# 분할 위치까지 출력하기
train_str = ' '.join(map(str, data[:k]))
print(f"train: {train_str}")

# 분할 위치부터 출력하기
val_str = ' '.join(map(str, data[k:]))
print(f"val: {val_str}")