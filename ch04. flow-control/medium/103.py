# range(len(text)-1, -1, -1)로 역순 순회
text = input()
result = ""

# (start, step, stop) 역순 순회하기
for char in range(len(text)-1, -1, -1):
    # 역순을 다시 합치기
    result += text[char]
# 뒤집은 문자열 출력하기
print("뒤집은 문자열:", result)
