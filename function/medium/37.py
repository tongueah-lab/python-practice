# 첫 값=요청 수량 n, 둘째 값=전역 재고 stock. 예: "5 10" → n=5, stock=10
parts = input().split()
n = int(parts[0])
stock = int(parts[1])

# 함수 정의하기
def in_stock(n):
    # 재고가 요청 수량이상이면 가능
    if n <= stock:
        return "가능"
    # 그렇지 않으면 불가
    else:
        return "불가"
# 결과 출력하기
print(in_stock(n))