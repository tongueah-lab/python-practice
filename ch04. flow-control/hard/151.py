# while True, if/elif로 메뉴 분기 후 break 처리
price1 = 1200
price2 = 1500
price3 = 2000
qty1 = 0
qty2 = 0
qty3 = 0


# 편의점 계산 반복하기
while True:
    # 메뉴판 출력하기
    print("===== 편의점 =====")
    print("1. 삼각김밥 (1200원)\n2. 음료수 (1500원)\n3. 과자 (2000원)")
    
    # 상품 번호 입력받기
    menu = input()

    # 만약 1, 2, 3이 아니면 반복문 멈추기
    if menu not in ("1", "2", "3"):
        print("잘못된 상품 번호입니다.")
        continue
    
    # 수량 입력받기
    qty = int(input())

    # 상품 1을 입력하면 삼각김밥, 갯수 출력하기
    if menu == "1":
        qty1 += qty
        print(f"삼각김밥 {qty}개 추가!")

    # 상품 2를 입력하면 음료수, 갯수 출력하기
    elif menu == "2":
        qty2 += qty
        print(f"음료수 {qty}개 추가!")

    # 상품 3을 입력하면 과자, 갯수 출력하기
    elif menu == "3":
        qty3 += qty
        print(f"과자 {qty}개 추가!")

        # 유효 입력 후 "계속 쇼핑?"을 입력받아 1이 아니면 반복문 멈추기
    keep_shopping = input()
    if keep_shopping != "1":
        break 
    print()

print()

# 계산서 출력하기
print("===== 계산서 =====")
# 구매 수량 > 0인 상품만 금액 구하기
if qty1 > 0:
    print(f"삼각김밥 x {qty1} = {qty1 * price1}원")
if qty2 > 0:
    print(f"음료수 x {qty2} = {qty2 * price2}원")
if qty3 > 0:
    print(f"과자 x {qty3} = {qty3 * price3}원")

# 총액 구하기
total = qty1 * price1 + qty2 * price2 + qty3 * price3
print(f"총액: {total}원")