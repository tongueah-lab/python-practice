# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 최소 최대 합 합수 정의하기
def stats(nums):
    # 세 값을 함께 반환하기
    return (min(nums), max(nums), sum(nums))
# 결과 출력하기
print(*stats(nums))