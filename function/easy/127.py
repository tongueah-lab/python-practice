# key=value 토큰을 dict 로 파싱합니다. 예: "greeting=안녕 name=철수" → opts={"greeting":"안녕","name":"철수"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 인자로 인사하는 함수 정의하기
def greet_kw(greeting, name):
    # 인사말, 이름 값 반환하기
    return f"{greeting}, {name}!"

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(greet_kw(**opts))
