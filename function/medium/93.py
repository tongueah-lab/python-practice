# 첫 줄은 한계값 T, 둘째 줄은 공백으로 구분된 정수들입니다.
# 예: 첫 줄 "10", 둘째 줄 "3 4 5 6" → threshold=10, nums=[3, 4, 5, 6]
threshold = int(input())
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_exceed(nums, threshold):
    # 누적합 초기화하기
    result = 0
    # 숫자 반복하기
    for i in range(len(nums)):
        # 누적 더하기
        result += nums[i]
        # 누적 값이 t를 초과하면 즉시 반환
        if result > threshold:
            return i
    # 한 번도 넘지 않으면 -1을 반환
    return -1

# 결과 출력하기
print(first_exceed(nums, threshold))
    
