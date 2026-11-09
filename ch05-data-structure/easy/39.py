# 짝수 판별: 2로 나눈 나머지가 0.
data_sets = [
    [1, 4, 7, 2, 9, 6, 3, 8, 10, 5],
    [1, 2, 3, 4, 5],
    [1, 3, 5, 7, 9],
]
t = int(input())
data = data_sets[t]

# 컴프리헨션으로 짝수만 추출해서 출력하기
even_numbers = [x for x in data if x % 2 == 0]
print(" ".join(str(n) for n in even_numbers))