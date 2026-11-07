# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 여러 수의 합 함수 정의하기
def total(*nums):
    # 정수 합 값 반환하기
    return sum(nums)
    
# ↓ 호출부 (수정하지 마세요) — 리스트를 * 로 풀어 total 에 전달
print(total(*nums))
