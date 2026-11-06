# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def sum_avg(nums):
    # (합, 평균) 반환하기
    avg = sum(nums) // len(nums)
    return sum(nums), avg
# 결과 출력하기
print(*sum_avg(nums))