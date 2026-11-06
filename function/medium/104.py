# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# 함수 정의하기
def check_pass(score, pass_line=60):
    # 값 반환하기
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"

# 토큰이 1개면 기본 커트라인
if len(parts) == 1:
    print(check_pass(int(parts[0])))
# 2개면 둘째 값이 커트라인
elif len(parts) == 2:
    print(check_pass(int(parts[0]), int(parts[1])))