# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.
n = int(input())

# 가로 줄을 1부터 n까지 반복하기
for i in range(1, n + 1):
    # 세로 줄을 1부터 i번까지 반복하기
    for j in range(1, i + 1):
        # 숫자 출력하기
        print(j, end="")
    # 줄 띄우기
    print()