# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def count_even(*nums):
    # 카운트 초기화하기
    count = 0
    # 정수 반복하기
    for num in nums:
        # 정수가 짝수이면 카운트 세기
        if num % 2 == 0:
            count += 1
    # 카운트 값 반환하기
    return count

# ↓ 호출부 (수정하지 마세요)
print(count_even(*nums))
