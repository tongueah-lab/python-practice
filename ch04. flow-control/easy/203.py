# 정수를 이진수로 변환하여 1의 개수를 출력하세요. (bin() 사용 금지)
n = int(input())

# 카운트 초기화하기
count = 0
# n이 정수면 반복하기
while n > 0:
    # 만약 n이 홀수이면
    if n % 2 == 1:
        # 카운트하기
        count += 1
    # n//2
    n//=2
# 결과 출력하기
print(count)