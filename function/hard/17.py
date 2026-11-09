# 위치: 첫째=상품, 둘째=가격, 나머지=옵션. "discount=값" 은 키워드 전용, 그 외 "key=value" 는 기타 정보(info).
# 예: "노트북 1000 마우스 키보드 discount=100 color=검정" → product=노트북, price=1000, options=[마우스,키보드], discount=100, info={color:검정}
raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
info = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)
        else:
            info[k] = v


# 주문 처리 함수 정의하기
def order2(product, price, *options, discount=0, **info):
    # [기타정보를 키 사전순 'k=v' 로 ','연결] 변수 잡기
    info_str = f"[{','.join(f'{k}={v}' for k, v in sorted(info.items()))}]"
    # 상품명, 가격, 옵션, 할인액, 그 외 기타 정보를 받아 주문 요약을 반환하기
    return f"{product} {price-discount}원 옵션{len(options)}개 {info_str}"
# ↓ 호출부 (수정하지 마세요)
print(order2(product, price, *options, discount=discount, **info))
