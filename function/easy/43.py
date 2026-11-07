# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "4" 이면 n == 4
n = int(input())

# 짝수 함수 정의하기
def is_even(n):
    # 짝수면 True
    if n % 2 == 0:
        return "True"
    # 홀수면 False
    else:
        return "False"
# 결과 출력하기
print(is_even(n))