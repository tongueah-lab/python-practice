# 컴프리헨션 한 줄로 새 리스트를 만든 뒤 출력하세요.
data_sets = [
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30],
    [0],
]
t = int(input())
nums = data_sets[t]

# 리스트 숫자들을 하나씩 순회하면서 제곱하기
squared_nums = [num ** 2 for num in nums]

# 컴프리헨션 출력하기
print(" ".join(str(n) for n in squared_nums))