# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 2회, 2개면 둘째 값(정수)이 반복 횟수입니다.
parts = input().split()

# 문자열 반복 함수 정의하기
def repeat_text(text, times = 2):
    # 값 반환하기
    return text * times

# 토큰이 1개면 기본 2회
if len(parts) == 1:
    print(repeat_text(parts[0]))
# 2개면 둘째 값이 반복 횟수
else:
    print(repeat_text(parts[0], int(parts[1])))