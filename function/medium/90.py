# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_even(nums):
    # 정수 반복 확인하기
    for num in nums:
        # 정수가 짝수면
        if num % 2 == 0:
            # 값 반환하기
            return num
    # 짝수가 하나도 없으면 "None"을 반환하기
    return None
# 결과 출력하기
print(first_even(nums))