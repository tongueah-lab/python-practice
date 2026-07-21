# i==0 또는 i==n-1 또는 j==0 또는 j==n-1 이면 테두리입니다.
n = int(input())

# N x N 사각형 반복하기
for row in range(n):
    for col in range(n):
        # 테투리이면 * 출력하기
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            print("*", end="")
        # 그렇지 않으면 공백으로 채우기
        else:
            print(" ", end="")
    # 줄 바꾸기
    print()