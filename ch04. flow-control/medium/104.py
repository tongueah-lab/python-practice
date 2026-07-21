# for + if char != remove: result += char
text = input()
remove = input()
result = ""

# 문자열 반복하기
for char in text:
    # 문자열과 제거할 문자를 제외한 나머지를 문자열로 만들기
    if char != remove:
        result += char
# 결과 출력하기
print("결과:", result)
