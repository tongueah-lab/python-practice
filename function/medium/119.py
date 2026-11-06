# 첫 토큰=배수(factor), 나머지=더할 정수들. 예: "2 1 2 3" → factor=2, nums=[1, 2, 3]
parts = input().split()
factor = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 배수를 곱한 합의 함수 정의하기
def sum_scaled(factor, *nums):
    # 배수 * 정수의 총 합 값 반환하기
    return factor * sum(nums)

# ↓ 호출부 (수정하지 마세요) — factor 는 위치 인자, 나머지는 * 로 풀어 전달
print(sum_scaled(factor, *nums))
