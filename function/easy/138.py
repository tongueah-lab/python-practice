# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def add3(a, b, c):
    # 세 정수의 합 값을 반환하기
    return a + b + c

# TODO: nums 를 * 로 풀어 add3 에 넘기고, 그 반환값을 print 하세요.
print(add3(*nums))