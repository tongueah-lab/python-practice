# 문자열 변환 후 len 으로 자릿수 산출.
data_sets = [
    [1, 23, 456, 7890, 5, 100, 9999],
    [1, 5, 9],
    [10000],
]
t = int(input())
nums = data_sets[t]

# 문자열 길이 변환하고 문자열 길이 반환하기
result = [len(str(x)) for x in nums]

# 결과 출력하기
print(" ".join(map(str, result)))

# 출력할 때 정수를 문자열로 변환하고 길이도 반환하기
# print(" ".join(str(len(str(x))) for x in nums))