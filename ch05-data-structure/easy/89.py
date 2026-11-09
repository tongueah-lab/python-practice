# `s.discard(x)` 는 원소가 없어도 오류를 내지 않습니다 (반면 `s.remove(x)` 는 KeyError).
fruits = {"apple", "banana", "cherry", "date", "fig"}
item = input()

# set에서 원소 제거하기
fruits.discard(item)
print(*sorted(fruits))