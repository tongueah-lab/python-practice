# while num > 0으로 반복하며 마지막 자리를 꺼내 reverse에 쌓으세요.
num = int(input())
reverse = 0

# num이라는 변수는 0이상 잡는다
while num > 0:
    # 몇 자리 수인지 알기 위해 10씩 나눈다
    digit = num % 10
    # 뒤집기 위해 다시 10을 곱하고 더한다
    reverse = reverse * 10 + digit
    num //= 10
# 뒤집은 숫자 출력하기
print(f"뒤집은 숫자: {reverse}")