# 첫 토큰=기준값(threshold), 나머지=검사할 정수들. 예: "5 3 6 1 8" → threshold=5, nums=[3, 6, 1, 8]
parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 함수 정의하기
def count_above(threshold, *nums):
    # 카운트 초기화하기
    count = 0
    # 정수 반복하기
    for num in nums:
        # 정수가 threshold보다 크면
        if num > threshold:
            # 카운트 세기
            count += 1
    # 값 반환하기
    return count
# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))
