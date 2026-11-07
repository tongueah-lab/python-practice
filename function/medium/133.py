# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "a=hi b=hello" → opts={"a":"hi","b":"hello"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 정의하기
def longest_value(**kwargs):
    # 가장 긴 함수 변수 만들기
    long_word = ""
    # 딕셔너리의 값들을 돌기
    for word in kwargs.values():
        # 만약 딕셔너리 값들이 긴 함수 변수보다 크면
        if len(word) > len(long_word):
            # 긴 함수 변수에 딕셔너리 값 저장하기
            long_word = word
    # 가장 긴 함수 변수 값 반환하기
    return long_word
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(longest_value(**opts))
