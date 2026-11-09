# `len(word) == n` 을 컴프리헨션의 if 절로 사용하세요.
words = ["apple", "cat", "banana", "fig", "kiwi", "lemon", "pear"]
n = int(input())

# 길이가 n인 단어만 추출하기
result = [word for word in words if len(word) == n]
# 공백으로 구분하여 한 줄로 출력하기
print(" ".join(result))