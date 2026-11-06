# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=3 b=7" → opts={"a":3,"b":7}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 가장 큰 값의 키 찾는 함수 정의하기
def max_value_key(**kwargs):
    # 가장 큰 값의 키 값 반환하기
    return max(kwargs, key=kwargs.get)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(max_value_key(**opts))
