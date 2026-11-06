# 전역 positive_count 시작값 0. 검사할 정수들을 리스트로 읽습니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]
positive_count = 0

# 함수 정의하기
def check(n):
    # global 선언하기
    global positive_count
    # 만약 n > 0이면 카운트 세기
    if n > 0:
        positive_count += 1

# 숫자들 반복하기
for num in nums:
    check(num)
# 결과 출력하기
print(positive_count)