# 입력을 정수 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def sum_positive(*nums):
    # 값 초기화하기
    result = 0
    # 정수들 반복 확인하기
    for num in nums:
        # 정수가 0보다 크면
        if num > 0:
            # 다 합하기
            result += num
    # 총 합 값 반환하기
    return result

# ↓ 호출부 (수정하지 마세요)
print(sum_positive(*nums))
