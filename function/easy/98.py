# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()

# 함수 정의하기
def range_sum(n, start = 1):
    # 합 초기화하기
    result = 0
    # stat부터 n까지 합하기
    for i in range(start, n + 1):
        result += i
    # 합 반환하기
    return result

# 토큰이 1개면 1부터 n까지
if len(parts) == 1:
    print(range_sum(int(parts[0])))
# 토큰이 2개면 start부터 n까지 더하기
elif len(parts) == 2:
    print(range_sum(int(parts[0]), int(parts[1])))