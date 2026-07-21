# 연산자를 if/elif로 판별하고 나누기에서 0 체크를 추가하세요.
num1 = float(input())
op = input()
num2 = float(input())

# 연산자가 +이면 num1 + num2하고 출력하기
if op == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
# 연산자가 -이면 num1 - num2하고 출력하기
elif op == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
# 연산자가 *이면 num1 * num2하고 출력하기
elif op == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
# 연산자가 /이고 num2 == 0이면 0으로 나눌 수 없음 출력하기
elif op == "/":
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
# 그 외는 지원하지 않는 연산자 출력하기
else:
    print("지원하지 않는 연산자입니다.")