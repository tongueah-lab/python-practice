# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-5" 이면 n == -5
n = int(input())

# 절댓값과 부호 함수 정의하기
def abs_sign(n):
    # 0보다 크면 "양수"
    if n > 0:
        return n, "양수"
    # 0보다 작으면 "음수"
    elif n < 0:
        return -n, "음수"
    # 0이면 "0"
    elif n == 0:
        return 0, "0"
    # 그 외면 "n"
    else:
        return n
# 결과 출력하기
print(*abs_sign(n))