# range(i, 0, -1)로 i부터 1까지 역순 출력하세요.
n = int(input())

# n부터 1까지 -1씩 빼면서 반복하기
for i in range(n, 0, -1):
    # i부터 1까지 -1씩 빼면서 반복하기
    for j in range(i, 0, -1):
        # 역순 출력하기
        print(j, end = "")
    # 한 줄씩 띄우기
    print()