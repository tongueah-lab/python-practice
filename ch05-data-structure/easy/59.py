# tuple도 list처럼 `in` 연산자로 멤버십을 검사할 수 있습니다.
menu = ("Espresso", "Latte", "Cappuccino", "Americano")
order = input()

# 메뉴 안에 주문 메뉴가 있다면 가능
if order in menu:
    print("주문 가능")
# 없다면 불가
else:
    print("주문 불가")