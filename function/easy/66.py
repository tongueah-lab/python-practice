"""두 수 중 큰 값을 반환한다.`, 본문은 더 큰 값을 반환
- 출력: 첫 줄 = `max_two.__doc__`, 둘째 줄 = `max_two(a, b)`
"""

# 두 정수를 읽습니다. 예: "10 2" → a=10, b=2
parts = input().split()
a = int(parts[0])
b = int(parts[1])

# 최댓값 함수 정의하기
def max_two(a, b):
    # docstring 적기
    """두 수 중 큰 값을 반환한다."""
    # 최댓값 값 반환하기
    return max(a, b)
# 결과 출력하기
print(max_two.__doc__)
print(max_two(a, b))