# 전역 total, count 시작값 0. 처리할 정수들을 리스트로 읽습니다. 예: "10 20 30" → nums=[10, 20, 30]
nums = [int(x) for x in input().split()]
total = 0
count = 0

# 함수 정의하기
def record(n):
    # 두 전역을 바꾸므로 함수 total, oount 하기
    global total, count
    total += n
    count += 1

# 정수들 반복하기
for num in nums:
    record(num)

# 결과 출력하기
print(total)
print(count)