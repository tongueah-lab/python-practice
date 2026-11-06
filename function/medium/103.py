# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 low, high 가 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# 함수 정의하기
def clamp(value, low=0, high=100):
    # 값 반환하기
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

# 토큰이 1개면 값만
if len(parts) == 1:
    print(clamp(int(parts[0])))
# 토큰이 2개면 값, 하한
elif len(parts) == 2:
    print(clamp(int(parts[0]), int(parts[1])))
# 토큰이 3개면 상한(정수, 기본값 100)
elif len(parts) == 3:
    print(clamp(int(parts[0]), int(parts[1]), int(parts[2])))