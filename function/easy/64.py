"""이름으로 인사말을 만든다.`, 본문 `return "안녕하세요, " + name + "님!"`
- 출력: 첫 줄 = `greet.__doc__`, 둘째 줄 = `greet(name)`
"""

# 이름을 한 줄로 읽습니다. 예: "철수" → name="철수"
name = input()

# 인사 함수 정의하기
def greet(name):
    # docstring 적기
    """이름으로 인사말을 만든다."""
    # 인사 반환하기
    return f"안녕하세요, {name}님!"
# 설명 출력하기
print(greet.__doc__)
# 인사 함수 출력하기
print(greet(name))