# while문과 %10, //10을 사용하세요.
num = int(input())

# 자릿수 합 초기화하기
digit_sum = 0

# 숫자가 1 이상이어야 값이 나옴
while num > 0:
    # 각 자릿수 구하기
    digit_sum += num % 10
    num //= 10 
# 출력하기
print(f"각 자릿수의 합: {digit_sum}")