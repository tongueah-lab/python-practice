# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def stats4(nums):
    # 값 반환하기
    return (min(nums), max(nums), sum(nums), sum(nums) // len(nums))
# 출력하기
print(*stats4(nums))