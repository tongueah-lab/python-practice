# 단가와 수량범위 N을 입력받아 가격표를 출력하세요.
price = int(input())
n = int(input())

# 수량을 1부터 n까지 반복하기
for i in range(1, n + 1):
    # 수량 x 단가를 곱해서 가격표 출력하기
    print(f"{i} x {price} = {i*price}")