# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
n = int(input())

# 부호 함수 정의하기
def sign(n):
    # n이 양수면 양수라고 반환하기
    if n > 0:
        return "양수"
    # 음수면 음수라고 반환하기
    elif n < 0:
        return "음수"
    # 0이면 0이라고 반환하기
    else:
        return "0"
# 부호 함수 출력하기
print(sign(n))