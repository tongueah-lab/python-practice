# 한 줄을 공백으로 나눕니다. 토큰이 2개면 기본 구분자("-"), 3개면 셋째 값이 구분자입니다.
parts = input().split()

# 두 단어 잇기 함수 정의하기
def join_two(a, b, sep="-"):
    # 값 반환하기
    return a + sep + b

# 토큰이 2개면 기본 구분자
if len(parts) == 2:
    print(join_two(parts[0], parts[1]))
# 3개면 셋째 값이 구분자
else:
    print(join_two(parts[0], parts[1], parts[2]))