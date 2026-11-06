# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "price=1000 tax=10" → opts={"price":1000,"tax":10}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 키워드 인자로 세금 포함 금액 함수 정의하기
def total_with_tax(price, tax):
    # 값 + 값 * 세금 // 100 값 반환하기
    return price + price * tax // 100

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(total_with_tax(**opts))
