# 공백을 먼저 (n-i)개 출력한 뒤 별을 i개 출력하세요.
n = int(input())

# 반복문 실행하기
for i in range(1, n + 1):
    # n - i * 공백만들어서 한 줄로 출력하기
    print(" " * (n - i), end = "")
    # * 출력하기
    print("*" * i)