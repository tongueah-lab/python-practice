# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 증가폭(1), 2개면 둘째 값이 증가폭입니다. (정수)
parts = input().split()

# 값 증가 함수 정의하기
def increment(n, step=1):
    # 반환하기
    return n + step

# 토큰이 1개면 기본 증가폭(1)
if len(parts) == 1:
    print(increment(int(parts[0])))
# 2개면 둘째 값이 증가폭임
else:
    print(increment(int(parts[0]), int(parts[1])))