# key=value 토큰을 dict 로 파싱합니다. 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 인자로 프로필 만드는 함수 정의하기
def make_profile(name, age):
    # 이름 나이 값 반환하기
    return f"{name}({age})"

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(make_profile(**opts))
