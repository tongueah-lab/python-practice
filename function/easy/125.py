# key=value 토큰을 dict 로 파싱합니다. 예: "a=1 b=2" → opts={"a":"1","b":"2"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 인자 개수 세는 함수 정의하기
def count_kwargs(**kwargs):
    # 키워드 개수 값 반환하기
    return len(kwargs)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(count_kwargs(**opts))
