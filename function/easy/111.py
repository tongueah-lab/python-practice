# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 최솟값 함수 정의하기
def min_all(*nums):
    # 최솟값 값 반환하기
    return min(nums)
# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))