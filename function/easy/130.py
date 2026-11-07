# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "width=4 height=5" → opts={"width":4,"height":5}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 키워드 인자로 넓이 계산 함수 정의하기
def rectangle_kw(width, height):
    # 넓이 * 높이 값 반환하기
    return width * height

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(rectangle_kw(**opts))
