# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "3 -1 4" → nums=[3, -1, 4]
nums = [int(x) for x in input().split()]

# 함수 정의하기
def first_negative(nums):
    # 정수 반복 확인하기
    for num in nums:
        # 처음 나오는 음수를 찾는 즉시
        if num < 0:
            # 반환하기
            return num
    # 음수가 하나도 없으면 "없음"을 반환하기
    return "없음"
# 결과 출력하기
print(first_negative(nums))