# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 점수 평균 함수 정의하기
def average(nums):
    # 평균 계산 반환하기
    return sum(nums) // len(nums)
# 점수 평균 값 출력하기
print(average(nums))