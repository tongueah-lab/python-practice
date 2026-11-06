# key=value 토큰을 dict 로 파싱합니다. 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 키워드 이름 정렬 함수 정의하기
def list_keys(**kwargs):
    # ,로 구분하고 사전순으로 값 반환하기
    return ",".join(sorted(kwargs))

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(list_keys(**opts))
