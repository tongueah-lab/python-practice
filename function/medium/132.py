# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=5 b=-3" → opts={"a":5,"b":-3}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 함수 정의하기
def sum_positive_values(**kwargs):
    # 총 합 초기화하기
    total = 0
    # 키워드 값 반복하기
    for i in kwargs.values():
        # 만약 양수면
        if i > 0:
            # 다 더하기
            total += i
    # 값 반환하기
    return total
# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_positive_values(**opts))