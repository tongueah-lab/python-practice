# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 지수(2), 2개면 둘째 값이 지수입니다. (값은 정수)
parts = input().split()

# 기본값 함수 정의하기
def power(base, exp=2):
    # 반환하기
    return base ** exp

# 토큰이 1개면 기본 지수(2)
if len(parts) == 1:
    print(power(int(parts[0])))
# 2개면 둘째 값이 지수
else:
    print(power(int(parts[0]), int(parts[1])))