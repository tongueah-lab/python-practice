# for문으로 순회하며 모음 여부를 확인하세요.
s = input()
result = []

# 모음 list 만들기
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# vowels = "aeiouAEIOU"
# 문자열 순회하기
for char in s:
    # 모음이 아닌 경우 새 리스트로 넣기
    if char not in vowels:
        result.append(char)
# 구분자 없이 출력하기
print("".join(result))