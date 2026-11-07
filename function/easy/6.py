# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 모든 정수의 합을 구하는 함수를 정의하기
def sum_to(n):
    # 1부터 n까지의 정수를 다 합하기
    total = 0
    for i in range(1, n + 1):
        total += i
    # 다 합한 값을 반환하기
    return total
# 합 출력하기
print(sum_to(n))