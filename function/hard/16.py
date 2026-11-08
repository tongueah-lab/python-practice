# 위치 토큰: 첫째=상품, 둘째=가격, 나머지=옵션. "discount=값" 은 키워드 전용 할인액.
# 예: "노트북 1000 마우스 키보드 discount=100" → product="노트북", price=1000, options=["마우스","키보드"], discount=100
raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)



# 주문 처리 함수 정의하기
def order(product, price, *options, discount=0):
    # 상품명, 가격, 옵션, 할인액을 받아 주문 요약 문자열을 반환합니다.
    return f"{product} {price-discount}원 옵션{len(options)}개"

# ↓ 호출부 (수정하지 마세요) — discount 는 키워드 전용이라 이름으로 전달
print(order(product, price, *options, discount=discount))
