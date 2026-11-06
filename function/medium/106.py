# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()

# 함수 정의하기
def build_tag(name, level=1):
    # 값 반환하기
    return "#" * level + name

# 토큰이 1개면 기본 레벨
if len(parts) == 1:
    print(build_tag(parts[0]))
# 토큰이 2개면 둘째 값이 레벨
elif len(parts) == 2:
    print(build_tag(parts[0], int(parts[1])))