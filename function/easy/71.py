# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# 양수 개수 세기 함수 정의하기
def count_positive(nums):
    # 카운트 초기화하기
    count = 0
    # 개수 반복 확인해서
    for num in nums:
        # 0보다 큰 정수면
        if num > 0:
            # 카운트 세기
            count += 1
    return count
# 결과 출력하기
print(count_positive(nums))