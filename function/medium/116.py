# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 가변 인자의 범위 함수 정의하기
def range_span(*nums):
    # 최대 정수에서 최소 정수를 뺀 값을 반환하기
    return max(nums) - min(nums)

# ↓ 호출부 (수정하지 마세요)
print(range_span(*nums))
