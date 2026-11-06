# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 팩토리얼 함수 정의하기
def factorial(n):
    num = 1
    # 값 반환하기
    for i in range(1, n+1):
        num = num * i
    return num
# 결과 출력하기
print(factorial(n))