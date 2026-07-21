# 3자리 정수를 입력받아 각 자리를 분해하고 합, 곱을 출력하세요.
num = int(input())

# 백의자리 구하기
hundred_digit = num // 100

# 나머지 숫자
remainder = num % 100

# 십의 자리 구하기
ten_digit = remainder // 10

# 일의 자리 구하기
one_digit = remainder % 10


# 백의 자리 출력하기
print(f"백의자리: {hundred_digit}")
# 십의 자리 출력하기
print(f"십의자리: {ten_digit}")
# 일의 자리 출력하기
print(f"일의자리: {one_digit}")
# 합 출력하기
print(f"합: {hundred_digit + ten_digit + one_digit}")
# 곱 출력하기
print(f"곱: {hundred_digit * ten_digit * one_digit}")