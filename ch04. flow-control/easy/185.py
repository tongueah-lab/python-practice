# 숫자와 N을 입력받아 2~N의 배수인지 각각 출력하세요.
num = int(input())
n = int(input())

# 2부터 n까지 반복하기
for i in range(2, n + 1):
    # 숫자가 i로 나누어 떨어지는 배수라면 배수라고 출력하기
    if num % i == 0:
        print(f"{i}의 배수입니다.")
    # 그렇지 않으면 배수가 아니라고 출력하기
    else:
        print(f"{i}의 배수가 아닙니다.")