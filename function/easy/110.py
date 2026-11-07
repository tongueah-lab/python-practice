# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 최댓값 함수 정의하기
def max_all(*nums):
    # 가장 큰 값 반환하기
    return max(nums)

# ↓ 호출부 (수정하지 마세요)
print(max_all(*nums))
