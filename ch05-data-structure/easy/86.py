# 빈 set 은 `set()` 으로 만든다는 점이 중요.
data_sets = [
    {"apple", "banana", "cherry", "date"},
    {"single"},
    set(),
]
t = int(input())
fruits = data_sets[t]

# 중복을 허용하지 않고 고유 워소 개수 출력하기
print(len(set(fruits)))