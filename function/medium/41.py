# 전역 nums 를 정수 리스트로 읽습니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 합산 함수 정의하기
def total():
    # 원소들의 합 값 반환하기
    return sum(nums)
# 전역 리스트 읽어 합산 결과 출력하기
print(total())