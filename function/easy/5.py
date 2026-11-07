# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-7" 이면 n == -7
n = int(input())

# 절댓값 함수 정의하기
def my_abs(n):
    # n이 0보다 작으면
    if n < 0:
        # -로 반환하기
        return -n
    # 0보다 크면
    else:
        # 그대로 반환하기
        return n
# 절댓값 출력하기
print(my_abs(n))