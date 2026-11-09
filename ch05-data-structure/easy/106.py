# 문자열의 `replace(old, new)` 메서드는 일치하는 모든 부분을 치환합니다.
text = input()
old = input()
new = input()

# 문자열의 old부분을 new로 모두 치환
result = text.replace(old, new)
# 치환 결과 출력하기
print(result)