# 1부터 N까지 반복하며 i % 2 == 1인 경우에만 print(i)로 출력하세요.
n = int(input())

# 1부터 n + 1까지 반복하기
for i in range(1, n + 1):
    # 1부터 n까지의 수 중 홀수만 출력
    if i % 2 == 1:
        print(i)