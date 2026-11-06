# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_and_last_sum(*nums):
    # 첫 인자 + 마지막 인자 값 반환하기
    return nums[0] + nums[-1]
# ↓ 호출부 (수정하지 마세요)
print(first_and_last_sum(*nums))
