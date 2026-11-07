# 한 줄을 공백으로 나눕니다. 예: "철수" → ["철수"](기본값 사용) / "철수 반가워" → ["철수","반가워"](override)
parts = input().split()

# greeting에 기본값을 가진 함수를 직접 정의하기
def greet(name, greeting = "안녕하세요"):
    # 인사말 출력하기
    return f"{greeting}, {name}님!"

# 토큰이 1개면 기본인사말을
if len(parts) == 1:
    print(greet(parts[0]))
# 2개면 둘째 값으로 인사말을 바꿔 호출하기
else:
    print(greet(parts[0],parts[1]))