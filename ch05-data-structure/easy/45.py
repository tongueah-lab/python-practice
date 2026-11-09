# 조건 검사 시 대소문자 차이를 없애려면 `c.lower() in "aeiou"` 가 편합니다.
# 결과를 한 문자열로 이어 붙이려면 `"".join(...)` 을 사용하세요.
s = input()

# 대소문자 모음만 고르기
vowels = "aeiouAEIOU"
# 문자열 안에 모음이 있으면 모음만 출력하기
result = [ch for ch in s if ch in vowels]
print("".join(result))