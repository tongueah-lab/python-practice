# 15의 배수를 먼저 검사해야 함

# 1부터 50까지 반복하기
for i in range(1, 51):
    # 15의 배수이면 "FizzBuzz" 출력하기
    if i % 15 == 0:
        print("FizzBuzz")
    # 3의 배수이면 "Fizz" 출력하기
    elif i % 3 == 0:
        print("Fizz")
    # 5의 배수이면 "Buzz" 출력하기
    elif i % 5 == 0:
        print("Buzz")
    # 나머지 숫자는 그대로 출력하기
    else:
        print(i)