# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=1 b=2" → opts={"a":1,"b":2}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 키워드 값 모두 더하는 함수 정의하기
def sum_values(**kwargs):
    # 키워드 총 합 값 반환하기
    return sum(kwargs.values())

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_values(**opts))
