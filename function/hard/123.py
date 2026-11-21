# 첫 토큰=개수(k), 나머지=정수들. 예: "2 1 2 3 4" → k=2, nums=[1, 2, 3, 4]
parts = input().split()
k = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 가장 큰 k개의 합 정의하기
def top_k_sum(k, *nums):
    # 결과 초기화하기
    result = 0
    # 큰 순서대로 정렬 뒤 앞 k를 가져오기
    for num in sorted(nums, reverse=True)[:k]:
        # 잘나낸 정수 다 더하기
        result += num
    # 값 반환하기
    return result
# ↓ 호출부 (수정하지 마세요) — k 는 위치 인자, 나머지는 * 로 풀어 전달
print(top_k_sum(k, *nums))
