"""정수의 제곱을 반환한다.`, 본문 `return n * n`
- 출력: 첫 줄 = `square.__doc__`, 둘째 줄 = `square(n)`
"""

# 정수 n 을 읽습니다. 예: "5" → n=5
n = int(input())

# 제곱 함수 정의하기
def square(n):
    # docstring 적기
    """정수의 제곱을 반환한다."""
    # 제곱 값 반환하기
    return n * n
# 제곱 함수 출력하기
print(square.__doc__)
print(square(n))